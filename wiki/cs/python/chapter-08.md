---
type: Study Note
title: "Chapter 08: Python Tuples and Dictionaries (파이썬 튜플과 딕셔너리)"
description: "수정이 불가능한 불변성 컨테이너인 튜플(Tuple)의 물리적 선언 규칙 및 리스트와의 상호 변환 관계를 분석합니다. 또한 키(Key)-값(Value)의 쌍으로 고속 데이터 조회를 지원하는 해시 기반의 딕셔너리(Dictionary) 구조와 필수 제약조건(Key의 Hashable 조건), 그리고 조회/삽입/수정/삭제 등 핵심 연산 메서드를 다룹니다. 실전 응용 과제(수학 채점, 회원 가입, 재고 관리 시스템)의 코드 구현까지 수록합니다."
tags: [data-structures, tuple, dictionary, immutability, hash-table, dictionary-methods, key-value, practical-examples]
timestamp: 2026-06-18
status: active
---

# 8. 튜플과 딕셔너리 (Python Tuples & Dictionaries)

## 8.1 튜플 (Tuple)

### (1) 튜플의 개념과 리스트와의 차이점
튜플은 리스트와 유사하게 여러 데이터를 순서대로 묶어서 관리하는 선형 컨테이너 자료형입니다. 
* **불변성 (Immutability)**: 튜플의 가장 핵심적인 특징은 **한 번 선언되면 내부 아이템을 추가, 수정, 삭제하는 모든 가변(Mutable) 연산이 절대 불가능**하다는 점입니다.
* **사용 목적**: 프로그램 작동 중 데이터의 무결성과 안정성이 절대적으로 보장되어야 하는 고정성 데이터를 관리할 때 사용합니다. (예: 회사 급여 명세서 항목명, 주민등록번호 구조식, 2차원 평면의 고정 좌표 $(x, y)$, 설정 상수 값 등)
* **메모리 최적화**: 튜플은 크기가 고정되어 있으므로 리스트에 비해 메모리 점유율이 낮고 연산 속도가 소폭 빠릅니다.

### (2) 튜플의 선언 규칙
* **소괄호(`( )`)**를 사용하여 선언하며, 각 아이템은 **쉼표(`,`)**로 구분합니다. 소괄호를 아예 생략하고 쉼표만으로 나열해도 파이썬은 자동으로 튜플로 인지합니다.
  ```python
  fruits = ("apple", "banana", "cherry")
  numbers = 10, 20, 30  # 소괄호 생략 가능 -> (10, 20, 30)
  ```
> [!IMPORTANT]
> **단일 요소 튜플의 특수 규칙**:
> 튜플에 단 하나의 데이터만 담으려고 할 경우, 반드시 값의 오른쪽에 쉼표(`,`)를 붙여 선언해야 합니다. 쉼표가 누락되면 파이썬은 튜플이 아닌 **일반 수식 괄호**로 취급하여 단일 자료형으로 해석합니다.
> ```python
> not_tuple = (10)   # 정수형(int) 10으로 판정
> real_tuple = (10,) # 튜플(tuple)로 정상 판정
> ```

### (3) 튜플의 조회 및 활용 연산
튜플은 불변성을 가지므로 `append()`, `insert()`, `pop()`, `remove()` 등의 수정형 메서드는 존재하지 않고, 오직 안전한 **조회 및 불변 병합** 연산만을 제공합니다.

#### 1) 인덱스 참조와 슬라이싱
리스트와 동일하게 0-based 인덱스를 사용하여 개별 아이템을 읽어올 수 있으며, 슬라이싱 구문도 똑같이 지원합니다.
```python
letters = ('a', 'b', 'c', 'd')
print(letters[1])   # 'b'
print(letters[1:3]) # ('b', 'c')
```

#### 2) index() 및 멤버 검사(in)
* `index(값)`: 특정 값의 위치 인덱스를 반환하며, 값이 존재하지 않을 시 `ValueError`를 반환합니다.
* `in` / `not in`: 특정 데이터의 존재 유무를 부울(`True`/`False`) 값으로 판단합니다.
```python
names = ("Kim", "Lee", "Park")
if "Lee" in names:
    print(f"Lee의 위치는 {names.index('Lee')}번 인덱스입니다.")
```

#### 3) 튜플 결합 (`+`)
두 튜플을 더하여 기존 튜플을 수정하지 않고, 두 요소가 합쳐진 **새로운 제3의 튜플 객체를 생성**하여 반환합니다.
```python
tuple_a = (1, 2)
tuple_b = (3, 4)
tuple_c = tuple_a + tuple_b
print(tuple_c) # (1, 2, 3, 4)
```

### (4) 리스트와 튜플 간의 상호 형변환
* **튜플 ➡️ 리스트**: `list()` 생성자 함수를 사용합니다. 튜플로 관리하던 불변 데이터를 임시로 수정하거나 요소를 추가해야 할 때 리스트로 바꾼 뒤 작업합니다.
* **리스트 ➡️ 튜플**: `tuple()` 생성자 함수를 사용합니다. 동적 추가 작업을 마친 리스트 데이터를 불변 상태로 고정시켜 안정성을 높이고자 할 때 변환합니다.
```python
my_tuple = (10, 20, 30)
my_list = list(my_tuple)  # 리스트로 변환
my_list.append(40)        # 값 수정 허용
final_tuple = tuple(my_list) # 다시 튜플로 묶어서 불변 고정
```

### (5) 튜플의 정렬: sorted()
튜플 자체는 수정이 불가능하므로 리스트의 `sort()` 메서드처럼 내부 데이터를 직접 정렬할 수 없습니다. 대신 파이썬 내장 함수인 **`sorted(tuple)`**을 사용해야 합니다.
> [!WARNING]
> 내장 함수 `sorted()`는 입력받은 이터러블을 정렬하여 **언제나 "새로운 리스트(List)"** 형태로 반환합니다. 따라서 정렬된 결과를 튜플로 유지하고 싶다면 명시적으로 튜플 형변환을 한 단계 더 거쳐야 합니다.
> ```python
> data = (5, 2, 9, 1)
> sorted_data = sorted(data)
> print(sorted_data)  # [1, 2, 5, 9] (리스트 반환!)
> print(tuple(sorted_data)) # (1, 2, 5, 9) (튜플로 재변환)
> ```

---

## 8.2 딕셔너리 (Dictionary)

### (1) 딕셔너리의 개념과 내부 구조
딕셔너리는 **키(Key)와 값(Value)의 쌍(Pair)**을 요소로 관리하는 컨테이너 자료형입니다.
* **해시 테이블(Hash Table) 기반**: 리스트나 튜플이 0부터 시작하는 정수형 물리 인덱스에 의존하여 값을 찾는다면, 딕셔너리는 개발자가 임의로 지정한 **고유의 키(Key) 값**을 내부 해싱 함수를 거쳐 메모리 주소로 직접 계산하여 고속 참조합니다.
* **비교 비유**: 학교 사물함에서 번호표(인덱스)로 칸을 찾는 것은 리스트이며, 학생 이름표(Key)가 붙은 칸을 보고 물건(Value)을 찾는 것이 딕셔너리입니다.

### (2) 딕셔너리 선언 및 제약조건
```python
ages = {"홍길동": 20, "임꺽정": 35, "장길산": 28}
```
* **선언 구조**: 중괄호(`{ }`)를 사용하고, 각 요소는 `Key: Value` 형태로 표현하며 쉼표로 분리합니다.
* **키(Key)의 제약 조건**:
  1. **고유성 (Unique)**: 키는 중복될 수 없습니다. 만약 동일한 키를 중복하여 선언하면 나중에 기재된 값이 이전 키-값을 덮어씁니다.
  2. **불변성 (Hashable)**: 키 값은 파이썬 내부 해시 알고리즘이 적용될 수 있도록 **수정이 불가능한 불변 객체(Immutable)**여야 합니다. 따라서 문자열, 정수, 실수, 튜플은 키로 사용할 수 있지만, **리스트나 딕셔너리처럼 바뀔 수 있는 가변형 자료형은 키로 절대 사용할 수 없습니다.**
* **값(Value)의 제약 조건**:
  * 값은 중복을 자유롭게 허용하며, 자료형의 제한도 전혀 없습니다. 리스트, 튜플, 또 다른 딕셔너리도 값으로 지정 가능합니다.

---

## 8.3 딕셔너리 조회, 삽입, 수정, 삭제 연산

### (1) 데이터 조회 기법 2가지
딕셔너리 조회의 핵심은 키를 인덱스처럼 대괄호에 대입하는 것입니다.

#### 1) 대괄호(`[Key]`) 방식
가장 직관적인 방식이지만 존재하지 않는 키를 전달 시 예외를 발생시킵니다.
```python
user_info = {"name": "Gildong", "age": 24}
print(user_info["name"]) # "Gildong"
```
> [!IMPORTANT]
> 존재하지 않는 키인 `user_info["address"]` 등을 대괄호로 직접 조회하려 하면 파이썬은 즉시 **`KeyError`**를 던지고 실행을 정지합니다.

#### 2) get(Key, Default) 메서드 (안전한 조회)
대괄호 방식의 에러 발생을 예방하는 안정적인 조회 통로입니다.
* **동작**: 조회하려는 키가 존재하지 않으면 에러를 내는 대신 **`None`**을 조용히 반환합니다.
* **기본값 지정**: 두 번째 인자로 기본값을 설정하면, 키가 없을 때 `None` 대신 그 기본값을 반환합니다.
```python
print(user_info.get("address"))          # None (에러 없음)
print(user_info.get("address", "Seoul")) # "Seoul" (기본값 출력)
```

### (2) 아이템 삽입과 수정
`딕셔너리[Key] = Value` 구문을 사용하며, 전달하는 키의 존재 유무에 따라 동작이 갈립니다.
* **키가 없는 경우**: 새로운 키와 값을 가진 요소 쌍이 신규 삽입됩니다.
* **키가 있는 경우**: 기존의 해당 키의 값이 전달한 새 값으로 갱신(수정)됩니다.
```python
info = {"name": "Gildong"}
info["age"] = 20        # 삽입 (새로운 키)
info["name"] = "Cheolsu" # 수정 (기존 키)
print(info) # {"name": "Cheolsu", "age": 20}
```
> [!NOTE]
> 딕셔너리는 삽입 위치를 명시하는 인덱스가 없으므로 리스트용 메서드인 `append()`, `insert()` 등은 문법적으로 사용 불가능합니다.

### (3) 아이템 삭제와 갯수 판별
* **del 키워드**: `del 딕셔너리[Key]` 형태로 요소를 삭제합니다. 존재하지 않는 키를 삭제하려 하면 `KeyError`가 발생합니다.
* **clear() 메서드**: 딕셔너리 내 모든 요소를 한꺼번에 삭제하여 완전히 비웁니다.
* **len() 함수**: 딕셔너리가 보관 중인 키-값 쌍의 개수를 반환합니다.
```python
data = {"a": 1, "b": 2}
del data["a"]
print(data) # {"b": 2}
print(len(data)) # 1
```

### (4) 전체 키/값 집합 추출
딕셔너리를 루프 연산과 연계하기 위해 키와 값을 집합 형태로 리스트형 뷰 객체로 추출해내는 세 가지 메서드입니다.
* **keys()**: 딕셔너리의 모든 키 목록을 `dict_keys` 객체로 반환합니다.
* **values()**: 딕셔너리의 모든 값 목록을 `dict_values` 객체로 반환합니다.
* **items()**: 딕셔너리의 모든 요소를 `(Key, Value)` 튜플 쌍 형태로 묶은 `dict_items` 객체로 반환합니다.

```python
grades = {"math": 95, "eng": 80, "sci": 90}

# 키를 이용한 전체 순회 조회
for subject in grades.keys():
    print(f"과목: {subject}, 점수: {grades[subject]}")

# 키와 값을 동시에 unpacking 하여 조회
for subject, score in grades.items():
    print(f"{subject} ➡️ {score}점")
```

---

## 8.4 실전 문제 해결 (Practical Exercises)

### (1) 수학 채점 프로그램
* **요구사항**: 사용자에게 수학 문제 3개를 내고 딕셔너리에 담긴 정답 리스트와 대조하여 점수와 최종 정/오답 개수를 집계해 출력하십시오.
```python
# 문제와 정답을 딕셔너리로 관리
exam_papers = {
    "3 + 5 = ? ": 8,
    "12 * 4 = ? ": 48,
    "25 - 9 = ? ": 16
}

correct_cnt = 0
wrong_cnt = 0

for question, answer in exam_papers.items():
    user_ans = int(input(question))
    if user_ans == answer:
        print("정답입니다!")
        correct_cnt += 1
    else:
        print(f"틀렸습니다. (정답: {answer})")
        wrong_cnt += 1

total_score = int((correct_cnt / len(exam_papers)) * 100)
print("---------------------------")
print(f"맞은 개수: {correct_cnt}개")
print(f"틀린 개수: {wrong_cnt}개")
print(f"최종 점수: {total_score}점")
```

### (2) 회원등록 및 가입 프로그램
* **요구사항**: 사용자가 아이디와 비밀번호를 연속으로 입력하여 가입을 진행하며, 회원 ID가 중복 입력되는 경우 가입을 차단합니다. 입력을 끝내면 등록된 전체 회원 목록을 보여줍니다.
```python
members = {}

while True:
    user_id = input("가입할 아이디를 입력하세요 (종료는 'exit'): ")
    if user_id == 'exit':
        break
        
    if user_id in members:
        print("이미 존재하는 아이디입니다. 다른 아이디를 사용하세요.")
        continue
        
    user_pw = input("비밀번호를 입력하세요: ")
    members[user_id] = user_pw
    print(f"[{user_id}] 회원님의 가입이 성공적으로 완료되었습니다.")

print("\n=== 가입된 전체 회원 목록 ===")
for u_id, u_pw in members.items():
    print(f"ID: {u_id} (비밀번호: {'*' * len(u_pw)})")
```

### (3) 과목 학점 업데이트 (실습과제)
* **요구사항**: `classes` 딕셔너리에서 현재 `'3학점'`으로 설정된 모든 과목을 찾아 일괄 `'5학점'`으로 변경하는 프로그램을 구현하십시오.
```python
classes = {
    'python': '5학점',
    'C/C++': '5학점',
    'HTML5': '3학점',
    'Java': '5학점',
    'Javascript': '3학점'
}

# 학점 수정 진행
for course in list(classes.keys()):  # 루프 도중 딕셔너리 크기 변동 에러 방지를 위해 list 변환
    if classes[course] == '3학점':
        classes[course] = '5학점'

print("=== 변경된 학점 목록 ===")
for course, credit in classes.items():
    print(f"{course} : {credit}")
```

### (4) 야채 냉장고 재고 관리 프로그램 (실습과제)
* **요구사항**:
  - 초기 비어 있는 야채 재고 딕셔너리를 설계합니다.
  - 다음 시나리오 순서대로 입고 및 소비 처리를 실행하십시오.
    1. 당근 10개, 건대추 100개, 대파 20개, 애호박 3개, 부추 1개 입고.
    2. 당근 1개, 건대추 10개, 대파 1개, 애호박 1개, 부추 1개 소비.
    3. 소비 완료 후 최종 야채별 재고 현황을 출력합니다.
```python
refrigerator = {}

# 입고 및 소비 일괄 처리 도우미 함수 정의
def stock_in(item, count):
    refrigerator[item] = refrigerator.get(item, 0) + count

def stock_out(item, count):
    if item in refrigerator:
        refrigerator[item] -= count
        # 재고가 0 미만으로 내려가지 않도록 차단
        if refrigerator[item] < 0:
            refrigerator[item] = 0
    else:
        print(f"경고: {item}은 냉장고에 존재하지 않아 소비할 수 없습니다.")

# 1. 입고 처리
stock_in('당근', 10)
stock_in('건대추', 100)
stock_in('대파', 20)
stock_in('애호박', 3)
stock_in('부추', 1)

# 2. 소비 처리
stock_out('당근', 1)
stock_out('건대추', 10)
stock_out('대파', 1)
stock_out('애호박', 1)
stock_out('부추', 1)

# 3. 최종 재고 현황 출력
print("=== 냉장고 야채 재고 목록 ===")
for vegetable, stock in refrigerator.items():
    print(f"- {vegetable}: {stock}개")
```

---

# Related Concepts
* [Lists](chapter-07.md) — 튜플과의 상호 형변환 연계 및 리스트 구조 분석.

# Citations
* Chapter 08_튜플과 딕셔너리_업데이트.pdf [Python 8장](../../../raw/notes/Python/Chapter 08_튜플과 딕셔너리_업데이트.pdf)
