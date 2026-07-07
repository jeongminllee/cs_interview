---
type: Study Note
title: "Chapter 15: Python Lambda and List Comprehensions (파이썬 람다와 리스트 축약)"
description: "이름이 없는 익명 함수인 람다(Lambda)의 정의와 메모리 상의 작동 이점, 선언 즉시 인자를 주입하는 인라인 람다의 기법을 학습합니다. 지연 평가(Lazy Evaluation) 메커니즘을 내장한 filter()와 map() 함수의 동작 원리를 분석하고, 파이썬 고유의 직관적 리스트 생성 기법인 리스트 축약(List Comprehension)의 조건문 필터링 구조, 여러 값을 일괄 수신하는 파싱 기법, 그리고 문자열 연결 메서드인 join()의 조건 제약까지 심층 분석합니다."
tags: [lambda-expression, anonymous-function, filter-function, map-function, lazy-evaluation, list-comprehension, string-join, practical-examples]
timestamp: 2026-06-18
status: active
---

# 15. 람다 함수와 리스트 축약 (Python Lambda & List Comprehensions)

## 15.1 람다 함수 (Lambda Function)

### (1) 람다 함수의 정의
람다 함수는 **단 한 줄로 간단하게 정의하여 사용하는 이름이 없는 익명 함수(Anonymous Function)** 또는 람다 표현식(Lambda Expression)입니다. 
* **특징**: `def` 키워드로 정식 선언하여 함수 테이블에 이름을 등록하지 않고, 일회성 혹은 짧은 휘발성 연산이 필요할 때 호출문 내에 인라인(Inline) 형태로 즉시 선언해 사용합니다.

### (2) 람다 함수의 기본 구조
```python
lambda 매개변수1, 매개변수2, ... : 표현식
```
* **lambda 키워드**: 람다 표현식의 시작을 지시합니다.
* **매개변수**: 일반 함수의 매개변수와 동일하며, 쉼표로 구분하여 여러 개를 둘 수 있습니다.
* **표현식**: 매개변수를 이용해 연산할 수식입니다. `return` 키워드를 쓰지 않아도 **표현식의 연산 결과가 자동으로 반환**됩니다.

```python
# 일반 함수 구현
def add_func(x, y):
    return x + y

# 람다 함수로 일대일 매핑 구현
add_lambda = lambda x, y: x + y

print(add_func(3, 5))    # 8
print(add_lambda(3, 5))  # 8
```

### (3) 인라인 람다 함수 (Inline Lambda)
변수에 람다 함수를 담아두지도 않고, 선언문 뒤에 직접 소괄호로 인자들을 넘겨서 즉시 실행(IIFE 패턴)시키는 방식입니다.
```python
result = (lambda x, y: x * y)(10, 20)
print(result) # 200
```

### (4) 람다 함수의 명확한 장단점
* **장점**:
  1. **코드 간결화**: 함수 정의와 반환 코드가 한 라인으로 축약되어 불필요한 라인 낭비가 줄어듭니다.
  2. **메모리 절약**: 호출이 끝난 람다 함수는 메모리 네임스페이스에 영구 등록되지 않고 즉시 정리되므로 미세한 오버헤드를 줄입니다.
* **단점**:
  * **가독성 저하**: 람다 내부에는 다중 조건문(`if ~ elif ~ else`)이나 복잡한 반복문을 적을 수 없고, 로직이 조금만 길어져도 코드를 읽고 분석하기가 매우 까다로워집니다.

---

## 15.2 필터(filter)와 맵(map) 함수의 지연 평가(Lazy Evaluation)

`filter()`와 `map()`은 함수형 프로그래밍 패러다임을 지원하는 파이썬의 강력한 내장 함수입니다.

### (1) 필터 함수 (Filter Function)
이터러블 객체의 각 요소를 특정 판별 조건 함수에 하나씩 대입해 본 뒤, 결과가 **참(`True`)인 요소들만 선별(Filtering)**해내는 함수입니다.
* **기본 문법**: `filter(조건검사함수, 이터러블자료형)`
* **조건검사함수**: 인자를 받아 `True` 또는 `False`를 리턴해 주는 함수(또는 람다식)입니다.

#### [예제] 19세 이상의 성년만 선별하기 (def vs lambda)
```python
ages = [34, 39, 20, 18, 13, 54]

# 1. 정식 함수 선언 방식
def is_adult(n):
    return n >= 19
adults_1 = list(filter(is_adult, ages))

# 2. 람다 결합 방식 (변수 선언 및 중복 코드 배제)
adults_2 = list(filter(lambda x: x >= 19, ages))

print(adults_2) # [34, 39, 20, 54]
```

### (2) 맵 함수 (Map Function)
이터러블 객체의 모든 요소에 변환 함수를 **일대일로 매핑 적용(Mapping)**하여, 변환된 결과 전체를 다시 리스트 등으로 반환해주는 함수입니다.
* **기본 문법**: `map(변환함수, 이터러블자료형)`

#### [예제] 숫자 리스트의 제곱근 계산
```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares) # [1, 4, 9, 16]
```

### (3) 핵심 작동 원리: 지연 평가 (Lazy Evaluation)
> [!IMPORTANT]
> `filter()`와 `map()` 함수를 단독으로 구동하면 리스트나 튜플이 아닌 **`filter` 객체**, **`map` 객체**가 반환됩니다.
> * **메모리 효율 극대화**: 이 객체들은 수만 개의 데이터를 한꺼번에 연산하여 메모리에 전부 적재해 두는 방식이 아닙니다. 단지 **데이터 이터러블 주소와 적용할 함수 포인터만 기억하고 있는 대기 상태**입니다.
> * **트리거 시점**: 나중에 `list()`, `tuple()` 생성자에 인자로 전달되거나, `for`문에 의해 순회가 개시되는 **그 시점(구체적 확인이 필요한 시점)에 비로소 하나씩 계산을 처리**합니다. 이를 **지연 평가(Lazy Evaluation)**라고 부르며, 메모리 절약과 속도 개선에 탁월합니다.
> ```python
> raw_filter = filter(lambda x: x > 0, [-1, 2, -3])
> print(raw_filter) # <filter object at 0x0000021A...> (주소만 출력됨)
> print(list(raw_filter)) # [2] (이 시점에 비로소 실제 연산이 가동됨)
> ```

---

## 15.3 리스트 축약 (List Comprehension)

리스트 축약은 파이썬이 자랑하는 고유의 문법으로, 기존 리스트나 범위 이터러블을 기반으로 조건 필터링이나 연산을 간결하게 한 줄의 대괄호식으로 명시하여 새 리스트를 제조하는 기법입니다.

### (1) 기본 문법
```python
[ 표현식 for 변수 in 이터러블 ]
```
* **동작**: 이터러블에서 요소를 하나씩 꺼내 변수에 할당하고, 이를 표현식에 통과시켜 도출된 값들을 모아 최종 리스트를 빌드합니다.
```python
# 1부터 5까지의 제곱 리스트
squares = [x**2 for x in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]
```

### (2) 조건 필터가 가미된 문법 (Comprehension with if)
```python
[ 표현식 for 변수 in 이터러블 if 조건식 ]
```
* **동작**: 이터러블에서 꺼낸 요소 중 **조건식이 참(`True`)인 요소들만 선별하여 표현식에 통과**시킵니다. `filter()` + `map()` 연산의 완벽한 축약 대안입니다.
```python
# 1부터 10 중 짝수들의 제곱만 추출
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares) # [4, 16, 36, 64, 100]
```

### (3) 다중 조건 필터 (if의 연속 사용)
`if` 조항을 꼬리에 꼬리를 물듯 연달아 배치하면, 논리 곱(`and`)으로 엮인 복합 조건 필터링을 깔끔하게 수행합니다.
```python
# 1부터 30까지의 숫자 중 2와 3의 공배수(즉 6의 배수) 구하기
common_multiples = [n for n in range(1, 31) if n % 2 == 0 if n % 3 == 0]
print(common_multiples) # [6, 12, 18, 24, 30]
```

### (4) 실무형 응용: 다중 정수 입력 파싱 기법
사용자로부터 여러 개의 정수를 한 줄에 공백 구분으로 입력받았을 때, 리스트 축약과 `split()`을 엮어 즉각 정수형 리스트로 바인딩하는 대표 기법입니다.
```python
# 사용자 입력: 10 20 30 40 50
numbers = [int(x) for x in input("정수들을 공백으로 구분해 입력하세요: ").split()]
print("정수 리스트:", numbers) # [10, 20, 30, 40, 50]
```

---

## 15.4 조인 함수 (join)

`join()`은 리스트나 튜플로 쪼개져 있는 다수의 문자열들을 하나의 연결된 단일 문자열로 봉합할 때 사용하는 **문자열 객체 전용 내장 메서드**입니다.

### (1) 기본 문법
```python
'구분자'.join(문자열_리스트)
```
* **구분자**: 결합할 단어와 단어 사이에 삽입할 틈새 문자입니다. (빈 문자열 `''`, 공백 `' '`, 하이픈 `'-'` 등)

```python
chars = ['H', 'E', 'L', 'L', 'O']
word = ''.join(chars)  # 빈 공백 없이 딱 붙임
print(word)  # "HELLO"

words = ["Python", "is", "fun"]
sentence = ' '.join(words)  # 단어 사이에 공백 하나 삽입
print(sentence)  # "Python is fun"
```
> [!CAUTION]
> **TypeError 발생 주의**:
> `join()` 메서드는 **오직 문자열(str) 원소들로만 채워진 이터러블 객체만 결합**할 수 있습니다. 만약 리스트에 단 하나라도 정수나 실수 데이터(예: `[1, 2, "three"]`)가 포함되어 있다면 `TypeError: sequence item 0: expected str instance, int found` 예외를 내고 즉시 중단되므로 사전 변환이 강제됩니다.

---

## 15.5 실전 퀴즈 풀이 및 코드 구현

### [퀴즈 1] 음수 필터링 처리 비교 (filter+lambda vs 리스트 축약)
* **요구사항**: 주어진 정수 리스트 `[-30, 45, -5, -90, 20, 53, 77, -36]`에서 음수만 걸러내어 새로운 리스트에 저장하는 코드를 1) `filter()`와 `lambda` 조합, 2) 리스트 축약 조합 두 방식으로 작성하여 비교 분석하시오.
```python
n_list = [-30, 45, -5, -90, 20, 53, 77, -36]

# 방식 1: filter() + lambda
minus_filter = list(filter(lambda x: x < 0, n_list))

# 방식 2: 리스트 축약 표현식 (가독성이 가장 뛰어남)
minus_comp = [x for x in n_list if x < 0]

print("filter 결과:", minus_filter)
print("축약식 결과:", minus_comp)
```
```text
filter 결과: [-30, -5, -90, -36]
축약식 결과: [-30, -5, -90, -36]
```

### [퀴즈 2] 쉼표로 구분된 영단어의 대문자 변환 및 결합 (join 연계)
* **요구사항**: 사용자로부터 영어 소문자 단어 여러 개를 쉼표(`,`) 구분으로 입력받습니다. 이 단어들을 리스트로 쪼갠 뒤 각각 대문자로 변환하고, 다시 하이픈(`-`) 기호로 연결해 하나의 문자열로 출력하는 프로그램을 리스트 축약과 `join`을 활용해 구현하십시오.
```python
# 입력 예시: apple,banana,cherry
raw_input = input("소문자 단어들을 쉼표로 구분하여 입력하세요: ")

# 1. split으로 쪼개고 대문자로 변환하는 리스트 축약 수행
upper_words = [word.strip().upper() for word in raw_input.split(',')]

# 2. 하이픈 구분자로 최종 병합
final_result = '-'.join(upper_words)

print("최종 변환 결과:", final_result)
# 출력 예시: APPLE-BANANA-CHERRY
```

---

# Related Concepts
* [Lists](chapter-07.md) — 컨테이너 리스트의 기본 연산 및 인덱싱.
* [Advanced Functions](chapter-10.md) — split()의 구조 분해 및 파싱 기법.

# Citations
* Chapter 15_람다함수와리스트축약_업데이트_0609.pdf [Python 15장](/raw/notes/Python/Chapter 15_람다함수와리스트축약_업데이트_0609.pdf)
