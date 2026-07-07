---
type: Study Note
title: "Chapter 09: Module and Package (모듈과 패키지)"
description: "자바의 네임스페이스 및 배포 구조인 패키지와 모듈 시스템을 살펴보고, 자바 핵심 내장 라이브러리 클래스인 Object, Wrapper, String, StringBuffer, StringBuilder, Math, Calendar, 그리고 java.time 패키지의 상세 구현과 특징을 분석합니다."
tags: [java, package, module, object, wrapper-class, string, string-builder, java-time]
timestamp: 2026-06-19
status: active
---

# Summary

본 장에서는 자바 응용 프로그램의 구조적 관리와 배포 단위를 규정하는 **패키지(Package)**와 Java 9부터 도입된 **모듈(Module)** 시스템을 탐구합니다. 또한 자바 기본 API의 근간을 이루는 핵심 패키지(`java.lang`, `java.util`, `java.time`)의 핵심 클래스들을 심층 분석합니다. 특히 최상위 클래스인 `Object`, 박싱과 언박싱을 수행하는 `Wrapper`, 불변성 및 메모리 풀을 특징으로 하는 `String`, 동기화 유무에 따라 스레드 안전성을 달리하는 `StringBuffer`와 `StringBuilder`, 그리고 기존 `Calendar` 클래스의 한계를 극복하기 위해 설계된 `java.time` 패키지의 시간 관련 클래스들의 내부 원리와 올바른 활용 방법을 알아봅니다.

---

# Why it matters

* **대규모 협업 및 코드 보호**: 패키지를 통해 클래스명 충돌을 방지하고 모듈을 통해 패키지 수준의 접근을 제한함으로써 캡슐화 수준을 한 단계 더 강화하고 외부 라이브러리 간의 의존성을 명확히 선언할 수 있습니다.
* **자바 런타임 최적화**: 모듈 시스템을 활용해 불필요한 패키지를 제외한 초경량화된 커스텀 JRE를 구성할 수 있으며, 핵심 내장 클래스들의 메모리 구조(예: 문자열 풀, 불변 객체, 스레드 동기화)를 정확히 이해함으로써 고성능/고안정성 자바 애플리케이션을 개발할 수 있습니다.

---

# Key Ideas

## 1. 패키지(Package)의 개념과 필요성

### 패키지의 정의
* **개념**: 물리적으로는 컴퓨터의 **디렉터리(Directory)** 구조와 1:1로 매핑되는 개념으로, 서로 관련 있는 클래스와 인터페이스의 컴파일된 바이트코드(`.class`) 파일들을 하나로 묶어 관리하는 단위입니다.
* **필요성**:
  * **이름 충돌 방지**: 대규모 프로젝트나 외부 라이브러리를 병합할 때, 이름이 동일한 클래스가 존재하더라도 패키지 경로가 다르면 서로 다른 클래스로 구분되므로 충돌이 발생하지 않습니다.
    * 예: `Project/FileIO/Tools.class`와 `Project/UI/Tools.class`는 서로 무관한 클래스로 취급됩니다.

### `import` 예약어 활용
* **FQN (Fully Qualified Name)**: 다른 패키지의 클래스를 사용할 때 패키지명까지 포함한 전체 이름을 다 명시해 주는 방식입니다.
  ```java
  java.util.Scanner scanner = new java.util.Scanner(System.in);
  ```
* **`import` 사용**: 소스 코드 최상단에 사용할 클래스를 명시하여 소스 내부에서는 클래스명만으로 호출할 수 있게 돕습니다.
  ```java
  import java.util.Scanner;
  Scanner scanner = new Scanner(System.in);
  ```
* **와일드카드(`*`) 사용의 규칙과 한계**:
  * `import java.util.*;` 형식으로 패키지 내의 모든 클래스를 가져올 수 있습니다.
  * **중요**: **와일드카드 `*`는 현재 패키지 내에 속한 클래스만을 지칭**하며, 그 하위 패키지(Sub-package)에 속한 클래스들은 함께 import되지 않습니다. (예: `import java.util.*;`을 해도 `java.util.zip.ZipFile` 클래스는 자동으로 import되지 않아 개별 지정이 필요함)

### 사용자 정의 패키지 선언
* 소스 파일의 첫 줄에 `package 패키지명;` 선언을 명시해야 합니다. 해당 파일 컴파일 시 명시한 패키지명 형태의 디렉터리에 클래스 파일이 자동 저장됩니다.

---

## 2. 자바의 모듈(Module) 시스템 (Java 9+)

### 모듈의 정의
* **개념**: 여러 개의 관련 패키지들을 하나로 묶어 관리하는 자바의 더 큰 소프트웨어 배포 단위입니다.

### 패키지 단위의 한계와 모듈의 도입 배경
1. **패키지 수준 접근 제어 불가**: 자바의 접근 지정자(Access Modifier)는 클래스 내부 또는 패키지 내부 단위로만 접근을 통제합니다. 따라서 외부 패키지에서는 사용하지 못하게 하고 특정 내부 패키지 간에만 공유하고 싶은 경우에도 `public`을 선언할 수밖에 없어 캡슐화가 깨지는 문제가 있었습니다.
2. **의존성 파악의 어려움**: 프로젝트가 거대해질수록 어떤 외부 패키지나 라이브러리에 의존하고 있는지 구조 파악이 어려웠습니다.
3. **JDK 경량화의 필요성**: 자바 9 이전에는 단순한 앱 하나를 실행하기 위해서도 전체 자바 API 패키지가 포함된 무거운 `rt.jar`를 통째로 로드해야 했습니다.

### 모듈 시스템의 효과
* **캡슐화 강화**: 모듈 내 특정 패키지만 외부로 노출(`exports`)하고, 나머지는 감춤으로써 완벽한 정보 은닉을 구현합니다.
* **의존성 명시**: `module-info.java` 설정 파일에 의존하는 모듈(`requires`)을 기술하여 빌드 시점에 유효성을 바로 검증할 수 있습니다.
* **JRE 경량화**: 필요한 모듈들만 조합하여 압축함으로써 소규모 디바이스나 클라우드 네이티브 환경에 맞는 경량화된 실행 환경(Custom JRE)을 구축할 수 있습니다.

### 패키지(Package) vs 모듈(Module) 차이점 요약

| 구분 | 패키지 (Package) | 모듈 (Module) |
| :--- | :--- | :--- |
| **단위** | 클래스와 인터페이스의 묶음 | 패키지의 묶음 |
| **선언 위치** | 각 클래스 파일 내부 (`package` 키워드) | 모듈 루트 디렉터리의 `module-info.java` 파일 |
| **접근 제한 수준** | 클래스/멤버 단위 (`public`, `protected`, `default`, `private`) | 패키지 단위 (`exports`, `opens` 등을 모듈 기술서에 선언) |
| **도입 시기** | 자바 초창기 (JDK 1.0) | Java 9 (JDK 9) |
| **핵심 목적** | 클래스의 논리적 그룹화, 이름 충돌 방지 | 대규모 라이브러리 관리, 강력한 캡슐화, 명시적 의존성 정의 |

---

## 3. 자바 주요 핵심 패키지와 클래스 분석

### 1) `java.lang` 패키지
자바 프로그램에 가장 기본이 되는 클래스들이 모여 있으며, 컴파일러가 소스 코드에 자동으로 `import java.lang.*;`을 추가해 주기 때문에 개발자가 별도로 import하지 않고 사용합니다.

#### 최상위 `Object` 클래스
* 자바의 모든 클래스는 자동으로 `Object` 클래스를 상속받습니다.
* **`boolean equals(Object obj)`**:
  * 두 객체가 물리적으로 동일한지(주소 비교, `==`와 동일) 판별합니다.
  * 인스턴스가 가지는 필드 값의 동등 비교를 위해 자식 클래스에서 오버라이딩하여 주로 재정의합니다.
* **`String toString()`**:
  * 객체를 설명하는 문자열을 반환합니다. 기본형은 `클래스이름@16진수해시코드`입니다.
  * 객체 상태를 사람이 읽을 수 있는 형태로 편리하게 출력하기 위해 오버라이딩하여 재정의합니다.
* **`Class<?> getClass()`**:
  * 실행 중(Runtime)인 객체의 실제 클래스 정보(Class 메타데이터)를 반환하는 메서드로, 동적 리플렉션이나 런타임 객체 구별 시에 사용됩니다.

#### `Wrapper` 클래스 (포장 클래스)
* 기본 자료형(byte, short, int, long, float, double, char, boolean)을 객체 형태로 다루기 위해 대응되도록 만든 클래스군입니다.

* **오토박싱(Auto-boxing) & 언박싱(Unboxing)**:
  * **오토박싱**: 기본 타입 값이 자동으로 해당하는 Wrapper 객체로 감싸지는 과정입니다. (예: `Integer num = 100;` -> 내부적으로 `Integer.valueOf(100)`으로 변환됨)
  * **언박싱**: Wrapper 객체에서 기본 타입 값이 자동으로 추출되는 과정입니다. (예: `int i = num;` -> 내부적으로 `num.intValue()`가 자동 실행됨)

* **주요 메서드**:
  * **`parse[Type]()`**: 문자열을 해당 기본 타입으로 파싱하여 반환합니다. (예: `Integer.parseInt("100")` -> `int` 반환)
  * **`valueOf()`**: 문자열이나 기본 타입을 Wrapper 객체로 생성하여 반환합니다. 내부적으로 자주 쓰이는 캐시(Integer Cache: -128 ~ 127 등)를 타기 때문에 `new Integer()`로 매번 생성하는 것보다 **메모리 효율이 우수하여 사용이 강력히 권장**됩니다.

#### `Math` 클래스
* 수학적 계산을 처리하는 유틸리티 클래스입니다.
* **구조적 특징**: 생성자가 `private` 접근 제한으로 설정되어 있어 `new Math()`와 같이 인스턴스화할 수 없으며, 모든 멤버와 메서드가 `static`으로 정의되어 있습니다.
* **주요 메서드**: `abs()`, `max()`, `min()`, `ceil()` (올림), `floor()` (내림), `round()` (반올림), `pow()` (거듭제곱), `sqrt()` (제곱근), `random()` ($0.0 \le \text{난수} < 1.0$)

#### `String` 클래스와 불변성(Immutability)
* **불변 객체(Immutable Object)**: 자바의 String 객체는 한 번 생성되면 내부 문자열 값을 변경할 수 없습니다. 문자열 결합이나 수정을 실행하면 원본 객체가 바뀌는 것이 아니라, **메모리에 완전히 새로운 String 객체가 생성**됩니다.
* **문자열 풀 (String Pool)**:
  * 힙(Heap) 영역 내부의 특수한 메모리 공간입니다.
  * 리터럴 방식을 사용하여 문자열을 대입하면(`String s1 = "Java";`), 동일한 내용의 문자열을 생성할 때 새로 메모리를 잡지 않고 문자열 풀에 이미 존재하는 인스턴스를 공유(참조)합니다.
  * 반면 `new String("Java")`와 같이 생성자를 통하면 문자열 풀을 거치지 않고 무조건 힙 영역에 매번 독립적인 객체를 할당합니다.
  ```java
  String s1 = "Java";
  String s2 = "Java";
  String s3 = new String("Java");
  
  System.out.println(s1 == s2);      // true (주소 동일 - 문자열 풀 공유)
  System.out.println(s1 == s3);      // false (주소 다름 - new 생성)
  System.out.println(s1.equals(s3)); // true (내용 동일)
  ```

#### `StringBuffer` vs `StringBuilder`
String의 불변성 때문에 대량의 문자열 조작(+ 연산자 남발) 시 메모리가 낭비되는 문제를 해결하기 위해 제공되는 가변(Mutable) 문자열 처리 클래스입니다.

* **`StringBuffer`**:
  * 내부적으로 동기화(Synchronization) 처리가 되어 있습니다.
  * **스레드 안전(Thread-Safe)**하므로 멀티스레드 환경에서 데이터 오염 없이 안전하게 작동합니다.
  * 단, 동기화에 따른 락(Lock) 획득 비용으로 성능 오버헤드가 있습니다.
* **`StringBuilder`**:
  * 동기화 처리가 배제되어 있습니다.
  * **싱글스레드 환경에 적합**하며, StringBuffer에 비해 훨씬 빠른 동작 성능을 발휘합니다. 일반적인 로컬 변수 수준의 문자열 조합에는 StringBuilder를 사용하는 것이 좋습니다.

---

### 2) `java.util` 패키지

#### `Calendar` 클래스
* 자바에서 오래 사용된 날짜 및 시간 조작 클래스입니다.
* **구조적 한계**:
  * 추상 클래스이므로 `Calendar.getInstance()` 정적 메서드로 런타임 장비 설정에 맞는 인스턴스를 생성해야 합니다.
  * **월(Month) 계산 주의**: `Calendar.MONTH` 값은 `0`이 1월을 뜻하고 `11`이 12월을 뜻하기 때문에 계산할 때 항상 `+1` 보정이 필수입니다.
  * **가변 객체(Mutable)**: 내부 시간 정보가 쉽게 오염될 수 있고 멀티스레드 환경에서 안전하지 못합니다.

#### `StringTokenizer` 클래스
* 문자열을 특정 구분자(Delimiter) 기준으로 쪼개어 토큰으로 순차 추출해 주는 유틸리티 클래스입니다.
* `String.split()` 정규식 분리에 비해 다용도 제어는 어렵지만, 단순 구분자로 빠르게 순회 처리 시 성능 오버헤드가 적습니다.
* **주요 메서드**: `hasMoreTokens()`, `nextToken()`, `countTokens()`

---

### 3) `java.time` 패키지 (Java 8 이후)
`Calendar` 클래스의 가변성 문제, 월 인덱싱 오류 등의 문제를 완벽히 극복하고 직관적인 설계를 위해 새롭게 구성된 현대 자바 표준 날짜/시간 API입니다. 이 패키지의 모든 클래스는 **불변 객체(Immutable Object)**로 설계되어 안전합니다.

* **`LocalDate`**: 날짜 정보만 저장 (`LocalDate.now()`, `LocalDate.of(2026, 4, 19)`)
* **`LocalTime`**: 시간 정보만 저장 (`LocalTime.now()`)
* **`LocalDateTime`**: 날짜와 시간 모두를 조작 (`LocalDateTime.now()`)
* **`DateTimeFormatter`**: 날짜/시간 인스턴스를 지정한 포맷의 문자열로 변환하거나 그 반대로 문자열을 날짜 객체로 파싱할 때 사용하는 패턴 정의 클래스입니다.
  ```java
  LocalDateTime now = LocalDateTime.now();
  DateTimeFormatter f = DateTimeFormatter.ofPattern("yyyy년 M월 d일 a h시 m분");
  String formatted = now.format(f); // 지정 포맷 문자열 획득
  ```

---

# Citations
* [09객체지향 - 모듈 패키지.pdf](../../../raw/notes/java/09객체지향 - 모듈 패키지.pdf)
