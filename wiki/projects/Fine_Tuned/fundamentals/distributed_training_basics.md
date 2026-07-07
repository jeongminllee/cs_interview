---
type: Study Note
title: Distributed Training Basics
description: process, rank, world size, local rank, torchrun, DDP 기본기와 B200 4-GPU 해석법.
tags: [finetuning, distributed-training, torchrun, ddp, basics]
timestamp: 2026-07-03
status: active
---

# Summary

분산 학습은 여러 GPU나 여러 node에 학습 일을 나눠서 처리하는 방식이다. B200 4장 서버에서는 일반적으로 GPU 1장당 training process 1개를 띄운다.

중요한 점은 `4개 PID = CPU core 4개`가 아니라는 것이다. `torchrun --nproc_per_node 4`는 하나의 node에서 4개의 distributed rank process를 만든다.

# Process And Rank

Process는 OS가 실행하는 독립 실행 단위다. Distributed training에서는 보통 각 process가 하나의 GPU를 맡는다.

Rank는 distributed group 안에서 process를 식별하는 번호다.

대표 용어:

- `rank`: 전체 process 중 내 번호
- `local_rank`: 현재 node 안에서 내 번호
- `world_size`: 전체 process 수
- `nproc_per_node`: node 하나에서 띄울 process 수

B200 4-GPU 단일 node 예:

```text
nproc_per_node = 4
world_size = 4
local_rank = 0, 1, 2, 3
GPU = cuda:0, cuda:1, cuda:2, cuda:3
```

# torchrun

`torchrun`은 PyTorch distributed launcher다. LLaMA-Factory가 multi-GPU 학습을 시작할 때 내부적으로 `torchrun`을 호출한다.

예:

```bash
torchrun --nproc_per_node 4 train.py
```

의미:

- `train.py`를 4개 process로 실행한다.
- 각 process에 local rank 정보를 전달한다.
- process들이 distributed communication group을 구성한다.

# DDP

DDP는 Distributed Data Parallel의 약자다.

기본 구조:

- 각 GPU에 model replica가 있다.
- 각 process가 서로 다른 mini-batch를 처리한다.
- backward 후 gradient를 all-reduce로 동기화한다.
- 각 process가 같은 update를 적용한다.

장점은 단순하고 안정적이라는 점이다. 단점은 model weight, gradient, optimizer state가 각 GPU/process에 중복될 수 있다는 점이다.

# Why Rank Count Can Increase Memory

Rank를 늘리면 GPU가 늘어 처리량은 좋아질 수 있다. 하지만 checkpoint loading 단계에서는 각 rank가 weight shard를 독립적으로 읽거나 임시 buffer를 만들 수 있다.

따라서 큰 모델에서는 rank 수가 늘면서 CPU RSS 총합이 거의 선형으로 커질 수 있다. 480B loading에서 rank별 RSS를 보는 이유가 여기에 있다.

# SIGTERM And SIGKILL In torchrun

한 rank가 먼저 죽으면 torchrun은 나머지 rank를 정리한다.

해석:

- root cause rank가 `SIGKILL(-9)`이면 외부 kill 또는 kernel/cgroup kill 가능성을 본다.
- 나머지 rank의 `SIGTERM(-15)`은 torchrun cleanup일 수 있다.
- Python traceback이 없으면 Python exception이 아니라 process 외부 종료일 수 있다.

# Project Connection

우리 480B 로그에서 보이는 4개 PID는 다음 의미다.

```text
PID 1 -> local_rank 0 -> GPU 0
PID 2 -> local_rank 1 -> GPU 1
PID 3 -> local_rank 2 -> GPU 2
PID 4 -> local_rank 3 -> GPU 3
```

이 PID들은 CPU core가 아니다. 각 process 안에는 여러 CPU thread가 있을 수 있다. CPU 문제를 보려면 PID 수보다 CPU utilization, thread count, `cpu.pressure`, `pids.current`를 봐야 한다.

# Related Concepts

- [PyTorch Training Basics](pytorch_training_basics.md)
- [DeepSpeed ZeRO Basics](deepspeed_zero_basics.md)
- [W&B and Telemetry Basics](wandb_telemetry_basics.md)
- [B200 Qwen3-Coder 480B SIGKILL Analysis Process](../repos/AegisLM/docs/B200_QWEN3_480B_MEMORY_PROCESS.md)

# Citations

- [PyTorch torchrun documentation](https://docs.pytorch.org/docs/stable/elastic/run.html)
- [PyTorch distributed run source note](https://github.com/pytorch/pytorch/blob/main/torch/distributed/run.py)
