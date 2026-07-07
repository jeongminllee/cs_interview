---
type: Study Note
title: project_Nurilab Library Notes
description: project_Nurilab malicious-code-detection pipeline에서 쓰이는 Python 표준/데이터/ML 라이브러리의 역할.
tags: [project-nurilab, malware-analysis, static-analysis, libraries]
timestamp: 2026-07-03
status: active
---

# Summary

project_Nurilab는 malicious-code-detection 목적의 분석 파이프라인이다. AegisLM fine-tuning은 이 목적을 더 강한 LLM reviewer로 확장하기 위한 학습 축이고, project_Nurilab는 실제 코드 분석과 report 생성 축을 담당한다.

직접 의존성:

```text
requests
numpy
pandas
scikit-learn
matplotlib
```

코드에서 중요한 표준 라이브러리:

```text
ast
re
json
subprocess
dataclasses
pathlib
```

# Static Analysis Layer

## `ast`

Python source를 abstract syntax tree로 파싱한다. 문자열 검색보다 구조적으로 function call, import, assignment 등을 분석할 수 있다.

프로젝트 역할:

- suspicious call detection
- Python syntax parse 가능 여부 확인
- file별 static finding 생성

공부 포인트:

- `ast.parse()`
- `ast.NodeVisitor`
- call/import/assignment node 구조

## `re`

Regular expression 기반 pattern matching에 사용한다.

프로젝트 역할:

- secret-like pattern 탐지
- suspicious string/function pattern 탐지
- AegisLM redaction policy 이해와 연결

주의:

- regex는 빠르고 단순하지만 false positive/false negative가 생긴다.
- 보안 데이터셋에서는 실제 secret 값을 보존하지 않고 pattern signal만 남기는 방향이 안전하다.

# LLM Review Layer

## `requests`

HTTP API 호출에 쓰인다. project_Nurilab에서는 local/remote LLM review endpoint를 호출하는 역할과 연결된다.

공부 포인트:

- timeout 설정
- status code 처리
- JSON request/response
- retry 정책
- token/secret을 log에 남기지 않는 습관

# Data and Evaluation Layer

## `numpy`

수치 계산의 기본 배열 라이브러리다. metric 계산, vectorized operation, 통계 요약의 기반으로 쓸 수 있다.

## `pandas`

표 형태 데이터를 다룬다. scan result, finding list, evaluation result를 CSV/DataFrame으로 분석할 때 유용하다.

## `scikit-learn`

전통적인 ML과 metric/evaluation 도구를 제공한다. malicious-code-detection에서 baseline classifier, precision/recall/F1, train/test split, confusion matrix 같은 평가에 연결할 수 있다.

## `matplotlib`

시각화 라이브러리다. loss curve, finding distribution, evaluation metric chart를 보고서에 넣을 때 사용할 수 있다.

# How It Connects To AegisLM

project_Nurilab와 AegisLM의 관계:

```text
project_Nurilab
-> code collection/static analysis/report
-> malicious-code-detection task definition

AegisLM
-> security dataset preprocessing
-> LLM fine-tuning
-> stronger LLM reviewer/evaluator candidate
```

즉, project_Nurilab는 “무엇을 탐지하고 보고할 것인가”를 보여주고, AegisLM은 “그 판단을 LLM이 더 잘 하도록 어떻게 학습시킬 것인가”를 담당한다.

# Study Questions

- AST 기반 finding과 LLM 기반 finding은 어떻게 다르게 검증해야 하는가?
- regex secret detector의 false positive를 dataset label로 넣어도 되는가?
- LLM review 결과를 pandas/scikit-learn metric으로 평가하려면 ground truth를 어떻게 만들어야 하는가?
- report generator는 사람이 읽을 summary와 machine-readable JSON 중 무엇을 source of truth로 삼아야 하는가?

# Related Concepts

- [MalwareAnalysisLLM Library Stack Map](malwareanalysisllm_library_stack_map.md)
- [Security Datasets](../data/security_datasets.md)
- [AegisLM Training Libraries](aegislm_training_libraries.md)
- [Fine-Tuning Framework Comparison Basics](../fundamentals/finetuning_framework_comparison.md)

# Citations

- [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [NumPy absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)
- [matplotlib documentation](https://matplotlib.org/stable/)
