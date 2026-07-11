---
type: Study Note
title: "정보처리기사 실기 개인 학습 기록 (260710)"
description: "2026-07-10일 자 정보처리기사 실기 퀴즈 풀이 및 오답 분석 기록 일지"
tags: [engineer-info-processing, study-log]
timestamp: 2026-07-10
status: active
---

# Summary
2026-07-10일 자 정보처리기사 실기 퀴즈 풀이와 오답, 그리고 15년 차 강사 에이전트의 상세 피드백을 기록한 일지입니다.

---

## 47. C언어 - 포인터 매개변수와 매개변수 전달 방식 (Call by Value vs Call by Reference)

### 문제
아래 C 코드를 실행했을 때 출력되는 결과를 쓰시오. (단, 1라인의 `ffinclude (stdio.h)` 등 OCR 오타는 `#include <stdio.h>`로 보정하여 풀이한다.)
```c
#include <stdio.h>
void fn(int *a, int b){
    int temp=0;
    temp=*a;
    *a=b;
    b=temp+1;
}
int main(){
    int a = 10, b= 5;
    fn(&a, b);
    printf("%d %d\n", a, b);
    return 0;
}
```

### 정답 및 풀이 결과
* **작성한 답**: `5 5` (Call by Value와 Call by Reference의 동작 메커니즘을 정확히 파악하여 풀이 성공)
* **모범 답안**: **`5 5`**
* **결과**: **정답 (100% 매칭 및 계산 과정 완벽)**

### 핵심 해설
* **매개변수 전달 방식의 비교**:
  1. **`fn(&a, b)` 호출 시**:
     * 첫 번째 인자 `&a`는 변수 `a`의 **주소값**을 전달합니다. (포인터 전달 $\rightarrow$ Call by Reference 형태)
     * 두 번째 인자 `b`는 변수 `b`의 **값(`5`)**을 복사해서 전달합니다. (값 전달 $\rightarrow$ Call by Value 형태)
  2. **함수 `fn(int *a, int b)` 내부 연산**:
     * 매개변수 `a`는 포인터 변수로서 `main`의 변수 `a` 메모리 공간을 직접 가리킵니다.
     * 매개변수 `b`는 `main`의 `b`와는 메모리 영역이 완전히 독립된 임시 로컬 변수입니다 (값 `5`만 복사됨).
     * `temp = *a;` $\rightarrow$ `temp = 10` (가리키는 곳의 값 대입)
     * `*a = b;` $\rightarrow$ `*a = 5` (가리키는 곳 즉, `main`의 `a` 메모리 공간에 `5`를 저장 $\rightarrow$ **`main`의 `a`가 5로 변경**)
     * `b = temp + 1;` $\rightarrow$ 로컬 변수 `b`에 `11`을 대입합니다. 이 연산은 `main`의 `b` 메모리와 전혀 무관하므로 **`main`의 `b`는 여전히 `5`**로 남습니다.
  3. **출력 단계**:
     * 함수 수행 완료 후 `main`에서 `printf("%d %d\n", a, b)`가 가동되면, 최종적으로 바뀐 `a` 값인 **`5`**와 원본 그대로인 `b` 값인 **`5`**가 출력됩니다.

---

# Related Concepts
- [정보처리기사 실기 학습 대시보드](index.md)
- [[6과목] 프로그래밍 언어 활용](book1/subject06.md)
- [[11과목] 응용 소프트웨어 기초 기술 활용](book2/subject11.md)
- [[1과목] 요구사항 확인](book1/subject01.md)
- [[5과목] 인터페이스 구현](book1/subject05.md)
- [[4과목] 통합 구현](book1/subject04.md)
- [[9과목] 소프트웨어 개발 보안 구축](book2/subject09.md)
- [[10과목] 애플리케이션 테스트 관리](book2/subject10.md)
