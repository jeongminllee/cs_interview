---
type: Decision Note
title: MalwareAnalysisLLM LLM Candidate Matrix
description: B200 서버에서 MalwareAnalysisLLM fine-tuning 및 serving에 사용할 LLM 후보군을 현재 실험 결과 기준으로 재정리
tags: [llm, b200, finetuning, serving, qwen, glm, deepseek]
timestamp: 2026-07-03
status: active
---

# Summary

초기 후보군은 `B200_server.md`에서 **4×B200 기준 대형 모델 serving + LoRA fine-tuning 가능성**을 함께 고려해 잡았다. 이후 실제 LLaMA-Factory fine-tuning 실험에서 다음 사실이 확인되었다.

- 30B/72B급 모델은 LLaMA-Factory + DeepSpeed + PEFT LoRA 경로 검증에는 유용했지만, active full-size training queue에서는 제외한다.
- 실제 학습 큐는 `Qwen/Qwen3-Coder-Next` 80B부터 시작한다.
- 480B FP8은 serving 극한 실험 후보로는 여전히 중요하지만, 현재 LLaMA-Factory fine-tuning에서는 checkpoint loading 중 cgroup 800GiB limit에 걸린다.
- 480B fine-tuning을 계속 밀려면 LLaMA-Factory만 고집하기보다 Megatron/NeMo 같은 large-model-native framework를 후보로 올려야 한다.

따라서 이제 후보군은 **active real training 후보**, **대형 모델 compatibility 후보**, **480B급 loader/framework 후보**, **serving 한계 테스트 후보**로 분리한다.

# Candidate Matrix

| 후보 | 역할 | 현재 평가 | 다음 액션 |
| --- | --- | --- | --- |
| `Qwen/Qwen3-Coder-Next` | 80B coder real training 1순위 | 72B를 대체할 active full-size training 후보. 480B와 같은 coder 계열에 더 가까움 | full dataset LoRA SFT를 먼저 실행 |
| `zai-org/GLM-4.5-Air-FP8` | 현실적인 LoRA fine-tuning 후보 | Qwen 계열과 다른 reasoning/agent 성향을 비교할 때 가치가 있음 | Qwen3-Coder-Next 이후 compatibility와 real training 확인 |
| `deepseek-ai/DeepSeek-V4-Flash` | DeepSeek 계열 full-size 후보 | 취소된 다운로드 재개 대상. Qwen/GLM 이후 후보 | `model/base/deepseek-v4-flash`에 다운로드 재개 |
| `deepseek-ai/DeepSeek-V4-Flash-Base` | DeepSeek Base 비교 후보 | Base variant가 필요할 때 별도 경로에 저장 | `model/base/deepseek-v4-flash-base`에 별도 관리 |
| `zai-org/GLM-4.5-FP8` | full GLM FP8 한계 후보 | GLM Air보다 더 큰 upper-limit 후보 | load/training 한계 확인 |
| `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` | 480B급 코딩 특화 극한 모델 | serving 실험 후보로 중요. LLaMA-Factory fine-tuning은 checkpoint loading 40% 부근에서 cgroup 800GiB 도달 | Axolotl FSDP2, HF/TRL loader baseline, NeMo/Megatron 경로로 별도 설계 |
| `Qwen/Qwen3-Coder-480B-A35B-Instruct` | non-FP8 비교 후보 | FP8보다 memory 부담이 커서 현재 4×B200/800GiB cgroup에서는 우선순위 낮음 | FP8 load 문제가 해결된 뒤 비교 |
| `Qwen/Qwen3-Coder-30B-A3B-Instruct` | 이전 경량 기준선 | ZeRO-3 patched smoke 통과. dataset/W&B/LLaMA-Factory 경로 검증용으로 사용 완료 | active queue에서는 제외 |
| Qwen2/Qwen2.5 72B 계열 | 이전 중대형 기준선 | 72B ZeRO-3 patched smoke 통과. 단, 목적상 80B Qwen3-Coder-Next로 대체 가능 | active queue에서는 제외 |
| `gpt-oss-120b` | 기준선/검증 모델 | vLLM/API/client benchmark 확인용. fine-tuning 메인 후보는 아님 | serving stack sanity check에 사용 |

# Current Recommendation

## Fine-tuning 우선순위

1. **Qwen3-Coder-Next 80B**
   - 현재 active real training 1순위.
   - Qwen3-Coder 계열이라 480B와 tokenizer/template/모델 계열이 가깝다.
   - Qwen2/72B를 대체하는 full-size 후보로 둔다.

2. **GLM-4.5-Air-FP8**
   - 기존 후보군에서 현실적 LoRA fine-tuning 모델로 잡았던 후보.
   - Qwen 계열과 다른 reasoning/agent 성향을 비교할 때 가치가 있다.
   - Qwen3-Coder-Next 이후 compatibility와 real training을 확인한다.

3. **DeepSeek-V4-Flash**
   - 취소된 다운로드를 먼저 재개해 후보 풀에 올린다.
   - Qwen/GLM 이후 학습 또는 compatibility 후보로 둔다.

4. **Qwen3-Coder-480B FP8**
   - 최종 도전 후보.
   - 현재 LLaMA-Factory 4-rank 경로에서는 checkpoint loading 중 cgroup memory limit에 닿는다.
   - 바로 full training 대상이 아니라, loader 구조와 framework 전환 판단 대상이다.

## Serving 우선순위

1. **Qwen3-Coder-480B FP8**
   - 코딩/agentic workload 극한 serving 후보.

2. **GLM-4.5-FP8**
   - reasoning/agent 비교 후보.

3. **gpt-oss-120b**
   - serving stack 기준선.

4. **DeepSeek-R1/V3**
   - 4×B200 상한선 확인용 한계 테스트.

# Framework Implication

모델 후보는 framework 후보와 함께 봐야 한다.

| 모델 규모 | 우선 framework | 이유 |
| --- | --- | --- |
| 30B | LLaMA-Factory | 이전 smoke 기준선. active queue에서는 제외 |
| 72B | LLaMA-Factory + DeepSpeed | 이전 중대형 기준선. Qwen3-Coder-Next 80B로 대체 |
| 80B Qwen3-Coder-Next | LLaMA-Factory + DeepSpeed | 현재 full dataset real training 1순위 |
| GLM-4.5-Air | LLaMA-Factory 또는 Axolotl | 현실적인 LoRA 반복 학습 후보 |
| DeepSeek-V4-Flash | LLaMA-Factory 또는 framework compatibility check | 다운로드 재개 후 template/model support 확인 |
| 480B FP8 | Axolotl FSDP2, HF/TRL loader baseline, NeMo/Megatron | 현재 LLaMA-Factory 4-rank checkpoint loading은 cgroup memory limit에 막힘 |
| 671B급 DeepSeek | vLLM serving 또는 Megatron/NeMo 계열 검토 | 안정 학습보다 한계 테스트 성격 |

# Decisions

- 480B FP8은 "바로 학습" 후보가 아니라 "대형 모델 load/framework 검증" 후보로 유지한다.
- 실제 MalwareAnalysisLLM 학습 품질 실험은 Qwen3-Coder-Next 80B -> GLM-4.5-Air-FP8 -> DeepSeek-V4-Flash 순서로 진행한다.
- Qwen2/72B는 Qwen3-Coder-Next 80B로 대체 가능하므로 active queue에서 제외한다.
- 480B를 포기하는 것은 아니다. 다만 LLaMA-Factory 4-rank checkpoint loading 문제가 해결되거나 Megatron/NeMo 경로가 준비된 뒤 다시 승격한다.
- serving 후보와 fine-tuning 후보를 섞어서 판단하지 않는다.

# Related Concepts

- [B200 Server Fine-Tuning](B200_server.md)
- [B200 Full-Size Training Queue](b200_full_size_training_queue.md)
- [B200 Fine-Tuning Troubleshooting Report](b200_finetuning_troubleshooting_report_20260703.md)
- [Fine-Tuning Framework Comparison Basics](../fundamentals/finetuning_framework_comparison.md)
- [B200 480B FP8 Framework Matrix Experiments](../repos/AegisLM/docs/FRAMEWORK_MATRIX_EXPERIMENTS.md)
- [LLaMA-Factory Qwen3-Coder 480B FP8 SIGKILL Investigation](../../../errors/llamafactory-qwen3-coder-480b-fp8-oom-kill.md)
