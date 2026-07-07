---
type: Study Note
title: "Chapter 12: Python Object-Oriented Programming (파이썬 객체지향 프로그래밍)"
description: "절차적 프로그래밍과 객체지향 프로그래밍(OOP)의 구조적 차이점과 클래스(Class), 객체(Object), 인스턴스(Instance)의 개념적 유기 관계를 심층 정리합니다. 클래스 선언 문법, 메서드 내 self 매개변수의 물리적 참조 역할, 객체 자동 초기화를 담당하는 생성자 __init__()의 연산 규칙을 분석합니다. Rectangle 클래스 설계 등 다양한 퀴즈와 실전 예제를 통해 OOP 기초를 완성합니다."
tags: [oop, class, object, instance, self-parameter, constructor, init-method, instance-variables, practical-examples]
timestamp: 2026-06-18
status: active
---

# 12. 객체지향 프로그래밍 (Python OOP)

## 12.1 객체지향 프로그래밍(OOP)의 철학

### (1) 두 패러다임의 비교
* **절차적 프로그래밍 (Procedural Programming)**:
  * 프로그램의 실행 논리 흐름과 명령어의 실행 순서에 집중하는 방식입니다.
  * 필요한 기능들을 함수나 모듈로 만들어 두고, 위에서 아래로 문제를 해결하는 순서에 따라 단계별로 함수를 호출해 가며 실행합니다.
  * 대표 언어: C, Fortran, BASIC 등
  * 단점: 현대의 그래픽 기반 앱이나 수많은 이벤트가 동시다발적으로 발생하는 복잡한 시스템에서는 로직이 엉키기 쉽고 유지보수가 매우 어려워집니다.
* **객체지향 프로그래밍 (Object-Oriented Programming, OOP)**:
  * 현실 세계의 사물과 개념들을 데이터(속성)와 행위(메서드)를 가진 하나의 독립된 객체(Object)로 규명하고, 이 객체들 간의 상호작용(메시지 송수신)을 통해 전체 문제를 해결해 나가는 개발 방법론입니다.
  * 대표 언어: Java, Python, C++, C# 등

### (2) 파이썬은 모든 것이 객체다
파이썬 내부에 존재하는 거의 모든 요소(정수, 실수, 문자열, 리스트, 튜플, 딕셔너리, 함수, 모듈 등)는 특정 클래스를 기반으로 메모리에 구체화되어 적재된 **객체**입니다.
* **리스트 객체 연산 예시**:
  ```python
  animals = ['lion', 'tiger', 'cat', 'dog']
  animals.sort()   # animals 리스트 객체의 sort() 메서드 호출
  animals.append('rabbit') # append() 메서드 호출
  s = animals.pop() # pop()으로 마지막 값 삭제 및 반환
  print(s.upper()) # 문자열 객체 s의 upper() 메서드 연계 호출 -> "RABBIT"
  ```

---

## 12.2 클래스, 객체, 인스턴스의 정의와 관계

많은 개발자가 혼동하기 쉬운 세 개념의 명확한 기술적 정의와 유기적 관계는 다음과 같습니다.

### (1) 3대 개념 정의
1. **클래스 (Class)**: 객체를 만들어 내기 위한 **설계도, 템플릿(틀), 청사진**입니다. 객체가 어떤 데이터(속성)를 갖고 어떤 기능(메서드)을 수행할지 미리 뼈대를 정의해 놓은 틀입니다.
2. **객체 (Object)**: 클래스로부터 실제로 만들어질 수 있는 **모든 실체와 대상**을 총칭하는 포괄적 개념입니다.
3. **인스턴스 (Instance)**: 설계도(클래스)를 바탕으로 컴퓨터 **실제 물리 메모리 영역에 구체적으로 할당되어 살아 움직이는 개별적인 실체**입니다.

### (2) 비유적 표현과 올바른 표현 규칙
* **붕어빵 틀과 붕어빵**:
  * 클래스 ➡️ 붕어빵을 구워내는 '붕어빵 틀' (설계도)
  * 객체 ➡️ 붕어빵 틀로 찍어낼 수 있는 모든 '붕어빵'들을 통칭하는 추상명사
  * 인스턴스 ➡️ 지금 내 눈앞의 접시 위에 노릇하게 구워져 놓인 '이 붕어빵' (실제 존재)
* **표현 가이드**: 클래스와 개별 실체 간의 관계를 수식할 때는 **인스턴스**라는 표현이 문맥상 가장 정확합니다.
  * "나비는 객체다." ⭕ (맞는 말이지만 다소 모호함)
  * "나비는 Cat 클래스의 인스턴스이다." 🎯 (관계가 완벽하게 명시된 베스트 표현)

---

## 12.3 클래스 선언과 self 매개변수의 물리적 역할

### (1) 클래스 선언 기본 문법
```python
class 클래스명:
    def 메서드명(self):
        실행문
```
* **class 키워드**: 클래스 정의의 시작을 알립니다.
* **클래스명 작명 규칙**: 파이썬 관례상 첫 글자는 **대문자**로 시작하며, 여러 단어가 결합될 때는 각 단어 첫 글자만 대문자로 쓰는 **파스칼 케이스(PascalCase)**를 채택합니다. (예: `MyCalculator`)
* **메서드 (Method)**: 클래스 내부에서 정의되어 클래스의 인스턴스가 호출하여 사용하는 함수를 의미합니다.

### (2) `self` 매개변수의 핵심 작동 원리
클래스 내에 속한 모든 메서드들은 **첫 번째 매개변수로 반드시 `self`를 기재**해 두어야 합니다.
* **물리적 의미**: `self`는 현재 메서드가 실행되고 적용되는 **"호출 인스턴스 객체 자신"**의 메모리 시작 주소를 가리키는 파이썬 내부의 포인터 변수입니다.
* **속성 참조**: 클래스가 자신의 내부 변수(인스턴스 변수)나 또 다른 내부 메서드를 참조할 때는 반드시 변수명이나 메서드명 앞에 **`self.` 도트 접근자**를 접두어로 붙여야 합니다.
* **호출 시 생략**: 인스턴스에서 메서드를 호출할 때(`nabi.meow()`), 파이썬 엔진이 자동으로 호출 객체인 `nabi`를 첫 번째 인자 자리에 주입하므로, 개발자가 소괄호 안에 `self` 값을 수동으로 적어줄 필요는 없습니다.
> [!NOTE]
> `self`는 파이썬 문법의 공식 예약어(Keyword)가 아닙니다. 단지 첫 번째 매개변수 자리에 오는 인자를 가리키기 위해 커뮤니티 전반이 약속한 식별자 이름일 뿐이므로 다른 단어로 대체해도 작동은 하지만, 관례 위반으로 인한 심각한 가독성 하락을 막기 위해 반드시 `self`로 통일해야 합니다.

```python
class Cat:
    def meow(self):  # self 필수 지정
        print("야옹 야옹~~~")

nabi = Cat()  # Cat 인스턴스 생성
nabi.meow()   # 메서드 실행 -> "야옹 야옹~~~"
```

---

## 12.4 생성자(Constructor)와 인스턴스 변수

### (1) 생성자: `__init__()` 메서드
`__init__()` 메서드는 객체가 메모리에 새로 생성될 때 파이썬 엔진에 의해 **자동으로 즉각 실행되는 특수한 초기화 메서드(생성자)**입니다.
* **주요 용도**: 객체가 탄생하는 그 시점에 가져야 할 초기 속성 변수(이름, 색상, 나이 등)를 매개변수로 받아와 강제로 세팅할 때 사용합니다.
* **자동 실행**: 사용자가 명시적으로 `nabi.__init__()` 형태로 호출할 필요 없이, `Cat('나비')`처럼 클래스명을 함수처럼 호출할 때 인스턴스화 과정과 함께 자동으로 즉시 가동됩니다.

### (2) 인스턴스 변수 (Instance Variable)
각각의 인스턴스가 저마다 개별적인 데이터 값을 저장하기 위해 가지는 속성 공간을 의미하며, 필드(Field) 또는 멤버 변수라고도 합니다. 생성자 내에서 **`self.변수명 = 값`** 구문으로 선언합니다.

```python
class Cat:
    # 생성자 정의
    def __init__(self, name, color='흰색'):
        self.name = name       # 인스턴스 변수 name 생성 및 초기화
        self.color = color     # 인스턴스 변수 color 생성 및 초기화
        
    def meow(self):
        # self를 붙여 인스턴스 고유 변수값 호출
        print(f"내 이름은 {self.name}, 색깔은 {self.color}, 야옹 야옹~~")

# 인스턴스별로 서로 다른 속성을 부여하며 생성
nabi = Cat('나비', '검정색')
nero = Cat('네로')  # color는 디폴트값 '흰색' 적용

nabi.meow() # "내 이름은 나비, 색깔은 검정색, 야옹 야옹~~"
nero.meow() # "내 이름은 네로, 색깔은 흰색, 야옹 야옹~~"
```

---

## 12.5 퀴즈 및 연습문제 풀이 해설

### [퀴즈 1] 강아지(Dog) 클래스 구현
* **요구사항**: `bark(self)` 메서드를 호출하면 `"멍멍~~"`을 출력하는 `Dog` 클래스를 작성하고 인스턴스를 만들어 실행해 보시오.
```python
class Dog:
    def bark(self):
        print("멍멍~~")

my_dog = Dog()
my_dog.bark() # 출력: 멍멍~~
```

### [퀴즈 2] Dog 클래스에 생성자 도입 및 호출
* **요구사항**: 개 이름(`name`)과 품종(`breed`)을 초기화하는 생성자를 도입하고, 이름이 `"Jindo"`, 품종이 `"진돗개"`인 인스턴스를 만든 뒤 울음소리를 내는 메서드를 구동시키시오.
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} ({self.breed}): 멍멍~~")

jindo = Dog("Jindo", "진돗개")
jindo.bark() # 출력: Jindo (진돗개): 멍멍~~
```

### [퀴즈 3] Test 클래스 분석 질문 답변
```python
class Test:
    def __init__(self, a):
        self.a = a
    def display(self):
        print(self.a)

obj = Test(99)
obj.display()
```
* **답변**:
  1. **클래스의 이름**: `Test`
  2. **가지고 있는 속성(인스턴스 변수)**: `self.a`
  3. **메서드 종류**: 생성자인 `__init__()`와 값을 출력하는 `display()`
  4. **최종 실행 결과**: 콘솔에 `99` 출력.

### [퀴즈 4 & 5] 사각형(Rectangle) 클래스 종합 구현
* **요구사항**: 
  - 사각형의 가로(`width`)와 세로(`height`) 속성을 가지는 `Rectangle` 클래스를 설계합니다.
  - 가로와 세로 정보를 기반으로 면적($\text{가로} \times \text{세로}$)을 반환하는 `area()` 메서드를 추가합니다.
  - 사각형의 둘레($2 \times (\text{가로} + \text{세로})$)를 반환하는 `perimeter()` 메서드를 추가합니다.
  - 사각형의 모든 정보(가로, 세로, 면적, 둘레)를 예시 포맷에 맞게 일괄 출력하는 `display_info()` 메서드를 추가하여 프로그램을 작동시키십시오.
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * (self.width + self.height)
        
    def display_info(self):
        print(f"사각형의 가로: {self.width}")
        print(f"사각형의 높이: {self.height}")
        print(f"사각형의 면적: {self.area()}")
        print(f"사각형의 둘레: {self.perimeter()}")

# 가로 5, 세로 3인 사각형 인스턴스 생성 및 검증
rect = Rectangle(5, 3)
rect.display_info()
```
```text
사각형의 가로: 5
사각형의 높이: 3
사각형의 면적: 15
사각형의 둘레: 16
```

---

# Related Concepts
* [Function Basics](chapter-09.md) — 클래스 내 메서드 구조의 기초가 되는 함수 문법.
* [Advanced Functions](chapter-10.md) — 매개변수 기본값 설정 및 변수 스코프 규칙.

# Citations
* Chapter 12_객체지향_최종.pdf [Python 12장](../../../raw/notes/Python/Chapter 12_객체지향_최종.pdf)
