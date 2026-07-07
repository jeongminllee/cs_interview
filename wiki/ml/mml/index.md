---
type: Project
title: MML Book Study (Mathematics for Machine Learning)
description: 머신러닝에 필요한 핵심 수학 교과서인 Mathematics for Machine Learning을 완독하기 위한 학습 프로젝트 대시보드입니다.
tags: [mml, math, project]
timestamp: 2026-06-18
status: active
---

# Goal
* *Mathematics for Machine Learning (MML)* 원서 완독 및 한국어 요약 정리.
* 핵심 수학 개념(선형대수, 미분, 확률 등)을 독자적인 Concept 문서로 파편화하여 지식화.
* 학습한 수학 개념이 실제 머신러닝 모델(회귀, PCA, SVM 등)에 어떻게 쓰이는지 연결 관계 파악.

# Current Status
* **전체 진척도**: 12 / 12 Chapters (100.0%)
* **진행 중인 챕터**: 없음 (완독 완료)

# Structure & Chapter Logs
본 스터디는 아래와 같이 12개의 챕터로 분할하여 관리합니다.

## Part I: Mathematical Foundations
- [Chapter 01: Introduction and Motivation](chapter-01.md) - `status: active` (Completed)
- [Chapter 02: Linear Algebra](chapter-02.md) - `status: active` (Completed)
- [Chapter 03: Analytic Geometry](chapter-03.md) - `status: active` (Completed)
- [Chapter 04: Matrix Decompositions](chapter-04.md) - `status: active` (Completed)
- [Chapter 05: Vector Calculus](chapter-05.md) - `status: active` (Completed)
- [Chapter 06: Probability and Distributions](chapter-06.md) - `status: active` (Completed)
- [Chapter 07: Continuous Optimization](chapter-07.md) - `status: active` (Completed)

## Part II: Central Machine Learning Problems
- [Chapter 08: When Models Meet Data](chapter-08.md) - `status: active` (Completed)
- [Chapter 09: Linear Regression](chapter-09.md) - `status: active` (Completed)
- [Chapter 10: Dimensionality Reduction with PCA](chapter-10.md) - `status: active` (Completed)
- [Chapter 11: Density Estimation with GMM](chapter-11.md) - `status: active` (Completed)
- [Chapter 12: Classification with SVM](chapter-12.md) - `status: active` (Completed)

# Key Decisions
- **문서 분할 원칙**: 개별 챕터 스터디 노트에는 전반적인 흐름과 감상을 적고, 구체적이고 재사용성이 높은 수학 정의(예: SVD, PCA, Kernel)는 [wiki/ml/](../) 또는 [wiki/cs/](../../cs/) 하위에 독립된 **Concept** 문서로 생성하여 상호 링크한다. (AGENTS.md 규칙 준수)
- **출처 명시**: 각 스터디 문서 하단에 원서 파일([mml-book.pdf](../../../raw/notes/math_for_deeplearning/mml-book.pdf))을 Citation으로 표기한다.

# Related Concepts
- [ML Index](../index.md)
