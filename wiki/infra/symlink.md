---
type: Concept
title: 심볼릭 링크 생성 및 해제 방법 (Symbolic Link)
description: Linux, macOS, Windows 환경에서 심볼릭 링크를 안전하게 생성하고 해제하는 명령어 정리
tags: [infra, os, command]
timestamp: 2026-07-02
status: active
---

# Summary
심볼릭 링크(Symbolic Link, Symlink)는 파일 시스템에서 다른 파일이나 디렉토리를 가리키는 특별한 유형의 파일(바로가기)입니다. 이 문서에서는 OS 환경별로 심볼릭 링크를 생성하고 안전하게 해제(삭제)하는 명령어를 설명합니다.

# Why it matters
심볼릭 링크를 삭제할 때 잘못된 명령어를 사용하면 링크 대상이 아닌 **원본 디렉토리나 파일의 내용이 삭제되는 불상사**가 발생할 수 있습니다. 특히 디렉토리 심볼릭 링크를 삭제할 때는 경로 끝에 슬래시(`/`)를 붙이지 않는 등 올바른 해제 방법을 숙지해야 합니다.

# Key Ideas

## 1. Linux / macOS
유닉스 계열 환경에서는 `rm` 또는 `unlink` 명령어를 사용합니다.

### 1.1. 안전한 해제 방법 (`unlink`)
`unlink` 명령어는 대상이 파일이든 디렉토리이든 상관없이 **심볼릭 링크 파일 자체만 안전하게 삭제**합니다. 가장 권장되는 방식입니다.
```bash
unlink <링크_이름>
```
*예시:*
```bash
unlink my_shortcut
```

### 1.2. 일반 삭제 방법 (`rm`)
`rm` 명령어로도 심볼릭 링크를 삭제할 수 있지만, 디렉토리 링크의 경우 주의가 필요합니다.
- **파일 링크 삭제**:
  ```bash
  rm <링크_이름>
  ```
- **디렉토리 링크 삭제 (매우 중요)**:
  디렉토리 링크 뒤에 슬래시(`/`)를 붙이지 않고 명령어만 실행해야 합니다.
  ```bash
  # 올바른 방법
  rm <링크_이름>
  
  # 절대 하지 말아야 할 방법 (원본 디렉토리의 데이터가 삭제될 위험이 있음)
  rm -rf <링크_이름>/
  ```

---

## 2. Windows
윈도우 환경에서는 명령 프롬프트(cmd), PowerShell, 또는 GUI 탐색기에서 해제할 수 있습니다.

### 2.1. 명령 프롬프트 (cmd.exe)
윈도우 cmd에서는 파일 링크와 디렉토리 링크를 삭제하는 명령어가 다릅니다.
- **파일 심볼릭 링크 삭제**:
  ```cmd
  del <링크_이름>
  ```
- **디렉토리 심볼릭 링크 삭제**:
  ```cmd
  rmdir <링크_이름>
  ```

### 2.2. PowerShell
PowerShell에서는 파일과 디렉토리 구분 없이 `Remove-Item`을 사용하면 안전하게 링크만 해제됩니다.
```powershell
Remove-Item <링크_이름>
# 또는 alias 사용
rm <링크_이름>
del <링크_이름>
```

### 2.3. 파일 탐색기 (GUI)
파일 탐색기에서 해당 심볼릭 링크 아이콘을 마우스 우클릭하여 **삭제**를 누르거나, 선택 후 `Delete` 키를 누르면 원본 손상 없이 바로가기만 삭제됩니다.

---

## 3. 심볼릭 링크 생성 방법 (참고)
해제하기 전에 생성하는 방법은 다음과 같습니다.

### Linux / macOS
```bash
ln -s <원본_경로> <링크_이름>
```

### Windows (cmd.exe - 관리자 권한 필요)
- 파일 링크: `mklink <링크_이름> <원본_경로>`
- 디렉토리 링크: `mklink /d <링크_이름> <원본_경로>`

### Windows (PowerShell - 관리자 권한 필요)
```powershell
New-Item -ItemType SymbolicLink -Path <링크_이름> -Value <원본_경로>
```

# Related Concepts
- [Infra Index](index.md)
