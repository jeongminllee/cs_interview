---
type: Project
title: Data Structure & Algorithm Study (자료구조와 알고리즘 학습)
description: 자료구조의 기본 개념과 10진/고정/부동소수점 데이터 표현, 선형/비선형 자료구조, 다양한 정렬 및 검색 성능을 분석하고 시험에 완벽히 대비하는 지식베이스 대시보드입니다.
tags: [algorithms, data-structures, computer-science, study]
timestamp: 2026-06-18
status: active
---

# Goal
* 자료구조와 알고리즘의 핵심 수학적 증명 및 대수 변환 과정 완전 학습.
* 1장(개론 및 데이터 표현)부터 6장(파일편성)까지의 시험 대비 고밀도 지식 정밀 정리.
* 연습문제 및 퀴즈의 Python 실행 결과, 버블/선택/삽입/퀵/힙 정렬의 회전별 수치 추적 과정을 체계화.

# Current Status
* **전체 진척도**: 6 / 6 Chapters (100.0%)
* **진행 중인 챕터**: 없음 (완독 및 정리 완료)

# Quick Reference: 정렬 및 검색 알고리즘 복잡도 종합 테이블

| 분류 | 알고리즘 | 최선 시간복잡도 | 평균 시간복잡도 | 최악 시간복잡도 | 공간복잡도 | 특징 및 안정성 (Stable) |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **정렬** | 버블 정렬 | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | 인접 원소 비교 교환, Stable |
| | 선택 정렬 | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | 최솟값 선별 교환, Unstable |
| | 삽입 정렬 | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | 거의 정렬 시 속도 최상, Stable |
| | 퀵 정렬 | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(\log n)$ | 평균 성능 최상, Unstable |
| | 힙 정렬 | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(1)$ | 항상 일정한 성능 보장, Unstable |
| | 병합 정렬 | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ | 추가 메모리 공간 소요, Stable |
| **검색** | 선형 검색 | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 정렬되지 않은 상태 가능 |
| | 이진 검색 | $\mathcal{O}(1)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | 정렬 상태 필수, 분할 정복 |
| | 보간 검색 | $\mathcal{O}(1)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 정렬 상태 필수, 불균등 시 $\mathcal{O}(n)$ |
| | 해싱 | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | 해시 함수 주소 직접 접근 |

# Structure & Chapter Logs
본 스터디는 아래와 같이 6개의 장으로 분할하여 관리합니다.

## Part I: 기초 개념 및 선형 구조
- [Chapter 01: Introduction and Data Representation](chapter-01.md) - `status: active` (Completed)
- [Chapter 02: Linear Data Structures (Lists, Stack, Queue, Deque)](chapter-02.md) - `status: active` (Completed)

## Part II: 비선형 구조, 정렬, 검색 및 파일편성
- [Chapter 03: Non-Linear Data Structures (Trees, Graphs, BFS/DFS)](chapter-03.md) - `status: active` (Completed)
- [Chapter 04: Sorting Algorithms (Bubble, Insertion, Quick, Heap, etc.)](chapter-04.md) - `status: active` (Completed)
- [Chapter 05: Search Algorithms and Hashing](chapter-05.md) - `status: active` (Completed)
- [Chapter 06: File Structures and Access Methods (ISAM, DAM)](chapter-06.md) - `status: active` (Completed)

# Key Decisions
- **문서화 원칙**: 강의안의 요약 요소를 일체 생략하지 않고, 수치 연산식(예: IEEE 754 실수 변환, 보간 검색 위치, 스택 Python 추적, 힙 정렬 Max Heap, 퀵 정렬 low/high 교환)을 하나하나 논리적으로 전개하여 시험 직전 완벽한 학습 가이드 역할을 할 수 있도록 기술한다.
- **출처 명시**: 각 문서 하단에 원본 pdf 파일(예: [README.md](../../raw/notes/DataStructure_Algorithm/README.md))들을 명시하여 로컬 경로 링크를 활성화한다.

# Related Concepts
- [CS Index](../../cs/)
- [Algorithms Index](../)
