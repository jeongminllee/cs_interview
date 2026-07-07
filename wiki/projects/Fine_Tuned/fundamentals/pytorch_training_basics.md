---
type: Study Note
title: PyTorch Training Basics
description: LLM fine-tuning을 이해하기 위한 tensor, dtype, device, autograd, training step 기본기.
tags: [finetuning, pytorch, basics, llm]
timestamp: 2026-07-03
status: active
---

# Summary

PyTorch는 현재 LLM 학습 스택의 가장 아래층이다. LLaMA-Factory, TRL, Axolotl 같은 프레임워크를 쓰더라도 실제 학습은 결국 PyTorch tensor 연산, autograd, optimizer step 위에서 돌아간다.

우리 프로젝트에서 PyTorch 기본기를 이해해야 하는 이유는 단순하다.

- `bf16`, `fp8`, `fp16` 같은 dtype 차이가 메모리와 오류에 직접 영향을 준다.
- GPU VRAM과 CPU RAM 사용량은 tensor가 어느 device에 올라가느냐에 따라 달라진다.
- `loss.backward()`와 `optimizer.step()`이 어디서 일어나는지 알아야 DeepSpeed ZeRO 오류를 해석할 수 있다.

# Core Ideas

## Tensor

Tensor는 PyTorch의 기본 데이터 단위다. LLM 학습에서는 token id, attention mask, model weight, gradient, optimizer state, activation이 모두 tensor로 표현된다.

중요한 속성:

- `shape`: tensor 크기
- `dtype`: 숫자 표현 방식
- `device`: CPU에 있는지 GPU에 있는지
- `requires_grad`: gradient를 추적할지 여부

## Dtype

dtype은 숫자를 저장하는 방식이다. 같은 parameter라도 dtype에 따라 메모리 사용량과 연산 방식이 달라진다.

대표 dtype:

- `float32`: 안정적이지만 메모리를 많이 쓴다.
- `float16`: 메모리는 적게 쓰지만 numerical stability 이슈가 있을 수 있다.
- `bfloat16`: 큰 모델 학습에서 자주 쓰는 mixed precision dtype이다.
- `fp8`: 더 작지만 framework와 hardware 지원 조건이 더 까다롭다.

우리 상황에서 30B/72B ZeRO-3 dtype mismatch는 단순한 메모리 문제가 아니라, 서로 다른 dtype tensor를 DeepSpeed all-gather buffer에 모으는 과정에서 생긴 문제로 본다.

## Device

Tensor는 CPU나 GPU에 올라갈 수 있다.

```python
x = x.to("cuda:0")
model = model.to("cuda:0")
```

LLM 학습에서는 model weight와 activation은 주로 GPU VRAM을 쓰고, checkpoint loading이나 offload는 CPU RAM을 크게 쓸 수 있다.

## Autograd

Autograd는 forward 연산 그래프를 기록하고, loss에서 parameter까지 gradient를 자동 계산하는 PyTorch 기능이다.

전형적인 training step:

```python
outputs = model(**batch)
loss = outputs.loss
loss.backward()
optimizer.step()
optimizer.zero_grad()
```

의미:

- forward: input을 넣고 prediction과 loss를 계산한다.
- backward: loss를 줄이기 위해 각 parameter가 어떻게 바뀌어야 하는지 gradient를 계산한다.
- optimizer step: 계산된 gradient로 parameter를 실제 업데이트한다.
- zero grad: 다음 batch에 gradient가 누적되지 않게 초기화한다.

# Training Terms

## Batch Size

한 번의 forward/backward에 들어가는 sample 수다. LLM에서는 sequence length까지 같이 생각해야 한다.

실제 메모리 사용량은 대략 다음에 영향을 받는다.

- per-device batch size
- sequence length
- hidden size
- activation checkpointing 여부
- optimizer state 저장 방식

## Gradient Accumulation

GPU 메모리 때문에 한 번에 큰 batch를 못 넣을 때, 작은 batch 여러 번의 gradient를 모은 뒤 optimizer step을 한 번 수행하는 방식이다.

예:

```text
per_device_train_batch_size = 1
GPU count = 4
gradient_accumulation_steps = 8
global batch = 1 * 4 * 8 = 32
```

## Step

일반적으로 training log의 step은 optimizer update 횟수다. gradient accumulation이 있으면 forward/backward 횟수보다 optimizer step 수가 적다.

## Epoch

전체 train dataset을 한 번 모두 보는 단위다. train sample이 332,807건이고 global batch가 32라면 1 epoch는 약 10,400 update step이다.

# Memory Use In Training

학습 중 메모리는 여러 종류로 나뉜다.

- model weights: base model parameter
- gradients: backward 후 생기는 parameter별 gradient
- optimizer states: Adam 계열에서 momentum/variance 등 추가 상태
- activations: backward를 위해 저장되는 중간 activation
- temporary buffers: all-gather, reduce-scatter, checkpoint loading buffer 등

LoRA는 base model weight 대부분을 frozen 상태로 두기 때문에 gradient와 optimizer state를 크게 줄인다. 하지만 base model weight 자체와 checkpoint loading 비용은 여전히 남는다.

# Project Connection

우리 B200 프로젝트에서 PyTorch 기본기는 이렇게 연결된다.

- 480B FP8 loading 문제: weight shard를 읽고 tensor로 만드는 단계의 CPU/GPU 메모리 사용을 봐야 한다.
- 30B/72B ZeRO-3 dtype 문제: optimizer step 후 DeepSpeed all-gather에서 dtype이 맞지 않았다.
- W&B loss: PyTorch training loop에서 계산한 loss가 logging backend로 넘어간 결과다.
- memory watcher: PyTorch tensor가 직접 보이지는 않지만 process RSS, GPU memory, cgroup memory로 간접 관찰한다.

# Related Concepts

- [Transformers SFT Basics](transformers_sft_basics.md)
- [LoRA and PEFT Basics](lora_peft_basics.md)
- [Distributed Training Basics](distributed_training_basics.md)
- [DeepSpeed ZeRO Basics](deepspeed_zero_basics.md)

# Citations

- [PyTorch: Learning PyTorch with Examples](https://docs.pytorch.org/tutorials/beginner/pytorch_with_examples.html)
- [PyTorch torchrun documentation](https://docs.pytorch.org/docs/stable/elastic/run.html)
