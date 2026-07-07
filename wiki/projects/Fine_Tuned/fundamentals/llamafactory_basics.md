---
type: Study Note
title: LLaMA-Factory Basics
description: LLaMA-Factory가 담당하는 역할, YAML config, dataset registration, AegisLM과의 경계 기본기.
tags: [finetuning, llamafactory, sft, lora, basics]
timestamp: 2026-07-03
status: active
---

# Summary

LLaMA-Factory는 LLM fine-tuning을 YAML config 중심으로 실행하게 해주는 framework다. 직접 PyTorch Trainer 코드를 작성하지 않고도 SFT, LoRA, DeepSpeed, dataset registration, logging을 연결할 수 있다.

우리 프로젝트에서는 LLaMA-Factory가 training loop를 맡고, AegisLM은 dataset preprocessing과 안전 변환을 맡는다.

# Responsibility Boundary

## AegisLM

AegisLM이 담당하는 것:

- raw security dataset 수집
- 안전한 preprocessing
- canonical JSONL schema
- train/validation/test split
- LLaMA-Factory export
- evaluation harness

## LLaMA-Factory

LLaMA-Factory가 담당하는 것:

- tokenizer/model loading
- chat template 적용
- SFT training loop
- PEFT LoRA adapter 구성
- DeepSpeed integration
- W&B logging
- adapter/checkpoint save

# Main YAML Fields

중요 필드:

```yaml
stage: sft
finetuning_type: lora
model_name_or_path: model/base/qwen3-coder-480b-a35b-instruct-fp8
template: qwen3_nothink
dataset: aegislm_security_sft_train_full
deepspeed: configs/deepspeed/ds_z3_b200.json
report_to: wandb
run_name: malware-analysis-qwen3-coder-480b-fp8-lora-full-z3-patched
```

의미:

- `stage: sft`: supervised fine-tuning 실행
- `finetuning_type: lora`: full fine-tuning이 아니라 LoRA adapter 학습
- `model_name_or_path`: base model 위치
- `template`: tokenizer/chat formatting 규칙
- `dataset`: `dataset_info.json`에 등록된 dataset name
- `deepspeed`: DeepSpeed JSON config
- `report_to`: logging backend
- `run_name`: W&B run 이름

# Dataset Registration

LLaMA-Factory는 dataset name을 보고 `LLaMA-Factory/data/dataset_info.json`에서 실제 file을 찾는다.

따라서 다음 두 단계가 모두 필요하다.

1. JSON dataset file 생성
2. `dataset_info.json` 등록

file만 있고 registration이 없으면 YAML에서 dataset name을 찾지 못한다.

# Run Script Role

우리 프로젝트의 shell runner는 다음을 수행한다.

- `.env` 값은 직접 포함하지 않는다.
- CUDA device를 지정한다.
- W&B 관련 기본값을 설정한다.
- memory watcher를 observe-only로 켠다.
- `llamafactory-cli train <config.yaml>`을 실행한다.

Python helper script는 dataset export나 patch check 같은 준비 작업에 쓰고, 실제 training은 bash runner로 실행한다.

# Why LLaMA-Factory First

현재 baseline으로 LLaMA-Factory를 쓰는 이유:

- YAML 중심이라 팀원이 config를 리뷰하기 쉽다.
- SFT/LoRA/DeepSpeed/W&B가 이미 연결되어 있다.
- AegisLM과 책임 경계가 깔끔하다.
- 실패 로그가 반복 가능하다.

단, 480B checkpoint loading 문제가 LLaMA-Factory/Transformers/DeepSpeed 초기화 순서에서 계속 발생하면 NeMo나 ms-swift Megatron 같은 large-model-native framework로 비교해야 한다.

# Related Concepts

- [Datasets and SFT Format Basics](datasets_sft_format_basics.md)
- [LoRA and PEFT Basics](lora_peft_basics.md)
- [DeepSpeed ZeRO Basics](deepspeed_zero_basics.md)
- [W&B and Telemetry Basics](wandb_telemetry_basics.md)
- [LLaMA-Factory + W&B Fine-Tuning Integration](../training/llamafactory_wandb_finetuning.md)

# Citations

- [LLaMA-Factory GitHub](https://github.com/hiyouga/LLaMA-Factory)
- [LLaMA-Factory documentation example](https://llamafactory.readthedocs.io/en/latest/advanced/best_practice/gpt-oss.html)
