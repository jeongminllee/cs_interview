---
type: Study Note
title: AegisLM Training Libraries
description: AegisLM/MalwareAnalysisLLM 데이터, 모델 다운로드, schema validation, logging에 직접 쓰이는 Python 라이브러리 해설.
tags: [aegislm, libraries, datasets, transformers, wandb, jsonschema]
timestamp: 2026-07-03
status: active
---

# Summary

이 문서는 AegisLM/MalwareAnalysisLLM 코드가 직접 import하거나 `pyproject.toml`에 직접 의존성으로 둔 라이브러리를 프로젝트 관점에서 해설한다.

직접 의존성:

```text
datasets
huggingface-hub
jsonschema
torchao
transformers
wandb
```

서버 training 환경에서는 여기에 PyTorch, LLaMA-Factory, DeepSpeed, PEFT가 런타임으로 결합된다.

# `datasets`

## What It Is

Hugging Face Datasets는 Hub나 local file에서 dataset을 불러오고 split/row를 다루는 라이브러리다.

## Where We Use It

프로젝트에서는 `build_security_dataset.py`와 `aegislm/datasets/security_builder.py` 흐름에서 Hugging Face 보안 데이터셋을 받아 canonical JSONL로 변환하는 데 사용한다.

대표 source:

- `rezaduty/cybersecurity-qa-v2`
- `Rowden/CybersecurityQAA`
- `bstee615/diversevul`
- `DynaOuchebara/BigVul`

## Project Pain Point

처음에는 `rezaduty/cybersecurity-qa-v2`가 `datasets.load_dataset()` 경로에서 실패했다. 그래서 HF Hub JSONL 직접 로딩 fallback을 추가했다. 여기서 배울 점은 dataset library가 편하지만, source별 schema와 파일 구조 문제를 반드시 방어해야 한다는 것이다.

## What To Study

- `load_dataset()`
- split 선택
- streaming/cache
- row schema inspection
- 실패 시 fallback loader 설계

# `huggingface-hub`

## What It Is

Hugging Face Hub의 model/dataset repository에 접근하는 Python client다.

## Where We Use It

`download_hf_model.py`에서 model snapshot 파일 목록을 확인하고, base model을 `model/base/` 아래로 다운로드하는 데 사용한다.

## Project Pain Point

480B FP8 model은 shard가 크다. 따라서 다운로드 전 예상 용량, local shard 개수, 누락 shard 여부를 확인해야 한다. 단, partial shard download는 training memory 해결책이 아니다. full checkpoint training에는 필요한 shard가 모두 있어야 한다.

## What To Study

- `HfApi`
- `snapshot_download()`
- allow/ignore patterns
- local cache와 target directory
- gated/private model에서 `HF_TOKEN` 처리

# `transformers`

## What It Is

Pretrained model, tokenizer, config, generation/training ecosystem의 중심 라이브러리다.

## Where We Use It

LLaMA-Factory 내부에서 Qwen model loading, tokenizer, chat template, model forward가 Transformers 계열로 이어진다. AegisLM inference baseline에서도 model/tokenizer loading 개념이 필요하다.

## Project Pain Point

480B FP8는 checkpoint loading 단계에서 실패 이력이 있다. 이때 `from_pretrained()`가 shard를 어떻게 읽고 dtype/device를 어떻게 결정하는지 이해해야 torchrun 로그만 보고 잘못 판단하지 않는다.

## What To Study

- `AutoTokenizer`
- `AutoModelForCausalLM`
- `from_pretrained()`
- tokenizer chat template
- Qwen architecture와 MoE/dtype 처리

# `torchao`

## What It Is

PyTorch native quantization/sparsity/low precision workflow를 다루는 라이브러리다.

## Where We Use It

현재 AegisLM 직접 의존성에 포함되어 있으며, FP8/quantization 개념을 이해하는 데 연결된다. 실제 480B FP8 training path에서 어떤 quantization runtime이 쓰이는지는 서버 config와 model loader 기준으로 재확인해야 한다.

## Project Pain Point

FP8 checkpoint라고 해서 training memory가 단순히 checkpoint file size만큼 줄어드는 것은 아니다. loading buffer, dequant/compute dtype, optimizer state, adapter dtype이 별도로 작동할 수 있다.

## What To Study

- float8/int8 weight-only 또는 activation quantization 개념
- Transformers TorchAoConfig
- quantized checkpoint와 training runtime memory 차이

# `jsonschema`

## What It Is

JSON object가 정해진 schema를 만족하는지 검증하는 라이브러리다.

## Where We Use It

AegisLM에서 dataset record와 model output contract를 검증한다.

대표 위치:

- `aegislm/datasets/validation.py`
- `aegislm/evaluation/validation.py`
- `aegislm/schemas.py`

## Project Pain Point

보안 데이터는 source가 다양하고 target output이 민감할 수 있다. schema validation은 “형식이 맞는가”를 확인하고, safety policy validation은 “학습 target으로 넣어도 되는가”를 별도로 확인한다.

## What To Study

- `validate()`
- `Draft202012Validator`
- `ValidationError`
- schema와 safety policy의 역할 분리

# `wandb`

## What It Is

학습 experiment tracking 도구다.

## Where We Use It

LLaMA-Factory YAML의 `report_to: wandb`와 run script의 `WANDB_*` 환경변수로 loss, step, learning rate, config를 기록한다.

## Project Pain Point

480B에서는 model artifact upload와 gradient watch가 부담이다. 그래서 기본값은 다음이다.

```bash
WANDB_LOG_MODEL=false
WANDB_WATCH=false
```

W&B는 학습 지표를 보고, cgroup/memory watcher는 system kill 원인을 본다. 둘을 섞어 생각하면 안 된다.

# Related Concepts

- [MalwareAnalysisLLM Library Stack Map](malwareanalysisllm_library_stack_map.md)
- [Datasets and SFT Format Basics](../fundamentals/datasets_sft_format_basics.md)
- [Transformers SFT Basics](../fundamentals/transformers_sft_basics.md)
- [W&B and Telemetry Basics](../fundamentals/wandb_telemetry_basics.md)

# Citations

- [Hugging Face Datasets loading](https://huggingface.co/docs/datasets/en/loading)
- [Hugging Face Hub download guide](https://huggingface.co/docs/huggingface_hub/en/guides/download)
- [Transformers tokenizer docs](https://huggingface.co/docs/transformers/main_classes/tokenizer)
- [Transformers torchao quantization](https://huggingface.co/docs/transformers/en/quantization/torchao)
- [jsonschema validation docs](https://python-jsonschema.readthedocs.io/en/stable/validate/)
- [W&B PyTorch integration](https://docs.wandb.ai/models/integrations/pytorch)
