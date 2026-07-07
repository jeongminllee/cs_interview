# Change Log

## 2026-07-07

- **Update**: `wiki/cs/engineer_info_processing/`의 정보처리기사 실기 OCR 추출 Markdown 69개를 대상으로 한글 조각 공백, 반복 OCR 오독, 문장부호를 1차 교정했다. 원문 확인이 필요한 줄에는 `[확인 필요]`를 표시했으며, 작업 전 백업은 `backups/engineer_info_processing-before-ocr-cleanup-20260707-113046.zip`에 보존했다.
- **Ingest**: 정보처리기사 실기 학습 대시보드 구조를 활용하여 실시간 퀴즈 풀이 및 오답 노트를 누적 기록하는 [정보처리기사 실기 개인 학습 기록 (260707)](wiki/cs/engineer_info_processing/my_study_log_260707.md)을 신규 생성했다.
- **Update**: [정보처리기사 실기 학습 대시보드](wiki/cs/engineer_info_processing/index.md)에 개인 학습 기록 섹션 및 링크를 업데이트했다.
- **Decision**: GitHub 지식베이스 백업 시 개인정보 및 로컬 절대 경로 유출 방지를 위해 `raw/` 폴더 등을 제외하는 `.gitignore` 파일을 루트 디렉토리에 신규 생성했다.
- **Ingest**: 정보처리기사 15년 차 강사 페르소나 및 풀이 출력 템플릿 명세를 레퍼런스 문서 [정보처리기사 실기 강사 페르소나 프롬프트](references/instructor-prompt.md)로 보관하였으며, [대시보드 index.md](index.md)의 References 영역에 링크를 추가했다.
- **Ingest**: 머신러닝 리서처 및 엔지니어 2대 축으로 성장하려는 수험생의 학습 환경 구축을 위해 [ML 엔지니어 프롬프트](references/ml-engineer-prompt.md) 및 [ML 리서처 프롬프트](references/ml-researcher-prompt.md) 레퍼런스 문서를 각각 신규 보관하고 [대시보드 index.md](index.md)에 연계했다.
- **Ingest**: 요구사항 엔지니어링의 전체 프로세스와 핵심 기법을 일괄 요약 정리한 [요구사항 엔지니어링 종합 가이드](wiki/cs/engineer_info_processing/requirements_engineering_bible.md)를 신규 작성하여 업로드하고 대시보드 index.md에 요점 정리 섹션으로 노출했다.
- **Ingest**: GitHub 업로드 시 대문 화면 노출을 극대화하기 위해 저장소 구조, 대시보드 바로가기 및 에이전트 소개를 상세히 수록한 [README.md](README.md) 파일을 신규 생성했다.

## 2026-07-06

- **Error Note**: `MalwareAnalysisLLM`에서 `.venv/bin/llamafactory-cli`가 누락되어 training runner가 시작 즉시 실패한 사건을 [LLaMA-Factory CLI Missing After Dependency Drift](wiki/errors/llamafactory-cli-missing-after-uv-sync.md)에 기록했다. 해결책은 root `pyproject.toml`의 `training` dependency group과 local editable `LLaMA-Factory` source를 기준으로 `uv sync --group training`을 수행하는 것이다.
- **Fix**: `MalwareAnalysisLLM` root `pyproject.toml`을 B200 학습/다운로드 흐름에 맞게 재조정했다. `datasets`는 LLaMA-Factory guard에 맞춰 `<=4.0.0`로 유지하고, `transformers!=4.57.0`, `hf-transfer`, local editable `LLaMA-Factory` training group(`accelerate`, `deepspeed`, `peft`, `trl`)을 추가했으며 `uv.lock`을 갱신했다.
- **Update**: B200 GPU 서버를 더 이상 smoke 중심으로 비워두지 않기 위해 [B200 Full-Size Training Queue](wiki/projects/Fine_Tuned/b200/b200_full_size_training_queue.md)를 추가했다. 원격 `MalwareAnalysisLLM`에는 `Qwen/Qwen3-Coder-Next` 80B full dataset LLaMA-Factory config와 runner를 추가하고, `scripts/download_hf_model.py`에 DeepSeek/GLM/Qwen3-Coder-Next variant alias를 등록했으며 Qwen2/72B는 active training queue에서 제외했다.
- **Recovery**: `log.md`가 PowerShell 인코딩 경로에서 mojibake 상태가 되어, 최근 Fine_Tuned/B200 프로젝트 중심의 changelog를 읽을 수 있는 한국어 요약 형태로 복원했다.

## 2026-07-03

- **Update**: `wiki/projects/Fine_Tuned` 루트에 흩어져 있던 문서를 `b200/`, `data/`, `training/`, `libraries/`, `fundamentals/` 폴더로 재정리했다. 루트 `index.md`는 폴더형 진입점으로 단순화하고, 각 하위 폴더에 `index.md`를 추가했으며 이동된 문서들의 상대 링크를 갱신했다.
- **Experiment**: B200 서버의 800GiB container profile에서 모델 로딩 한계를 측정하기 위해 [B200 Model Limit Load-Only Probes](wiki/projects/Fine_Tuned/b200/b200_model_limit_load_only_probes.md)를 추가했다. 원격 `MalwareAnalysisLLM`에는 후보 manifest, `scripts/run_model_limit_probe.py`, observe-only telemetry 연동, unit test와 실행 문서를 구현했다.
- **Decision**: 기존 B200 LLM 후보군을 현재 실험 결과 기준으로 재정리해 [MalwareAnalysisLLM LLM Candidate Matrix](wiki/projects/Fine_Tuned/b200/llm_candidate_matrix_20260703.md)를 추가했다. 이후 2026-07-06 결정에 따라 Qwen2/72B는 active queue에서 제외하고 Qwen3-Coder-Next 80B를 우선 후보로 승격했다.
- **Report**: `MalwareAnalysisLLM` B200 fine-tuning 준비 중 발생한 데이터셋 build, Hugging Face 로딩, secret-like row validation, memory soft-stop 혼선, DeepSpeed ZeRO-3 dtype mismatch, LLaMA-Factory dependency guard, 480B FP8 checkpoint loading `SIGKILL` 문제를 [B200 Fine-Tuning Troubleshooting Report](wiki/projects/Fine_Tuned/b200/b200_finetuning_troubleshooting_report_20260703.md)로 종합 정리했다.
- **Study Notes**: `MalwareAnalysisLLM` 프로젝트가 실제로 사용하는 라이브러리 스택을 기준으로 [MalwareAnalysisLLM Library Stack Map](wiki/projects/Fine_Tuned/libraries/malwareanalysisllm_library_stack_map.md), [AegisLM Training Libraries](wiki/projects/Fine_Tuned/libraries/aegislm_training_libraries.md), [Training Runtime Libraries](wiki/projects/Fine_Tuned/libraries/training_runtime_libraries.md), [project_Nurilab Library Notes](wiki/projects/Fine_Tuned/libraries/project_nurilab_library_notes.md)를 추가했다.
- **Study Notes**: PyTorch, Transformers/SFT, dataset format, LoRA/PEFT, distributed training, DeepSpeed ZeRO, LLaMA-Factory, W&B/telemetry, framework comparison 기본기 노트를 [Fine-Tuned Project](wiki/projects/Fine_Tuned/index.md)에 연결했다.
- **Setup Guide**: B200 `Qwen3-Coder-480B-A35B-Instruct-FP8` full training 전 사용자가 직접 실행/모니터링할 gate를 [B200 Qwen3-Coder 480B Training Gate Guide](wiki/projects/Fine_Tuned/b200/b200_480b_training_gate_guide.md)에 정리했다.
- **Error Note**: B200 서버의 30B/72B LLaMA-Factory LoRA run이 첫 optimizer step에서 `TypeError: output tensor must have the same type as input tensor`로 실패한 사건을 [LLaMA-Factory DeepSpeed ZeRO-3 LoRA BF16 Dtype Mismatch](wiki/errors/llamafactory-deepspeed-zero3-dtype-mismatch.md)에 기록했다.
- **Experiment**: B200 서버에서 Qwen3-Coder-30B-A3B와 Qwen2-72B의 ZeRO-2 1-step diagnostic run이 통과했음을 기록했다. 이 결과는 이후 Qwen2/72B를 active queue에서 제외하기 전의 pipeline sanity 기준선으로 남긴다.
- **Update**: B200 Qwen3-Coder 480B FP8 재분석을 위해 프로젝트 자체 memory soft-limit/controlled stop 경로를 제거하고 observe-only telemetry 정책으로 전환했다.

## 2026-07-02

- **Update**: B200 480B FP8 multi-framework 비교 실험 골격을 원격 `MalwareAnalysisLLM` 프로젝트에 추가하고, wiki mirror 문서 [B200 480B FP8 Framework Matrix Experiments](wiki/projects/Fine_Tuned/repos/AegisLM/docs/FRAMEWORK_MATRIX_EXPERIMENTS.md)를 생성했다.
- **Update**: B200 480B FP8 실패 분석 문서에서 원인을 OOM으로 확정하지 않도록 표현을 정정했다. `SIGKILL(-9)`은 외부 kill 신호이며, 현재는 cgroup memory limit kill이 강한 가설이지만 CPU pressure, pids limit, loader 경로를 추가 실험으로 분리해야 한다고 기록했다.
- **Update**: B200 `Qwen3-Coder-480B-A35B-Instruct-FP8` smoke run의 2026-07-02 15:44 KST 추가 실패를 기록했다. torchrun 로그와 memory watcher JSONL을 결합해 container cgroup memory limit kill 가능성이 높다고 분석했다.
- **Update**: B200 memory watch 로그에 process-level snapshot을 추가하고, `scripts/check_memory_budget.py --watch`가 JSONL/CSV에 cgroup, GPU, process metrics를 기록하도록 확장했다.
- **Error Note**: B200 4-GPU 환경의 `Qwen3-Coder-480B-A35B-Instruct-FP8` LLaMA-Factory/DeepSpeed ZeRO-3 run이 checkpoint loading 약 40% 지점에서 `SIGKILL(exitcode -9)`로 종료된 원인을 [LLaMA-Factory Qwen3-Coder 480B FP8 SIGKILL Investigation](wiki/errors/llamafactory-qwen3-coder-480b-fp8-oom-kill.md)에 기록했다.
- **Fix**: AegisLM 데이터셋 빌더에서 `rezaduty/cybersecurity-qa-v2` parquet 로딩 실패를 HF Hub JSONL 직접 로더로 우회하고, `--max-per-source -1`을 source별 전체 수집 옵션으로 확장했다.
- **Update**: [Symlink](wiki/infra/symlink.md) 및 [Infra Index](wiki/infra/index.md)를 생성하여 OS별 심볼릭 링크 생성/해제 방법을 지식베이스에 추가했다.

## 2026-07-01

- **Fix**: 사용자가 원하는 하드코딩 credential류 보안 패턴을 데이터셋에서 버리지 않도록 AegisLM 변환 정책을 변경했다. `password=`, `api_key=`, `client_secret=` assignment는 실제 값을 `[REDACTED_SECRET]`으로 마스킹하고 학습에는 포함하되 secret 값은 보존하지 않도록 수정했다.
- **Update**: AegisLM 데이터셋 빌더를 원래 5갈래 흐름(Cybersecurity QA, DiverseVul, BigVul, CTF write-up, ZIP/source corpus)으로 확장하고, CTF/BigVul target redaction, ZIP path traversal 방어, `.env.example`, `scripts/check_environment.py` 기반 B200 환경 preflight 계획을 문서화했다.
- **Update**: B200 서버의 `/home/wyhwang/workspace/MalwareAnalysisLLM`에 AegisLM 스타일 파인튜닝 파이프라인을 구현했다. Hugging Face 직접 추출, AegisLM canonical JSONL 전처리, train/validation/test split, LLaMA-Factory dataset export/registration, Qwen3-Coder-480B 및 FP8 LoRA SFT 설정, W&B online logging run script를 추가했다.
- **Update**: [Security Datasets](wiki/projects/Fine_Tuned/data/security_datasets.md)를 현재 AegisLM 구조에 맞춰 정리하고, 데이터셋 추출, canonical preprocessing, train/validation/test split, LLaMA-Factory export 절차를 문서화했다.
- **Update**: [LLaMA-Factory + W&B Fine-Tuning Integration](wiki/projects/Fine_Tuned/training/llamafactory_wandb_finetuning.md)을 작성하고, LLaMA-Factory exporter, B200 DeepSpeed ZeRO-3 설정, W&B logging YAML, 실행 스크립트, Project NuriLab 연동 문서를 반영했다.
