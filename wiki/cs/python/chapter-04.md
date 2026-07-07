---
type: Study Note
title: "Chapter 04: Python Operators (파이썬 연산자)"
description: "사칙연산을 포함한 산술 연산자들의 동작 특성과 나눗셈(/) 연산 시 실수형 고정 반환 규칙을 학습합니다. 또한 문자열 곱셈의 특이 조건, 복합 할당 연산자 및 비교/논리 연산자의 단락 평가(Short-circuit evaluation) 메커니즘을 에러 미발생 예제를 통해 수학적으로 증명합니다. 마지막으로 삼항 연산 조건식(x if condition else y)과 인터프리터 연산 가속을 돕는 operator 모듈의 필요성 및 매핑 함수들을 정리합니다."
tags: [operators, division-rules, short-circuit, conditional-expression, operator-module, performance-optimization]
timestamp: 2026-06-18
status: active
---

# 4. 연산자 (Python Operators)

## 4.1 산술 연산자 (Arithmetic Operators)

수학적 수치 데이터를 연산하기 위해 사칙연산 기호 및 몫/나머지 특수 연산자를 사용합니다.

### (1) 나눗셈 연산자 (`/`)의 자료형 규칙
파이썬에서 나누기 연산자 `/`를 실행하면, 피연산자들이 정수이거나 나눈 몫이 정수값으로 나누어떨어지는 경우(예: `10 / 5`)에도 **언제나 예외 없이 실수형(`float`) 데이터를 반환**합니다.
* 만약 정수형 결과값만을 취하고자 한다면 직접 `int()` 형 변환을 취해 하위 소수점을 버려야 합니다.

### (2) 0으로 나누기 예외 제한
컴퓨터 대수 연산 상 분모가 0이 되는 연산은 불가능합니다. 파이썬에서 어떤 숫자를 $0$ 혹은 $0.0$으로 나누려 하거나 몫/나머지 분모에 0을 투입하면 `ZeroDivisionError` 시스템 예외가 발생하여 프로그램이 즉시 강제 종료됩니다. 
* *참고*: 분자(피연산자 1)가 0이고 분모가 0이 아닌 경우는 정상적으로 $0$을 반환합니다.

### (3) 나머지와 몫, 거듭제곱 연산
* **나머지 연산자 (`%`)**: 나눈 뒤의 잔여값(나머지)만 계산. 데이터의 홀수/짝수 판별($\pmod 2 == 1$ 또는 $0$) 및 특정 정수의 배수 판별에 널리 활용됩니다.
* **몫 연산자 (`//`)**: 나눈 몫의 정수값만 소수점 이하를 버리고 취하는 연산.
* **거듭제곱 연산자 (`**`)**: 왼쪽 피연산자에 대해 오른쪽 피연산자만큼 누적 곱 연산을 수행.

### (4) 문자열 연산 규칙
* **문자열 덧셈 (`+`)**: 두 개의 문자열을 하나로 인접 병합하여 새로운 연결 문자열을 생성. (숫자와 문자열 간의 직접 덧셈은 타입 불일치 에러 발생)
* **문자열 곱셈 (`*`)**: 문자열을 특정 횟수만큼 반복 복사.
  * **상수 곱 규칙**:
    * 문자열 $\times$ **양의 정수 ($n$)**: 문자열을 $n$회 반복 복사.
    * 문자열 $\times$ **$0$ 또는 음의 정수**: 에러를 내지 않고 **빈 문자열 `''`**을 최종 반환함.

---

## 4.2 논리 연산자와 단락 평가 (Short-Circuit Evaluation)

파이썬의 논리 연산자 `and`, `or`, `not`은 참/거짓 판별 시 불필요한 연산을 건너뛰는 **단락 평가(Short-circuit evaluation)** 메커니즘을 작동시킵니다.

### (1) and 연산 단락 평가
`and` 연산자는 좌우의 모든 피연산자가 참(`True`)이어야만 최종 참을 반환합니다. 따라서 인터프리터가 첫 번째 피연산자를 평가했을 때 그 결과가 **`False`**이면, 뒤쪽 피연산자의 값이 무엇이든 전체 식의 결과는 무조건 거짓으로 고정됩니다. 이 경우 파이썬은 **뒤쪽 피연산자의 연산(평가) 과정을 생략하고 즉각 실행을 종료**합니다.
* **단락 평가 에러 우회 증명 예제**:
  ```python
  num = 10
  # abc는 아직 선언 및 초기화하지 않은 미지 변수이므로 단독 호출 시 NameError가 나야 함
  result = (num < 5) and abc
  print(result) # 에러 없이 정상 실행되어 "False" 출력
  ```
  * *이유*: `num < 5`가 `False`이므로 `and` 우측의 `abc` 변수를 전혀 들여다보지(실행하지) 않고 즉각 연산을 끝냈기 때문에 참조 에러가 방지됩니다.

### (2) or 연산 단락 평가
`or` 연산자는 피연산자 중 단 하나만 참이어야만 최종 참을 반환합니다. 따라서 첫 번째 피연산자의 연산 결과가 **`True`**이면, 뒤쪽 피연산자의 값과 무관하게 전체 조건식 결과는 항상 `True`가 되므로 **우측 피연산자의 연산 과정을 완전히 스킵**합니다.
* **단락 평가 에러 우회 증명 예제**:
  ```python
  num = 10
  result = (num > 5) or abc
  print(result) # 에러 없이 정상 실행되어 "True" 출력
  ```
  * *이유*: `num > 5`가 `True`이므로 우측의 미선언 변수 `abc`에 접근하지 않고 단락 평가하여 참을 반환합니다.

---

## 4.3 조건식 (삼항 연산자 - Conditional Expressions)

피연산자가 세 개로 구성되어 특정 조건식의 만족 여부에 따라 최종 결과값을 다르게 치환 선택하는 연산자로, 코드를 간결하게 묶어주는 유용한 도구입니다.

* **조건식 표준 문법**:
  $$\text{R-value} = X \quad \text{if} \quad \text{Condition} \quad \text{else} \quad Y$$
* **동작 순서**:
  1. 가운데 위치한 `Condition` 조건식을 가장 먼저 연산 평가합니다.
  2. 평가 결과가 참(`True`)이면 조건식 좌측의 $X$ 값을 최종 선택하여 대입합니다.
  3. 평가 결과가 거짓(`False`)이면 `else` 우측의 $Y$ 값을 최종 선택하여 대입합니다.
* *사용 예시*:
  ```python
  result = '합격' if myScore >= 90 else '불합격'
  ```

---

## 4.4 `operator` 모듈을 통한 연산 최적화

파이썬은 수학 연산자 기호를 내장 함수 형태로 대체 제공하는 표준 라이브러리인 `operator` 모듈을 제공합니다.

### (1) 주요 매핑 함수 정리
* **산술 연산**:
  * `+` $\rightarrow$ `operator.add(a, b)`
  * `-` $\rightarrow$ `operator.sub(a, b)`
  * `*` $\rightarrow$ `operator.mul(a, b)`
  * `/` $\rightarrow$ `operator.truediv(a, b)`
  * `%` $\rightarrow$ `operator.mod(a, b)`
  * `//` $\rightarrow$ `operator.floordiv(a, b)`
  * `**` $\rightarrow$ `operator.pow(a, b)`
* **비교 연산**:
  * `==` $\rightarrow$ `operator.eq(a, b)`
  * `!=` $\rightarrow$ `operator.ne(a, b)`
  * `<` $\rightarrow$ `operator.lt(a, b)`
  * `<=` $\rightarrow$ `operator.le(a, b)`
  * `>` $\rightarrow$ `operator.gt(a, b)`
  * `>=` $\rightarrow$ `operator.ge(a, b)`
* **논리 연산**:
  * `and` $\rightarrow$ `operator.and_(a, b)`
  * `or` $\rightarrow$ `operator.or_(a, b)`
  * `not` $\rightarrow$ `operator.not_(a)`

### (2) `operator` 모듈의 사용 목적 (연산 속도 가속화)
일반 연산자 기호(예: `a + b`)를 사용하여 소스 코드를 실행하면, 파이썬 인터프리터 내부(CPython)는 해당 기호를 파싱하여 매핑되는 내부 연산 함수로 다시 변환하고 해석하여 실행하는 오버헤드 단계를 거칩니다.

반면 모듈 함수인 `operator.add(a, b)`를 명시적으로 직접 사용하면, **기호를 함수로 번역 매핑하는 연산 파싱 처리 경로가 완전히 생략**되어 PVM(가상 머신) 런타임 성능이 개선됩니다. 따라서 대규모 수치 해석 프로그램이나 대용량 데이터 반복 루프 처리 시 `operator` 함수를 사용하는 것이 연산 처리 속도 극대화에 필수적입니다.

---

# Citations
* Chapter 04_연산자.pdf [Python 4장](../../../raw/notes/Python/Chapter 04_연산자.pdf)
