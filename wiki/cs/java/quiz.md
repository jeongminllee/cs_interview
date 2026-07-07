---
type: Study Note
title: "Java Practical Programming Quiz (자바 프로그래밍 실무 퀴즈 풀이 및 심층 분석)"
description: "배열, 반복문, 예외 처리, 컬렉션 프레임워크 및 정렬 알고리즘을 종합적으로 평가하는 5가지 실무 퀴즈에 대한 단계별 알고리즘 설계와 완성된 자바 소스 코드를 제공합니다."
tags: [java, quiz, algorithm, exception-handling, sorting, collection-framework]
timestamp: 2026-06-19
status: active
---

# Summary
본 문서는 자바 프로그래밍의 기초 논리와 실무적 예외 처리, 그리고 핵심 알고리즘(최대값 검색, 화폐 분할 그리디 알고리즘, 예외 검증 계산기, 자료구조를 통한 중복 제거, 중첩 루프 정렬)을 검증하는 5가지 퀴즈에 대한 해답과 해설을 제공합니다. 각 퀴즈별 알고리즘적 논리, 예외 상황에 대한 대비책, 그리고 동작 가능한 완전한 자바 소스 코드가 포함되어 있습니다.

---

# Quiz 1: 최고 득점자 구하기 (Highest Score Finder)

### 1. 문제 정의
- **설명**: 제시된 자바 프로그래밍 시험 응시자 9명의 이름과 점수 배열을 이용하여 최고 득점을 기록한 1등 수험생의 이름과 점수를 출력하는 프로그램을 작성하십시오.
- **주어진 입력 데이터**:
  - 이름: `Elena`, `Suzie`, `John`, `Emily`, `Neda`, `Kate`, `Alex`, `Daniel`, `Sam`
  - 점수: `65`, `74`, `23`, `75`, `68`, `96`, `88`, `98`, `54`
- **실행 결과 예시**:
  ```text
  1등: Daniel(98점)
  ```
  *(참고: 원안 PDF의 실행 결과 이미지에는 'Diniel'로 타이핑 오류가 있으나, 논리상 수험생 Daniel의 점수가 98점으로 최고점이므로 정답 코드에서는 원본 데이터 Daniel 매핑을 준수합니다.)*

### 2. 해결 논리 및 CS 원리
- **최대값 검색 알고리즘 (Max Value Search)**:
  - 컴퓨터는 인간처럼 배열 전체를 한눈에 볼 수 없으므로 순차 탐색(Sequential Search)을 수행해야 합니다.
  - 임시 최대값 변수 `maxScore`와 1등 인덱스 변수 `maxIndex`를 각각 가장 첫 번째 원소(인덱스 0)의 값과 0으로 초기화합니다.
  - 인덱스 1부터 배열의 마지막 원소까지 루프를 순회하면서, 현재 원소의 점수가 `maxScore`보다 크다면 `maxScore`를 현재 점수로 업데이트하고 `maxIndex` 역시 현재 인덱스로 갱신합니다.
  - 시간 복잡도는 배열 크기 $N$에 대해 단 한 번 순회하므로 $O(N)$을 가집니다.

### 3. 소스 코드 구현
```java
public class HighestScoreFinder {
    public static void main(String[] args) {
        // 1차원 병렬 배열 구조 설계
        String[] names = {"Elena", "Suzie", "John", "Emily", "Neda", "Kate", "Alex", "Daniel", "Sam"};
        int[] scores = {65, 74, 23, 75, 68, 96, 88, 98, 54};

        // 초기 기준 설정 (인덱스 0번째 학생을 가상 최고점으로 설정)
        int maxScore = scores[0];
        int maxIndex = 0;

        // 인덱스 1부터 끝까지 비교 루프 실행
        for (int i = 1; i < scores.length; i++) {
            if (scores[i] > maxScore) {
                maxScore = scores[i]; // 최대 점수 업데이트
                maxIndex = i;         // 최고점 학생 인덱스 업데이트
            }
        }

        // 결과 출력
        System.out.println("1등: " + names[maxIndex] + "(" + maxScore + "점)");
    }
}
```

---

# Quiz 2: 화폐 단위로 분리하기 (Currency Divider)

### 1. 문제 정의
- **설명**: 키보드를 통해 정수 금액을 입력받은 후, 지정된 화폐 단위에 맞춰 필요한 화폐 매수를 큰 단위부터 분리하여 상세 내역을 표시하는 프로그램을 작성하십시오.
- **화폐 규격**: `50000원`, `10000원`, `5000원`, `1000원`, `500원`, `100원`, `50원`, `10원`
- **실행 결과 예시** (입력: `1235678`):
  ```text
  금액을 입력하세요: 1235678
  화폐 단위로 분리한 결과:
  50000원: 24개(1200000)
  10000원: 3개(30000)
  5000원: 1개(5000)
  500원: 1개(500)
  100원: 1개(100)
  50원: 1개(50)
  10원: 2개(20)
  원 단위 이하 금액: 8원
  ```

### 2. 해결 논리 및 CS 원리
- **그리디 알고리즘 (Greedy Algorithm)**:
  - 최소 개수의 지폐 및 동전으로 거스름돈을 교환하는 대표적인 탐욕법 유형입니다.
  - 화폐 단위가 서로 배수 관계(50000은 10000의 배수, 10000은 5000의 배수 등)를 이루기 때문에, 항상 **가장 큰 화폐 단위부터 최대한 채우는 방식**이 수학적 최적해를 보장합니다.
  - 매 반복 루프마다 `현재 금액 / 화폐 단위` 연산의 몫을 통해 필요한 화폐 수량을 구하고, `현재 금액 % 화폐 단위` 연산의 나머지를 취하여 다음 화폐 단위 계산용 입력값으로 재대입합니다.

### 3. 소스 코드 구현
```java
import java.util.Scanner;

public class CurrencyDivider {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("금액을 입력하세요: ");
        int money = sc.nextInt();
        
        // 내림차순 정렬된 화폐 단위 배열
        int[] units = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
        
        System.out.println("화폐 단위로 분리한 결과:");
        
        for (int unit : units) {
            int count = money / unit; // 몫 계산 (해당 화폐 개수)
            if (count > 0) {
                int totalValue = count * unit;
                System.out.println(unit + "원: " + count + "개(" + totalValue + ")");
            }
            money = money % unit; // 나머지 갱신
        }
        
        // 10원 단위 미만의 잔돈 처리
        System.out.println("원 단위 이하 금액: " + money + "원");
        
        sc.close();
    }
}
```

---

# Quiz 3: 계산기 구현하기 (Calculator with Exception Handling)

### 1. 문제 정의
- **설명**: 키보드로부터 사칙연산자(`+`, `-`, `*`, `/`) 하나와 정수 두 개를 순차적으로 입력받아 계산 결과를 출력하는 애플리케이션을 구현하십시오. 이 과정에서 정수가 아닌 값을 넣거나 분모에 0을 입력하는 경우 예외 처리를 수행하고 즉시 프로그램을 종료해야 합니다.
- **예외 요구 사항**:
  - 실수를 입력할 경우 -> `"실수는 입력하면 안됩니다."` 출력 후 종료.
  - 0으로 나누려고 할 경우 -> `"0으로 나눌 수 없습니다."` 출력 후 종료.
- **실행 결과 예시**:
  ```text
  계산 입력(+, -, *, /) : -
  첫 번째 숫자 입력 : 33
  두 번째 숫자 입력 : 55
  계산 결과 : -22
  ```

### 2. 해결 논리 및 CS 원리
- **자바 예외 처리 아키텍처 (Exception Architecture)**:
  - `Scanner.nextInt()` 수행 중 사용자가 정수가 아닌 실수(예: 3.14)나 문자열을 입력하면 `InputMismatchException`이 발생합니다.
  - 정수형 나눗셈 연산 시 나누는 수(분모)가 0인 상태에서 `/` 또는 `%` 연산을 시도하면 JVM은 런타임에 `ArithmeticException` 예외를 던집니다.
  - `try-catch` 블록을 통하여 각각의 비정상 예외 상황을 조기에 가로채어 적합한 안내 문구를 송출하고, 시스템 크래시 없이 프로그램을 명시적으로 안전하게 탈출시킵니다.

### 3. 소스 코드 구현
```java
import java.util.InputMismatchException;
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        try {
            System.out.print("계산 입력(+, -, *, /) : ");
            char op = sc.next().charAt(0);
            
            System.out.print("첫 번째 숫자 입력 : ");
            int num1 = sc.nextInt(); // 실수 입력 시 InputMismatchException 발생
            
            System.out.print("두 번째 숫자 입력 : ");
            int num2 = sc.nextInt(); // 실수 입력 시 InputMismatchException 발생
            
            int result = 0;
            switch (op) {
                case '+':
                    result = num1 + num2;
                    break;
                case '-':
                    result = num1 - num2;
                    break;
                case '*':
                    result = num1 * num2;
                    break;
                case '/':
                    // num2가 0인 경우 ArithmeticException 유도 및 예외 블록 처리
                    result = num1 / num2; 
                    break;
                default:
                    System.out.println("잘못된 연산자입니다.");
                    return;
            }
            
            System.out.println("계산 결과 : " + result);
            
        } catch (InputMismatchException e) {
            System.out.println("실수는 입력하면 안됩니다.");
        } catch (ArithmeticException e) {
            System.out.println("0으로 나눌 수 없습니다.");
        } finally {
            sc.close(); // 자원 유실 방지
        }
    }
}
```

---

# Quiz 4: 중복값 제거하기 (Duplicate Remover)

### 1. 문제 정의
- **설명**: 키보드를 통해 정수 10개를 한 줄로 공백 단위로 입력받은 후, 중복을 제거한 고유한 정수 데이터들만 입력되었던 원래 순서대로 출력하는 프로그램을 작성하십시오.
- **예외 사항**: 정수가 아닌 타입이 입력될 시 `"입력 값 오류"` 메시지를 띄우고 종료합니다.
- **실행 결과 예시**:
  ```text
  정수 10개 입력: 1 2 2 3 4 4 5 1 6 7
  결과: 1 2 3 4 5 6 7
  ```

### 2. 해결 논리 및 CS 원리
- **Set 컬렉션의 성질 및 순서 보존**:
  - `Set` 인터페이스는 고유한 원소의 삽입만을 보장하고 중복 값을 자동으로 무시합니다.
  - 보편적인 `HashSet`은 내부적으로 해시 맵(Hash Map) 버킷을 활용하므로 입력 순서(Insertion Order)가 보존되지 않고 뒤섞입니다.
  - 중복은 배제하면서 입력받은 순서 그대로 유지하기 위해 해시 테이블과 양방향 연결 리스트(Doubly-linked List)가 결합된 **`LinkedHashSet` 자료구조**를 사용합니다.

### 3. 소스 코드 구현
```java
import java.util.LinkedHashSet;
import java.util.Scanner;
import java.util.InputMismatchException;

public class DuplicateRemover {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 입력 순서 보존 및 중복 필터링을 위한 Set 선언
        LinkedHashSet<Integer> uniqueSet = new LinkedHashSet<>();
        
        System.out.print("정수 10개 입력: ");
        try {
            for (int i = 0; i < 10; i++) {
                int value = sc.nextInt(); // 정수가 아닐 시 InputMismatchException 트리거
                uniqueSet.add(value);
            }
            
            // 결과 출력
            System.out.print("결과: ");
            for (int val : uniqueSet) {
                System.out.print(val + " ");
            }
            System.out.println();
            
        } catch (InputMismatchException e) {
            System.out.println("입력 값 오류");
        } finally {
            sc.close();
        }
    }
}
```

---

# Quiz 5: 숫자 정렬하기 (Number Sorter)

### 1. 문제 정의
- **설명**: 정수 5개를 임의로 입력받은 뒤, API(예: `Arrays.sort()`)를 사용하지 않고 중첩 반복문(Nested Loops)을 활용하여 내부 값들을 오름차순(Ascending order)으로 직접 정렬하여 출력하는 프로그램을 작성하십시오.
- **실행 결과 예시**:
  ```text
  숫자 5개 입력: 7 9 1 6 4
  정렬 결과: 1 4 6 7 9
  ```

### 2. 해결 논리 및 CS 원리
- **거품 정렬 (Bubble Sort) 및 스왑 (Swap) 메커니즘**:
  - 인접한 두 원소를 비교하여 정렬 순서가 맞지 않으면 서로 교환하는 방식으로, 바깥쪽 루프가 한 번 돌 때마다 가장 큰 수가 우측 끝(제자리)으로 밀려납니다.
  - **스왑(Swap) 연산**: 임시 보관용 변수 `temp`를 경유하여 두 변수의 메모리 레퍼런스 값을 뒤바꿉니다.
    ```java
    int temp = arr[j];
    arr[j] = arr[j+1];
    arr[j+1] = temp;
    ```
  - 배열 길이가 $N$일 때 바깥 루프는 $N-1$번, 안쪽 루프는 $N-1-i$번 돌며 최종 시간 복잡도는 $O(N^2)$이 소요됩니다.

### 3. 소스 코드 구현
```java
import java.util.Scanner;

public class NumberSorter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];

        System.out.print("숫자 5개 입력: ");
        for (int i = 0; i < 5; i++) {
            arr[i] = sc.nextInt();
        }

        // 중첩 반복문을 이용한 버블 정렬 알고리즘 수행
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - 1 - i; j++) {
                // 인접 원소를 비교하여 앞의 값이 더 크면 위치 교환 (Swap)
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        // 결과 출력
        System.out.print("정렬 결과: ");
        for (int val : arr) {
            System.out.print(val + " ");
        }
        System.out.println();
        
        sc.close();
    }
}
```

# Related Concepts
- **Time Complexity (시간 복잡도)**: 알고리즘의 실행 속도가 입력량 증가에 따라 어떻게 증가하는지 나타내는 지표로, 버퍼 정렬은 $O(N^2)$인 반면 자바 `Arrays.sort()`는 Dual-Pivot Quicksort를 사용하여 평균 $O(N \log N)$의 성능을 냅니다.
- **Java Collection Framework**: 자바에서 자료구조를 효율적으로 다루기 위해 표준화한 프레임워크로, List, Set, Queue, Map 계열의 다앙한 인터페이스 및 구현 구현체들을 통칭합니다.

# Citations
* [Quiz.pdf](../../../raw/notes/java/Quiz.pdf)
