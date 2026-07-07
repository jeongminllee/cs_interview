---
type: Study Note
title: DeepSpeed ZeRO Basics
description: ZeRO가 필요한 이유, ZeRO-1/2/3 차이, offload와 대형 모델 학습에서의 tradeoff.
tags: [finetuning, deepspeed, zero, distributed-training, basics]
timestamp: 2026-07-03
status: active
---

# Summary

DeepSpeed는 대형 모델 학습을 위한 분산 학습 최적화 라이브러리다. 그중 ZeRO는 data parallel 학습에서 중복 저장되는 model state를 나눠 메모리 사용량을 줄이는 핵심 기능이다.

우리 프로젝트에서 DeepSpeed가 중요한 이유는 480B급 모델은 일반 DDP 방식으로는 model state 중복이 너무 크기 때문이다.

# Why ZeRO Exists

일반 DDP에서는 각 rank가 많은 학습 상태를 중복해서 가진다.

대표 model state:

- optimizer states
- gradients
- parameters

ZeRO는 이 중복을 data-parallel process들 사이에 partition해서 각 GPU/process가 들고 있는 양을 줄인다.

# ZeRO Stages

## ZeRO-1

Optimizer state를 partition한다.

효과:

- Adam 계열 optimizer state 메모리를 줄인다.
- parameter와 gradient는 여전히 중복될 수 있다.

## ZeRO-2

Optimizer state와 gradient를 partition한다.

효과:

- backward 후 gradient 메모리까지 줄인다.
- 30B/72B smoke에서 ZeRO-2가 통과한 것은 기본 training path가 정상임을 보여줬다.

## ZeRO-3

Optimizer state, gradient, parameter를 모두 partition한다.

효과:

- 대형 모델에서 가장 큰 메모리 절감이 가능하다.
- parameter를 필요할 때 gather/scatter해야 하므로 communication과 implementation complexity가 커진다.
- checkpoint loading, all-gather, save/load path에서 bug surface가 넓어진다.

# CPU Offload

Offload는 일부 state를 GPU가 아니라 CPU RAM 또는 disk에 두는 방식이다.

장점:

- GPU VRAM 부담을 줄인다.

단점:

- CPU RAM 사용량이 늘어난다.
- PCIe/NVLink/IO 병목이 생길 수 있다.
- container cgroup memory limit에 걸릴 수 있다.

# ZeRO-3 And Dtype Mismatch

우리 30B/72B ZeRO-3 실패는 optimizer step 이후 persistent parameter all-gather에서 발생했다.

핵심 해석:

- ZeRO-3는 parameter를 partition하고 필요 시 gather한다.
- PEFT LoRA와 bf16 base model 조합에서 mixed dtype parameter가 gather 대상에 섞일 수 있다.
- DeepSpeed 0.19.2의 해당 경로가 첫 parameter dtype만 보고 output buffer를 만들면서 mismatch가 난 것으로 본다.

# ZeRO-3 And 480B

480B에서는 ZeRO-3가 필요하지만, ZeRO-3만으로 checkpoint loading CPU RSS가 자동으로 줄어든다고 단정하면 안 된다.

봐야 할 지점:

- ZeRO partition이 적용되기 전 각 rank가 checkpoint를 얼마나 읽는지
- `from_pretrained`와 DeepSpeed initialization 순서
- rank별 RSS
- cgroup `memory.current`와 `memory.events`

# Project Defaults

현재 정책:

- 30B/72B: ZeRO-2는 diagnostic baseline으로 통과 확인
- 30B/72B ZeRO-3: DeepSpeed dtype patch regression 필요
- 480B FP8: ZeRO-3 patched config로 calibration 후 full run 승격
- memory watcher: observe-only, 학습 process kill 금지

# Related Concepts

- [Distributed Training Basics](distributed_training_basics.md)
- [LoRA and PEFT Basics](lora_peft_basics.md)
- [LLaMA-Factory Basics](llamafactory_basics.md)
- [DeepSpeed ZeRO-3 Dtype Mismatch Troubleshooting](../repos/AegisLM/docs/DEEPSPEED_ZERO3_DTYPE_MISMATCH.md)

# Citations

- [DeepSpeed ZeRO documentation](https://deepspeed.readthedocs.io/en/latest/zero3.html)
- [DeepSpeed ZeRO tutorial](https://www.deepspeed.ai/tutorials/zero/)
- [Hugging Face Accelerate DeepSpeed guide](https://huggingface.co/docs/accelerate/v0.10.0/en/deepspeed)
