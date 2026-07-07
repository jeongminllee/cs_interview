---
type: Study Note
title: "Chapter 04: Data Structures & Diagnostics - Arrays & Exception Handling (배열 및 예외 처리)"
description: "자바의 객체지향적 배열 모델과 힙 메모리 참조 매커니즘, 비정방형 배열의 물리적 메모리 구성을 파악하고, 예외 처리 프레임워크의 제어 흐름 및 InputMismatchException 등의 실무 예외 대응 기법을 학습합니다."
tags: [java, array, irregular-array, length-field, for-each, exception-handling, try-catch-finally, exception-classes]
timestamp: 2026-06-19
status: active
---

# 1. 자바 배열(Array)의 구조 및 특징

자바에서 배열은 단순히 연속된 메모리 공간을 가리키는 포인터가 아니라, **힙(Heap) 영역에 생성되는 객체(Object)**로 취급됩니다.

### 1) 배열의 핵심 특성
* **인덱스 기반 접근**: 0부터 시작하는 정수 인덱스를 사용하여 원소에 접근합니다. 마지막 원소의 인덱스는 `배열 크기 - 1`입니다.
* **동일 타입의 집합**: 배열 내부의 모든 원소는 동일한 데이터 타입이어야 합니다.
* **연속된 메모리 할당**: 배열 원소들은 메모리에 순차적으로 적재되므로 루프를 통한 일괄 처리에 최적화되어 있습니다.
* **상대적 주소 의미**: 인덱스는 배열의 시작 주소에서부터 해당 데이터까지 떨어진 상대적인 오프셋(Offset) 위치를 나타냅니다.

### 2) 일차원 배열 만들기: 선언과 생성의 2단계 프로세스
자바의 배열은 반드시 선언과 할당(생성)의 과정을 거쳐야 사용할 수 있습니다.

```mermaid
graph TD
    Decl[1단계: 배열 레퍼런스 변수 선언<br>int intArray[];] --> Alloc[2단계: new 연산자로 실제 배열 객체 힙에 할당<br>intArray = new int[5];]
    Alloc --> Access[배열 사용 가능<br>intArray[0] = 5;]
```

* **1단계: 배열 선언 (Declaration)**
  * **문법**: `int intArray[];` 또는 `int[] intArray;`
  * **원리**: 힙 메모리의 배열 객체를 가리킬 참조(주소) 변수를 스택에 생성하는 단계입니다. 이 상태에서는 실제 메모리 저장 공간이 할당되지 않았으므로 **배열 크기를 지정하면 컴파일 에러**가 발생합니다. (예: `int intArray[5];` (X))
* **2단계: 배열 생성 (Creation)**
  * **문법**: `intArray = new int[5];`
  * **원리**: `new` 연산자를 사용하여 힙 영역에 실제 5개의 정수를 저장할 메모리 공간을 가진 배열 객체를 할당하고, 그 주소를 `intArray` 참조 변수에 대입합니다. 이 단계에서 비로소 배열의 크기가 결정됩니다.
* **선언과 동시에 초기화**
  * 선언과 동시에 중괄호 `{}`를 사용해 초기값을 주면, `new` 연산자 없이도 값의 개수만큼 자동으로 힙 메모리에 배열 공간이 생성됩니다.
  * 문법: `int intArray[] = {4, 3, 2, 1, 0};`
* **잘못된 접근 시 에러**
  * 선언만 하고 메모리를 할당하지 않은 변수를 사용(`intArray[0] = 1;`)하려고 하면 컴파일 에러 혹은 NullPointerException을 마주합니다.
  * 존재하지 않는 인덱스에 접근하면 JVM에 의해 `ArrayIndexOutOfBoundsException` 예외가 발생합니다.

### 3) 레퍼런스 치환과 배열 공유 (Reference Assignment)
* 자바에서 배열 변수 간의 대입(`=`)은 데이터를 복사하는 것이 아니라 **메모리 주소(Reference)를 치환**하는 것입니다.
* 예: `int intArray[] = new int[5]; int myArray[] = intArray;`
  * 이 경우 `myArray`는 `intArray`가 가리키던 힙 메모리의 배열 객체 주소를 똑같이 복사받게 됩니다.
  * 결과적으로 두 변수는 **동일한 배열 객체를 공유**하므로, `myArray[1] = 6;`을 실행하면 `intArray[1]`의 값 또한 `6`으로 변하게 됩니다.

### 4) length 필드의 객체지향적 모델
* 자바의 모든 배열 객체는 컴파일러에 의해 자동으로 관리되는 읽기 전용 상수 필드인 **`length`**를 가집니다.
* `intArray.length`와 같이 호출하여 배열의 실제 크기를 언제든 참조할 수 있으며, 이는 루프 경계 조건을 설정할 때 하드코딩을 방지하여 코드의 가동률과 유지보수성을 극대화합니다.

### 5) for-each 문을 통한 안전한 순회
* **문법**: `for (타입 변수명 : 배열/컬렉션) { ... }`
* **특징**: 인덱스 제어 변수(i)를 직접 제어하지 않으므로 인덱스 경계 오류(`ArrayIndexOutOfBoundsException`) 발생 가능성을 원천 차단하고 가독성을 크게 개선합니다. 다만, 루프 내에서 배열 내부의 값을 임의로 변경할 수는 없습니다.

---

# 2. 다차원 배열과 비정방형 배열 (Irregular Array)

### 1) 2차원 배열의 메모리 물리 모델
자바의 2차원 배열은 '배열의 배열'로 구현됩니다. 즉, 2차원 배열 객체는 각 행을 가리키는 1차원 배열 레퍼런스들의 집합입니다.
```java
int[][] i = new int[2][5];
```
* `i.length` $\rightarrow$ 2차원 배열의 **행의 개수** (값은 `2`)
* `i[n].length` $\rightarrow$ n번째 **행의 열의 개수** (값은 `5`)

### 2) 비정방형 배열 (Irregular / Ragged Array)
각 행마다 열의 크기가 서로 다른 배열을 의미합니다. 자바에서는 2차원 배열 생성 시 최초 행의 크기만 지정하고 열의 크기를 비워둔 채 힙 영역에 행마다 개별적인 1차원 배열 객체를 동적으로 다르게 할당하여 이를 구현합니다.

```java
int intArray[][] = new int[4][]; // 행의 크기 4만 먼저 할당
intArray[0] = new int[3];        // 0번째 행은 3열짜리 1차원 배열 참조
intArray[1] = new int[2];        // 1번째 행은 2열짜리 1차원 배열 참조
intArray[2] = new int[3];        // 2번째 행은 3열짜리 1차원 배열 참조
intArray[3] = new int[2];        // 3번째 행은 2열짜리 1차원 배열 참조
```

```mermaid
graph TD
    subgraph Stack
        intArray[intArray 참조 변수]
    </main>
    subgraph Heap
        intArray --> RowRef[행 레퍼런스 배열: 크기 4]
        RowRef --> |0| Row0[1차원 배열: 크기 3]
        RowRef --> |1| Row1[1차원 배열: 크기 2]
        RowRef --> |2| Row2[1차원 배열: 크기 3]
        RowRef --> |3| Row3[1차원 배열: 크기 2]
    end
```

---

# 3. 메서드에서의 배열 리턴 (Array Return)

* 자바 메서드가 배열을 리턴할 때 역시 배열 원소들의 데이터 전체가 복사되어 넘어가는 것이 아니라, 힙 영역의 **배열을 가리키는 레퍼런스(메모리 주소값)가 복사되어 리턴**됩니다.
* **문법**: 리턴 타입 뒤에 대괄호 `[]`를 표기하며, 리턴 타입 선언문에는 배열의 크기를 지정하지 않습니다.
  ```java
  static int[] makeArray() {
      int temp[] = new int[4];
      return temp; // 힙에 만들어진 배열의 레퍼런스를 넘겨줌
  }
  ```

---

# 4. 자바의 예외 처리 (Exception Handling)

### 1) 오류의 분류
* **컴파일 오류 (Compile-time Error)**: 자바 문법 규칙을 위반하여 컴파일러가 잡아내는 문법 오류입니다. 빌드가 불가능합니다.
* **예외 (Exception / Runtime Error)**: 문법적으로는 이상이 없어 정상 컴파일되었으나, 프로그램 실행(Runtime) 중에 예측하지 못한 오동작이나 불합리한 환경 조건에 의해 유발되는 오류입니다.

### 2) 예외 처리 메커니즘 (try-catch-finally)
예외가 발생했을 때 프로그램이 강제 비정상 종료되는 것을 막고, 복구 기회를 제공하기 위해 예외 처리 코드를 명시합니다.

```java
try {
    // 예외가 발생할 가능성이 있는 실행 코드 (try 블록)
} catch (예외타입클래스 e) {
    // 예외 발생 시 이를 포착하여 복구/로그 처리하는 코드 (catch 블록)
} finally {
    // 예외 발생 여부와 전혀 무관하게 무조건 마지막에 실행되는 코드 (finally 블록)
    // 주로 DB 연결 종료, 파일 스트림 close() 등 리소스 해제 코드를 적음 (생략 가능)
}
```

* **동작 시나리오**:
  * **예외가 없는 경우**: `try` 블록 실행 $\rightarrow$ `finally` 블록 실행 $\rightarrow$ `try-catch` 이후 코드 실행.
  * **예외가 발생한 경우**: `try` 내 예외 시점 이전 코드 실행 $\rightarrow$ 예외 발생 $\rightarrow$ 즉시 `try` 중단 $\rightarrow$ 일치하는 `catch` 블록으로 이동 및 실행 $\rightarrow$ `finally` 블록 실행 $\rightarrow$ 이후 코드 실행.

---

# 5. 자주 발생하는 실무 자바 예외 클래스

JVM 표준 패키지가 정의하는 대표적인 예외 유형들입니다.

| 예외 클래스명 | 발생 조건 및 특징 | 패키지 |
| :--- | :--- | :--- |
| **ArithmeticException** | 정수를 `0`으로 나누는 연산 등 불가능한 산술 처리를 지시할 때 발생. | `java.lang` |
| **NullPointerException** | `null` 값을 가진 레퍼런스 변수를 통해 객체의 속성이나 메서드에 접근할 때 발생. | `java.lang` |
| **ClassCastException** | 상속/인터페이스 관계가 성립하지 않는 하위 클래스로 객체 타입을 억지로 변환할 때 발생. | `java.lang` |
| **ArrayIndexOutOfBoundsException** | 배열의 인덱스 한계를 벗어나 음수나 크기 이상의 범위로 접근 시 발생. | `java.lang` |
| **IllegalArgumentException** | 메서드에 잘못된 형식의 매개변수가 부적합하게 주입되었을 때 발생. | `java.lang` |
| **NumberFormatException** | 숫자 형태가 아닌 문자열을 정수나 실수로 강제 파싱하려 할 때 발생. (예: `Integer.parseInt("3.1415")`) | `java.lang` |
| **InputMismatchException** | `Scanner`의 `nextInt()` 등으로 타입 입력을 기대했으나 사용자가 문자를 입력할 때 발생. | `java.util` |
| **IOException** | 파일 읽기/쓰기 실패, 네트워크 소켓 이상 등 입출력 문제 발생 시 포착. | `java.io` |

### [InputMismatchException 예외 대처 핵심 패턴]
`Scanner`의 `nextInt()` 호출 시 사용자가 정수가 아닌 잘못된 문자(예: `'R'`)를 타이핑하면 `InputMismatchException`이 던져집니다.
이때 `catch` 블록 내부에서 단순히 루프를 재시도하기만 하면 **버퍼(Buffer)에 남아있는 잘못된 문자 토큰 `'R'`이 소비되지 않고 계속 버퍼의 맨 앞에 누적**되므로, 다음 `nextInt()` 시도에서도 똑같이 예외가 무한히 연속 발생하는 버그에 빠집니다.
따라서 `catch` 블록 안에 **`scanner.next();`**를 작성하여 입력 버퍼에 적재된 부적절한 문자 토큰을 강제로 꺼내어 소거(Discard)해야만 재시도를 올바르게 진행할 수 있습니다.

---

# Citations
* [04자바 기본 프로그래밍.pdf](../../../raw/notes/java/04자바 기본 프로그래밍.pdf)
