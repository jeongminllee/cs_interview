---
type: Study Note
title: W&B and Telemetry Basics
description: W&B loss logging, model/watch 설정, cgroup/GPU/process telemetry를 함께 읽는 기본기.
tags: [finetuning, wandb, telemetry, monitoring, basics]
timestamp: 2026-07-03
status: active
---

# Summary

Fine-tuning에서는 학습 loss만 보는 것으로 충분하지 않다. 특히 480B급 학습에서는 training log, W&B log, GPU log, cgroup memory log를 같이 봐야 한다.

W&B는 학습 지표를 기록하고, memory watcher는 system-level telemetry를 기록한다. 둘은 목적이 다르다.

# W&B

W&B는 experiment tracking 도구다.

주로 기록하는 것:

- loss
- learning rate
- global step
- epoch
- runtime
- config
- run name

LLaMA-Factory에서는 YAML의 `report_to: wandb`와 `run_name`으로 연결된다.

# WANDB_LOG_MODEL

`WANDB_LOG_MODEL`은 model artifact를 W&B에 업로드할지와 관련된다.

우리 기본값:

```bash
export WANDB_LOG_MODEL=false
```

이유:

- 480B base model과 adapter/checkpoint artifact는 매우 크다.
- 모델 파일은 `model/` 아래 local artifact policy로 관리한다.
- W&B에는 loss와 run metadata 중심으로 남긴다.

# WANDB_WATCH

`WANDB_WATCH` 또는 `wandb.watch()`는 gradient와 parameter histogram 같은 정보를 기록할 수 있다.

우리 기본값:

```bash
export WANDB_WATCH=false
```

이유:

- 대형 모델에서 gradient/parameter watch는 overhead가 커질 수 있다.
- 480B calibration 단계에서는 먼저 loss logging과 run 생존 여부가 중요하다.

# Memory Watcher

`scripts/check_memory_budget.py --watch`는 W&B가 보지 않는 system telemetry를 남긴다.

중요 필드:

- cgroup `memory.current`
- cgroup `memory.peak`
- cgroup `memory.max`
- `memory.events.oom`
- `memory.events.oom_kill`
- GPU memory used
- GPU utilization
- process RSS
- thread count
- pids current/max
- CPU pressure

현재 정책은 observe-only다. watcher가 학습 process에 signal을 보내면 원인 분석이 흐려지므로 금지한다.

# How To Read Logs Together

## Case 1: W&B loss가 찍히기 전 종료

가능성:

- model loading 실패
- dataset loading 실패
- distributed initialization 실패
- external kill

볼 것:

- torchrun root cause
- cgroup memory events
- rank별 RSS
- checkpoint loading progress

## Case 2: W&B loss가 찍힌 뒤 종료

가능성:

- optimizer step 오류
- checkpoint save 오류
- evaluation 오류
- memory drift

볼 것:

- 마지막 logged step
- traceback
- adapter/checkpoint directory
- cgroup events 변화

## Case 3: SIGKILL만 있고 Python traceback 없음

가능성:

- cgroup memory limit
- external watchdog/admin kill
- kernel-level kill

볼 것:

- `oom_kill` 증가 여부
- `memory.current`가 `memory.max`에 가까웠는지
- process RSS 급락 시점
- GPU OOM 메시지 유무

# Project Connection

480B calibration에서 기록해야 할 최소 항목:

- W&B run URL
- last step
- last loss
- cgroup peak
- `oom_kill` before/after
- peak GPU memory
- checkpoint path
- 종료 signal 또는 exception

# Related Concepts

- [Distributed Training Basics](distributed_training_basics.md)
- [DeepSpeed ZeRO Basics](deepspeed_zero_basics.md)
- [W&B Training Metrics Guide for MalwareAnalysisLLM](../training/wandb_training_metrics_guide.md)
- [B200 Qwen3-Coder 480B Training Gate Guide](../b200/b200_480b_training_gate_guide.md)
- [B200 Qwen3-Coder 480B SIGKILL Analysis Process](../repos/AegisLM/docs/B200_QWEN3_480B_MEMORY_PROCESS.md)

# Citations

- [W&B PyTorch integration](https://docs.wandb.ai/models/integrations/pytorch)
- [W&B Lightning logger common arguments](https://docs.wandb.ai/models/integrations/lightning)
