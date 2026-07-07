---
type: Study Note
title: "Chapter 09: Python Function Basics (파이썬 함수 기초)"
description: "파이썬 함수의 개념(내장 함수 vs 사용자 정의 함수)과 코드 재사용성, 모듈화, 유지보수 측면에서의 필요성을 분석합니다. 함수 정의를 위한 def 키워드의 구조적 요소와 파이썬의 작명 표준 규칙, 실행 유예를 위한 pass 키워드 활용법을 다루며, 다중 호출 시의 실행 제어 흐름과 실전 구현 과제(다국어 인사말, 계산기, 영수증 출력 프로그램)를 상세히 해설합니다."
tags: [functions, user-defined-functions, code-reuse, naming-rules, pass-keyword, execution-flow, practical-examples]
timestamp: 2026-06-18
status: active
---

# 9. 함수 기초 (Python Function Basics)

## 9.1 함수의 개념과 분류

### (1) 함수의 정의
프로그래밍에서 함수(Function)란 **특정 작업을 수행하기 위해 설계된 독립적인 코드의 집합(묶음)**입니다. 수학에서의 함수가 어떤 입력값 $x$를 대입했을 때 정해진 수식에 의해 하나의 결과값 $y$를 매칭해 주는 구조 $y = f(x)$인 것처럼, 프로그래밍의 함수 또한 매개 데이터(Parameter)를 인가받아 정의된 알고리즘을 수행한 뒤 처리 결과(Return)를 반환하는 방식으로 작동합니다.

### (2) 함수의 두 가지 대분류
1. **내장 함수 (Built-in Functions)**: 파이썬 인터프리터가 기본적으로 탑재하고 있어 별도의 임포트(`import`) 선언 없이 즉각 호출 가능한 함수들입니다.
   * 예: `print()`, `len()`, `input()`, `sum()`, `str()`, `int()` 등
2. **사용자 정의 함수 (User-defined Functions)**: 파이썬이 기본으로 제공하지 않는 특정 비즈니스 로직이나 반복 업무를 처리하기 위해, 개발자가 직접 문법에 맞추어 설계하고 이름을 부여하여 사용하는 함수입니다.

---

## 9.2 함수의 필요성 (왜 사용할까?)

### (1) 코드 재사용성 (Reusability)
프로그램 내에서 동일한 로직(예: 선수의 점프 거리를 입력받고 순위를 매겨 포맷팅 출력하는 코드)이 여러 곳에서 반복하여 사용될 때, 해당 코드를 매번 중복 기재하지 않고 하나의 함수로 정립해 둠으로써 필요할 때마다 한 줄의 호출 명령문으로 간단히 재사용할 수 있습니다.

### (2) 구조적 모듈화 (Modularity)
함수를 작성하면 기능별로 코드가 깔끔하게 나뉘므로 가독성이 높아지고, 관련이 깊은 함수들을 모아 독립된 모듈(Module) 파일(`.py`)로 보관할 수 있습니다. 모듈화된 함수들은 다른 프로젝트나 소스코드 파일로의 이식이 매우 쉬워집니다.

### (3) 유지보수(수정)의 편의성
함수를 쓰지 않고 작성한 코드에서 특정 계산 규칙(예: 부가세율 10% ➡️ 12% 변경)을 수정하려면 소스 전체에 흩어진 중복 코드들을 일일이 찾아 고쳐야 합니다. 이 과정에서 한두 곳을 누락하면 런타임에 큰 버그를 초래하게 됩니다. 반면 함수를 사용하여 설계했다면, **함수 정의부의 단 한 줄만 수정**해도 해당 함수를 호출하는 소스 전체에 일괄 반영됩니다.

---

## 9.3 함수 정의(Definition) 규칙과 작명소

### (1) 함수 정의의 기본 문법
```python
def 함수명():
    실행문(코드 블록)
```
* **def 키워드**: 'define'의 약어로, 새로운 사용자 정의 함수를 선언하겠다는 것을 인터프리터에 선언하는 지시어입니다.
* **함수명**: 함수의 고유한 식별 이름입니다.
* **소괄호 (`( )`)**: 매개변수(Parameter)를 지정하는 영역으로, 현재 장에서는 매개변수가 없는 기초 형태를 주로 다룹니다.
* **콜론 (`:`)**: 함수의 선언적 헤더가 끝나고 내부 알고리즘이 기술될 코드 블록이 시작됨을 나타냅니다.
* **들여쓰기 실행문**: 함수가 호출되었을 때 실행될 소스코드를 기재하며, 모두 일치된 칸 수의 들여쓰기 공백을 적용해야 합니다.

### (2) 함수명 작명의 표준 가이드라인
파이썬에서 함수명을 정할 때 문법적 위반 에러를 방지하고 가독성을 높이기 위해 다음 4가지 규칙을 엄격히 준수해야 합니다.

1. **내장 함수명 중복 금지**: `print`, `len`, `sum` 등 이미 파이썬이 선점한 내장 함수 이름을 사용자 함수의 이름으로 사용하면 기존 내장 함수의 작동이 마비(Shadowing)됩니다. 따라서 `my_print()`, `custom_len()` 등 중복을 비한 이름을 설계해야 합니다.
2. **소문자 시작 권장**: 파이썬 스타일 가이드(PEP 8)에 따르면 함수명은 주로 **소문자**로 시작하며, 필요 시 언더바(`_`)로 단어를 연결하는 스네이크 케이스(snake_case)가 권장됩니다. 첫 글자를 대문자로 쓰면 클래스(Class)명과 혼동되어 가독성을 해칩니다.
3. **숫자로 시작 금지**: 함수명의 첫 글자에 숫자를 사용할 수 없습니다. (`2myCalculator()` ❌, `myCalculator2()` ⭕)
4. **특수 문자 사용 금지**: 언더바(`_`)를 제외한 어떠한 특수 문자도 사용할 수 없습니다. 대시(`-`) 등도 금지됩니다. (`my-Calculator()` ❌, `my_calculator()` ⭕)

### (3) pass 키워드를 통한 실행 유예
함수 구조(인터페이스)를 먼저 선언해 두고 세부 알고리즘 구현을 나중으로 미뤄두고 싶을 때, 들여쓰기 블록을 비워두면 `IndentationError` 에러가 납니다. 이때 **`pass`** 문을 기재하여 컴파일 에러를 방지하고 정상적으로 가동될 수 있도록 뼈대만 구축합니다.
```python
def calculate_distance():
    pass  # 추후 물리 거리 계산 수식 적용 예정
```

---

## 9.4 함수의 호출과 실행 제어 흐름

### (1) 함수 호출 (Function Call)
정의된 함수를 실제로 가동시키는 것을 "호출한다"고 말합니다. 함수의 이름 뒤에 소괄호를 붙여 기재합니다.
```python
def greet():
    print("안녕하세요!")

greet() # 함수 호출 ➡️ 콘솔에 "안녕하세요!" 출력
```

### (2) 함수 간 제어 전파 (다중 함수 호출)
함수 내부의 실행문 블록 안에서 또 다른 제2, 제3의 함수를 연쇄적으로 호출할 수 있습니다. 이때 파이썬 인터프리터는 호출된 함수로 제어권(실행 포인터)을 임시 이전시켰다가, 해당 함수가 끝나면 정확히 호출했던 다음 행으로 복귀하여 잔여 코드를 실행합니다.

```python
def fun1():
    print("[fun1] 실행 시작")

def fun2():
    print("[fun2] 실행 시작")

def fun3():
    print("[fun3] 진입")
    fun1()  # fun1 호출
    fun2()  # fun2 호출
    print("[fun3] 모든 연계 호출 완료 후 종료")

# 실행 가동
fun3()
```
* **콘솔 출력 순서**:
  1. `[fun3] 진입`
  2. `[fun1] 실행 시작`
  3. `[fun2] 실행 시작`
  4. `[fun3] 모든 연계 호출 완료 후 종료`

---

## 9.5 실전 문제 해결 (Practical Exercises)

### (1) 다국어 인사말 프로그램
* **요구사항**: 사용자에게 번호 선택을 유도하여 1번(한국), 2번(USA), 3번(Japan)에 해당하는 나라별 인사말 함수를 실행시킵니다. 단, 선택 범위를 벗어난 입력을 가할 시 올바른 번호를 고를 때까지 반복해서 다시 입력을 받도록 `while` 루프와 결합하여 설계하십시오.
```python
def greet_kr():
    print("안녕하세요.")

def greet_us():
    print("Hello.")

def greet_jp():
    print("こんにちは (곤니치와).")

while True:
    print("\n[다국어 인사 프로그램]")
    print("1: 한국, 2: USA, 3: Japan, 4: 프로그램 종료")
    choice = input("국가를 선택하세요 (1~4): ")
    
    if choice == '1':
        greet_kr()
    elif choice == '2':
        greet_us()
    elif choice == '3':
        greet_jp()
    elif choice == '4':
        print("인사 프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다! 1에서 4 사이의 숫자를 입력해 주세요.")
```

### (2) 함수형 계산기 프로그램
* **요구사항**: 숫자 2개를 입력받고, 사용자가 원하는 사칙 연산 기호(+, -, *, /)에 매칭되는 독립적인 사칙연산 함수를 각각 정의 및 가동하여 결과를 도출하는 프로그램을 만드시오.
```python
def add(a, b):
    print(f"결과: {a} + {b} = {a + b}")

def subtract(a, b):
    print(f"결과: {a} - {b} = {a - b}")

def multiply(a, b):
    print(f"결과: {a} * {b} = {a * b}")

def divide(a, b):
    if b == 0:
        print("에러: 0으로 나눌 수 없습니다.")
    else:
        print(f"결과: {a} / {b} = {a / b:.2f}")

# 메인 흐름 제어
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))
operator = input("연산자를 선택하세요 (+, -, *, /): ")

if operator == '+':
    add(num1, num2)
elif operator == '-':
    subtract(num1, num2)
elif operator == '*':
    multiply(num1, num2)
elif operator == '/':
    divide(num1, num2)
else:
    print("잘못된 연산자입니다.")
```

### (3) 홀수/짝수 판별기: `printEvenOdd()` (연습문제 1)
* **요구사항**: 사용자로부터 양의 정수 하나를 입력받아 그 수가 홀수인지 짝수인지 여부를 연산 출력하는 `printEvenOdd()` 함수를 작성하시오.
```python
def printEvenOdd():
    user_num = int(input("정수를 입력하세요: "))
    
    if user_num <= 0:
        print("양의 정수를 입력해 주세요.")
        return
        
    if user_num % 2 == 0:
        print("입력한 정수는 짝수 입니다.")
    else:
        print("입력한 정수는 홀수 입니다.")

# 함수 테스트 호출
printEvenOdd()
```

### (4) 상품 가격표 기반 영수증 출력기: `print_receipt()` (연습문제 2)
* **요구사항**:
  - 슈퍼마켓 상품 단가: 새우깡 1200원, 비비빅 400원, 초코파이 500원, 맛동산 1500원.
  - 사용자에게 각 품목별 구매 개수를 입력받아 각 금액 합계와 최종 총 청구액 영수증을 규격에 맞춰 출력하는 `print_receipt()` 사용자 함수를 정의하십시오.
```python
def print_receipt():
    # 상품 단가 정보 딕셔너리 정의
    prices = {
        "새우깡": 1200,
        "비비빅": 400,
        "초코파이": 500,
        "맛동산": 1500
    }
    
    # 사용자 수량 입력 수신
    counts = {}
    for product in prices.keys():
        counts[product] = int(input(f"{product} 구매 개수 : "))
        
    print("\n" + "=" * 35)
    total_bill = 0
    
    # 품목별 정산 출력
    for product, unit_price in prices.items():
        qty = counts[product]
        item_total = unit_price * qty
        total_bill += item_total
        print(f"{product} 구매 금액 : {item_total:>5d} 원")
        
    print("=" * 35)
    print(f"총 구매 금액 : {total_bill:>9d} 원")
    print("=" * 35)

# 함수 테스트 호출
print_receipt()
```

---

# Related Concepts
* [Tuples and Dictionaries](chapter-08.md) — 상품 단가 및 회원 정보 관리를 위한 컨테이너 활용.
* [Advanced Functions](chapter-10.md) — 매개변수(Parameter)와 반환값(Return Value), 그리고 변수 스코프(Scope) 학습.

# Citations
* Chapter 09_함수 기초 다지기_260329.pdf [Python 9장](../../../raw/notes/Python/Chapter 09_함수 기초 다지기_260329.pdf)
