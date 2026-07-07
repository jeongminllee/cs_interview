---
type: Study Note
title: "Chapter 10: Python Advanced Functions (파이썬 함수 활용)"
description: "지역변수(Local)와 전역변수(Global)의 스코프 영역 차이, global 키워드의 선언 및 초기화 분리 규칙, 매개변수(Parameter)와 인수(Argument)의 관계를 심층 학습합니다. 가변 매개변수(*args), 키워드 인수, 기본값 매개변수의 작동 규칙을 분석하고, 튜플을 반환하는 다중 리턴 구조, 중첩 함수(Nested) 및 재귀 함수(Recursive)의 제어 방식, split() 메서드를 활용한 문자열 구조 분해 할당(Unpacking)까지 정리합니다."
tags: [variable-scope, local-global, global-keyword, parameters-arguments, variable-length-arguments, return-values, nested-functions, recursive-functions, string-split]
timestamp: 2026-06-18
status: active
---

# 10. 함수 활용 (Python Advanced Functions)

## 10.1 지역변수와 전역변수의 스코프(Scope)

변수는 선언된 물리적 위치에 따라 수명 주기와 접근 권한 범위(Scope)가 나뉩니다.

### (1) 지역변수 (Local Variable)
* **정의**: 함수 내부에서 선언된 변수입니다.
* **유효 범위**: 오직 해당 함수가 실행되는 동안 함수 내 영역에서만 존재하고 작동하며, 함수의 실행이 완전히 끝나(Return 또는 블록 종료)는 순간 메모리에서 즉시 소멸(Garbage Collected)됩니다.
* **접근 차단**: 함수 외부나 다른 함수에서는 특정 함수의 지역변수를 들여다보거나 수정할 수 없습니다.

### (2) 전역변수 (Global Variable)
* **정의**: 함수 외부(모듈 최상위 수준)에서 선언된 변수입니다.
* **유효 범위**: 프로그램이 실행되어 시작될 때 생성되어 전체 프로그램 가동이 완전히 끝날 때까지 수명을 유지합니다.
* **접근**: 함수 내부와 외부를 가리지 않고 프로그램 내 어디서나 읽어올(Read) 수 있습니다.

### (3) 변수 이름 충돌과 우선순위 (Shadowing)
전역변수와 동일한 이름의 변수를 함수 내부에서 새로 선언하면 어떻게 될까요?
```python
num = 100  # 전역변수

def fun1():
    num = 20  # 지역변수 선언
    print("함수 내부:", num)

fun1()
print("함수 외부:", num)
```
* **결과**: 함수 내부에서는 `20`, 외부에서는 `100`이 출력됩니다.
* **원리**: 두 변수는 이름만 똑같을 뿐 메모리 번지가 완전히 다른 별개의 변수입니다. 함수 내부에서는 지역변수가 더 높은 우선순위를 가지므로 전역변수를 가리게 되는데, 이를 **변수 섀도잉(Variable Shadowing)**이라고 부릅니다.

### (4) global 키워드를 통한 전역 변수 값 갱신 규칙
함수 내부에서 전역변수의 값을 수정(재할당)하려면 단순 대입 연산이 아니라 **`global`** 키워드로 해당 변수가 전역 영역의 변수임을 미리 튜닝 선언해주어야 합니다.
```python
num = 10

def update_global():
    global num  # 1. 전역변수 num을 사용하겠다고 지시
    num = 30    # 2. 전역변수의 값 실제 수정
```
> [!IMPORTANT]
> **global 선언 및 초기화의 물리적 분리 법칙**:
> `global num = 30`과 같이 전역변수 선언과 값 할당을 한 행에 동시에 결합해 쓰면 파이썬은 **구문 에러(SyntaxError)**를 냅니다. 반드시 `global num`으로 먼저 선언한 후, 다음 줄에 `num = 30`과 같이 초기화(할당)하는 독립 행으로 분리 기술해야 합니다.

---

## 10.2 매개변수(Parameter)와 인수(Argument)의 제어 규칙

### (1) 기본 개념
* **인수 (Argument)**: 함수를 사용하는 쪽(호출부)에서 함수에 실제 대입하여 넘겨주는 **실제 데이터 값**입니다.
* **매개변수 (Parameter)**: 전달받은 인수를 함수가 내부적으로 활용하기 위해 정의부 헤더에 선언해 놓은 **로컬용 임시 변수**입니다.

### (2) 가변 매개변수 (`*` 접두사)
함수 호출 시 몇 개의 인수가 전달될지 미리 예측하기 어렵거나 유동적으로 변하는 구조라면 가변 매개변수를 사용합니다.
* **문법**: 매개변수 이름 앞에 아스테리스크(`*`)를 붙여 선언합니다. (`*args` 등)
* **취합 형태**: 전달된 다수의 인수들은 함수 내부에 들어올 때 하나의 **튜플(Tuple)** 객체로 포장되어 바인딩됩니다.
```python
# 과목 성적 합산 함수 (과목 수가 동적으로 바뀌어도 대응 가능)
def print_average(*scores):
    total = sum(scores)
    avg = total / len(scores) if scores else 0
    print(f"총 {len(scores)}과목 평균: {avg:.2f}점")

print_average(90, 80, 70)      # 3과목 전달
print_average(100, 95, 90, 85) # 4과목 전달
```

### (3) 키워드 인수 (Keyword Arguments)
함수를 호출할 때 인수의 순서를 헷갈려 잘못 인가하는 논리 에러를 막기 위해, 매개변수명과 대입할 값을 한 쌍으로 묶어 직접 지정 호출하는 기능입니다. 이 경우 정의된 순서와 어긋나게 인수를 기재해도 이름에 정확히 매핑됩니다.
```python
def introduce_member(name, age):
    print(f"이름: {name}, 나이: {age}")

# 매개변수 이름을 키워드로 지정하여 순서를 섞어 호출
introduce_member(age=28, name="Kim")
```

### (4) 매개변수 기본값 설정 (Default Parameters)
호출부에서 인수를 생략하고 보내지 않았을 때 사용할 기본 대체 값을 정의부에 선언할 수 있습니다.
* **주의**: 기본값 매개변수들은 반드시 **일반 매개변수들보다 오른쪽에 마지막에 배치**되어야 합니다. 그렇지 않으면 어떤 인수가 어떤 자리에 대입되어야 할지 해석할 수 없으므로 `SyntaxError: non-default argument follows default argument` 에러를 냅니다.
```python
def calculate_pay(hours, rate=10000): # 시급 기본값 10,000원 설정
    pay = hours * rate
    print(f"급여: {pay:,}원")

calculate_pay(8)         # rate 생략 ➡️ 10,000원 적용 ➡️ 80,000원
calculate_pay(8, 15000)  # rate 재지정 ➡️ 15,000원 적용 ➡️ 120,000원
```

---

## 10.3 데이터 반환 (Return Value)

### (1) return 키워드의 양면적 역할
1. **결과 데이터 송신**: 함수 내부 계산을 거쳐 나온 최종 결과물을 함수를 호출한 원래의 라인으로 되돌려 보냅니다.
2. **함수 강제 종료**: 함수 실행 흐름 도중 `return`을 만나는 즉시, 그 하위에 잔여 실행 코드가 남아 있을지라도 실행을 칼같이 멈추고 제어권을 호출부로 강제 복귀시킵니다.

### (2) 다중 결과값 반환 규칙
파이썬은 단 한 번의 return 문으로 2개 이상의 복수 데이터를 한꺼번에 호출부로 반환할 수 있습니다.
* **물리적 반환 형식**: 2개 이상의 값을 쉼표로 연결해 반환하면, 파이썬은 이들을 자동으로 묶어서 **단 하나의 튜플(Tuple) 객체**로 만들어 반환합니다.
```python
def calculate_stat(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg  # 튜플로 묶여 반환됨

res = calculate_stat([10, 20, 30])
print(type(res)) # <class 'tuple'>
print(res)       # (60, 20.0)

# 호출부에서 Unpacking(구조 분해)하여 받아내기
tot_val, avg_val = calculate_stat([10, 20, 30])
```

---

## 10.4 중첩 함수와 재귀 함수

### (1) 중첩 함수 (Nested Function)
함수 내부에 또 다른 헬퍼 함수를 정의하여 사용하는 구조입니다.
* **캡슐화 기능**: 안쪽에 선언된 중첩 함수는 자신을 감싸고 있는 바깥쪽 부모 함수의 내부 스코프 내에서만 호출 가능하며, 부모 함수 밖(외부 영역)에서는 보이지 않고 직접 접근도 불가능합니다.
```python
def outer_calculator(a, b):
    # 중첩 함수 정의
    def inner_divide(x, y):
        return x / y if y != 0 else 0
    
    val = inner_divide(a, b)
    print("계산 완료:", val)

# inner_divide(10, 2) ➡️ 외부에서 직접 호출 시 NameError 발생
outer_calculator(10, 2)
```

### (2) 재귀 함수 (Recursive Function)
함수가 정의부 내부에서 **자기 자신을 다시 호출**하도록 구현된 알고리즘 구조입니다.
* **필수 조건 - 종료 조건 (Base Case)**: 재귀 호출은 통제하지 않으면 무한 호출 궤도에 돌입하여 메모리 스택 한계를 초과하는 `RecursionError: maximum recursion depth exceeded` 스택 오버플로우 오류를 냅니다. 따라서 특정 깊이에 도달했을 때 자신 호출을 중단하는 명확한 조건 분기가 반드시 전제되어야 합니다.

```python
# 1씩 감소하며 카운트다운하고 멈추는 재귀 함수
def countdown(n):
    if n <= 0:  # 1. 종료 조건 (Base Case)
        print("발사!")
    else:
        print(n)
        countdown(n - 1)  # 2. 자기 자신 재귀 호출 (n이 감소하여 종료 조건에 근접)

countdown(3)
```
```text
3
2
1
발사!
```

---

## 10.5 부록: split() 메서드 작동 원리와 Unpacking

`split()`은 문자열을 특정 구분자 기준으로 분할하여 리스트로 쪼개주는 핵심 내장 메서드입니다.

### (1) 작동 특징
* **기본 구분자**: 구분자 인자를 생략하고 `split()`으로 호출하면, 공백(스페이스, 탭, 개행 문자 `\n`)을 기준으로 자릅니다. 이때 연속된 여러 개의 공백이 나타나도 하나의 공백으로 인식하여 빈 문자열 요소 없이 말끔하게 자릅니다.
* **구분자 지정**: `split(',')`과 같이 지정하면 해당 쉼표 문자를 기준으로 자릅니다.
* **최대 분할 횟수**: `split(구분자, maxsplit)` 형태로 지정 시 데이터가 너무 길 때 앞단만 추출하고 뒷단은 통째로 유지시키는 것이 가능합니다.
  ```python
  log_text = "2026-06-18:Server Error Occurred In Database Module"
  date, msg = log_text.split(":", 1) # 단 한 번만 쪼갬
  print(date) # "2026-06-18"
  print(msg)  # "Server Error Occurred In Database Module"
  ```

### (2) 구조 분해 할당 (Unpacking) 연계
`split()` 연산이 반환하는 결과 리스트의 크기와 동일한 개수의 변수를 좌변에 나열하면 데이터가 순서대로 착착 할당됩니다.
```python
formula = "5 + 3"
num1, operator, num2 = formula.split()
print(f"피연산자1: {num1}, 연산자: {operator}, 피연산자2: {num2}")
```

---

## 10.6 실전 문제 해결 (Practical Exercises)

### (1) 길이 단위 환산 프로그램
* **요구사항**: mm 단위를 입력받아 이를 cm, m, inch, ft 단위로 한꺼번에 환산해 출력하는 변환 함수를 정의하십시오. (환산 공식: $1\text{ mm} = 0.1\text{ cm} = 0.001\text{ m} = 0.03937\text{ inch} = 0.00328\text{ ft}$)
```python
def convert_length(mm_val):
    cm = mm_val * 0.1
    m = mm_val * 0.001
    inch = mm_val * 0.03937
    ft = mm_val * 0.00328
    return cm, m, inch, ft  # 다중 값 반환

# 가동
input_mm = float(input("mm 단위 길이를 입력하세요: "))
cm_res, m_res, inch_res, ft_res = convert_length(input_mm)

print("\n=== 단위 환산 결과 ===")
print(f"센티미터: {cm_res:.4f} cm")
print(f"미터: {m_res:.4f} m")
print(f"인치: {inch_res:.4f} inch")
print(f"피트: {ft_res:.4f} ft")
```

### (2) 오늘의 할인율 적용 상품 가격표 출력
* **요구사항**: 오늘의 할인율을 전역변수로 입력받고, 정가 목록이 담긴 상품 딕셔너리를 입력받아 할인 후 가격을 표로 출력하는 프로그램을 함수화하여 구성하십시오.
```python
# 전역 변수 선언
discount_rate = 0.0

def print_discounted_prices(items):
    global discount_rate  # 전역변수 참조 읽기 (수정하지는 않으므로 필수 지정은 아니나 명시화)
    print(f"\n[오늘의 할인율: {discount_rate * 100:.0f}% 상품 가격표]")
    print("-" * 35)
    
    for item_name, original_price in items.items():
        discounted_price = int(original_price * (1.0 - discount_rate))
        print(f"{item_name:<7s} ➡️ 정가: {original_price:>6d}원 | 할인가: {discounted_price:>6d}원")

# 상품 목록 정보
product_catalog = {
    "청바지": 50000,
    "티셔츠": 25000,
    "원피스": 80000,
    "자켓": 120000
}

# 오늘의 할인율 설정 입력
input_rate = float(input("오늘의 할인율을 입력하세요 (예: 20%는 20 입력): "))
discount_rate = input_rate / 100.0

print_discounted_prices(product_catalog)
```

### (3) 옷가게 거스름돈 계산 (연습문제 1)
* **요구사항**: 옷가게 상품 가격표(스커트: 18000원, 바지: 25000원, 자켓: 85000원)를 기초 데이터로 매핑합니다. 구매 상품명과 지불 현금을 입력받아 거스름돈을 연산 및 출력하는 함수를 설계하십시오.
```python
def calculate_change():
    shop_catalog = {
        "스커트": 18000,
        "바지": 25000,
        "자켓": 85000
    }
    
    item = input("구매 상품을 입력하세요 (스커트/바지/자켓): ")
    if item not in shop_catalog:
        print("매장에 존재하지 않는 상품입니다.")
        return
        
    price = shop_catalog[item]
    cash = int(input("지불 금액을 입력하세요: "))
    
    if cash < price:
        print(f"금액이 부족합니다! 상품 가격은 {price}원입니다.")
    else:
        change = cash - price
        print(f"거스름 돈 : {change}원")

# 실행 테스트
calculate_change()
```

### (4) 영-한 사전 매핑 번역기 (연습문제 2)
* **요구사항**: 사전에 등록된 영단어(apple ➡️ 사과, piano ➡️ 피아노, cat ➡️ 고양이, book ➡️ 책)가 있습니다. 영어 단어를 매개변수로 전달받아 매핑되는 한국어 뜻을 찾아 반환(Return)해주는 번역 헬퍼 함수를 구현하십시오.
```python
def translate_to_korean(eng_word):
    dictionary = {
        "apple": "사과",
        "piano": "피아노",
        "cat": "고양이",
        "book": "책"
    }
    # get 메서드로 안전하게 가져오며, 단어가 없을 경우의 문구도 리턴 설정
    return dictionary.get(eng_word.lower(), "사전에 등록되지 않은 단어입니다.")

# 테스트 실행
search_word = input("영어 단어를 입력하세요: ")
translated_result = translate_to_korean(search_word)
print(f"{search_word} : {translated_result}")
```

---

# Related Concepts
* [Function Basics](chapter-09.md) — 사용자 정의 함수 선언의 기초 틀 및 작명 규칙.

# Citations
* Chapter 10_함수 활용하기_260329.pdf [Python 10장](../../../raw/notes/Python/Chapter 10_함수 활용하기_260329.pdf)
