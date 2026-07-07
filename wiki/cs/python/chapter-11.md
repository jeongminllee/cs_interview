---
type: Study Note
title: "Chapter 11: Python Modules (파이썬 모듈)"
description: "파이썬 모듈(Module)의 개념과 협업/분업화 장점, 모듈 탐색 경로를 추가하는 sys.path.append() 설정 기법을 학습합니다. import, as, from 키워드를 활용한 효율적인 코드 로드 방식과 모듈 가드 블록 구축을 위한 __name__ 전역 변수의 작동 메커니즘을 규명합니다. 나아가 파이썬 표준 라이브러리(math, random, time)의 핵심 함수와 포맷 규격, 그리고 실전 로또 시뮬레이터 예제를 수록합니다."
tags: [modules, import-keywords, sys-path, main-guard, math-module, random-module, time-module, practical-examples]
timestamp: 2026-06-18
status: active
---

# 11. 모듈 (Python Modules)

## 11.1 모듈의 정의와 장점

### (1) 모듈(Module)이란?
모듈은 특정 목적을 위해 설계된 **함수, 변수, 클래스 등을 모아놓은 파이썬 소스코드 파일(`.py`)**입니다. 비유하자면, 식당에서 매번 밀가루를 반죽해 면을 뽑기보다 이미 조리 완료되어 포장된 간편식(HMR)을 구매해 즉시 상에 올리는 것처럼, 이미 검증된 공용 코드를 내 코드로 손쉽게 가져와 사용하는 기능입니다.

### (2) 모듈의 분류
* **표준 모듈 (Standard Modules)**: 파이썬 인터프리터 설치 시 기본 내장되어 별도 설치 없이 `import`만으로 즉시 구동할 수 있는 라이브러리. (예: `math`, `random`, `time`, `sys` 등)
* **사용자 정의 모듈 (User-defined Modules)**: 개발자가 프로젝트 구성상 필요에 의해 직접 코딩하여 저장해 둔 파이썬 파일.

### (3) 모듈 사용의 3대 이점
1. **생산 속도 향상**: 복잡한 공통 기능(수학 연산, 날짜 포맷팅 등)을 바닥부터 코딩하지 않아 개발 시간이 크게 줄어듭니다.
2. **코드 안정성 확보**: 수많은 테스트를 통과해 검증된 모듈을 가져다 쓰므로, 직접 짠 코드 대비 버그 발생율이 비약적으로 줄어듭니다.
3. **분업화 및 협업**: 큰 프로젝트를 기능 단위로 쪼개어 여러 개발자가 병렬 코딩한 뒤, 서로의 파일을 모듈 형태로 공유 및 결합해 전체 프로그램을 완성할 수 있습니다.

---

## 11.2 모듈 제작 및 로드(Load) 메커니즘

### (1) 사용자 정의 모듈 제작
간단한 사칙연산을 수행하는 함수들을 담은 `calculator.py` 파일을 생성하는 것만으로 모듈 제작이 완료됩니다. 파일 확장자명인 `.py`를 제외한 **파일명(본문 이름) `calculator`가 모듈의 명칭**이 됩니다.

```python
# calculator.py (모듈 파일)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

### (2) 모듈 가져오기 (Import) 와 도트 접근자
동일한 폴더 내에 있는 실행용 파일 `main.py`에서 제작한 모듈을 불러옵니다.
```python
# main.py (실행 파일)
import calculator  # calculator 모듈 로드

res = calculator.add(10, 20)  # 도트 접근자(.)를 이용해 접근
print(res)  # 30
```
> [!WARNING]
> 모듈을 가져올 때 `import calculator.py`처럼 파일 확장자까지 기재하면 문법 에러(`ModuleNotFoundError` 또는 `SyntaxError`)가 발생하므로 반드시 순수 파일명만 기술해야 합니다.

### (3) sys.path.append()를 통한 물리 경로 확장
만약 로드하려는 모듈 파일이 실행 파일과 완전히 다른 폴더나 상위 디렉토리에 위치해 있다면, 파이썬이 모듈을 찾아갈 수 있도록 탐색 경로(Search Path) 리스트에 해당 경로를 직접 등록해야 합니다.
```python
import sys
# 파이썬 모듈 검색 대상 경로 목록의 맨 끝에 모듈이 들어있는 물리 폴더 위치 강제 추가
sys.path.append("C:/project/custom_modules") 

import my_module  # 이제 에러 없이 정상 로드 가능
```

---

## 11.3 슬기로운 모듈 제어 키워드 (as, from)

### (1) Alias 지정: as 키워드
불러오려는 모듈의 이름이 너무 길어 코딩 시 타이핑 피로도가 높거나 가독성을 해칠 경우, `as` 지시어를 써서 짧고 간결한 임시 단축명(Alias)으로 치환하여 활용할 수 있습니다.
```python
import convert_unit_module as cu

# 기존의 긴 이름 대신 cu를 매개체로 작동
result = cu.convert_mm_to_cm(500)
```

### (2) 기능 발췌 수입: from 키워드
모듈 내부에는 수백 개의 함수가 존재할 수 있습니다. 그중 내가 사용할 기능이 극히 일부분(예: 더하기와 빼기만 사용)이라면, 모듈 전체가 아니라 필요한 특정 요소만 선별하여 가져오는 것이 메모리와 자원 효율에 좋습니다.
* **문법**: `from 모듈명 import 함수1, 함수2`
* **호출 가독성**: 이 방식으로 수입된 함수들은 호출부에서 **`모듈명.` 도트 접근자를 완전히 생략하고 함수명만 단독으로 직접 사용**할 수 있어 코드가 깔끔해집니다.
```python
from calculator import add, subtract

res = add(5, 3)  # calculator.add가 아닌 그냥 add로 다이렉트 호출 가능
```
> [!TIP]
> `from calculator import *` 처럼 아스테리스크(`*`)를 붙이면 모듈 내 모든 요소를 도트 생략 상태로 가져옵니다. 다만, 이 방식은 메인 파일 내의 기존 변수/함수명과 모듈 내부 명칭 간에 충돌이 일어날 경우 추적이 매우 어렵고 가독성이 떨어지므로, 현업에서는 사용을 자제하고 명시적으로 이름을 나열하는 방식을 권장합니다.

---

## 11.4 메인 가드 블록 지정 (`__name__` 전역 변수)

### (1) 모듈 로딩 시 강제 실행 문제
모듈 제작자가 개발 단계에서 함수가 잘 돌아가는지 테스트해 보려고 모듈 파일 내부에 즉석 실행문(`print(add(1, 2))`)을 직접 적어두는 경우가 많습니다. 
* **문제점**: 이 모듈을 다른 실행 파일에서 단지 `import my_module` 하기만 해도, 호출하지도 않은 모듈 내부의 테스트 코드가 자동으로 런타임에 즉시 구동되어 출력 결과를 지저분하게 만드는 부작용이 발생합니다.

### (2) `__name__` 전역 변수의 정체
파이썬 엔진은 모든 코드 파일이 가동될 때 눈에 보이지 않는 **`__name__`**이라는 특별한 전역 변수를 내부에 자동 생성하고 문자열 값을 주입합니다. 이 변수에 담기는 값은 파일의 실행 형태에 따라 결정됩니다.

1. **최초 실행 메인 파일**: 터미널에서 `python main.py`처럼 사용자가 직접 실행시킨 메인 진입점 파일의 `__name__` 변수에는 무조건 **`'__main__'`**이라는 값이 강제 세팅됩니다.
2. **임포트된 모듈 파일**: 메인 파일에 의해 `import`되어 보조 도구로 올라온 모듈 파일의 `__name__` 변수에는 **해당 모듈의 실제 이름(파일명)**이 문자열로 주입됩니다.

### (3) 메인 가드 (Main Guard) 블록의 구축
이러한 물리적 차이를 이용해, **"직접 실행했을 때만 작동하고, 모듈로 임포트되었을 때는 침묵할 테스트 코드 영역"**을 다음과 같은 조건문으로 격리 코딩합니다.
```python
# my_module.py
def addition(a, b):
    return a + b

# 메인 가드 블록 지정
if __name__ == '__main__':
    # 이 밑의 코드는 my_module.py를 직접 실행했을 때만 가동됨
    # 다른 파일에서 import my_module 할 때는 가동되지 않음!
    print("모듈 자체 테스트 작동:", addition(10, 20))
```

---

## 11.5 파이썬 핵심 내장(표준) 모듈 분석

### (1) math 모듈 (수학 연산)
기본 사칙연산보다 고차원적인 공학 계산 기능들을 제공합니다.
* `math.pi`: 원주율 상수 ($3.141592...$)
* `math.sqrt(x)`: $x$의 제곱근 계산 ($\sqrt{x}$)
* `math.ceil(x)`: 올림 처리 (소수점을 무조건 다음 큰 정수로 변환)
* `math.floor(x)`: 내림 처리 (소수점을 버리고 이전 정수로 변환)
* `math.factorial(x)`: 팩토리얼 연산 ($x!$)

### (2) random 모듈 (난수 제어)
예측 불가능한 임의의 값을 무작위로 추첨해내는 모듈입니다.
* `random.random()`: $0.0 \le x < 1.0$ 범위의 무작위 실수 반환.
* `random.randint(a, b)`: $a \le x \le b$ 범위의 **양 끝값을 모두 포함하는** 무작위 정수 반환.
* `random.choice(seq)`: 리스트 등 시퀀스 데이터에서 요소 1개를 임의로 뽑아 반환.
* `random.shuffle(list)`: 리스트의 요소 순서를 무작위로 뒤섞음 (In-place 연산).
* `random.sample(seq, k)`: 중복 없이 무작위로 $k$개의 요소를 표본 추출하여 리스트로 반환.

### (3) time 모듈 (시간 계산)
시스템의 작동 시간 및 날짜 포맷 제어 기능을 제공합니다.
* `time.time()`: 에포크 시간(Epoch Time) 반환. 1970년 1월 1일 0시 0분 0초를 기점으로 현재까지 누적된 초(seconds) 단위를 정밀 실수로 알려줌.
* `time.localtime(sec)`: 전달받은 초 단위를 로컬 컴퓨터 타임존의 시간대로 변환한 구조화 튜플(`struct_time`)을 반환.
* `time.gmtime(sec)`: 세계 표준시(UTC/GMT) 기준의 구조화 튜플 반환.
* `time.strftime(format, t_struct)`: 구조화 튜플 시간을 포맷팅 규칙에 맞춰 아름다운 문자열로 출력.

#### [표] 자주 쓰이는 strftime 포맷 코드
| 코드 | 의미 | 예시 |
| :--- | :--- | :--- |
| **`%Y`** | 4자리 연도 (Year) | `2026` |
| **`%m`** | 2자리 월 (Month) | `06` (01~12) |
| **`%d`** | 2자리 일 (Day) | `18` (01~31) |
| **`%H`** | 24시간 형식의 시간 (Hour) | `15` (00~23) |
| **`%M`** | 분 (Minute) | `45` (00~59) |
| **`%S`** | 초 (Second) | `09` (00~59) |

```python
import time
now = time.localtime(time.time())
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
print("현재 시간:", formatted_time) # "2026-06-18 15:45:09"
```

---

## 11.6 실전 문제 해결 (Practical Exercises)

### (1) 로또 번호 시뮬레이터 프로그램
* **요구사항**: 
  - 사용자는 키보드 입력을 통해 1부터 45 사이의 번호 6개를 임의로 등록합니다. (중복 입력 금지)
  - 컴퓨터는 `random.sample()`을 이용하여 1부터 45 사이의 숫자 중 중복 없이 6개의 난수 당첨 번호를 생성합니다.
  - 두 당첨 번호 목록을 정렬하여 보여주고, 몇 개의 번호가 서로 일치하는지 비교하여 등수 결과를 알려주는 프로그램을 모듈 기법을 가미하여 설계하십시오.
```python
import random

def get_user_numbers():
    user_nums = []
    print("=== 로또 번호 입력 (1~45) ===")
    while len(user_nums) < 6:
        try:
            num = int(input(f"{len(user_nums) + 1}번째 번호 입력: "))
            if num < 1 or num > 45:
                print("1에서 45 사이의 숫자만 입력해 주세요.")
                continue
            if num in user_nums:
                print("이미 입력한 번호입니다. 다른 번호를 입력하세요.")
                continue
            user_nums.append(num)
        except ValueError:
            print("올바른 정수형태의 숫자를 입력해 주세요.")
    user_nums.sort()
    return user_nums

def generate_winning_numbers():
    # random.sample은 중복 없이 임의의 k개를 추출하므로 최적임
    winning_nums = random.sample(range(1, 46), 6)
    winning_nums.sort()
    return winning_nums

def check_lotto_results(user_lst, winning_lst):
    # 두 리스트에서 교집합(&)을 구하기 위해 Set 자료형 활용
    matches = list(set(user_lst) & set(winning_lst))
    matches.sort()
    
    print("\n" + "=" * 40)
    print(f"내가 선택한 번호: {user_lst}")
    print(f"컴퓨터 당첨 번호: {winning_lst}")
    print(f"일치하는 번호들: {matches} (총 {len(matches)}개 일치)")
    
    # 등수 산정
    if len(matches) == 6:
        print("결과: 🏆 대박! 1등에 당첨되셨습니다!!")
    elif len(matches) == 5:
        print("결과: 🎉 축하합니다! 2등에 당첨되셨습니다!!")
    elif len(matches) == 4:
        print("결과: 🥉 축하합니다! 3등에 당첨되셨습니다.")
    elif len(matches) == 3:
        print("결과: 🏅 4등 당첨 (고정 당첨금 5,000원)")
    else:
        print("결과: 😭 아쉽지만 낙첨되셨습니다. 다음 기회에!")
    print("=" * 40)

# 메인 실행 가드
if __name__ == '__main__':
    my_numbers = get_user_numbers()
    winning_numbers = generate_winning_numbers()
    check_lotto_results(my_numbers, winning_numbers)
```

---

# Related Concepts
* [Function Basics](chapter-09.md) — 모듈 내부 구성의 핵심인 사용자 정의 함수 구조.
* [Advanced Functions](chapter-10.md) — 매개변수 가변인자(*args) 및 반환 타입(튜플) 활용.

# Citations
* Chapter 11_모듈 활용하기_업데이트(250413).pdf [Python 11장](../../../raw/notes/Python/Chapter 11_모듈 활용하기_업데이트(250413).pdf)
