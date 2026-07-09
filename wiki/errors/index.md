# Errors

- [LLaMA-Factory Checkpoint Save Failed Because Model Symlink Target Disappeared](llamafactory-checkpoint-save-broken-model-symlink.md) - Qwen3-Coder-Next 80B full training이 checkpoint 저장 단계에서 깨진 `model` symlink 때문에 중단된 사건
- [LLaMA-Factory CLI Missing After Dependency Drift](llamafactory-cli-missing-after-uv-sync.md) - `.venv/bin/llamafactory-cli` 누락과 `pyproject.toml` training group 복구 기록
- [LLaMA-Factory Qwen3-Coder 480B FP8 SIGKILL Investigation](llamafactory-qwen3-coder-480b-fp8-oom-kill.md) - B200 4-GPU 환경에서 480B FP8 checkpoint loading 중 발생한 `SIGKILL` 분석
- [LLaMA-Factory DeepSpeed ZeRO-3 LoRA BF16 Dtype Mismatch](llamafactory-deepspeed-zero3-dtype-mismatch.md) - 30B/72B LoRA training의 첫 optimizer step dtype mismatch 분석
