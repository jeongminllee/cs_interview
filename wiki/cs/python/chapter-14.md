---
type: Study Note
title: "Chapter 14: Python Exception Handling (파이썬 예외처리)"
description: "프로그래밍에서 발생하는 에러의 3대 분류(Syntax, Semantic, Runtime Error)의 물리적 차이점과 디버깅의 주요 기법을 학습합니다. 예외처리(Exception Handling)의 정의와 가용성 측면에서의 필요성을 분석하고, try-except-else-finally 구문의 완벽한 통합 매커니즘과 상황별 3대 실행 흐름 시나리오를 규명합니다."
tags: [exception-handling, try-except, runtime-error, syntax-error, semantic-error, debugger, else-finally, execution-flow]
timestamp: 2026-06-18
status: active
---

# 14. 예외처리 (Python Exception Handling)

## 14.1 에러(Error)의 3대 분류와 특징

프로그램 소스 코드 및 가동 중 발생하는 모든 오류는 시점과 원인에 따라 크게 3가지로 나뉩니다.

### (1) 구문 에러 (Syntax Error)
* **정의**: 특정 프로그래밍 언어가 규정한 문법 규칙을 따르지 않고 코드를 기재하여 발생하는 컴파일 타임 에러입니다.
* **탐지 시점**: 파이썬 인터프리터가 소스코드를 기계어로 번역하는 과정에서 실행 전에 즉각 감지하며, 한 문장이라도 구문 에러가 있다면 프로그램은 시작조차 되지 않고 정지합니다.
* **주요 예시**: 들여쓰기 오류(`IndentationError`), 콜론(`:`) 누락, 괄호 짝 불일치, 맞춤법이 틀린 키워드 기재 등.

### (2) 의미상 에러 (Semantic Error) / 논리 에러 (Logical Error)
* **정의**: 문법 규칙(구문)도 맞고 실행도 아무런 에러 없이 잘 되지만, 개발자가 코드를 잘못 설계하여 **원치 않는 엉뚱한 결과값을 도출해 내는 에러**입니다.
* **탐지 시점**: 컴퓨터나 번역기는 이 오류를 감지할 수 없습니다. 오직 개발자가 테스트 도중 계산 결과가 틀린 것을 발견하고 수동으로 디버깅하여 찾아내야 합니다.
* **주요 예시**: 세 숫자의 평균을 구하기 위해 `a + b + c / 3`으로 기재한 경우. (사칙연산 우선순위에 따라 $a + b + (c/3)$가 계산되는 논리적 실수)
  ```python
  # 논리 에러 해결 방안
  average = (a + b + c) / 3  # 소괄호를 적절히 배치하여 로직 교정
  ```

### (3) 실행시 에러 (Runtime Error) / 예외 (Exception)
* **정의**: 구문 에러도 없고 실행도 정상적으로 가동되었으나, **프로그램이 실행되는 도중(Runtime)에 특정 예외적 상황을 만나 더 이상 연산을 수행하지 못하고 강제 종료**되는 상태입니다.
* **탐지 시점**: 프로그램 실행 중에 탐지됩니다.
* **주요 예시**:
  * 0으로 나누기 시도: `ZeroDivisionError`
  * 존재하지 않는 인덱스 접근: `IndexError`
  * 존재하지 않는 딕셔너리 키 조회: `KeyError`
  * 잘못된 형변환 시도 (예: 문자를 정수로): `ValueError`
  * 존재하지 않는 파일 열기 시도: `FileNotFoundError`

---

## 14.2 버그와 디버깅 (Debugging)

### (1) 디버깅의 정의
* **버그 (Bug)**: 프로그램 소스 코드 내부에 숨어 오류를 야기하는 논리적/구조적 에러들을 의미합니다.
* **디버깅 (Debugging)**: 소스 내에 잠복한 버그를 신속히 추적하여 원인을 밝히고, 코드를 올바르게 수정해 정상화시키는 일련의 해결 과정입니다.

### (2) 디버깅의 대표 수단
1. **print() 함수 이용**: 의심스러운 로직 중간에 변수의 현재 값이나 실행 여부를 콘솔에 출력(`print()`)해 가며 로직의 흐름을 인간이 눈으로 수동 추적하는 간편한 방식입니다.
2. **에디터 디버거 도구 (IDLE Debugger / VS Code Debugger)**:
   * **브레이크포인트 (Breakpoints)**: 실행을 일시정지하고 싶은 특정 줄에 빨간 중단점을 설정합니다.
   * **스텝 실행 (Step Over / Into)**: 정지 상태에서 코드를 딱 한 줄씩 실행시키며 메모리 내부의 변수 변화를 실시간으로 모니터링하여 논리 오류를 잡아냅니다.

---

## 14.3 예외 처리 (Exception Handling)

### (1) 예외 처리의 정의
예외 처리란 프로그램이 실행되는 도중에 에러(예외)가 감지되었을 때, **프로그램 전체가 충격으로 즉시 비정상 종료되는 것을 예방하고, 사전에 마련한 예외 대응 코드로 우회 처리하여 프로그램을 끝까지 안전하게 구동시키는 설계 기법**입니다.

### (2) 예외 처리의 필요성
1. **서비스 가용성 확보**: 예외 상황 하나 때문에 전체 시스템이나 서버 전체가 죽어 다운되는 사태를 차단합니다.
2. **친절한 에러 가이드**: 알 수 없는 시스템 기계어 에러 대신 `"입력하신 파일명을 다시 확인해주세요!"`와 같은 유용한 힌트를 사용자에게 전달하여 정상 동작을 유도할 수 있습니다.

---

## 14.4 try~except~else~finally 통합 구조

파이썬은 예외 처리를 정교하게 다루기 위해 다음과 같은 완전한 예외 처리 제어 블록을 제공합니다.

```python
try:
    # 1. 예외가 발생할 가능성이 있는 민감한 코드
except 예외클래스1:
    # 2. 예외클래스1이 터졌을 때 구동되는 대체 로직
except 예외클래스2 as e:
    # 3. 예외클래스2 발생 시 구동 및 시스템 에러 메시지(e) 활용
else:
    # 4. try 블록 내에서 단 하나의 예외도 없이 무사히 성공했을 때만 가동
finally:
    # 5. 예외 발생 유무에 상관없이 100% 무조건 마지막에 강제 구동
```

### (1) 각 블록의 물리적 역할
* **try**: 파일 I/O, 네트워크 통신, DB 연산 등 예측 불가능한 인프라성 연산들이 포함되는 안전 가드 영역입니다.
* **except**: try 블록에서 예외가 터지면 즉각 실행을 멈추고 제어권이 except 블록으로 넘어와 복구 처리를 합니다.
  * 복수 개 선언 가능하여 종류별(ZeroDivision, Index 등) 개별 튜닝 가능.
  * `as e`로 별칭을 지으면 시스템이 뽑아낸 상세 문자열을 에러 로그로 남길 수 있습니다.
* **else**: 가독성을 높여주는 블록으로, try문이 아무 탈 없이 완벽히 성공했을 때 가동될 후속 코드를 적어둡니다. (try에 모두 적는 것보다 논리적 구분이 확실해짐)
* **finally**: 리소스 반납 목적이 강한 최하단 블록입니다. 예외가 나서 except로 빠졌든, 예외 없이 else로 끝났든 상관없이 **최종 종료 직전에 무조건 수행**되므로 오픈한 물리 파일이나 네트워크 커넥션 등을 확실하게 소멸(`.close()`)시킬 때 최적입니다.

---

## 14.5 상황별 3대 실행 흐름 시나리오

try 블록 내 코드 실행 시나리오에 따라 파이썬 인터프리터의 제어 포인터는 다음과 같이 이동합니다.

### 1) 시나리오 A: 예외 없이 완벽히 실행된 경우
```
try ➡️ [성공] ➡️ else ➡️ finally
```
* try 블록을 무사히 통과하고, except 블록은 무시된 뒤, else 블록이 가동되고, 마지막으로 finally 블록이 100% 구동되고 정상 탈출합니다.

### 2) 시나리오 B: 예외가 발생했고 매칭되는 except 블록이 있는 경우
```
try ➡️ [예외 시점 즉시 중단] ➡️ except ➡️ finally
```
* try 블록을 실행하던 중 예외가 나타난 그 즉시 아래 잔여 try 코드는 스킵되고, 에러 타입에 상응하는 except 블록으로 점프하여 예외를 복구한 후, else 블록은 무시되고, finally 블록을 실행한 뒤 프로그램은 안정을 유지하며 다음 정상 코드로 계속 흘러갑니다.

### 3) 시나리오 C: 예외가 발생했으나 매칭되는 except 블록이 없는 경우
```
try ➡️ [예외 시점 즉시 중단] ➡️ [except 매칭 실패] ➡️ finally ➡️ [프로세스 강제 다운]
```
* try 실행 중 예외가 터졌으나 이를 수습할 except 규격이 소스에 없다면, 일단 **finally 블록에 작성된 자원 해제 코드 등은 무조건 끝까지 실행해 준 뒤**, 프로그램은 예외 에러를 그대로 콘솔에 내뿜으며 비정상 강제 종료됩니다.

---

## 14.6 실전 예외 처리 구현 예제

### (1) 안전한 나눗셈 및 정수 변환 처리
* **요구사항**: 사용자로부터 두 개의 정수를 입력받아 나누는 프로그램을 만들되, 숫자가 아닌 문자를 입력했을 때의 예외(`ValueError`)와 0으로 나눴을 때의 예외(`ZeroDivisionError`)를 각각 안전하게 잡아 복구 처리하십시오.
```python
def safe_divide():
    try:
        num1 = int(input("분자(나눌 수)를 입력하세요: "))
        num2 = int(input("분모(나누는 수)를 입력하세요: "))
        
        result = num1 / num2
        
    except ValueError:
        print("에러: 반드시 정수만 입력해 주셔야 합니다.")
    except ZeroDivisionError:
        print("에러: 어떤 수도 0으로 나눌 수는 없습니다.")
    else:
        # 정상 성공 시에만 출력
        print(f"나눗셈 결과: {result:.2f}")
    finally:
        print("나눗셈 연산 시도를 완료했습니다.")

# 가동
safe_divide()
```

### (2) 파일 읽기 안전 장치와 자원 반납
* **요구사항**: 파일을 열고 텍스트를 읽는 과정에서 파일이 존재하지 않는 에러(`FileNotFoundError`)를 안전하게 수습하고, 에러 유무와 관계없이 열려 있는 파일 스트림을 닫는 finally 가드를 안전하게 구현하십시오.
```python
filename = "non_existent_file.txt"
file_stream = None

try:
    print(f"[{filename}] 파일 읽기를 시도합니다.")
    # 파일 열기 시도 (cp949 에러 방지 인코딩 명시)
    file_stream = open(filename, "r", encoding="utf-8")
    content = file_stream.read()
    print("파일 내용:")
    print(content)
    
except FileNotFoundError as e:
    print(f"예외 수습 완료: 지정한 파일({filename})이 경로에 없습니다.")
    print(f"상세 에러 로그: {e}")
    
finally:
    # file_stream이 정상적으로 open 되었을 때만 close 수행하여 AttributeError 예방
    if file_stream is not None:
        file_stream.close()
        print("파일 스트림 자원을 안전하게 시스템에 반환했습니다.")
    else:
        print("파일이 열린 적이 없으므로 자원 해제를 생략합니다.")
```
```text
[non_existent_file.txt] 파일 읽기를 시도합니다.
예외 수습 완료: 지정한 파일(non_existent_file.txt)이 경로에 없습니다.
상세 에러 로그: [Errno 2] No such file or directory: 'non_existent_file.txt'
파일이 열린 적이 없으므로 자원 해제를 생략합니다.
```

---

# Related Concepts
* [File Input/Output](chapter-13.md) — FileNotFoundError 및 open 자원 close 안전 장치 연계.

# Citations
* Chapter 14_예외처리.pdf [Python 14장](../../../raw/notes/Python/Chapter 14_예외처리.pdf)
