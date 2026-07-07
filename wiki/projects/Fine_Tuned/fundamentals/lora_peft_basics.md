---
type: Study Note
title: LoRA and PEFT Basics
description: full fine-tuning과 LoRA/PEFT adapter fine-tuning의 차이, adapter checkpoint, dtype 이슈 기본기.
tags: [finetuning, lora, peft, adapter, basics]
timestamp: 2026-07-03
status: active
---

# Summary

PEFT는 Parameter-Efficient Fine-Tuning의 약자다. 큰 pretrained model 전체를 업데이트하지 않고, 일부 작은 trainable parameter만 학습해서 비용을 줄이는 접근이다.

LoRA는 대표적인 PEFT 기법이다. 우리 B200 프로젝트는 480B full fine-tuning이 아니라 LoRA SFT를 목표로 한다.

# Full Fine-Tuning

Full fine-tuning은 base model의 거의 모든 parameter를 업데이트한다.

장점:

- 모델 전체가 task에 맞게 변할 수 있다.
- 충분한 데이터와 자원이 있으면 강력하다.

단점:

- gradient와 optimizer state가 전체 parameter에 대해 필요하다.
- checkpoint가 매우 크다.
- 480B급 모델에서는 현실적인 비용이 매우 높다.

# LoRA Fine-Tuning

LoRA는 기존 weight matrix를 직접 크게 바꾸지 않고, 작은 low-rank adapter를 추가해 학습한다.

핵심 감각:

```text
base model weight: frozen
LoRA adapter weight: trainable
```

이렇게 하면 학습해야 할 parameter 수가 크게 줄고, gradient/optimizer state 메모리도 줄어든다.

# LoRA Hyperparameters

대표 설정:

- rank `r`: adapter의 표현 용량
- alpha: LoRA update scaling
- target modules: LoRA를 붙일 layer/module
- dropout: adapter 학습 중 regularization

LLaMA-Factory의 `lora_target: all`은 가능한 linear layer 전반에 LoRA를 적용하겠다는 뜻으로 이해하면 된다. 모델과 framework가 실제 어떤 module을 잡는지는 config와 model architecture에 따라 확인해야 한다.

# Adapter Checkpoint

LoRA 학습 결과는 base model 전체가 아니라 adapter weight 중심으로 저장된다.

장점:

- 저장 용량이 작다.
- 같은 base model에 여러 adapter를 붙여 비교할 수 있다.
- Git에 올리지 않아야 할 artifact이지만 base model보다는 이동이 쉽다.

주의:

- adapter만으로는 inference가 되지 않는다. 같은 base model이 필요하다.
- base model revision이 바뀌면 adapter compatibility를 다시 확인해야 한다.
- ZeRO-3 환경에서는 checkpoint save/load 경로가 더 복잡해질 수 있다.

# Dtype And PEFT

우리 프로젝트에서 중요한 지점은 dtype이다.

30B/72B ZeRO-3 실패는 다음 조합에서 발생했다.

```text
DeepSpeed 0.19.2
ZeRO-3
PEFT LoRA
bf16 base model
```

해석:

- base model parameter와 LoRA adapter parameter가 mixed dtype persistent parameter group에 들어갔을 가능성이 있다.
- DeepSpeed가 all-gather output buffer dtype을 첫 parameter dtype으로만 만들면서 mismatch가 났다.
- PR #8073 방식 patch는 parameter별 dtype에 맞는 buffer를 만들도록 고치는 방향이다.

# Project Connection

우리의 480B 목표는 다음 구조다.

```text
base model: model/base/qwen3-coder-480b-a35b-instruct-fp8
adapter output: model/adapters/qwen3-coder-480b-fp8/lora/...
training method: LoRA SFT
framework: LLaMA-Factory + PEFT + DeepSpeed
```

따라서 학습 성공 여부를 볼 때 base model weight가 바뀌었는지보다 adapter checkpoint가 정상 생성됐는지를 봐야 한다.

# Related Concepts

- [PyTorch Training Basics](pytorch_training_basics.md)
- [DeepSpeed ZeRO Basics](deepspeed_zero_basics.md)
- [LLaMA-Factory Basics](llamafactory_basics.md)
- [DeepSpeed ZeRO-3 Dtype Mismatch Troubleshooting](../repos/AegisLM/docs/DEEPSPEED_ZERO3_DTYPE_MISMATCH.md)

# Citations

- [Hugging Face PEFT documentation](https://huggingface.co/docs/peft/en/index)
- [Hugging Face PEFT LoRA reference](https://huggingface.co/docs/peft/package_reference/lora)
- [Transformers PEFT integration](https://huggingface.co/docs/transformers/en/peft)
