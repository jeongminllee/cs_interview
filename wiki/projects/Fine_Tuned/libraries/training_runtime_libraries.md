---
type: Study Note
title: Training Runtime Libraries
description: MalwareAnalysisLLM의 LLaMA-Factory, PEFT/LoRA, DeepSpeed, torchrun, Transformers Trainer 계열 런타임 해설.
tags: [llamafactory, deepspeed, peft, torchrun, training-runtime]
timestamp: 2026-07-03
status: active
---

# Summary

이 문서는 “학습을 실제로 돌리는 런타임”을 설명한다. AegisLM은 데이터와 안전 변환을 담당하지만, 실제 SFT/LoRA training loop는 LLaMA-Factory가 Transformers, PEFT, DeepSpeed, PyTorch distributed를 묶어서 실행한다.

# Runtime Flow

```text
bash run script
-> llamafactory-cli train config.yaml
-> LLaMA-Factory launcher
-> torchrun --nproc_per_node 4
-> per-rank Python process
-> Transformers model/tokenizer loading
-> PEFT LoRA adapter injection
-> DeepSpeed ZeRO runtime
-> W&B + local telemetry logging
```

# LLaMA-Factory

## Role

LLaMA-Factory는 현재 프로젝트의 baseline training framework다. 직접 Trainer 코드를 작성하지 않고 YAML로 SFT/LoRA/DeepSpeed/W&B를 연결한다.

## Project Inputs

대표 입력:

- model path: `model/base/qwen3-coder-480b-a35b-instruct-fp8`
- dataset name: `aegislm_security_sft_train_full`
- template: `qwen3_nothink`
- finetuning type: `lora`
- DeepSpeed config: `configs/deepspeed/...json`

## What To Study

- YAML field가 내부 trainer argument로 어떻게 바뀌는지
- dataset name lookup이 `dataset_info.json`에 의존하는 방식
- run script와 LLaMA-Factory launcher의 경계

# PEFT / LoRA

## Role

PEFT는 base model 위에 trainable adapter를 붙인다. LoRA는 그중 low-rank adapter를 쓰는 방식이다.

## Project Meaning

480B에서 full fine-tuning 대신 LoRA를 쓰는 이유:

- gradient/optimizer state를 adapter 중심으로 줄인다.
- adapter checkpoint만 저장해 output을 작게 유지한다.
- base model은 `model/base/` 아래 local artifact로 유지한다.

## Failure Connection

30B/72B ZeRO-3 dtype mismatch는 PEFT LoRA adapter parameter와 bf16 base parameter가 DeepSpeed all-gather 경로에서 섞인 문제로 해석된다.

# DeepSpeed

## Role

DeepSpeed는 ZeRO를 통해 distributed training memory를 줄인다.

## Project Use

- ZeRO-2: 30B/72B diagnostic smoke에서 통과한 baseline
- ZeRO-3: 480B full run에 필요한 후보, dtype patch regression 필요

## Failure Connection

30B/72B:

```text
TypeError: output tensor must have the same type as input tensor
```

원인 후보는 DeepSpeed 0.19.2 ZeRO-3 all-gather buffer dtype bug다. upstream PR #8073 방식 patch를 적용해 regression을 확인한다.

480B:

```text
checkpoint loading 중 SIGKILL(-9)
```

이 문제는 dtype mismatch와 분리한다. cgroup memory, rank별 RSS, loader 초기화 순서, external kill 가능성을 telemetry로 본다.

# torchrun

## Role

`torchrun`은 PyTorch distributed process launcher다.

4-GPU B200 run에서:

```text
--nproc_per_node 4
```

는 4개 distributed rank process를 의미한다. CPU core 4개를 뜻하지 않는다.

## What To Study

- rank/local_rank/world_size
- one process per GPU
- root cause rank와 cleanup SIGTERM 구분
- `SIGKILL(-9)`와 Python exception의 차이

# Transformers Trainer / Accelerate 계열

현재 프로젝트에서 직접 손으로 쓰는 API는 아니다. LLaMA-Factory 내부 training stack의 하위 계층으로 이해한다.

공부 포인트:

- SFT trainer가 batch를 model forward로 넣는 방식
- PEFT adapter를 trainable parameter로 등록하는 방식
- DeepSpeed config가 trainer runtime에 전달되는 방식

# Related Concepts

- [MalwareAnalysisLLM Library Stack Map](malwareanalysisllm_library_stack_map.md)
- [LLaMA-Factory Basics](../fundamentals/llamafactory_basics.md)
- [LoRA and PEFT Basics](../fundamentals/lora_peft_basics.md)
- [Distributed Training Basics](../fundamentals/distributed_training_basics.md)
- [DeepSpeed ZeRO Basics](../fundamentals/deepspeed_zero_basics.md)
- [DeepSpeed ZeRO-3 Dtype Mismatch Troubleshooting](../repos/AegisLM/docs/DEEPSPEED_ZERO3_DTYPE_MISMATCH.md)

# Citations

- [LLaMA-Factory GitHub](https://github.com/hiyouga/LLaMA-Factory)
- [Transformers PEFT integration](https://huggingface.co/docs/transformers/en/peft)
- [PEFT LoRA reference](https://huggingface.co/docs/peft/package_reference/lora)
- [DeepSpeed ZeRO docs](https://deepspeed.readthedocs.io/en/latest/zero3.html)
- [PyTorch torchrun docs](https://docs.pytorch.org/docs/stable/elastic/run.html)
- [TRL SFT Trainer](https://huggingface.co/docs/trl/en/sft_trainer)
