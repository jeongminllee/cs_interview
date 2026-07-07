# AGENTS.md — Personal Knowledge Base Operating Rules

이 문서는 이 지식베이스를 관리하는 LLM agent가 따라야 할 운영 규칙이다.

이 지식베이스는 **LLM Wiki 방식으로 운영**하고, 실제 지식 문서는 **OKF 스타일의 Markdown 문서**로 저장한다.

---

# 1. Core Principle

이 저장소의 목적은 단순한 메모 보관이 아니라, 시간이 지날수록 누적되고 갱신되는 개인 지식베이스를 만드는 것이다.

LLM agent는 단순히 원본 자료를 요약하는 것이 아니라 다음 작업을 수행해야 한다.

* 원본 자료에서 핵심 지식을 추출한다.
* 기존 wiki 문서와 연결한다.
* 기존 내용과 충돌하는 부분을 표시한다.
* 필요한 경우 기존 문서를 업데이트한다.
* 관련 문서 간 cross-link를 추가한다.
* `index.md`와 `log.md`를 갱신한다.

---

# 2. Repository Structure

기본 구조는 다음을 따른다.

knowledge/
├── AGENTS.md
├── index.md
├── log.md
├── references/
│   ├── llm-wiki.md
│   └── okf-spec.md
├── raw/
│   ├── articles/
│   ├── papers/
│   ├── error-logs/
│   ├── transcripts/
│   └── notes/
├── wiki/
│   ├── ml/
│   ├── infra/
│   ├── errors/
│   ├── cs/
│   ├── algorithms/
│   ├── projects/
│   └── papers/
└── assets/

---

# 3. Directory Roles

## references/

참고 원문을 보관한다.

예:

* `references/llm-wiki.md`
* `references/okf-spec.md`

이 파일들은 운영 철학과 문서 포맷을 이해하기 위한 reference이다.
일반적인 지식 정리 과정에서 원문을 직접 수정하지 않는다.

## raw/

원본 자료를 보관한다.

예:

* 에러 로그
* 논문 PDF에서 추출한 텍스트
* 웹 클리핑
* 강의 노트 원본
* ChatGPT 대화 복사본
* 실험 로그

`raw/` 안의 자료는 source of truth로 간주한다.
LLM agent는 이 파일을 읽을 수 있지만, 사용자가 명시적으로 요청하지 않는 한 수정하지 않는다.

## wiki/

LLM agent가 정리하고 유지보수하는 지식 문서를 보관한다.

`wiki/` 안의 모든 일반 Markdown 문서는 OKF 스타일을 따른다.

## assets/

이미지, 첨부파일, 다이어그램, 캡처 등을 보관한다.

---

# 4. OKF Document Rules

`wiki/` 안의 일반 지식 문서는 Markdown 파일 하나가 하나의 concept이다.

모든 concept 문서는 YAML frontmatter로 시작해야 한다.

필수 필드:

```yaml
---
type: <문서 유형>
---
```

권장 필드:

```yaml
---
type: Concept
title: 
description: 
tags: []
timestamp: 
status: active
---
```

## Recommended Types

다음 type을 우선 사용한다.

* `Concept`
* `Error Note`
* `Project`
* `Paper Note`
* `Command Note`
* `Setup Guide`
* `Study Note`
* `Decision Note`
* `Reference`

새로운 type이 필요하면 만들 수 있지만, 기존 type으로 표현 가능한 경우 기존 type을 우선 사용한다.

---

# 5. Standard Wiki Templates

## 5.1 Concept

```markdown
---
type: Concept
title:
description:
tags: []
timestamp:
status: active
---

# Summary

# Why it matters

# Key Ideas

# Examples

# Related Concepts

# Citations
```

## 5.2 Error Note

```markdown
---
type: Error Note
title:
description:
tags: [error]
timestamp:
status: solved
---

# Situation

# Error Message

# Cause

# Solution

# Prevention

# Related Concepts

# Citations
```

## 5.3 Project

```markdown
---
type: Project
title:
description:
tags: [project]
timestamp:
status: active
---

# Goal

# Current Status

# Structure

# How to Run

# Key Decisions

# Issues

# Next Actions

# Related Concepts
```

## 5.4 Paper Note

```markdown
---
type: Paper Note
title:
description:
resource:
tags: [paper]
timestamp:
status: reading
---

# One-line Summary

# Problem

# Method

# Experiments

# Key Findings

# My Understanding

# How I Can Use This

# Open Questions

# Citations
```

---

# 6. Linking Rules

문서 간 연결은 일반 Markdown link를 사용한다.

가능하면 bundle-relative 또는 repository-relative link를 사용한다.

예:

```markdown
See [AutoGluon](../ml/autogluon.md).
See [GUAM Project](../projects/guam.md).
```

LLM agent는 새 문서를 만들 때 관련 기존 문서를 찾아 cross-link를 추가해야 한다.

특히 다음 관계는 적극적으로 연결한다.

* 에러 ↔ 프로젝트
* 에러 ↔ 환경 설정
* 개념 ↔ 예제 코드
* 논문 ↔ 적용 가능한 프로젝트
* CS 개념 ↔ 알고리즘 문제
* 설치 가이드 ↔ 실제 발생한 오류

---

# 7. Ingest Workflow

새로운 원본 자료가 추가되면 LLM agent는 다음 절차를 따른다.

1. `raw/` 안의 원본 자료를 읽는다.
2. 핵심 내용을 요약한다.
3. 새 wiki 문서가 필요한지 판단한다.
4. 기존 wiki 문서에 통합할 내용이 있는지 확인한다.
5. 필요한 경우 새 concept 문서를 만든다.
6. 관련 기존 문서를 업데이트한다.
7. 문서 간 cross-link를 추가한다.
8. `index.md`를 업데이트한다.
9. `log.md`에 작업 내역을 기록한다.

원본 자료 하나가 여러 wiki 문서를 업데이트할 수 있다.

---

# 8. Query Workflow

사용자가 질문하면 LLM agent는 다음 순서로 답한다.

1. 먼저 `index.md`를 확인한다.
2. 관련성이 높은 wiki 문서를 찾는다.
3. 필요한 경우 raw source를 확인한다.
4. 답변을 작성한다.
5. 답변에서 새롭게 정리할 가치가 있는 내용은 wiki 문서로 저장하거나 기존 문서에 반영할 것을 제안한다.

질문에 대한 답이 기존 wiki에 없으면, 모른다고 말하고 필요한 source나 조사 방향을 제안한다.

---

# 9. Lint Workflow

정기적으로 LLM agent는 wiki 상태를 점검한다.

점검 항목:

* frontmatter가 없는 문서
* `type` 필드가 없는 문서
* description이 비어 있는 문서
* 고립된 문서
* 깨진 링크
* 중복 문서
* 오래된 내용
* 서로 충돌하는 주장
* tag가 과도하게 많거나 일관성이 없는 문서
* index.md에 누락된 문서
* log.md에 기록되지 않은 큰 변경 사항

Lint 결과는 필요하면 `wiki/_maintenance/` 아래에 기록한다.

---

# 10. Index Rules

`index.md`는 전체 지식베이스의 진입점이다.

각 디렉터리에도 필요하면 `index.md`를 둘 수 있다.

index 문서는 다음 형태를 따른다.

```markdown
# Section Name

- [Title](path/to/file.md) - one-line description
```

LLM agent는 새 문서를 만들거나 문서 제목·위치를 바꾸면 관련 `index.md`를 갱신해야 한다.

---

# 11. Log Rules

`log.md`는 시간순 변경 기록이다.

새로운 ingest, 큰 업데이트, lint, 구조 변경이 있으면 기록한다.

형식:

```markdown
## YYYY-MM-DD

- **Ingest**: raw 자료를 읽고 관련 wiki 문서를 생성 또는 갱신함.
- **Update**: 기존 문서를 수정함.
- **Lint**: 깨진 링크와 누락된 frontmatter를 점검함.
- **Decision**: 운영 규칙 또는 구조 변경을 결정함.
```

최신 기록이 위에 오도록 한다.

---

# 12. Writing Style

wiki 문서는 다음 스타일을 따른다.

* 한국어를 기본으로 작성한다.
* 기술 용어는 필요한 경우 영어 원어를 병기한다.
* 장황한 설명보다 재사용 가능한 구조를 우선한다.
* 에러 문서는 원인과 해결 방법을 명확히 분리한다.
* 프로젝트 문서는 현재 상태와 다음 작업을 분명히 적는다.
* 논문 문서는 “내가 어떻게 써먹을 수 있는가”를 반드시 포함한다.
* 추측은 추측이라고 표시한다.
* 확인된 사실과 개인 해석을 구분한다.

---

# 13. Safety and Privacy Rules

다음 정보는 GitHub에 올리기 전에 반드시 제거하거나 마스킹한다.

* API key
* password
* token
* private key
* 주민등록번호
* 전화번호
* 상세 주소
* 계정 인증 정보
* 회사 내부 기밀
* 공개하면 안 되는 개인 정보

에러 로그에 로컬 경로, 사용자명, 이메일, 토큰이 포함될 수 있으므로 주의한다.

---

# 14. Git Rules

이 지식베이스는 Git으로 관리한다.

권장 commit message:

```text
docs: add autogluon error note
docs: update guam project note
chore: update index and log
lint: fix broken wiki links
```

큰 변경 전에는 commit을 먼저 만든다.

---

# 15. Default Agent Behavior

LLM agent는 지식베이스를 수정할 때 다음 원칙을 따른다.

* 원본 자료는 보존한다.
* wiki 문서는 작고 명확한 단위로 나눈다.
* 하나의 큰 문서에 모든 내용을 합치지 않는다.
* 관련 문서는 반드시 링크한다.
* 새 문서를 만들면 index와 log를 갱신한다.
* 기존 문서와 충돌하는 내용이 있으면 덮어쓰기 전에 충돌을 표시한다.
* 모르는 내용은 추측해서 채우지 않는다.
* 사용자가 요청한 목적에 맞는 최소한의 구조부터 만든다.
