---
type: Project
title: B200 기반 대형 언어 모델 로컬 서빙 및 파인튜닝 실험 제안서
description: B200 GPU 5장/4장 환경에서의 LLM 로컬 서빙(vLLM) 및 LoRA/QLoRA 파인튜닝 전략과 모델 선정 제안
tags: [project, gpu, b200, fine-tuning, vllm, llm]
timestamp: 2026-06-30
status: active
---

# B200 기반 대형 언어 모델 로컬 서빙 및 파인튜닝 실험 제안서

## 1. 제안 개요

현재 사용 가능한 환경은 **B200 GPU 5장**이며, 가까운 시점에 1장을 반납하고 **B200 GPU 4장 체계로 전환될 가능성**이 있다. 따라서 이번 실험의 핵심 목적은 단순히 모델 하나를 구동하는 것이 아니라, 짧은 기간 동안 고성능 GPU 자원을 최대한 활용해 다음 세 가지 감각을 확보하는 데 있다.

첫째, **vLLM 기반 대형 모델 서빙의 한계 지점**을 직접 확인한다.
둘째, 향후 4장 환경에서도 재현 가능한 운영 구조를 만든다.
셋째, 최종적으로 로컬 모델을 대상으로 **LoRA/QLoRA 기반 파인튜닝 가능성**까지 검증한다.

이번 실험은 “안정적인 운영”만을 목표로 하지 않는다. 사용 가능한 자원이 B200급인 만큼, 일반적인 70B 또는 120B급 모델에서 멈추기보다는 **480B, 671B급 MoE 모델까지 도전하면서 OOM 경계, KV cache 압박, tensor parallel, expert parallel, long-context serving의 병목을 체감하는 것**을 목표로 한다.

다만 중요한 운영 원칙은 명확하다.

**실제 운영 기준은 4×B200으로 잡고, 현재의 5번째 GPU는 극한 실험, 비교 모델, 벤치마크 클라이언트, 파인튜닝 테스트 슬롯으로 활용한다.**

이 방식이 가장 실용적이다. 5장을 기준으로 구조를 설계하면 나중에 4장으로 축소될 때 다시 튜닝해야 한다. 반면 처음부터 4장 기준으로 모델을 띄우고, 5번째 GPU를 별도 실험용으로 쓰면 이후 환경 변화에도 운영 구조가 흔들리지 않는다.

---

## 2. 현재 환경과 제약 조건

### 2.1 하드웨어 전제

현재 가용 자원은 다음과 같이 본다.

```text
현재 환경: B200 GPU 5장
향후 환경: B200 GPU 4장 가능성 높음
운영 기준: 4×B200
임시 활용 자원: 5번째 B200
```

B200은 장당 GPU 메모리가 매우 큰 축에 속하므로, 4장 환경에서도 일반적인 대형 dense 모델뿐 아니라 상당수의 MoE 모델을 실험할 수 있다. 다만 480B, 671B, 1T급 모델은 weight memory뿐 아니라 KV cache, NCCL 통신, vLLM 내부 병렬화 전략, context length 설정이 모두 영향을 주므로 단순히 “총 파라미터 수 × dtype”만 보고 판단하면 안 된다.

특히 MoE 모델은 active parameter 수가 작더라도, 서빙 시에는 전체 expert weight를 분산 적재해야 한다. 따라서 VRAM 계산은 **active parameter가 아니라 total parameter 기준**으로 보수적으로 접근해야 한다.

---

### 2.2 소프트웨어 전제

서빙 프레임워크는 **vLLM**을 사용한다.

```text
Serving framework: vLLM
Serving API: OpenAI-compatible API
Model source: Hugging Face checkpoint
Model loading: local path 기반
운영 방식: 필요 시 로컬 모델 디렉터리에서 기동
```

서버에 직접 Hugging Face token을 남기는 것은 지양한다. 모델은 별도 다운로드 노드 또는 개인 PC에서 받은 뒤 서버로 전송하고, 서버에서는 local path만 사용해 vLLM을 실행하는 구조가 바람직하다.

---

## 3. 핵심 운영 전략

### 3.1 5장 전체를 하나의 tensor parallel 그룹으로 묶지 않는다

극한 실험을 하더라도 `tensor_parallel_size=5`는 권장하지 않는다.

대부분의 대형 모델은 hidden dimension, attention head, KV head, expert partitioning 등이 2, 4, 8 단위로 나누어지도록 설계되어 있다. 5-way tensor parallel은 모델 구조와 잘 맞지 않을 가능성이 높고, 맞더라도 성능이나 안정성 면에서 이점이 크지 않다.

따라서 기본 전략은 다음과 같다.

```text
GPU 0,1,2,3 → 메인 대형 모델 vLLM 서빙
GPU 4       → 별도 실험 슬롯
```

5번째 GPU의 활용 방식은 다음 중 하나가 적합하다.

```text
1. 벤치마크 클라이언트 전용
2. gpt-oss-120b 같은 비교 모델 단독 서빙
3. GLM-4.5-Air 또는 Qwen 계열 LoRA 실험
4. 데이터 전처리 및 평가 작업
5. 모니터링/프로파일링 보조 작업
```

이 구성의 장점은 명확하다.

현재 5장 환경을 충분히 활용하면서도, 나중에 4장만 남았을 때 메인 서빙 구조를 그대로 유지할 수 있다. 즉, “반납 전 실험”과 “반납 후 운영”이 분리되지 않는다.

---

## 4. Hugging Face Token 보안 운영 방안

서버에 Hugging Face token을 올려두는 것은 피하는 것이 좋다. 특히 여러 사람이 접근할 수 있는 서버이거나, 운영 서버에 가까운 환경이라면 `huggingface-cli login`을 직접 수행해 token을 cache에 남기는 방식은 바람직하지 않다.

권장 방식은 다음과 같다.

```text
개인 PC 또는 별도 다운로드 노드에서 모델 다운로드
→ 모델 디렉터리만 서버로 전송
→ 서버에서는 HF token 없이 local path로 vLLM 실행
→ 필요 시 HF_HUB_OFFLINE=1 설정
```

### 4.1 다운로드 노드에서 모델 받기

```bash
mkdir -p /mnt/models

read -s HF_TOKEN
export HF_TOKEN

hf download Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \
  --local-dir /mnt/models/Qwen3-Coder-480B-A35B-Instruct-FP8

unset HF_TOKEN
rm -f ~/.cache/huggingface/token
```

이 방식은 token을 shell session 안에서만 사용하고, 다운로드가 끝난 뒤 즉시 제거한다.

---

### 4.2 서버로 모델 전송

```bash
rsync -ah --info=progress2 \
  /mnt/models/Qwen3-Coder-480B-A35B-Instruct-FP8 \
  user@server:/models/
```

서버에는 다음과 같은 구조로 모델을 둔다.

```text
/models/
  qwen/
    Qwen3-Coder-480B-A35B-Instruct-FP8/
  glm/
    GLM-4.5-FP8/
    GLM-4.5-Air-FP8/
    GLM-4.5-Air/
  deepseek/
    DeepSeek-R1/
    DeepSeek-V3/
  openai/
    gpt-oss-120b/
  adapters/
    glm-4.5-air-lora-mydata/
    qwen-lora-mydata/
```

---

### 4.3 서버에서는 offline mode로 실행

```bash
export HF_HUB_OFFLINE=1
export CUDA_VISIBLE_DEVICES=0,1,2,3

vllm serve /models/qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \
  --served-model-name qwen3-coder-480b-fp8 \
  --tensor-parallel-size 4
```

이 구조에서는 서버가 Hugging Face Hub에 인증할 필요가 없다. 모델 checkpoint, tokenizer, config, generation config 등이 local path에 모두 존재해야 한다.

---

## 5. 추천 모델 후보군

이번 실험의 목적은 크게 두 갈래다.

하나는 **극한 서빙 실험**이고, 다른 하나는 **향후 파인튜닝까지 고려한 현실적인 운영 모델 확보**다.

따라서 모델을 하나만 고르기보다, 역할별로 모델을 나누는 것이 좋다.

---

## 5.1 1순위 극한 서빙 모델: Qwen3-Coder-480B-A35B-Instruct-FP8

### 선정 이유

`Qwen3-Coder-480B-A35B-Instruct-FP8`은 이번 환경에서 가장 먼저 도전해볼 만한 모델이다.

이 모델은 480B급 MoE 구조이며, active parameter는 상대적으로 작지만 전체 weight 규모가 매우 크다. 따라서 4×B200에서 vLLM으로 구동하면 다음 요소를 한 번에 실험할 수 있다.

```text
1. FP8 대형 MoE 모델 로딩
2. tensor parallel 4-way 구성
3. expert parallel 사용 여부
4. long-context serving
5. KV cache 압박
6. prefill latency와 decode throughput 차이
7. coding/agentic workload에서의 실사용성
```

코딩 특화 모델이라는 점도 장점이다. 단순 질의응답보다 repo-scale 코드 분석, 긴 context 기반 reasoning, tool-use 시나리오에서 GPU와 서빙 프레임워크의 한계를 더 잘 드러낸다.

### 권장 실행 예시

```bash
export CUDA_VISIBLE_DEVICES=0,1,2,3
export HF_HUB_OFFLINE=1

vllm serve /models/qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \
  --served-model-name qwen3-coder-480b-fp8 \
  --tensor-parallel-size 4 \
  --enable-expert-parallel \
  --gpu-memory-utilization 0.94 \
  --max-model-len 32768 \
  --max-num-seqs 1 \
  --trust-remote-code
```

### vLLM serve 옵션 상세 분석

위 명령어에 지정된 환경 변수 및 vLLM 서빙 옵션들의 구체적인 역할과 설정 목적은 다음과 같습니다.

| 파라미터 / 환경변수 | 설정값 | 상세 역할 및 B200 4장 환경에서의 설정 사유 |
| :--- | :--- | :--- |
| **`export CUDA_VISIBLE_DEVICES`** | `0,1,2,3` | 호스트 장비의 GPU 5장 중 **앞의 4장만 프로세스에 노출**시킵니다. 홀수 개수(5장)의 Tensor Parallel 연산 비효율을 방지하고, 남은 5번째 GPU(Index 4)를 파인튜닝 실험 및 벤치마크 전용으로 분리하기 위한 목적입니다. |
| **`export HF_HUB_OFFLINE`** | `1` | Hugging Face Hub와의 모든 온라인 통신을 전면 차단합니다. 로컬 경로(`/models/...`)의 가중치만 참조하도록 강제하여 외부 네트워킹 및 HF 토큰 유출 위험을 없앱니다. |
| **`/models/qwen/...`** | *(로컬 경로)* | 로컬에 영속 저장된 FP8 정밀도 기반 Qwen3-Coder-480B 모델 디렉터리를 가리키는 서빙 대상 소스 주소입니다. |
| **`--served-model-name`** | `qwen3-coder-480b-fp8` | OpenAI 호환 API 서버의 엔드포인트(`POST /v1/chat/completions`) 요청 본문 내 `model` 필드에 매핑할 공식 API 서빙 서비스명입니다. |
| **`--tensor-parallel-size`** | `4` | 모델 가중치(Dense 레이어)를 GPU 4장에 걸쳐 연산하도록 분할하는 **텐서 병렬화(TP) 크기**입니다. FP8 정밀도로 경량화해도 480B급 MoE 가중치 크기가 VRAM 약 240~280GB를 요구하므로, OOM을 피하기 위해 4장 분할 적재가 필수적입니다. |
| **`--enable-expert-parallel`** | *(활성화)* | MoE 모델의 다양한 전문가(Experts) 연산들을 GPU별로 교차 파티셔닝하는 **전문가 병렬화(EP)** 옵션입니다. 모든 GPU가 전문가 가중치를 중복 복제하지 않고 조각화하여 연산하므로, 통신 오버헤드를 대폭 낮추고 VRAM을 획기적으로 절약할 수 있습니다. |
| **`--gpu-memory-utilization`** | `0.94` | 전체 GPU VRAM 용량 중 vLLM 엔진(가중치 적재 및 KV 캐시 선점)이 확보해 둘 **VRAM 최대 비율(94%)**입니다. 초거대 모델 특성상 적재 후 잔여 VRAM이 빡빡하므로, 이 값을 최대한 높여 동적 추론 연산에 쓰일 KV 캐시 공간을 확보합니다. (단, 0.95 이상으로 과도하게 높이면 실행 단계에서 OOM이 날 수 있습니다.) |
| **`--max-model-len`** | `32768` | 모델이 처리하는 **최대 컨텍스트 길이(입력 + 출력 토큰 합계 = 32K)**입니다. 컨텍스트가 증가하면 KV 캐시 메모리 소요량이 2차 함수적으로 늘어나므로, 첫 구동 검증 시에는 안전하게 32K로 잡고 순차적으로(64K, 128K) 스케일 아웃합니다. |
| **`--max-num-seqs`** | `1` | **동시 처리 요청(Concurrency)의 수**를 최대 1개로 제한합니다. 극한 모델 서빙의 한계선 상에서 다중 세션 공유로 인한 VRAM 고갈을 원천 배제하고, 단일 요청의 long-context 연산 처리를 안전하게 통과시키기 위한 한계 점검 설정입니다. |
| **`--trust-remote-code`** | *(활성화)* | Hugging Face 모델 아키텍처에 정의된 사용자 정의 Python 코드를 서빙 시 그대로 신뢰하여 실행하도록 승인합니다. 최신 아키텍처 모델 및 커스텀 FP8 양자화 연산의 정상 동작을 위해 필수적입니다. |

처음부터 긴 context를 최대로 열지 않는다. 다음 순서로 올리는 것이 안전하다.

```text
max_model_len: 32K → 64K → 128K → 262K
max_num_seqs: 1 → 2 → 4
gpu_memory_utilization: 0.90 → 0.94 → 0.97
```

이 모델의 목표는 안정 운영 이전에 “어디서부터 무너지는지”를 확인하는 것이다. 즉, 성공 여부만 중요한 것이 아니라 실패 로그 자체가 중요한 산출물이다.

---

## 5.2 2순위 비교 모델: GLM-4.5-FP8

### 선정 이유

GLM 계열은 여전히 좋은 후보군이다. 특히 `GLM-4.5-FP8`은 reasoning, coding, agent workload를 두루 실험하기 좋고, Qwen3-Coder와 비교했을 때 모델 응답 스타일과 서빙 특성이 다르게 나타날 가능성이 높다.

Qwen3-Coder가 코딩 특화 극한 모델이라면, GLM-4.5는 더 범용적인 reasoning/agent 모델로 보는 것이 좋다.

### 권장 실행 예시

```bash
export CUDA_VISIBLE_DEVICES=0,1,2,3
export HF_HUB_OFFLINE=1

vllm serve /models/glm/GLM-4.5-FP8 \
  --served-model-name glm-4.5-fp8 \
  --tensor-parallel-size 4 \
  --enable-expert-parallel \
  --reasoning-parser glm45 \
  --tool-call-parser glm45 \
  --enable-auto-tool-choice \
  --kv-cache-dtype fp8_e4m3 \
  --gpu-memory-utilization 0.94 \
  --max-model-len 65536 \
  --max-num-seqs 2
```

GLM-4.5-FP8은 4×B200에서 충분히 도전할 가치가 있다. 다만 full long-context와 높은 concurrency를 동시에 욕심내면 KV cache에서 병목이 발생할 수 있으므로, context length와 동시 요청 수를 분리해서 실험해야 한다.

---

## 5.3 3순위 한계 테스트 모델: DeepSeek-R1 또는 DeepSeek-V3 계열

### 선정 이유

DeepSeek 계열은 이번 실험에서 “극한 테스트” 역할에 적합하다.

671B급 MoE 모델은 4×B200에서 상당히 빡빡하다. 따라서 이 모델은 안정적인 서비스 후보라기보다는 다음을 확인하기 위한 모델로 보는 편이 맞다.

```text
1. 4×B200에서 671B급 MoE checkpoint가 어느 정도까지 로딩 가능한가
2. FP8 또는 저정밀 checkpoint 사용 시 실질적인 KV cache 여유가 얼마나 남는가
3. vLLM의 expert parallel, tensor parallel 조합이 어디서 병목을 보이는가
4. NCCL, CUDA graph, memory fragmentation 이슈가 발생하는가
5. 짧은 context라도 실제 decode가 가능한가
```

### 권장 실행 예시

```bash
export CUDA_VISIBLE_DEVICES=0,1,2,3
export HF_HUB_OFFLINE=1

vllm serve /models/deepseek/DeepSeek-R1 \
  --served-model-name deepseek-r1 \
  --tensor-parallel-size 4 \
  --enable-expert-parallel \
  --gpu-memory-utilization 0.97 \
  --max-model-len 8192 \
  --max-num-seqs 1 \
  --trust-remote-code
```

처음은 반드시 보수적으로 시작한다.

```text
max_model_len: 8K
max_num_seqs: 1
gpu_memory_utilization: 0.95~0.97
```

이 모델은 실패 가능성이 있다. 하지만 실패해도 충분히 가치가 있다. 특히 OOM 위치, 로딩 시간, weight shard 분산, KV cache 예약량, NCCL 오류 여부를 확인하면 이후 어떤 규모의 모델까지 운영 가능한지 판단할 수 있다.

---

## 5.4 안정성 검증 및 기준 모델: gpt-oss-120b

### 선정 이유

`gpt-oss-120b`는 극한 모델은 아니지만, vLLM 환경 검증용으로 매우 유용하다.

B200 1장 또는 소수 GPU에서 비교적 수월하게 구동될 가능성이 높기 때문에, 다음 용도로 적합하다.

```text
1. vLLM 설치 및 OpenAI-compatible API 정상 동작 확인
2. benchmark pipeline 검증
3. request/response logging 확인
4. client SDK 호환성 확인
5. 5번째 GPU 단독 활용
6. 대형 MoE 모델과 품질/속도 비교
```

### 권장 실행 예시

```bash
export CUDA_VISIBLE_DEVICES=4
export HF_HUB_OFFLINE=1

vllm serve /models/openai/gpt-oss-120b \
  --served-model-name gpt-oss-120b \
  --gpu-memory-utilization 0.90 \
  --max-model-len 131072
```

이 모델은 “메인 타깃”이라기보다 기준선이다. Qwen3-Coder-480B나 GLM-4.5-FP8이 느리거나 불안정할 때, gpt-oss-120b를 통해 vLLM 자체 문제인지 모델 규모 문제인지 분리할 수 있다.

---

## 5.5 멀티 GPU 분산 파인튜닝 프레임워크 및 후보

4~5장의 B200 GPU 자원을 남김없이 묶어서 대형 모델을 분산 파인튜닝하기 위해서는 단일 GPU 최적화 도구(예: Unsloth) 대신, **멀티 GPU 분산 학습 분할 및 섀딩(Sharding)**을 안정적으로 지원하는 엔터프라이즈급 프레임워크를 사용해야 합니다.

### 추천 1순위: LLaMA-Factory (가장 권장)
*   **특징**: 현재 오픈소스 진영에서 가장 활발하고 안정적으로 유지 관리되는 LLM 파인튜닝 툴킷입니다. DeepSpeed, FSDP, FlashAttention-2와의 유기적인 결합을 지원하며 CLI 및 WebUI를 통해 직관적인 설정이 가능합니다.
*   **적합 사유**: B200 4~5장 환경에서 DeepSpeed ZeRO-3 설정을 적용해 메모리 분산을 수월하게 처리할 수 있고, 다중 GPU NCCL 에러 디버깅이 매우 신속합니다.

### 추천 2순위: Axolotl
*   **특징**: YAML 구성 파일 하나로 데이터셋, 모델 아키텍처, DeepSpeed 설정, 학습 하이퍼파라미터 등 분산 파인튜닝의 모든 상세 요소를 코딩 없이 정밀 조정할 수 있는 전문가 전용 툴킷입니다.
*   **적합 사유**: 대용량 MoE 아키텍처 파인튜닝 시 발생하는 특수 레이어 분산 연산 및 패킹(Dataset Packing) 기능이 매우 뛰어납니다.

---

### 분산 학습 핵심 아키텍처: DeepSpeed ZeRO-3
B200 4~5장 분산 학습 시 모델 가중치와 옵티마이저 상태가 VRAM을 과점하여 OOM이 발생하는 것을 막기 위해 **DeepSpeed ZeRO-3(Zero Redundancy Optimizer Stage 3)** 연동이 필수적입니다.

*   **ZeRO-1**: 옵티마이저 상태(Optimizer States)를 GPU들에 쪼개어 적재.
*   **ZeRO-2**: 그래디언트(Gradients)까지 쪼개어 적재.
*   **ZeRO-3**: 모델 가중치(Parameters/Weights) 자체를 4~5장 GPU 전체에 조각내어 분산 적재(Sharding)하고, 순방향/역방향 연산 직전에 필요한 가중치 블록만 NCCL 통신으로 당겨와 연산 후 즉시 비워내는 방식입니다.

---

### 파인튜닝 현실적 후보 모델
4~5장 전체를 DeepSpeed ZeRO-3로 묶는다면 다음과 같은 대형 모델도 QLoRA 혹은 LoRA 기반으로 원활하게 파인튜닝 주기를 돌릴 수 있습니다.

1.  **Qwen2.5-72B-Instruct / Qwen2.5-Coder-72B-Instruct**:
    *   B200 4~5장 + DeepSpeed ZeRO-3 조합 시 72B급 dense 모델의 BF16 LoRA 학습이 매우 쾌적하게 가능합니다.
2.  **GLM-4.5-Air**:
    *   B200 4~5장 전체를 사용한 SFT(Supervised Fine-Tuning) 반복 훈련에 적합한 최신 중대형 베이스 라인 모델입니다.

---

### LLaMA-Factory 멀티 GPU 분산 실행 예시

```bash
# 1. 4~5장의 GPU 활성화
export CUDA_VISIBLE_DEVICES=0,1,2,3,4

# 2. torchrun 및 deepspeed 기반 LLaMA-Factory 실행
torchrun --nproc_per_node=5 --master_port=29501 \
  src/train.py \
  --deepspeed ds_z3_config.json \
  --stage sft \
  --do_train \
  --model_name_or_path /models/qwen/Qwen2.5-72B-Instruct \
  --dataset my_custom_dataset \
  --dataset_dir ./data \
  --template qwen \
  --finetuning_type lora \
  --lora_target all \
  --output_dir ./adapters/qwen-72b-lora \
  --overwrite_output_dir \
  --cutoff_len 8192 \
  --preprocessing_num_workers 16 \
  --per_device_train_batch_size 1 \
  --gradient_accumulation_steps 8 \
  --lr_scheduler_type cosine \
  --logging_steps 10 \
  --warmup_ratio 0.1 \
  --learning_rate 5e-5 \
  --num_train_epochs 3.0 \
  --plot_loss \
  --fp16 False \
  --bf16 True
```
*(참고: `ds_z3_config.json` 설정에 ZeRO-3 파라미터 섀딩 옵션이 정의되어 있어야 합니다. 구체적인 보안 파인튜닝용 학습 데이터셋 목록은 [사이버 보안 데이터셋 가이드](../data/security_datasets.md)를 참고하시기 바랍니다.)*

### 5.6 사이버 보안 SFT 데이터셋 파인튜닝 연동 3단계 가이드
[사이버 보안 데이터셋 가이드](../data/security_datasets.md)의 빌더 스크립트로 생성한 `security_sft_dataset.json`을 LLaMA-Factory에 주입하여 학습을 실행하는 구체적인 실무 단계입니다.

#### 1단계. 데이터셋 등록 (`data/dataset_info.json`)
빌더가 추출한 데이터셋 파일(`security_sft_dataset.json`)을 LLaMA-Factory의 `data/` 폴더 하위로 복사한 후, `data/dataset_info.json`을 열어 아래와 같이 맵핑 메타데이터를 추가 등록합니다.
```json
  "security_sft_dataset": {
    "file_name": "security_sft_dataset.json",
    "columns": {
      "prompt": "instruction",
      "query": "input",
      "response": "output"
    }
  }
```

#### 2단계. DeepSpeed ZeRO-3 설정 작성 (`ds_z3_config.json`)
B200 GPU 서버의 VRAM을 극대화하고 학습 속도를 높이기 위해 가중치 조각화 병렬 처리를 지원하는 설정 파일을 학습 폴더 루트에 생성합니다.
```json
{
  "fp16": {
    "enabled": "auto"
  },
  "bf16": {
    "enabled": "auto"
  },
  "zero_optimization": {
    "stage": 3,
    "offload_optimizer": {
      "device": "none"
    },
    "offload_param": {
      "device": "none"
    },
    "overlap_comm": true,
    "contiguous_gradients": true,
    "sub_group_size": 1e9,
    "reduce_bucket_size": "auto",
    "stage3_prefetch_bucket_size": "auto",
    "stage3_param_persistence_threshold": "auto",
    "stage3_max_live_nodes": 1e6,
    "stage3_max_reuse_distance": 1e6,
    "stage3_gather_1d_weights": true
  },
  "gradient_accumulation_steps": "auto",
  "gradient_clipping": "auto",
  "steps_per_print": 2000,
  "train_batch_size": "auto",
  "train_micro_batch_size_per_gpu": "auto",
  "wall_clock_breakdown": false
}
```

#### 3단계. 파인튜닝 쉘 스크립트 실행 (B200 4장 / LoRA 기준)
아래 쉘 스크립트를 기동하여, 정제된 소스코드 보안 분석 학습을 시작합니다.
```bash
# 4개의 B200 GPU를 학습용으로 지정
export CUDA_VISIBLE_DEVICES=0,1,2,3

torchrun --nproc_per_node=4 --master_port=29502 \
  src/train.py \
  --deepspeed ds_z3_config.json \
  --stage sft \
  --do_train \
  --model_name_or_path /models/qwen/Qwen2.5-Coder-72B-Instruct \
  --dataset security_sft_dataset \
  --dataset_dir ./data \
  --template qwen \
  --finetuning_type lora \
  --lora_target all \
  --output_dir ./adapters/qwen-coder-security-lora \
  --overwrite_output_dir \
  --cutoff_len 8192 \
  --preprocessing_num_workers 16 \
  --per_device_train_batch_size 2 \
  --gradient_accumulation_steps 8 \
  --lr_scheduler_type cosine \
  --logging_steps 10 \
  --warmup_ratio 0.1 \
  --learning_rate 1e-4 \
  --num_train_epochs 3.0 \
  --fp16 False \
  --bf16 True
```

---

## 6. 권장 실험 계획

## 6.1 1단계: vLLM 환경 검증

먼저 작은 비교 모델 또는 GLM-4.5-Air-FP8로 vLLM 기본 환경을 검증한다.

목표는 다음과 같다.

```text
1. CUDA/NCCL 정상 동작 확인
2. vLLM serve 정상 기동 확인
3. OpenAI-compatible API 응답 확인
4. tokenizer/chat template 문제 확인
5. benchmark client 동작 확인
```

이 단계에서 바로 480B 모델로 들어가면 문제 원인을 분리하기 어렵다. 먼저 기준 모델로 API path와 serving stack을 검증한 뒤 대형 모델로 넘어가는 편이 안정적이다.

---

## 6.2 2단계: Qwen3-Coder-480B FP8 서빙

두 번째 단계에서 메인 극한 모델을 구동한다.

초기 설정은 보수적으로 잡는다.

```text
tensor_parallel_size: 4
expert_parallel: enabled
max_model_len: 32K
max_num_seqs: 1
gpu_memory_utilization: 0.90~0.94
```

이후 다음 항목을 단계적으로 올린다.

```text
1. max_model_len
2. max_num_seqs
3. random input length
4. random output length
5. benchmark concurrency
6. gpu_memory_utilization
```

이 단계의 핵심 산출물은 단순 성공 여부가 아니다.

```text
1. 최대 안정 context length
2. 최대 안정 concurrency
3. OOM 발생 조건
4. TTFT
5. TPOT
6. output tokens/sec
7. GPU별 memory balance
8. NCCL 오류 여부
9. 첫 요청 latency
10. 장시간 구동 안정성
```

---

## 6.3 3단계: GLM-4.5-FP8 비교

Qwen3-Coder-480B가 코딩 특화 극한 모델이라면, GLM-4.5-FP8은 reasoning/agent 성향 비교 모델로 둔다.

같은 benchmark 조건에서 비교한다.

```text
input length: 8K, 16K, 32K, 64K
output length: 1K, 2K, 4K
concurrency: 1, 2, 4
```

비교 항목은 다음과 같다.

```text
1. 모델 기동 시간
2. VRAM 사용량
3. TTFT
4. TPOT
5. 긴 context에서의 안정성
6. 코딩 태스크 품질
7. reasoning 태스크 품질
8. tool-call parser 사용성
9. vLLM 옵션 호환성
```

이 비교를 통해 최종적으로 어떤 모델을 메인 로컬 서빙 모델로 둘지 판단한다.

---

## 6.4 4단계: DeepSeek 계열 한계 테스트

DeepSeek-R1 또는 DeepSeek-V3는 안정 운영 후보라기보다, 4×B200의 상한선을 확인하기 위한 모델이다.

처음부터 긴 context를 시도하지 않는다.

```text
max_model_len: 8K
max_num_seqs: 1
concurrency: 1
```

이 단계에서 확인할 것은 다음이다.

```text
1. 모델 weight 로딩 가능 여부
2. vLLM 초기화 성공 여부
3. 첫 응답 생성 가능 여부
4. memory fragmentation 발생 여부
5. expert parallel 관련 오류 여부
6. GPU별 메모리 편차
7. 짧은 context에서의 decode 가능성
```

이 모델은 실패 가능성을 전제로 둔다. 하지만 이 실패는 의미 있는 실패다. 어디서 막히는지 알면, 이후 4×B200 환경에서 어떤 규모의 모델을 안정권으로 볼 수 있는지 판단할 수 있다.

---

## 6.5 5단계: LoRA/QLoRA 파인튜닝

파인튜닝은 GLM-4.5-Air 또는 중형 Qwen 계열로 시작한다.

권장 순서는 다음과 같다.

```text
1. base model 로컬 저장
2. 학습 데이터 chat format 정리
3. LoRA SFT 수행
4. adapter 저장
5. vLLM에서 base model + LoRA adapter 로딩
6. 원본 모델과 adapter 모델 응답 비교
7. latency 및 VRAM 변화 측정
```

초기 학습 설정은 다음처럼 잡는다.

```text
sequence length: 4096 또는 8192
per_device_train_batch_size: 1
gradient_accumulation_steps: 8~32
bf16: true
gradient_checkpointing: true
LoRA rank: 16
LoRA alpha: 32 또는 64
LoRA dropout: 0.05
```

처음부터 full fine-tuning은 하지 않는다. 이 환경에서 중요한 것은 “학습을 끝까지 한 번 돌리는 것”과 “학습된 adapter를 실제 vLLM serving에 붙여보는 것”이다.

---

## 7. 벤치마크 계획

vLLM의 `vllm bench serve`를 활용해 serving 성능을 측정한다.

기본 예시는 다음과 같다.

```bash
vllm bench serve \
  --backend openai-chat \
  --base-url http://127.0.0.1:8000 \
  --endpoint /v1/chat/completions \
  --model qwen3-coder-480b-fp8 \
  --dataset-name random \
  --num-prompts 64 \
  --max-concurrency 1 \
  --random-input-len 8192 \
  --random-output-len 1024 \
  --ignore-eos
```

벤치마크는 다음 순서로 올린다.

```text
input_len:    8K → 16K → 32K → 64K → 128K
output_len:   1K → 2K → 4K
concurrency:  1 → 2 → 4 → 8
num_prompts: 64 → 128 → 256
```

측정해야 할 핵심 지표는 다음과 같다.

```text
1. TTFT, Time To First Token
2. TPOT, Time Per Output Token
3. output tokens/sec
4. request throughput
5. GPU memory usage
6. KV cache usage
7. OOM 발생 조건
8. NCCL error 여부
9. server startup time
10. first request latency
11. long-running stability
```

벤치마크 결과는 모델별로 동일한 형식으로 남긴다.

```text
model_name
checkpoint_dtype
tensor_parallel_size
expert_parallel_enabled
max_model_len
max_num_seqs
gpu_memory_utilization
input_len
output_len
concurrency
TTFT
TPOT
tokens/sec
peak_memory_per_gpu
failure_condition
notes
```

이렇게 남겨야 나중에 5장 반납 후 4장 환경에서도 같은 조건을 재현할 수 있다.

---

## 8. 리스크와 대응 방안

### 8.1 OOM 리스크

대형 MoE 모델은 weight loading은 성공해도 실제 요청 시 KV cache에서 OOM이 발생할 수 있다.

대응 방안은 다음과 같다.

```text
1. max_model_len을 낮춘다
2. max_num_seqs를 낮춘다
3. concurrency를 낮춘다
4. kv-cache-dtype을 FP8로 설정한다
5. gpu_memory_utilization을 보수적으로 조정한다
6. 먼저 짧은 context에서 decode 가능 여부를 확인한다
```

---

### 8.2 5-way TP 비효율 리스크

5장을 하나의 tensor parallel group으로 묶으면 모델 구조와 맞지 않아 실패하거나 비효율이 발생할 수 있다.

대응 방안은 명확하다.

```text
메인 서빙은 TP=4로 고정
5번째 GPU는 독립 실험용으로 사용
```

---

### 8.3 Token 노출 리스크

서버에 Hugging Face token을 저장하면 보안상 부담이 생긴다.

대응 방안은 다음과 같다.

```text
1. 서버에서 huggingface-cli login 금지
2. 다운로드 노드에서만 HF_TOKEN 사용
3. 다운로드 후 token 제거
4. 서버에는 모델 artifact만 전송
5. 서버는 HF_HUB_OFFLINE=1로 실행
```

---

### 8.4 파인튜닝 대상 과대 설정 리스크

480B 또는 671B 모델을 바로 파인튜닝 대상으로 삼으면 실험 반복 속도가 지나치게 느려지고 디버깅 비용이 커진다.

대응 방안은 다음과 같다.

```text
서빙 극한 모델과 파인튜닝 모델을 분리한다.
서빙 극한: Qwen3-Coder-480B, GLM-4.5-FP8, DeepSeek 계열
파인튜닝: GLM-4.5-Air, 중형 Qwen 계열, gpt-oss-120b
```

---

## 9. 최종 권장 구성

가장 균형 잡힌 구성은 다음과 같다.

```text
메인 극한 서빙 모델:
Qwen3-Coder-480B-A35B-Instruct-FP8

비교 서빙 모델:
GLM-4.5-FP8

한계 테스트 모델:
DeepSeek-R1 또는 DeepSeek-V3

기준선/검증 모델:
gpt-oss-120b

파인튜닝 후보:
GLM-4.5-Air 또는 중형 Qwen 계열
```

GPU 구성은 다음을 권장한다.

```text
GPU 0,1,2,3:
대형 모델 vLLM serving

GPU 4:
benchmark client
또는 gpt-oss-120b 단독 serving
또는 LoRA fine-tuning 실험
```

운영 기준은 4장이다. 5번째 GPU는 메인 구조에 편입하지 않고, 실험 가속과 비교 평가에 사용한다. 이 방식이 향후 4장 환경으로 축소되었을 때 가장 손실이 적다.

---

## 10. 결론

이번 환경은 일반적인 로컬 LLM 실험 환경이 아니다. B200 5장을 사용할 수 있는 시점은 짧더라도, 이 기간 동안 얻을 수 있는 경험치는 상당히 크다. 따라서 70B급 안정 운영에 머무르기보다, 4×B200 기준에서 재현 가능한 구조를 만들고, 5번째 GPU를 활용해 대형 MoE 모델의 실질적인 한계선을 확인하는 편이 낫다.

가장 추천하는 진행 방향은 다음과 같다.

```text
1. 서버에는 Hugging Face token을 남기지 않는다.
2. 모델은 별도 환경에서 다운로드 후 /models 경로로 전송한다.
3. vLLM은 local path 기반으로 실행한다.
4. 메인 서빙 구조는 4×B200, TP=4로 고정한다.
5. Qwen3-Coder-480B-A35B-Instruct-FP8을 1순위 극한 모델로 실험한다.
6. GLM-4.5-FP8로 reasoning/agent 성향을 비교한다.
7. DeepSeek 계열로 4×B200의 상한선을 확인한다.
8. 파인튜닝은 GLM-4.5-Air 또는 중형 Qwen 계열 LoRA로 별도 진행한다.
9. 모든 실험은 context length, concurrency, TTFT, TPOT, OOM 조건을 기록한다.
```

최종적으로 이 제안의 핵심은 하나다.

**지금 5장을 “운영 구조”에 묶지 말고, 4장 기준의 재현 가능한 서빙 체계를 만든 뒤 5번째 GPU로 극한 실험과 비교 실험을 병렬 수행해야 한다.**

이렇게 접근하면 GPU를 반납하기 전에는 대형 모델 서빙의 한계를 충분히 밀어붙일 수 있고, 반납 이후에는 4×B200 환경에서 바로 이어갈 수 있는 실전형 로컬 LLM 운영 체계를 확보할 수 있다.
