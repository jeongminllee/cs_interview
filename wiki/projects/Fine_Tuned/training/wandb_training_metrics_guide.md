---
type: Study Note
title: W&B Training Metrics Guide for MalwareAnalysisLLM
description: LLaMA-Factory 기반 Qwen3-Coder fine-tuning 중 W&B에 표시되는 loss, learning rate, grad norm, epoch, runtime, system metric을 해석하는 가이드.
tags: [finetuning, wandb, metrics, llamafactory, b200]
timestamp: 2026-07-08
status: active
---

# Summary

W&B는 학습이 잘 되고 있는지 보는 dashboard이고, cgroup/GPU watcher는 서버가 왜 느려지거나 죽는지 보는 telemetry다.

우리 프로젝트의 LLaMA-Factory run은 Hugging Face Trainer 계열 logging을 W&B로 보낸다. 따라서 W&B에서 보이는 대부분의 항목은 다음 세 부류다.

- 학습 품질 지표: `loss`, `eval_loss`
- 학습 진행 지표: `learning_rate`, `epoch`, `global_step`, runtime
- 시스템 지표: GPU, CPU, memory, process 사용량

현재 Qwen3-Coder-Next 80B full config 기준:

```yaml
logging_steps: 5
eval_steps: 250
per_device_train_batch_size: 1
gradient_accumulation_steps: 8
learning_rate: 1.0e-4
num_train_epochs: 1.0
lr_scheduler_type: cosine
warmup_ratio: 0.1
report_to: wandb
```

4 GPU 기준 global batch size는 대략 `1 * 4 * 8 = 32`다. train dataset이 약 332,807건이면 1 epoch는 약 10,400 update step이다.

# Core Metrics

| W&B 항목 | 뜻 | 어떻게 읽나 | 우리 상황에서의 해석 |
| --- | --- | --- | --- |
| `loss` 또는 `train/loss` | 현재 training batch 또는 logging window의 language modeling loss | 내려가는 방향이 정상이다. 단, 너무 빠르게 낮아지면 과적합이나 데이터 중복도 의심한다. | 5 step마다 찍히는 핵심 지표다. 1 epoch 초반에는 흔들릴 수 있다. |
| `eval_loss` 또는 `eval/loss` | validation dataset에서 계산한 loss | train loss와 함께 내려가면 좋다. train loss만 내려가고 eval loss가 오르면 과적합 신호다. | `eval_steps: 250` 기준으로 250 update step마다 찍힌다. |
| `learning_rate` | 현재 step에서 optimizer가 쓰는 learning rate | warmup 구간에서는 올라가고, cosine scheduler에서는 이후 점진적으로 내려간다. | `1e-4`, `warmup_ratio: 0.1`, `cosine`이므로 초반 10% step은 상승, 이후 하강이 정상이다. |
| `epoch` | 전체 train dataset을 몇 번 봤는지의 진행률 | `0.5`면 전체 dataset의 절반 정도를 본 상태다. | 1.0에 도달하면 전체 train dataset 1회 학습이 끝난다. |
| `global_step` 또는 `_step` | optimizer update가 몇 번 일어났는지 | gradient accumulation 이후 실제 parameter update 단위다. | raw batch 수가 아니라 update step이다. |
| `grad_norm` | gradient의 전체 크기 | 갑자기 폭증하면 불안정 학습, NaN 전조일 수 있다. 0에 가까우면 학습 신호가 약할 수 있다. | LoRA에서도 optimizer step 안정성 확인에 유용하다. |

# Loss 해석

## 좋은 흐름

```text
train/loss 감소
eval/loss 감소 또는 안정
grad_norm 큰 폭발 없음
learning_rate scheduler 모양 정상
```

이 경우 1 epoch는 의미 있는 학습으로 본다. 1 epoch가 끝난 뒤 evaluation sample과 validation loss를 보고 2 epoch 여부를 결정한다.

## 주의할 흐름

```text
train/loss 감소
eval/loss 상승
```

이 경우 모델이 train dataset의 표현에 과하게 맞춰지고 있을 수 있다. epoch를 늘리기보다 learning rate, 데이터 중복, validation split 품질을 먼저 본다.

## 위험한 흐름

```text
loss = nan
grad_norm 급등
learning_rate는 정상인데 loss가 갑자기 폭발
```

이 경우 dtype, optimizer, gradient clipping, mixed precision, dataset outlier를 확인한다.

# Runtime Metrics

| W&B 항목 | 뜻 | 해석 |
| --- | --- | --- |
| `train_runtime` | 학습 전체 또는 현재 train call의 실행 시간 | run 종료 후 전체 소요 시간 계산에 쓴다. |
| `train_samples_per_second` | 초당 처리한 sample 수 | throughput 비교용이다. 다른 config와 비교할 때만 의미가 크다. |
| `train_steps_per_second` | 초당 update step 수 | ETA 계산에 중요하다. gradient accumulation이 크면 낮게 보일 수 있다. |
| `eval_runtime` | validation evaluation에 걸린 시간 | eval이 너무 길면 `eval_steps`를 늘릴 수 있다. |
| `eval_samples_per_second` | validation 처리 속도 | validation 병목 확인용이다. |
| `total_flos` | 추정 연산량 | 절대값보다 같은 framework/config 사이 비교에 쓴다. |

runtime metric은 성능 품질보다 throughput과 병목을 보는 항목이다. loss가 좋더라도 `steps_per_second`가 너무 낮으면 데이터 로딩, kernel fallback, 통신, CPU RAM pressure를 따로 봐야 한다.

# System Metrics

W&B는 run 환경에 따라 `system/` 계열 metric도 보여준다. 이름은 화면 설정과 W&B 버전에 따라 조금 다를 수 있다.

| 항목 | 뜻 | 주의점 |
| --- | --- | --- |
| GPU utilization | GPU가 계산 커널을 얼마나 실행 중인지 | GPU memory가 높아도 utilization은 0일 수 있다. 모델이 올라가 있지만 계산 중이 아닐 수 있기 때문이다. |
| GPU memory allocated/used | GPU VRAM 사용량 | model weight, activation, buffer, CUDA context가 포함된다. |
| CPU utilization | CPU 사용률 | tokenization, dataloader, checkpoint loading, DeepSpeed 초기화 병목을 볼 때 쓴다. |
| system memory/RAM | host 또는 process memory 사용량 | 우리 서버에서는 host RAM보다 container cgroup `memory.max`가 더 중요하다. |
| disk/network | checkpoint 저장, W&B sync, dataset read, model shard read/write 영향 | checkpoint save step에서 튈 수 있다. |

주의: W&B system memory만으로 cgroup kill 여부를 판단하면 안 된다. 480B/80B run에서는 반드시 `model/runs/memory/*.jsonl`의 `memory.current`, `memory.max`, `memory.events.oom_kill`을 같이 본다.

# W&B Step vs Epoch

W&B에서 x-axis가 `_step`일 때와 `epoch`일 때 해석이 다르다.

- `_step`: W&B가 log한 순번이다. Trainer의 global step과 거의 같이 움직이지만 완전히 같은 개념은 아닐 수 있다.
- `global_step`: optimizer update step이다.
- `epoch`: 전체 dataset 대비 진행률이다.

현재 full training에서는 대략 다음처럼 본다.

```text
global batch size ~= 32
train samples ~= 332,807
1 epoch ~= 10,400 update steps
logging_steps = 5
eval_steps = 250
```

따라서 train loss는 매우 자주 찍히고, eval loss는 상대적으로 드물게 찍히는 것이 정상이다.

# Project Reading Rules

## 학습이 정상 진행 중인지 빠르게 보는 순서

1. `loss`가 찍히는가?
2. `learning_rate`가 warmup/cosine 모양으로 움직이는가?
3. `grad_norm`이 NaN 또는 급등하지 않는가?
4. `eval_loss`가 train loss와 크게 벌어지지 않는가?
5. `train_steps_per_second`가 갑자기 0에 가까워지지 않는가?
6. 같은 시각 cgroup `oom_kill`이 증가하지 않았는가?

## W&B만 보면 안 되는 경우

- loss가 찍히기 전 종료
- `SIGKILL`만 있고 Python traceback이 없음
- GPU utilization이 낮고 CPU/RAM만 계속 증가
- checkpoint loading 중 멈춘 것처럼 보임

이 경우 W&B는 원인을 거의 보여주지 못한다. `torchrun` 로그와 memory watcher를 같이 봐야 한다.

# Current Qwen3-Coder-Next Notes

Qwen3-Coder-Next 80B full run에서는 GPU memory가 올라갔는데 GPU utilization이 낮게 보일 수 있다. 이는 model/버퍼가 GPU에 올라간 상태와 실제 forward/backward 계산이 계속 도는 상태가 다르기 때문이다.

초기화 구간에서는 다음이 병목일 수 있다.

- model shard loading
- CPU RAM에서 weight materialization
- DeepSpeed ZeRO initialization
- tokenizer/cache preprocessing
- kernel fast path fallback
- distributed rank synchronization

이때 W&B loss가 아직 없다면 학습 품질을 판단할 단계가 아니다. 먼저 첫 optimizer step과 첫 loss log가 찍히는지 확인한다.

# Related Concepts

- [LLaMA-Factory + W&B Fine-Tuning Integration](llamafactory_wandb_finetuning.md)
- [W&B and Telemetry Basics](../fundamentals/wandb_telemetry_basics.md)
- [PyTorch Training Basics](../fundamentals/pytorch_training_basics.md)
- [B200 Fine-Tuning Troubleshooting Report](../b200/b200_finetuning_troubleshooting_report_20260703.md)

# Citations

- [W&B Hugging Face integration](https://docs.wandb.ai/models/integrations/huggingface)
- [W&B PyTorch integration](https://docs.wandb.ai/models/integrations/pytorch)
- [Hugging Face Transformers Trainer](https://huggingface.co/docs/transformers/trainer)
- [Hugging Face Trainer API](https://huggingface.co/docs/transformers/main_classes/trainer)
