---
type: Study Note
title: "Chapter 07: Python Lists (파이썬 리스트)"
description: "파이썬의 대표적인 컨테이너 자료형인 리스트(List)의 구조와 메모리 저장 방식(참조 주소 보관), 다양한 메서드(append, insert, extend, pop, remove, sort, reverse)의 작동 원리를 심층 학습합니다. 또한 인덱싱과 슬라이싱, len() 및 index() 함수의 예외 조건, 반복문과의 결합(for, while, enumerate)을 분석하고 실전 예제(출석부, 혈액 보관, 합격 판정 프로그램)를 구성합니다."
tags: [data-structures, list, container-type, list-methods, indexing, slicing, practical-examples]
timestamp: 2026-06-18
status: active
---

# 7. 리스트 (Python Lists)

## 7.1 컨테이너 자료형의 정의와 종류

### (1) 컨테이너 자료형 (Container Data Type)
단일 변수에 데이터를 하나씩 개별적으로 저장하기보다는, 연관된 여러 데이터를 하나의 그룹으로 묶어서 저장하고 관리하는 것이 개발 편의성과 메모리 관리 측면에서 훨씬 효율적입니다. 이와 같이 **여러 개의 데이터 요소를 하나로 묶어 담는 데이터 집합체**를 컨테이너 자료형 또는 컬렉션(Collection)이라고 부릅니다.

### (2) 파이썬의 대표적 컨테이너 자료형
파이썬은 구조적 특징에 따라 다음과 같은 컨테이너 자료형을 내장하여 제공합니다.
* **리스트 (List)**: 순서가 있고, 중복을 허용하며, 수정 가능한 데이터 집합.
* **튜플 (Tuple)**: 순서가 있고, 중복을 허용하지만, 선언 후 수정이 불가능한 읽기 전용 데이터 집합.
* **딕셔너리 (Dictionary)**: 순서가 없으며(Python 3.7+부터는 삽입 순서 유지), 키(Key)와 값(Value)의 쌍으로 이루어진 데이터 집합. 키는 중복을 허용하지 않음.
* **세트 (Set)**: 순서가 없고, 중복을 절대 허용하지 않는 데이터 집합.

---

## 7.2 리스트의 개념과 선언 방식

### (1) 리스트(List)의 물리적 특징
리스트는 **동일하거나 서로 다른 자료형의 데이터를 순차적으로 정렬하여 나열한 집합**입니다.
* **메모리 할당 방식**: 파이썬의 리스트는 각 요소들이 저장된 실제 값의 **메모리 참조 주소(Reference)**들을 연속된 공간에 순서대로 배열하여 관리합니다.
* **참조 변수 fruits의 의미**: `fruits = ["apple", "banana"]`와 같이 리스트를 선언하고 변수에 할당할 때, `fruits` 변수 자체에는 리스트 내부 데이터 전체가 들어가는 것이 아니라, **리스트 객체 자체의 시작 메모리 주소(첫 번째 주소를 참조할 수 있는 포인터 정보)**가 보관됩니다.

```
fruits 변수 ────────> [ 리스트 객체 헤더 ]
                         │
                         ├─ index 0: 'apple' 객체의 주소 ───> "apple" (str 객체)
                         └─ index 1: 'banana' 객체의 주소 ──> "banana" (str 객체)
```

### (2) 리스트 선언 방법
* **대괄호(`[ ]`)**를 사용하며, 각 데이터 요소(아이템)는 **쉼표(`,`)**로 구분하여 선언합니다.
* **빈 리스트 선언**: 추후 동적으로 아이템을 추가할 예정일 때 선언합니다.
  * 방법 1: `empty_list = []` (가장 널리 쓰임)
  * 방법 2: `empty_list = list()` (내장 생성자 함수 사용)
* **이종 자료형 혼합 가능**: 파이썬 리스트는 자료형의 제한이 없으므로 정수, 실수, 문자열, 심지어 또 다른 리스트까지 한 리스트 안에 섞어 담을 수 있습니다.
  ```python
  mixed_list = [10, 3.14, "Python", [1, 2, 3]]
  ```

---

## 7.3 리스트 조회와 인덱싱(Indexing)

### (1) 아이템과 인덱스(Index)
리스트에 순서대로 입력된 개별 데이터를 **아이템(Item)** 또는 **요소(Element)**라고 부르며, 각 아이템의 물리적 위치를 나타내는 정수 일련번호를 **인덱스(Index)**라고 합니다.
* **0-based Indexing**: 인덱스는 무조건 **0**부터 시작하며 오른쪽으로 갈수록 1씩 증가합니다.
* **Negative Indexing**: 역방향 조회를 위해 음수 인덱스도 지원합니다. 맨 마지막 아이템은 `-1`, 그 앞은 `-2`가 부여됩니다.
* **동적 갱신**: 중간에 아이템이 삽입되거나 삭제되면 파이썬 엔진이 내부 인덱스 번호를 실시간으로 자동 갱신합니다.

### (2) 인덱스 참조와 IndexError
리스트 변수명 오른쪽에 대괄호와 인덱스 정수를 표기하여 해당 위치의 아이템을 꺼냅니다.
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # "apple"
print(fruits[-1])  # "cherry" (역방향 끝 요소)
```
> [!IMPORTANT]
> 리스트가 가지고 있는 인덱스의 범위를 벗어난 숫자(예: 길이가 3인 리스트에 `fruits[5]` 또는 `fruits[-4]` 요청)를 참조하면 파이썬은 즉시 **`IndexError: list index out of range`** 런타임 예외를 발생시키고 프로그램 가동을 중단합니다.

### (3) len() 함수를 통한 리스트 길이 판별
`len()` 함수는 리스트 내부에 담겨 있는 전체 아이템의 개수(길이)를 정수로 반환합니다.
```python
print(len(fruits)) # 3
```

### (4) index() 함수를 통한 값의 위치 역추적
`index(값)` 메서드는 리스트 안에서 특정 값을 가진 아이템을 검색하여 그 아이템이 위치한 최초의 인덱스를 정수로 반환합니다.
* **중복 값 존재 시**: 리스트 내에 동일한 값이 여러 개 있을 경우, **가장 앞쪽(낮은 인덱스)**에 위치한 단 하나의 인덱스만 알려주고 탐색을 끝냅니다.
* **문자열 지원**: 일반 문자열에서도 특정 문자나 단어의 위치를 인덱스로 추적할 수 있습니다. (`"python".index("th")` -> `2`)
```python
colors = ["red", "blue", "green", "blue"]
print(colors.index("blue")) # 1 (중복 요소 중 최초 인덱스)
```
> [!WARNING]
> 만약 리스트 내부에 존재하지 않는 값을 인덱스로 검색하려 시도할 경우, 프로그램은 **`ValueError: '값' is not in list`** 에러를 발생시킵니다. 따라서 실무에서는 사전에 `in` 연산자로 존재 여부를 검증하고 탐색해야 안전합니다.
> ```python
> if "yellow" in colors:
>     idx = colors.index("yellow")
> ```

### (5) 리스트 전체 순회(Traversal) 방법론
리스트의 모든 요소를 처음부터 끝까지 순서대로 방문하여 조회할 때 사용할 수 있는 세 가지 구조식입니다.

#### 1) for문을 이용한 요소 직접 순회
가장 일반적이고 가독성이 높은 방식으로, 이터러블 영역에 리스트 변수를 직접 넘깁니다.
```python
student_names = ["Park", "Kim", "Lee"]
for name in student_names:
    print(name)
```

#### 2) enumerate() 함수를 통한 인덱스와 값 동시 추출
순회 시 현재 아이템이 몇 번째 인덱스인지 번호 정보도 함께 필요할 때 사용합니다. `enumerate()`는 매 루프마다 `(인덱스, 값)` 형태의 튜플을 공급합니다.
```python
for idx, name in enumerate(student_names):
    print(f"{idx}번 학생: {name}")
```

#### 3) while문을 이용한 인덱스 루프 제어
인덱스 제어 변수(`i`)를 선언하고 `len()` 함수의 상한선 미만까지 수동 증가시키며 순회합니다.
```python
i = 0
while i < len(student_names):
    print(student_names[i])
    i += 1
```

---

## 7.4 아이템 삽입과 연결

### (1) 리스트 꼬리에 추가: append()
`append(item)` 메서드는 전달받은 데이터를 리스트의 **맨 마지막 자리에 단일 요소로 추가**합니다. 이로 인해 리스트의 길이는 즉시 1 증가합니다.
```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers) # [1, 2, 3, 4]
```

### (2) 원하는 위치에 삽입: insert()
`insert(index, item)` 메서드는 리스트 내 **원하는 인덱스 위치를 지정하여 데이터를 삽입**합니다.
* **동작 매커니즘**: 지정한 인덱스 자리에 신규 데이터가 강제 삽입되며, 기존에 그 자리와 그 오른쪽에 있던 모든 아이템들은 인덱스가 일제히 1씩 오른쪽으로 밀려납니다.
```python
numbers = [1, 2, 3]
numbers.insert(1, 99) # 인덱스 1 자리에 99 삽입
print(numbers) # [1, 99, 2, 3]
```

### (3) 리스트 연결 및 확장: extend() 와 + 연산자
두 개의 리스트를 합쳐 하나의 더 큰 리스트로 만들 때 두 가지 방식을 씁니다.

#### 1) extend() 메서드 (자체 수정)
`list_A.extend(list_B)` 형식으로 호출하며, `list_A` 리스트의 꼬리에 `list_B`에 들어있는 모든 요소들을 낱개로 쪼개어 연달아 추가합니다. 이 연산은 `list_A` 객체 내부의 데이터를 직접 수정(In-place)합니다.
```python
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a) # [1, 2, 3, 4] (a 자체가 변함)
```

#### 2) 더하기(`+`) 연산자 (새로운 객체 생성)
`list_A + list_B`는 두 리스트의 요소를 결합한 **완전히 새로운 제3의 리스트 객체를 생성**하여 반환합니다. 기존 `list_A`와 `list_B` 객체 내부의 데이터는 전혀 변하지 않습니다.
```python
a = [1, 2]
b = [3, 4]
c = a + b
print(c) # [1, 2, 3, 4]
print(a) # [1, 2] (a는 유지)
```

---

## 7.5 아이템 삭제

### (1) 꼬리 자르기 및 값 반환: pop()
`pop()` 메서드는 리스트의 **맨 마지막 아이템을 삭제하고, 삭제한 그 값을 반환(Return)**합니다.
* **매개변수 지정**: `pop(index)` 형태로 인덱스를 전달하면 맨 끝이 아닌 해당 특정 인덱스의 아이템을 삭제하고 반환받을 수 있습니다. 삭제된 위치 뒷요소들은 인덱스가 1씩 앞으로 당겨집니다.
```python
scores = [90, 80, 70]
last = scores.pop() # 맨 끝 70 삭제 후 반환
print(last)   # 70
print(scores) # [90, 80]
```

### (2) 인덱스 기반 무조건 삭제: del 키워드
`del` 키워드는 파이썬의 객체 소멸 지시어입니다. 리스트의 특정 인덱스를 지정하여 삭제할 수 있으나, `pop()`과 달리 **삭제한 값을 프로그램에 반환하지 않고 즉시 메모리 연결을 해제**합니다.
```python
numbers = [10, 20, 30]
del numbers[1] # 인덱스 1번(20) 강제 삭제
print(numbers) # [10, 30]
```

### (3) 값을 지정하여 삭제: remove()
`remove(item)` 메서드는 인덱스 번호가 아니라, **지우고자 하는 실제 데이터 값을 직접 기재하여 삭제**합니다.
* **중복 데이터 처리**: 리스트 안에 지우려는 값이 여러 개가 포진해 있는 경우, **가장 낮은 인덱스의 데이터 단 하나만 삭제**합니다.
* **다중 중복 요소 전원 삭제 로직**: 리스트 안에서 중복된 값 전체를 완벽히 지우려면 반복문(`while`과 `in` 연산자 조합)을 기용해야 합니다.
```python
# 다중 삭제 모범 패턴
data = [1, 2, 3, 2, 4, 2]
while 2 in data:
    data.remove(2)
print(data) # [1, 3, 4] (모든 2가 지워짐)
```

---

## 7.6 리스트 정렬, 순서 뒤집기, 슬라이싱

### (1) 정렬 메서드: sort()
`sort()`는 리스트 내부 요소들을 크기 순서대로 정렬하는 메서드입니다. 객체 내부 데이터를 직접 정렬(In-place Sort)하며, 반환값은 `None`입니다.
* **오름차순 (Ascending - 기본값)**: `reverse=False` (옵션 생략 가능)
* **내림차순 (Descending)**: `reverse=True` 명시
```python
nums = [5, 2, 9, 1]
nums.sort() # 오름차순 정렬
print(nums) # [1, 2, 5, 9]

nums.sort(reverse=True) # 내림차순 정렬
print(nums) # [9, 5, 2, 1]
```

### (2) 물리적 순서 뒤집기: reverse()
`reverse()` 메서드는 데이터의 크기 비교 정렬 없이, **현재 배치된 요소들의 순서를 물리적으로 그대로 거꾸로 뒤집어(Mirroring)** 줍니다. 이 역시 자체 인플레이스 연산입니다.
```python
chars = ['a', 'c', 'b']
chars.reverse()
print(chars) # ['b', 'c', 'a']
```

### (3) 리스트 슬라이싱 (List Slicing)
슬라이싱은 리스트에서 범위를 지정하여 필요한 일부분을 통째로 오려내어 새로운 서브 리스트를 복사 생성해내는 기술입니다.
* **기본 문법**: `리스트[시작인덱스:끝인덱스]`
* **수식 범위**: $\text{시작인덱스} \le x < \text{끝인덱스}$ (끝인덱스 위치의 요소는 포함되지 않음)
* **생략 규칙**:
  * 시작인덱스 생략 (`[:m]`): 0번 인덱스부터 복사.
  * 끝인덱스 생략 (`[n:]`): 리스트의 맨 마지막 요소까지 복사.
  * 전체 생략 (`[:]`): 리스트 전체 요소의 얕은 복사(Shallow Copy)본 생성.
```python
base = [10, 20, 30, 40, 50]
print(base[1:4])  # [20, 30, 40] (인덱스 1부터 3까지)
print(base[:3])   # [10, 20, 30] (0부터 2까지)
print(base[2:])   # [30, 40, 50] (2부터 끝까지)
```

---

## 7.7 실전 문제 해결 (Practical Exercises)

### (1) 좋아하는 과일 분류 검사
* **요구사항**: 빈 리스트 생성 후 사용자로부터 좋아하는 과일 3개를 키보드로 입력받아 보관합니다. 그 뒤, 추가로 과일 1개를 물어 그 과일이 내가 좋아하는 리스트에 존재하는지 판정하십시오.
```python
fruits = []

# 3회 입력 및 삽입
for i in range(3):
    fruit = input("좋아하는 과일을 입력하시오: ")
    fruits.append(fruit)

# 존재 여부 검사
search_name = input("과일의 이름을 입력하세요: ")
if search_name in fruits:
    print("이 과일은 당신이 좋아하는 과일입니다.")
else:
    print("이 과일은 당신이 좋아하는 과일이 아닙니다.")
```

### (2) 혈액 보관 시스템
* **요구사항**: 10명의 헌혈자로부터 기부받은 혈액형 데이터 집합이 있습니다. 각 혈액형(A, B, AB, O) 팩을 종류별로 각각 몇 팩씩 보유하고 있는지 수량을 종합 출력하십시오. (단, 리스트의 `count()` 메서드 활용)
```python
# 10명의 혈액 기부 내역 데이터 리스트
blood_donations = ['A', 'B', 'O', 'AB', 'O', 'A', 'A', 'B', 'O', 'AB']

blood_types = ['A', 'B', 'AB', 'O']

print("=== 혈액 보관 현황 ===")
for b_type in blood_types:
    cnt = blood_donations.count(b_type)  # 특정 값의 출현 횟수 카운트
    print(f"{b_type}형 혈액형: {cnt} 팩")
```

### (3) 공인중개사 시험 합격 여부 판독기
* **요구사항**: 
  - 공인중개사 시험 과목은 총 3과목(부동산학개론, 민법, 관계법규)입니다.
  - 사용자로부터 3과목의 성적을 키보드로 입력받아 리스트에 담습니다.
  - 합격 기준은 **평균 60점 이상**입니다.
  - 단, 3과목 중 단 1과목이라도 **40점 미만**의 점수가 있다면 과락으로 불합격 처리되어야 합니다.
```python
subjects = ["부동산학개론", "민법", "관계법규"]
scores = []

# 성적 입력받기
for sub in subjects:
    score = int(input(f"{sub} 점수를 입력하세요: "))
    scores.append(score)

# 합격 진단 로직
average = sum(scores) / len(scores)
is_pass = True
fail_subject = ""

# 과락 검사
for idx, score in enumerate(scores):
    if score < 40:
        is_pass = False
        fail_subject = subjects[idx]
        break  # 과락 발견 즉시 종료

print("---------------------------")
print(f"평균 점수: {average:.2f}점")

if not is_pass:
    print(f"결과: 불합격 (이유: {fail_subject} 과목 {scores[subjects.index(fail_subject)]}점 과락)")
elif average >= 60:
    print("결과: 최종 합격입니다!")
else:
    print("결과: 불합격 (이유: 평균 60점 미만)")
```

---

# Related Concepts
* [Loops](chapter-06.md) — 리스트 조회를 위한 `for`, `while` 순회 구조 제어.
* [Tuples and Dictionaries](chapter-08.md) — 리스트와 쌍벽을 이루는 다른 파이썬 컨테이너 구조들의 상세 작동 원리.

# Citations
* Chapter 07_리스트_업데이트.pdf [Python 7장](../../../raw/notes/Python/Chapter 07_리스트_업데이트.pdf)
