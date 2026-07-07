---
type: Study Note
title: Fine-Tuning Framework Comparison Basics
description: LLaMA-Factory, TRL, Axolotl, torchtune, ms-swift Megatron, NeMo, Unsloth의 기본 역할 비교.
tags: [finetuning, frameworks, llamafactory, trl, axolotl, torchtune, nemo, ms-swift]
timestamp: 2026-07-03
status: active
---

# Summary

Fine-tuning framework는 모두 같은 일을 하는 것처럼 보이지만, 실제로는 추상화 수준과 강점이 다르다.

우리 프로젝트의 기본 선택은 LLaMA-Factory다. 다만 480B FP8에서 load/training 문제가 계속되면 large-model-native framework인 ms-swift Megatron이나 NVIDIA NeMo를 비교해야 한다.

# Comparison Table

| Framework | 기본 성격 | 우리 프로젝트에서의 역할 |
|---|---|---|
| LLaMA-Factory | YAML 중심 end-to-end fine-tuning framework | 현재 baseline |
| HF Transformers/TRL | Hugging Face native trainer/SFTTrainer | 아래층 이해와 custom fallback |
| Axolotl | config-driven multi-GPU fine-tuning framework | LLaMA-Factory 대체 후보 |
| torchtune | PyTorch-native recipe framework | PyTorch/FSDP 이해와 비교 후보 |
| ms-swift Megatron | Megatron parallelism 기반 대형 모델 학습 | 480B/MoE 계열 핵심 후보 |
| NVIDIA NeMo | NVIDIA large-model training framework | Qwen3 LoRA/import recipe 후보 |
| Unsloth | 경량/효율 fine-tuning 및 inference 중심 | 작은 모델 PoC 또는 compatibility check |

# LLaMA-Factory

장점:

- YAML로 실행이 정리된다.
- SFT, LoRA, DeepSpeed, W&B가 연결되어 있다.
- 팀원이 config를 리뷰하기 쉽다.

주의:

- 매우 큰 모델에서 checkpoint loading과 DeepSpeed 초기화 순서가 문제가 될 수 있다.
- framework 내부 abstraction 때문에 낮은 레벨 디버깅이 어려울 수 있다.

# Transformers / TRL

TRL의 SFTTrainer는 Hugging Face Trainer 기반으로 SFT를 쉽게 구성하게 해준다.

장점:

- Transformers/PEFT/Accelerate와 직접 연결된다.
- custom code 작성이 쉽다.
- LLaMA-Factory 내부를 이해하는 데 좋다.

주의:

- 대규모 production run에서는 config와 glue code를 직접 관리해야 한다.

# Axolotl

Axolotl은 YAML 중심 fine-tuning framework이고, multi-GPU에서 DDP, DeepSpeed, FSDP 계열 전략을 지원한다.

장점:

- LLaMA-Factory와 비슷하게 config 중심이다.
- DeepSpeed/FSDP 선택지가 있다.

주의:

- 현재 프로젝트 dataset/export와 config compatibility를 별도로 맞춰야 한다.

# torchtune

torchtune은 PyTorch-native training recipe를 제공한다.

장점:

- PyTorch/FSDP 개념을 배우기 좋다.
- recipe 구조가 비교적 명시적이다.

주의:

- 480B FP8 Qwen3-Coder production path로 바로 쓰기 전에는 model support와 recipe compatibility를 확인해야 한다.

# ms-swift Megatron

ms-swift Megatron은 Megatron parallelism을 이용해 큰 모델 학습을 가속하는 방향의 framework다.

중요한 parallelism:

- data parallelism
- tensor parallelism
- pipeline parallelism
- sequence parallelism
- context parallelism
- expert parallelism

480B/MoE 계열에서 LLaMA-Factory가 계속 load memory 벽에 걸리면 가장 중요하게 볼 후보 중 하나다.

# NVIDIA NeMo

NeMo는 NVIDIA의 large model training framework다. Qwen3 관련 fine-tuning recipe와 LoRA 옵션을 제공한다.

장점:

- NVIDIA GPU 대형 학습 stack과 잘 맞을 가능성이 있다.
- Qwen3 LoRA recipe가 있다.

주의:

- Hugging Face checkpoint import와 NeMo format 변환이 필요할 수 있다.
- dependency/container 관리가 더 무거울 수 있다.

# Unsloth

Unsloth는 효율적인 fine-tuning과 inference에 강점이 있다.

우리 프로젝트에서는 우선 480B training 후보라기보다, 작은 모델 PoC와 Qwen 계열 compatibility 확인 후보로 둔다.

# Decision Rule

현재 우선순위:

1. LLaMA-Factory로 30B/72B regression과 480B calibration을 진행한다.
2. 480B가 load 단계에서 반복 실패하면 HF/TRL load-only와 LLaMA-Factory load-only를 비교한다.
3. load memory 문제가 framework 구조 문제로 보이면 ms-swift Megatron 또는 NeMo를 다음 후보로 올린다.
4. Axolotl/torchtune은 중간 대체 경로와 학습용 비교 대상으로 둔다.

# Related Concepts

- [LLaMA-Factory Basics](llamafactory_basics.md)
- [DeepSpeed ZeRO Basics](deepspeed_zero_basics.md)
- [Distributed Training Basics](distributed_training_basics.md)
- [B200 480B FP8 Framework Matrix Experiments](../repos/AegisLM/docs/FRAMEWORK_MATRIX_EXPERIMENTS.md)

# Citations

- [TRL SFT Trainer](https://huggingface.co/docs/trl/en/sft_trainer)
- [Axolotl Multi-GPU docs](https://docs.axolotl.ai/docs/multi-gpu.html)
- [torchtune end-to-end flow](https://pytorch.org/torchtune/0.4/tutorials/e2e_flow.html)
- [NVIDIA NeMo Qwen3 guide](https://docs.nvidia.com/nemo-framework/user-guide/25.09/llms/qwen3.html)
- [ms-swift Megatron quick start](https://swift.readthedocs.io/en/latest/Megatron-SWIFT/Quick-start.html)
- [Unsloth Qwen3 guide](https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune)
