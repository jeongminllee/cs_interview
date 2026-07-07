---
type: Study Note
title: Datasets and SFT Format Basics
description: raw dataset, preprocessing, split, Alpaca-style SFT format, LLaMA-Factory dataset registration 기본기.
tags: [finetuning, dataset, sft, llamafactory, basics]
timestamp: 2026-07-03
status: active
---

# Summary

Fine-tuning에서 데이터는 model보다 먼저 안정화해야 한다. 모델 config가 맞아도 dataset field가 틀리거나 split이 섞이면 학습 결과를 믿기 어렵다.

우리 프로젝트는 보안 데이터셋을 바로 LLaMA-Factory에 넣지 않고, 먼저 AegisLM canonical JSONL로 정규화한 뒤 export한다.

# Raw Dataset

Raw dataset은 원본 그대로의 데이터다.

예:

- Hugging Face QA dataset
- DiverseVul
- BigVul
- CTF write-up markdown
- ZIP/source corpus

Raw dataset은 source마다 schema가 다르다. 어떤 dataset은 `question/answer`, 어떤 dataset은 `func_before/func_after`, 어떤 dataset은 markdown 본문과 file path가 핵심이다.

# Preprocessing

Preprocessing은 raw record를 학습 가능한 의미 단위로 바꾸는 과정이다.

우리 프로젝트의 핵심 전처리 원칙:

- 보안 분석 목적에 맞게 instruction을 만든다.
- unsafe payload나 secret-like 값은 필요하면 redaction한다.
- BigVul `func_after` 전체 patch code를 target output으로 복사하지 않는다.
- CTF write-up 전문을 assistant target으로 넣지 않는다.
- 모든 record를 공통 schema로 만든다.

# Split

Train/validation/test split은 모델 학습과 평가를 분리하기 위한 기본 절차다.

- train: model parameter 또는 adapter를 업데이트하는 데 사용
- validation: 학습 중 성능 확인과 early signal 확인
- test: 최종 평가용으로 남겨두는 데이터

기본 split 비율은 `0.8/0.1/0.1`, seed는 `42`를 사용한다.

# AegisLM Canonical JSONL

Canonical JSONL은 source가 달라도 같은 구조로 관리하기 위한 중간 포맷이다.

이 중간 포맷을 두는 이유:

- source별 schema 차이를 흡수한다.
- 안전 변환 정책을 한 곳에서 적용한다.
- LLaMA-Factory 외 다른 framework로도 export할 수 있다.
- split과 record id를 안정적으로 관리한다.

# Alpaca-Style SFT Format

LLaMA-Factory export는 Alpaca-style column을 사용한다.

```json
{
  "system": "system prompt",
  "instruction": "task instruction",
  "input": "optional context",
  "output": "expected assistant answer"
}
```

여기서 `output`은 모델이 학습해야 하는 assistant 응답이다. 민감한 원문, exploit narrative 전문, patch 전체를 그대로 넣는 것은 피한다.

# dataset_info.json

LLaMA-Factory는 dataset file만 있다고 자동으로 찾지 않는다. `dataset_info.json`에 dataset name과 file 정보를 등록해야 YAML의 `dataset` 필드에서 사용할 수 있다.

우리 full dataset 등록명:

```text
aegislm_security_sft_train_full
aegislm_security_sft_validation_full
```

YAML에서 dataset name이 틀리면 training은 시작 전에 dataset lookup에서 실패한다.

# Project Connection

현재 export/register 단계는 학습 자체보다 먼저 끝나야 하는 gate다.

확인할 것:

- train full JSON count
- validation full JSON count
- output file size
- skipped/ignored record count
- `dataset_info.json` 등록명

# Related Concepts

- [Transformers SFT Basics](transformers_sft_basics.md)
- [LLaMA-Factory Basics](llamafactory_basics.md)
- [Security Datasets](../data/security_datasets.md)

# Citations

- [Hugging Face TRL: SFT Trainer](https://huggingface.co/docs/trl/en/sft_trainer)
- [LLaMA-Factory GitHub](https://github.com/hiyouga/LLaMA-Factory)
