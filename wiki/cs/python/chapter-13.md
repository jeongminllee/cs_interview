---
type: Study Note
title: "Chapter 13: Python File Input/Output (파이썬 파일 입출력)"
description: "영구적 데이터 보관을 위한 파일 입출력의 개념과 텍스트/이진 파일의 물리적 차이, 그리고 파일 처리 3단계 라이프사이클을 심층 학습합니다. 절대/상대 경로 지정 및 raw string(r'') 기법, open()의 인코딩 매핑(UTF-8 vs CP949)을 통한 UnicodeDecodeError 예방 수칙을 정리합니다. 또한 read, readline, readlines 메서드의 반환 타입 분석과 write()의 정수형 캐스팅 의무화 규칙, 실전 성적 산출 및 메트릭 계측 실습을 수록합니다."
tags: [file-io, text-files, file-modes, raw-string, file-encoding, read-methods, write-method, strip-method, practical-examples]
timestamp: 2026-06-18
status: active
---

# 13. 파일 입출력 (Python File I/O)

## 13.1 파일 입출력의 필요성과 유형

### (1) 파일 입출력(File I/O)의 필요성
* **데이터 영속성 (Persistence)**: 프로그램 실행 중에 변수나 리스트에 저장한 데이터는 프로그램이 종료되면 RAM(휘발성 메모리)에서 즉시 사라집니다. 데이터를 영구히 저장하고 나중에 다시 읽어오려면 SSD/HDD 같은 보조기억장치에 파일 형태로 기록해야 합니다.
* **편의성 및 대용량 처리**: 매번 수동으로 실행 화면에 데이터를 타이핑할 필요 없이, 파일에 저장된 빅데이터를 자동으로 읽어 신속히 연산 처리할 수 있습니다.

### (2) 표준 입출력 vs 파일 입출력
* **표준 입출력 (Standard I/O)**: 키보드나 마우스 등 표준 입력장치로 값을 받아 모니터 화면에 결과를 출력하는 단기성 데이터 제어.
* **파일 입출력 (File I/O)**: 보조기억장치 상의 물리 파일로부터 데이터를 읽어오고(Read), 연산 결과를 파일로 저장(Write)하는 장기성 데이터 제어.

### (3) 파일의 두 가지 물리적 유형
1. **텍스트 파일 (Text File)**: 사람이 텍스트 에디터로 열어서 직접 읽고 쓸 수 있는 형태의 파일입니다. 문자, 숫자, 특수 문자 등이 아스키(ASCII) 또는 유니코드(UTF-8, UTF-16) 규격 인코딩에 맞춰 숫자로 저장됩니다. (예: `.txt`, `.csv`, `.py` 등)
2. **이진 파일 (Binary File)**: 사람이 읽을 수 있는 문자가 아니라, 컴퓨터가 메모리 내부에서 데이터를 나타내는 방식 그대로의 이진수(0과 1) 데이터를 그대로 보관한 파일입니다. 전용 뷰어 프로그램이 필요합니다. (예: 이미지 `.png`, 오디오 `.mp3`, 실행파일 `.exe` 등)

---

## 13.2 파일 처리의 3단계 라이프사이클

파이썬에서 파일을 제어할 때는 물리적인 OS 자원을 다루므로 반드시 다음 **3단계 순서**를 엄격히 준수해야 합니다.

```
1단계: 파일 열기 (open) ➡️ 2단계: 파일 읽기/쓰기 (작업) ➡️ 3단계: 파일 닫기 (close)
```

### (1) 1단계: 파일 열기 (open)
`open()` 함수를 호출하여 파일 스트림 객체를 획득합니다.
```python
file_object = open(파일경로, 모드, encoding='utf-8')
```

#### 1) 절대 경로와 상대 경로
* **절대 경로**: 컴퓨터 루트(예: `C:/`)에서부터 모든 폴더 명칭을 다 적어 고정된 위치를 정확히 가리키는 방식입니다.
  * **윈도우 경로 주의**: 백슬래시(`\`)를 사용하여 경로를 기재할 때 `\n`, `\t` 등 이스케이프 특수 문자로 오인되어 경로가 깨질 수 있습니다. 이를 막기 위해 슬래시(`/`)를 쓰거나, 경로 문자열 앞에 **`r`**을 붙여 날것 그대로의 문자열로 처리하는 **Raw String 접두사**를 붙여야 합니다.
  ```python
  f = open(r"C:\project\data\test.txt", "r") # raw string 사용
  ```
* **상대 경로**: 현재 파이썬 스크립트가 실행되고 있는 작업 디렉토리(Current Working Directory)를 기준으로 파일 위치를 추적하는 유연한 방식입니다.
  * `.` : 현재 폴더
  * `..` : 상위 부모 폴더
  * `./sub_dir/test.txt` : 하위 폴더인 sub_dir 내 파일 지칭.

#### 2) 파일 접근 모드 (File Modes)
| 모드 | 명칭 | 기능 설명 |
| :--- | :--- | :--- |
| **`'r'`** | 읽기 (Read) | 기본 설정값. 파일 내용을 읽을 때 사용하며, 파일이 해당 경로에 없으면 `FileNotFoundError` 발생. |
| **`'w'`** | 쓰기 (Write) | 파일에 데이터를 새로 쓸 때 사용. 파일이 없으면 신규 생성하고, 이미 있다면 **기존 내용을 완전히 덮어쓰고 지운 뒤(Overwrite)** 새로 기재함. |
| **`'a'`** | 추가 (Append) | 기존 파일의 내용 끝에 새로운 데이터를 덧붙여 쓰고 싶을 때 사용. 파일이 없으면 새로 생성함. |

#### 3) 인코딩 매핑 및 UnicodeDecodeError 예방
한글이 포함된 텍스트 파일을 읽고 쓸 때, 인코딩이 맞지 않으면 글자가 깨지거나 `UnicodeDecodeError: 'cp949' codec can't decode...` 와 같은 치명적인 에러가 발생합니다.
* **원인**: 윈도우 OS의 기본 인코딩은 한국 전용 완성형인 **CP949**이며, 대다수 개발 소스나 최신 웹 텍스트 표준은 **UTF-8** 유니코드입니다. 저장할 때 쓴 인코딩과 파이썬이 읽을 때 시도하는 인코딩 인자가 맞지 않아 해독에 실패하는 것입니다.
* **해결책**: 파일을 생성하거나 읽을 때 항상 **`encoding='utf-8'`** 옵션을 매개변수에 명시적으로 강제 매핑해 줍니다.
  ```python
  infile = open("hangul.txt", "r", encoding="utf-8")
  ```

### (2) 3단계: 파일 닫기 (close)
작업이 끝난 파일은 반드시 `.close()` 메서드를 호출해 주어야 합니다. 닫지 않고 방치하면 파일 디스크립터 자원 누수(Leak)가 일어나 OS가 파일을 잠금(Lock) 상태로 유지하거나, 쓰기 버퍼에 남아 있던 데이터가 물리 디스크로 최종 기록되지 않아 소실되는 논리 에러가 생깁니다.
```python
infile.close()
```
> [!TIP]
> **with open 구문의 활용 (권장)**:
> 파이썬에서는 `with` 구문 블록을 제공합니다. 이 블록 내에서 작업이 끝나거나 예외가 발생해 블록을 이탈하는 즉시, 파이썬이 내부적으로 자동으로 `.close()` 처리를 완료해 주어 안전합니다.
> ```python
> with open("test.txt", "r", encoding="utf-8") as f:
>     content = f.read()
> # 이 라인부터 f는 자동으로 close 됨
> ```

---

## 13.3 파일 읽기(Read) 메서드 비교 분석

파이썬은 파일 읽기를 위해 각각 다른 데이터 타입을 반환하는 4가지 핵심 메서드를 제공합니다.

| 메서드명 | 반환 타입 | 작동 특징 |
| :--- | :--- | :--- |
| **`read()`** | **`str`** | 파일의 첫 바이트부터 끝까지 전체 본문을 단 하나의 거대한 통 문자열로 로드하여 반환합니다. |
| **`read(n)`** | **`str`** | 현재 포인터 위치로부터 딱 $n$ 바이트(글자)만 읽어 반환하고 포인터를 이동시킵니다. 파일 끝에 닿으면 빈 문자열(`""`)을 냅니다. |
| **`readline()`** | **`str`** | 한 번 호출할 때마다 딱 한 줄만 문자열로 반환합니다. 반환 문자열 끝에는 개행 문자(`\n`)가 무조건 포함됩니다. |
| **`readlines()`** | **`list`** | 파일의 모든 줄을 통째로 읽어 **줄 단위 리스트(List of Strings)**로 반환합니다. 각 원소 끝에는 개행 문자(`\n`)가 포함됩니다. |

#### [코드] 개행 문자 정제 및 출력 패턴 비교
```python
# 1. readline()을 이용한 한 줄씩 순회 출력
with open("text.txt", "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:  # 빈 문자열(파일 끝)이면 루프 탈출
            break
        # strip()으로 우측 개행 \n 제거 후 출력
        print(line.strip())

# 2. readlines() 리스트를 이용한 루프 출력
with open("text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

---

## 13.4 파일 쓰기(Write) 제약과 정수형 캐스팅

`write(string)` 메서드를 통해 문자열을 파일 스트림으로 방출하여 저장합니다.
> [!IMPORTANT]
> **정수/실수 데이터의 str 캐스팅 규칙**:
> `write()` 메서드는 **오직 문자열(str) 자료형만 인자로 수신**합니다. 정수나 실수형 값(예: `99` 또는 `3.14`)을 가공 없이 그냥 대입하면 `TypeError: write() argument must be str, not int` 에러가 납니다. 따라서 반드시 **`str()` 내장 함수로 형변환**한 뒤 출력 버퍼로 보내야 합니다.
> ```python
> with open("numbers.txt", "w", encoding="utf-8") as f:
>     f.write(str(99) + "\n")  # 정수 99를 str형으로 형변환하여 기록
> ```

---

## 13.5 실전 퀴즈 풀이 및 코드 구현

### [퀴즈 1] 성적 파일 처리 시뮬레이션 (scores.txt)
* **요구사항**: 
  - `scores.txt` 파일에는 한 줄당 점수 정수가 하나씩 기재되어 있습니다.
  - 파일로부터 점수들을 모두 읽어 정수형 리스트로 바인딩합니다.
  - 이 리스트를 바탕으로 합계, 평균 점수, 최고 점수, 최저 점수를 구하는 프로그램을 만드십시오.
```python
# scores.txt 파일 생성 (가상 테스트용)
with open("scores.txt", "w", encoding="utf-8") as f:
    f.write("85\n92\n78\n90\n64\n88\n")

# 읽기 및 성적 연산 가동
scores = []
try:
    with open("scores.txt", "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line:
                scores.append(int(clean_line))
                
    # 결과 계산
    total = sum(scores)
    avg = total / len(scores) if scores else 0
    max_score = max(scores) if scores else 0
    min_score = min(scores) if scores else 0
    
    print("=== 성적 통계 결과 ===")
    print(f"점수 목록: {scores}")
    print(f"합계 점수: {total}점")
    print(f"평균 점수: {avg:.2f}점")
    print(f"최고 점수: {max_score}점")
    print(f"최저 점수: {min_score}점")
    
except FileNotFoundError:
    print("에러: scores.txt 파일을 찾을 수 없습니다.")
```

### [퀴즈 2] 텍스트 파일의 라인 수, 단어 수, 문자 수 카운터
* **요구사항**: `text_kor.txt` 텍스트 파일을 분석하여 총 몇 개의 줄(라인)로 이루어졌는지, 공백 기준으로 단어가 몇 개 존재하는지, 개행을 포함한 총 문자 수는 몇 개인지 종합 계측해 보여주는 통계 프로그램을 작성하십시오.
```python
# text_kor.txt 가상 텍스트 파일 생성
dummy_text = """Python is a high-level programming language
Python is an object-oriented language
파이썬은 고급 프로그래밍 언어
파이썬은 객체 지향 언어"""

with open("text_kor.txt", "w", encoding="utf-8") as f:
    f.write(dummy_text)

# 메트릭 계측 시작
line_count = 0
word_count = 0
char_count = 0

with open("text_kor.txt", "r", encoding="utf-8") as f:
    for line in f:
        line_count += 1
        char_count += len(line)  # 문자수 (개행문자 포함)
        
        # split()은 연속 공백 및 개행을 정제하여 단어 리스트로 전환함
        words = line.split()
        word_count += len(words)

print("=== 텍스트 메트릭 분석 ===")
print(f"분석 파일: text_kor.txt")
print(f"총 라인 수: {line_count} 줄")
print(f"총 단어 수: {word_count} 개")
print(f"총 문자 수: {char_count} 자")
```
```text
=== 텍스트 메트릭 분석 ===
분석 파일: text_kor.txt
총 라인 수: 4 줄
총 단어 수: 16 개
총 문자 수: 104 자
```

---

# Related Concepts
* [Lists](chapter-07.md) — readlines()의 리스트 반환 구조 및 요소 가공.
* [Advanced Functions](chapter-10.md) — split()을 활용한 데이터 파싱 가공 기법.

# Citations
* Chapter 13_파일입출력__업데이트_260516.pdf [Python 13장](../../../raw/notes/Python/Chapter 13_파일입출력__업데이트_260516.pdf)
