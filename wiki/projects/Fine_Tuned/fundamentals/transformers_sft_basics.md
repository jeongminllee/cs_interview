---
type: Study Note
title: Transformers SFT Basics
description: Hugging Face Transformers, tokenizer, causal LM, chat template, SFT 데이터 구조 기본기.
tags: [finetuning, transformers, sft, tokenizer, basics]
timestamp: 2026-07-03
status: active
---

# Summary

Transformers는 pretrained LLM을 불러오고 tokenizer와 model forward를 다루는 중심 라이브러리다. LLaMA-Factory를 사용해도 내부적으로는 Hugging Face Transformers의 model loading, tokenizer, Trainer 계열 기능을 많이 사용한다.

SFT는 Supervised Fine-Tuning의 약자다. 이미 학습된 causal language model에 instruction-response 예시를 추가로 학습시켜, 원하는 응답 형식을 더 잘 따르게 만드는 과정이다.

# Tokenizer

Tokenizer는 사람이 읽는 문자열을 model이 처리할 수 있는 token id로 바꾼다.

주요 출력:

- `input_ids`: token id 배열
- `attention_mask`: 실제 token과 padding을 구분하는 mask
- labels: causal LM 학습에서 정답으로 사용할 token id

LLM은 원문 문자열을 직접 읽지 않는다. 항상 tokenizer가 만든 token sequence를 읽는다.

# Causal Language Modeling

Causal LM은 앞 token들을 보고 다음 token을 예측한다.

SFT도 본질적으로는 다음 token 예측이다. 차이는 학습 데이터가 일반 텍스트가 아니라 `instruction -> response` 형식이라는 점이다.

예:

```text
user: 이 코드의 취약점을 설명해줘.
assistant: 입력 검증 없이 command를 실행하므로 command injection 위험이 있습니다.
```

모델은 assistant 응답 token들을 잘 예측하도록 학습된다.

# from_pretrained

`from_pretrained`는 pretrained model이나 tokenizer를 local path 또는 Hugging Face Hub에서 불러온다.

대략의 흐름:

1. config를 읽는다.
2. tokenizer 파일을 읽는다.
3. model class를 결정한다.
4. weight shard를 읽는다.
5. dtype과 device 배치 정책에 따라 tensor를 만든다.

우리 480B 문제는 이 중 weight shard loading 단계와 관련이 깊다. train step까지 가기 전에 checkpoint loading 중 process RSS가 크게 늘 수 있다.

# Chat Template

Chat template은 `system/user/assistant` 메시지 목록을 모델이 기대하는 단일 문자열 또는 token sequence로 바꾸는 규칙이다.

모델마다 기대하는 prompt 형식이 다르다. Qwen 계열, Llama 계열, Mistral 계열은 special token과 role 표기가 다를 수 있다. 따라서 template mismatch는 학습 품질을 크게 떨어뜨릴 수 있다.

LLaMA-Factory YAML의 `template: qwen3_nothink` 같은 설정은 이 변환 규칙을 고르는 역할을 한다.

# SFT Data Shape

우리 프로젝트의 LLaMA-Factory export는 Alpaca-style column을 사용한다.

```json
{
  "system": "system prompt",
  "instruction": "user prompt",
  "input": "",
  "output": "assistant answer"
}
```

이 구조는 학습 전에 template을 거쳐 하나의 대화 문자열로 합쳐지고, tokenizer를 거쳐 token id가 된다.

# Project Connection

현재 AegisLM 데이터 흐름:

```text
raw security sources
-> AegisLM canonical JSONL
-> train/validation/test split
-> LLaMA-Factory Alpaca-style export
-> dataset_info.json registration
-> LLaMA-Factory SFT
```

AegisLM은 데이터의 의미와 안전 변환을 책임진다. Transformers/LLaMA-Factory는 그 데이터를 token sequence로 바꿔 학습한다.

# Related Concepts

- [PyTorch Training Basics](pytorch_training_basics.md)
- [Datasets and SFT Format Basics](datasets_sft_format_basics.md)
- [LLaMA-Factory Basics](llamafactory_basics.md)

# Citations

- [Hugging Face Transformers: Chat templates](https://huggingface.co/docs/transformers/en/chat_templating)
- [Hugging Face Transformers: Tokenizer](https://huggingface.co/docs/transformers/main_classes/tokenizer)
- [Hugging Face TRL: SFT Trainer](https://huggingface.co/docs/trl/en/sft_trainer)
