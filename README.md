# 🧠 Nuri's CS & Machine Learning Knowledge Base

> **시간이 지날수록 누적되고 갱신되는 개인 CS 및 머신러닝 지식베이스 아카이브**
>
> 본 저장소는 **LLM Wiki** 방식으로 운영되며, 모든 기술 문서는 **OKF(Open Knowledge Format) 스펙**을 준수하여 작성 및 관리됩니다. 정보처리기사 실기 합격을 위한 페이스메이커 강사 에이전트와 미래의 머신러닝 엔지니어/리서처로 성장하기 위한 학습 환경이 융합되어 있습니다.

---

## 📅 실시간 학습 대시보드 바로가기

* 📑 **[정보처리기사 실기 학습 대시보드](wiki/cs/engineer_info_processing/index.md)**: 기사 실기 전 과목 핵심 요약 및 기출 분석 대시보드
* 📝 **[오늘 자 학습 일지 (2026-07-11)](wiki/cs/engineer_info_processing/my_study_log_260711.md)**: 실시간 퀴즈 풀이 및 15년 차 강사 에이전트의 밀착 오답 교정 일지 (48번~ 수록)
* 💡 **[요구사항 엔지니어링 종합 가이드](wiki/cs/engineer_info_processing/requirements_engineering_bible.md)**: 1과목 핵심인 요구사항 도출/분석/명세/확인 기법 요점정리 바이블

---

## 🛠️ 학습을 지원하는 AI 에이전트 페르소나 명세

본 지식베이스의 생성, 교정, 멘토링을 전담하는 세 가지 핵심 AI 페르소나 프롬프트 명세서입니다.

1. 🎓 **[정보처리기사 실기 15년 차 강사](references/instructor-prompt.md)**: 풍부한 비유와 실기시험 채점 함정을 조밀하게 짚어주는 수험 멘토
2. 💻 **[ML 엔지니어 (Nuri-Engine)](references/ml-engineer-prompt.md)**: PyTorch 가속, 메모리 최적화(OOM), 분산 학습 환경 튜닝 전담 전문가
3. 🔬 **[ML 리서처 (Nuri-Research)](references/ml-researcher-prompt.md)**: 신규 논문 수식 유도, 수학적 이론 해석 및 신규 아키텍처 연구 전담 전문가

---

## 📂 저장소 디렉토리 구조 (Directory Structure)

```text
D:/wiki/
├── AGENTS.md                   # 개인 지식베이스 운영 수칙 및 Git Rules
├── README.md                   # GitHub 대문 문서 (현재 파일)
├── index.md                    # 로컬 지식베이스 대시보드 진입점
├── log.md                      # 전체 지식베이스 수정/Ingest 히스토리
├── references/                 # 시스템 운영 규칙 및 AI 프롬프트 원문
└── wiki/                       # 카테고리별 마크다운 지식 노트
    ├── cs/                     # 컴퓨터 과학 (Java, Python, 정보처리기사)
    ├── ml/                     # 머신러닝 이론 및 수학 기초
    ├── errors/                 # 실무 에러 디버깅 노트 (LLaMA-Factory 등)
    ├── infra/                  # 인프라 구축 및 셋업 가이드
    └── projects/               # 진행 중인 AI 연구 및 미세조정(Fine-Tuning) 프로젝트
```

---

## 📜 지식베이스 운영 규칙 (Core Principles)

1. **상호 연결성 (Cross-Linking)**: 모든 문서들은 고립되지 않고 개념 ↔ 예제 ↔ 프로젝트 간 유기적인 마크다운 링크로 상호 연결됩니다.
2. **출처 표기 (Citations)**: 모든 지식의 원천은 신뢰할 수 있는 공식 문서 및 레퍼런스를 참조하여 투명하게 추적합니다.
3. **보안성 (Safety & Privacy)**: API Key, 비밀번호, 기밀 정보 등은 `.gitignore` 필터링 및 익명화 처리를 거쳐 GitHub 업로드 전 철저히 차단됩니다.
4. **Git 통제권**: 모든 변경사항의 Commit 및 Push는 오직 사용자의 명시적 요청과 승인하에만 실행됩니다.
