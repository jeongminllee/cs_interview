---
type: Study Note
title: "Final 모의고사 09회 (문제+해설)"
description: "수제비 2026 정보처리기사 실기 final 모의고사 09회 문제+해설 본문 추출본"
tags: [engineer-info-processing, final-mock-exam, exam-09]
timestamp: 2026-06-19
status: active
---

# Final 모의고사 09회 (문제+해설)

## Page 231

1 8 다음 SQL 쿼리의 결과를 쓰시오.
SELECT COUNT(*)
FROM EMP
WHERE EMPNO)100 AND SAL)3000 OR EMPNO=200;
[EMP]
EMPNO SAL
100 1000
200 3000
300 1500
20 다음에서 설명하는 디자인 패턴은 무엇인지
[보기]에서 골라서 쓰시오.
• 구체적인 클래스에 의존하지 않고 서로 연관
되거나 의존적인 객체들의 조합을 만드는 인
터페이스를 제공하는 패턴으로 Kit라고 불림 [확인 필요]
• 패턴을 통해 생성된 클래스에서는 사용자에게
인터페이스(API)를 제공하고, 구체적인 구현은
Concrete Product 클래스에서 이루어짐
[보기]
Builder, Prototype, Factory Method, Abstract
Factory, Singleton, Bridge, Decorator, Facade,
Flyweight, Proxy, Composite, Adapter
다음에서 설명하고 있는 보안 공격기법을 [보
기]에서 골라서 쓰시오.
• 특정 타깃을 목표로 하여 다양한 수단을 통한
지속적이고 지능적인 맞춤형 공격기법이다.
• 공격기법은 침투一검색—수집一유출 4단계
의 절차로 진행된다.
[보기]
@ 사회공학 기법 © Watering Hole
© MITM @XDR
@ Replace Attack @ Key Logger
©APT @ NAT
® HeartBleed ® Smishing
2024년 기출문제 1 회 231
## Page 232

서베昌
수제비
2O2U 기출문제 2히 으
01 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class Soojebi {
02 public static void check(int[ ] a, int[ ] b) {
03 if(a==b)
04 System.out.print("O");
05 else
06 System.out.print("N");
07 }
08 public static void main(String[ ] args) {
09 int a[ ]=new int[ ] {1, 2, 3, 4};
10 int b[ ]=new int[ ] {1, 2, 3, 4};
11 int c[ ]=new int[ ] {1, 2, 3};
12 check(a, b);
13 check(b, c);
14 check(a, c);
15 }
16 }
02 사원 테이블과 부서 테이블은 다음과 같다.
다음 조건에 부합하는 SQL문을 작성하고자 [확인 필요]
할 때, 빈칸에 들어갈 SQL 쿼리를 쓰시오.
사원 테이블 [사원번호(PK), 이름, 나이, 부서]
부서 테이블 [사원번호(PK), 이름, 주소, 나이]
⑴ 신입사원이 입사해서 부서 테이블에 추가
하는 SQL 문 작성
INSERT INTO 부서(사원번호, 이름, 주소, 나이)
① (100, '이순신', '서울', 26);
(2) 신입사원을 검색하면서 사원 테이블에 추
가하는 SQL 문 작성
INSERT INTO 사원(사원번호, 이름, 나이, 부서)
② 사원번호, 이름, 나이, '기획' FROM 부서;
(3) 사원이 퇴사해서 삭제해야 하는 SQL 문
작성
DELETE ③ 사원
WHERE 사원번호=100;
다음에서 설명하는 데이터베이스 관련 기법
은 무엇인지 쓰시오.
• 정규화된 엔터티, 속성, 관계에 대해 성능 향상
과 개발 운영의 단순화를 위해 중복, 통합, 분
리 등을 수행하는 데이터 모델링의 기법이다.
• 정규화의 원칙을 일부러 깨는 작업이기 때문
에, 정규화를 배반하는 것처럼 보일 수 있지만,
정규화와 상반되는 개념이 아니라, 정규화를
기본적으로 따르면서도 성능 최적화를 위해
필요한 경우에 선택적으로 적용하는 기법이다.
⑷ 특정 부서의 데이터를 수정하는 SQL 문
작성
UPDATE 사원 ④ 부서 = '개발'
WHERE 부서 = '기획';
①____________________________________________
②____________________________________________
③____________________________________________
④______________________________________ ______
232 수제비 정보처리기사 실기 FINAL 모의고사
## Page 233

04 다음 릴레이션의 카디널리티와 차수를 구하
시오.
학번 이름 나이 학과
2025111 홍길동 30 컴퓨터
2025112 장길산 31 기계
2025113 임꺽정 34 경영
2025114 이철수 28 전기
2025115 김영희 26 영어영문
① 카디널리티:___________________________
② 차수:_________________________________
05 다음에서 설명하는 보안 기술은  무엇인지 쓰
시오.
• 기업에서 공용 인터넷망을 회사 사설 인터넷
망으로 사용할 수 있는 VPN 기술이다 .
• IP 계층(3계층)에서 무결성과 인증을 보장하는
인증 헤더(AH)와 기밀성을 보장하는 암호화
(ESP)를 이용한 보안 기술이다 .
07 des에 한계성과 성능 문제를 극복하기 위 [확인 필요]
해 NIST에서 개발한 블록 알고리즘으로 [확인 필요]
128bit의 블록 크기를 가지며 키 길이에 따라 [확인 필요]
128bit, 192bit, 256bit로 분류할 수 있는 대칭 [확인 필요]
키 암호화 알고리즘은 무엇인지 쓰시오.
08 다음은 패킷 교환 방식의 세부 유형에 대한
설명이다. 괄호 ( ) 안에 들어갈 패킷 교환
방식의 세부 유형을 쓰시오.
• ( ① )방식은 패킷이 전송되기 전에 송 ■
수신 스테이션 간의 논리적인 통신 경로를 미
리 설정하는 방식으로 목적지 호스트와 미리
연결 후 통신하는 연결형 교환 방식이다.
• ( ② )방식은 연결 경로를 확립하지 않고
각각의 패킷을 순서에 무관하게 독립적으로
전송하는 방식으로 헤더를 붙여서 개별적으로
전달하는 비 연결형 교환 방식이다.
06 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 def fn(x, y):
02 result=0;
03 for i in range(len(x)):
04 s=x[i:i 十 len(y)]
05 if s==y:
06 result+=1;
07 return result
08
09 str三 "abdcabcabca"
10 p1="ca"
11 p2="ab"
12 print(f'ab{fn(str, p1)}' f'ca{fn(str, p2)}')
①___________________________________________________________________________________
②___________________________________________________________________________________
09 다음은 응집도 유형에 대한 설명이다. 괄호
( ) 안에 공통으로 들어갈 응집도 유형을
쓰시오.
•( )응집도는 이전 기능의 출력을 다음 기
능의 입력으로 사용하는 경우의 응집도이다.
•( )응집도는 한 기능이 작업을 수행한 결
과가 다음 기능의 입력으로 연결되는 형태의
응집도로 기능 간의 의존성이 존재하기 때문
에, 모듈의 기능들이 논리적으로 밀접하게 연
결되어 있다.
2024년 기출문제 2회 233
## Page 234

10 다음에서 설명하는 디자인 패턴의 이름을 쓰
시오.
• 컬렉션(예: 배열, 리스트) 내부구조를 노출하지
않고, 그 집합체 안에 들어있는 모든 요소를
순차적으로 탐색할 수 있는 디자인 패턴이다.
• 컬렉션 내부에서 현재 위치를 추적하는 방식
이 커서와 유사하므로 "Cursor 패턴"이라고도
불린다.
다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 #include <stdio.h>
02 int main() {
03 int arr[3][3]={1, 2, 3, 4, 5, 6, 7, 8, 9};
04 int* parr[2]={arr[1], arr[2]};
05 printf("%d", parr[1][1]+*(parr[1]十2)十**parr);
06 return 0;
07 }
RIP 알고리즘을 이용하여 라우터 A에서 라우
터 日가지 어떤 경로를 거쳐야 최단 경로로 갈
수 있을지 경로의 순서를 쓰시오.
A —(
프로세스의 도착시간과 서비스 시간은 다음
과 같다. SRT 스케줄링을 적용할 때 평균 대
기시간을 구하시오.
프로세스 도착시간 서비스 시간
P1 0 8
P2 1 4
P3 2 9
P4 3 5
다음은 자바 코드이다. 출력 결과를 쓰시오.
01 interface A {
02 int sum(int[ ] a, boolean odd);
03 }
04 class B implements A {
05 public int s니m(int[ ] a, boolean odd) { [확인 필요]
06 int result=O;
07 for(int i=0; Ka.length; i+十) {
08 if((odd&&a[i]%2 != 0) II (!odd&&a[i]%2==0))
09 result+三 a[i];
10 }
11 return result;
12 }
13 }
14
15 class Soojebi {
16 public static void main(String[ ] args) {
17 int a[ ]={1, 2, 3, 4, 5, 6,7, 8, 9};
18 Bx=newB();
19 System,out.print(x.sum(a, true)+", " + x.sum(a, false));
20 }
21 }
234 수제비 정보처리기사 실기 FINAL 모의고사
## Page 235

다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 void fn(char *d, const char *s) {
03 while(*s) {
04 *d=*s;
05 d+十;
06 s+ +;
07 }
08 *d='\0';
09 }
10 int main() {
11 const char* str1="first";
12 char str2[50]="teststring";
13 int result=0;
14 int i;
15
16 fn(str2, str1);
17 for(i=0; str2[i] !=\0'; i十+) {
18 result 十 긔;
19 }
20 printf("%d", result);
21 return 0;
22 }
16 다음이 설명하는 소프트웨어 모듈 관련 용어
는 무엇인지 쓰시오.
어떤 모듈이 다른 모듈의 내부 논리 조직을 제
어하기 위한 목적으로 제어 신호를 이용하여 통
신하는 경우의 결합도이다.
) Coupling
다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class Soojebi {
02 public static String fn(String str, int index, boolean[ ] seen) {
03 if(index<0) return "";
04 char c=str.charAt(index);
05 String res니t=fn(str, index-1, seen); [확인 필요]
06 if(!seen[c]) {
07 seen[c] 三 true;
08 return c+result;
09 }
10 return result;
11 }
12 public static void main(String[ ] args) {
13 String str="abacabcd";
14 int length=str.length( );
15 booleanf ] seen=new boolean[256];
16 System.out.print(fn(str, length-1, seen));
17 }
18 }
2024년 기출문제 2회 235
## Page 236

18 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 void swap(int a, int b) {
03 int t=a;
04 a=b;
05 b긔;
06 }
07 int main() {
08 int a=11;
09 int b=19;
10 swap(a, b);
11 switch(a) {
12 case 19:
13 b+=1;
14 case 11:
15 b 十 =2;
16 default:
17 b 十 =3;
18 }
19 print!("%d", a-b);
20 return 0;
21 }
다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 #include <stdio.h>
02
03 struct node {
04 int n1;
05 struct node *n2;
06 };
07
08 int main() {
09 struct node *head=NULL;
10 struct node a 三 {10, 0};
11 struct node b={20, 0};
12 struct node c={30, 0};
13 head 三 & a;
14 a.n2=&b;
15 b.n2=&c;
16 printf("%d", head—>n2—>n1);
17 return 0;
18 }
20 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 def fn(str, k):
02 s=str.split(T)
03 return s[k]
04
05 str="ITISTESTSTI기 NG" [확인 필요]
06 k=3
07 result=fn(str, k)
08 print(result)
236 수제비 정보처리기사 실기 FINAL 모의고사
## Page 237

수제비 FINAL
기출문제 3히스
01 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class Soojebi {
02 static void func(String[ ] sM, int size) {
03 for (int i=1; i<size; i++) {
04 if (sM[i-1].equals(sM[i])) {
05 System.out.print("O");
06 }
07 else {
08 System.out.print("N");
09 }
10 }
11 for (String m : sM) {
12 System.out.print(m);
13 }
14 }
15 public static void main(String[ ] args) {
16 String[ ] sM 三 new String[3];
17 sM[0]="A";
18 sM[1]="A";
19 sM[2]=new String("A");
20 func(sM, 3);
21 }
22 }
02 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 def func(x):
02 for i in range(len(x)/ /2):
03 x[i], x[—i—1] 三><[—i—1], x[i]
04
05 x=[1, 2, 3, 4, 5, 6]
06 func(x)
07 print(sum(x[::2])—sum(x[1::2]))
03 다음은 employees, projects 테이블이다.
SQL 결과에서 괄호 ( )에 들어갈 값을 쓰
시오.
[employees] 테이블
[projects] 테이블
id first_name last_name deptjd
1 John Doe 10
2 Jim Carry 20
3 Rachel Redmond 10
[SQL]
deptjd name
10 Alpha
20 Beta
30 Charlie
select count(*)
from employees e join projects p
on e.dept_id=p.dept_id
where p.name in(select name
from projects
where dept_id in(select deptjd
from employees
group by deptjd
having count(*)<2));
[결과]
count(*)
( )
2024년 기출문제 3회 237
## Page 238

04 3개의 프레임을 수용할 수 있는 주기억장치가
있으며, 초기에는 모두 비어 있다고 가정한다.
다음 순서로 페이지 참조가 발생할 때, LRU
알고리즘 사용 시, 페이지 결함(Page Fa니t) 발 [확인 필요]
생 횟수를 쓰시오.
페이지 참조 순서: 7, 0, 1, 2, 0, 1, 2, 7, 1, 0, 2,
1. 7, 0, 2, 1, 7
05 다음에서 설명하는 공격기법을 한 단어로 쓰
시오.
출발지 주소를 공격 대상의 ip로 변조하여 네트 [확인 필요]
워크 전체에게 ICMP Echo 패킷을 직접 브로드
캐스팅(Directed Broadcasting)하여 타겟 시스템을
마비시키는 공격
07 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 int increase(){
03 static int x=0;
04 x+=2;
05 return x;
06 }
07
08 int main() {
09 int x=0;
10 int sum=0;
11 inti=O;
12 for(i=0; i<4; i++){
13 x++;
14 sum+三 increase( );
15 }
16
17 printf("%d", sum);
18 return 0;
19 }
06 다음은 GoRGang of Four) 디자인 패턴과 관
련된 문제이다. 괄호 ( ) 안에 들어갈 용어
를 쓰시오.
( ) 패턴은 클래스나 객체들이 상호 작
용하는 방법과 역할 분담을 다루는 패턴으로
Mediator, Interpreter, Iterator, Observer, Visitor,
State, Command 등의 패턴이 포함된다.
08 다음은( )무결성 제약 조건을 위반한 [고
객] 릴레이션이다. 괄호 ( ) 안에 들어갈
용어를 쓰시오.(단, 고객 아이디는 기본키이다.)
[고객] 릴레이션
고객 아이디 고객이름 나이 직업 포인트
apple 기:기도 O So 20 학생 1000
NULL 장길산 28 회사원 3000
carrot 호기도 32 교사 2000
NULL 이 꺼저
= —1 O 26 학생 4500
238 수제비 정보처리기사 실기 FINAL 모의고사
## Page 239

09 다음 [보기]에서 올바른 URL 주소가 되도록
순서에 맞게 번호를 쓰시오.
[보기]
① ?name=ferret (query)
② /over/there (path)
③ example.com:8042 (authority)
④ foo:// (scheme)
⑤ #nose (fragment)
( ) —( ) —( ) —( ) —( ) J
10 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 def func(value):
02 if type(value)==type(100):
03 return 100
04 elif type(value)==type(""):
05 return len(value)
06 else:
07 return 20
08
09 a="100.0"
10 b=100.0
11 c=(100,200)
12
13 print(func(a)+func(b)+func(c))
1 1 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class Base{
02 public int x=3;
03 int getX() {
04 return x*2;
05 }
06 }
07
08 class Derivate extends Base{
09 public int x=7;
10 int getX() {
11 return x*3;
12 }
13 }
14
15 class Soojebi {
16 public static void main(String[ ] args) {
17 Base b=new Derivate( );
18 Derivate d=new Derivate( );
19 System.out.piint(b.getX()+b.x+d.getX( )+d.x);
20 }
21 }
2024년 기출문제 3회 239
## Page 240

12 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 ffinclude (stdio.h)
02 struct Node {
03 int v;
04 struct Node* next;
05 };
06 void func(striict Node* n) {
07 while (n !=NULL&&n—>next !=NULL) {
08 int t=n-)v;
09 n—>v=n—>next—>v;
10 n—>next—>v=t;
11 n=n-> next-) next;
12 }
13 }
14
15 int main() {
16 struct Node n1={1, NULL};
17 struct Node n2={2, NULL};
18 struct Node n3={3, NULL};
19 struct Node* c=&n1;
20
21 n1.next=&n3;
22 n3.next=&n2;
23 func(&n1);
24 while (c !=NULL) {
25 printf("%d", c->v);
26 c=c->next;
27 }
28 return 0;
29 }
다음 설명을 보고 해당되는 테스트 커버리지
유형을 [보기]에서 찾아 쓰시오.
① 모든 명령문을 적어도 한 번 실행되도록 조
합하는 커버리지
② 각 결정문이 참, 거짓을 한 번 이상 갖도록
조합하는 커버리지
③ 결정문 내의 각 조건이 참, 거짓을 한 번 이
상 갖는 조합하는 커버리지
[보기]
0 Statement © Branch
© Condition ® Default
@ Condition/Decision
@ Modified Condition/Decision
①_______________________________________________
②_______________________________________________
③_______________________________________________
UML 다이어그램의 관계를 표현한 그림이다.
괄호 ( ) 안에 들어갈 관계의 유형을 보기
에서 골라서 기호로 쓰시오.
• ( ① ): 2개 이상의 사물이 서로 관련되어
있는 상태를 표현하는 관계
축구팀 공격수
------- >
• ( ② ): 하나의 사물이 다른 사물에 비해 더
일반적인지 구체적인지를 표현하는 관계
차
. 느。I 우그 ,
버스 승용차 택시
240 수제비 정보처리기사 실기 FINAL 모의고사
## Page 241

( ③ ): 사물 사이에 서로 연관은 있으나 필
요에 따라 서로에게 영향을 주는 짧은 시간 동
안만 연관을 유지하는 관계를 표현하고, 기존
객체가 변경되면 다른 객체도 변경되는 관계
[보기]
0> 슈퍼 키(Super Key)
© 외래 키(Foreign Key)
© 대체 키(Alternate Key)
(르) 후보 ? ((Candidate Key)
© 기본 키(Primary Key)
[보기]
(3)연관(Association) 관계
© 일반화(Generalization) 관계
© 의존(Dependency) 관계
@ 실체화(Realization) 관계
@ 포함(Composition) 관계
@ 집합(Aggregation) 관계
①_____________________________________________
②_____________________________________________
③_____________________________________________
④_____________________________________________
16 다음은 c언어 코드이다. 출력 결과를 쓰시오.
①_____________________________________________
②_____________________________________________
③_____________________________________________
다음은 키(Key)에 대한 설명이다. 괄호 ( )
안에 들어갈 키의 종류를 [보기]에서 골라서
쓰시오.
•( ① ): 한 릴레이션의 컬럼이 다른 릴레이
션의 기본 키로 이용되는 키로 테이블 간의
참조 데이터 무결성을 위한 제약 조건
• ( ② ): 테이블에서 각 튜플을 구별하는 데
기준이 되는 키로 유일성과 최소성을 만족하
는 키
• ( ③ ): 후보 키 중에서 기본 키로 선택되
지 않은 키
• ( ④ ): 릴레이션을 구성하는 모든 튜플에
대해 유일성은 만족하지만, 최소성은 만족하
지 못하는 키
01 include <stdio.h>
02 void func(int **arr, int size){
03 int i;
04 for(i=0; i<size; i++){
05 *(*arr+i)=(*(*arr 十 i)+i)%size;
06 }
07 }
08 int main(){
09 int arr[ ]={3,1, 4,1, 5};
10 int *p=arr;
11 int **pp=&p;
12
13 func(pp, 5);
14 printf("%d", arr[2]);
15 return 0;
16 }
2024년 기출문제 3회 241
## Page 242

괄호 ( ) 안에 공통으로 들어갈 용어를 쓰
시오.
• 여러 공중 인터넷망을 하나의 사설망처럼 사
용할 수 있는 기술로  공중망과 사설망의 중간
단계이고 방식으로는 SSL 방식과 IPSec 방식
이 있다.
• SSL ( '은/는 4계층에서 소프트웨어적으
로 동작하므로 별도의 장치가 필요 없으며 가
격이 저렴하다.
• IPSec ( '은/는 3계층에서 동작하므로 IP
헤더를 조작해야 하므로 별도의 하드웨어 장
치가 필요하나 보안성이 뛰어나다.
18 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int sum=0;
04 try {
05 func( );
06 }
07 catch (NullPointerException e) {
08 sum=sum+1;
09 }
10 catch (Exception e) {
11 sum=sum+10;
12 }
13 finally {
14 sum=sum+100;
15 }
16 System.out.print(sum);
17 }
18 static void func() throws Exception {
19 throw new NullPointerException( );
20 }
21 }
19 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class Printer{
02 void print(lnteger x) {
03 System.out.print("A" +x);
04 }
05 void print(Object x) {
06 System.out.print("B" +x);
07 }
08 void print(Number x) {
09 System.out.print("C" +x);
10 }
11 }
12 class Collection<T>{
13 T value;
14 public Collection(T t) {
15 value=t;
16 }
17 public void print() {
18 new Printer( ).print(value);
19 }
20 }
21 class Soojebi {
22 public static void main(String[ ] args) {
23 new Collection<>(O).print( );
24 }
25 }
20 다음 빈칸( )에 들어갈 용어를 작성하
시오.
( '은/는 네트워크의 구성 및 유지를 위해
기지국이나 액세스 포인트와 같은 기반 네트워
크 장치를 필요로 하지 않는 네트워크로 노드
(Node)들에 의해 자율적으로 구성되는 구조이다.
긴급 구조, 긴급회의, 전쟁터에서의 군사 네트워
크로 활용된다.
242 수제비 정보처리기사 실기 FINAL 모의고사
## Page 243

다음은 네트워크 보안에 관련된 문제이다. 괄
호 ( ) 안에 알맞은 용어를 작성하시오.
• ( '은/는 케빈 미트닉이 사용했던 공격 방
법 중 하나로 TCP의 세션 관리 취약점을 이용 [확인 필요]
한 공격기법이다.
• TCP ( )은/는 TCP의 3-Way Handshake [확인 필요]
가 완료된 후에 공격자가 시퀀스 번호 등을
조작하여 정상적인 세션을 가로채고 인증없이
통신을 탈취하는 공격이다.
02 다음은 오류 검출 코드에 대한 설명이다. 괄
호 ( ) 안에 공통으로 들어갈 알맞은 용어
를 영문 약자로 쓰시오.
• ( )은/는 3글자의 영어 약자로 이루어진 기
법으로, 데이터를 전송하거나 저장할 때 데이
터의 오류를 감지하는 데 사용되는 오류 검출
코드이다.
• ( )은/는 다항식을 통해 산출된 값을 토대
로 오류를 검사하는 방식으로 집단 오류를 해
결하기 위한 방식이다.
• ( )은/는 데이터에 체크섬을 추가하여 데
이터를 전송하거나 저장한 후, 수신 시 체크섬
을 다시 계산하여 데이터가 변경되었는지 혹두
인하는 기법이다.
02 다음은 제약 조건과 관련된 문제이다. 괄호
( ) 안에 알맞은 용어를 쓰시오.
• ( ① )무결성은 한 엔터티에서 같은 기
본키(PK)를 가질 수 없거나, 기본키의 속성이
NULL을 허용할 수 없는 제약조건이다. [확인 필요]
• ( ② ) 무결성은 외래키가 참조하는 다른
개체의 기본키에 해당하는 값이 기본키 값이
나 NULL이어야 하는 제약조건이다. [확인 필요]
• ( ③ ) 무결성은 속성(컬럼)이 가질 수 있는
값의 범위를 정의하고 준수하도록 하는 제약
조건이다.
①____________________________________________
②____________________________________________
③____________________________________________
04 다음은 악성코드 관련된 설명이다. 다음 내용
을 확인하여 [보기]에서 골라 쓰시오.
• 사용자가 원치 않는 소프트웨어를 구매하도록
조직하기 위해 사회공학을 활용하여 충격, 불
안 또는 위협에 대한 인식을 유발하는 악성 소
프트웨어의 한 형태이다.
• '겁을 주다'라는 영어 단어에서 유래한 것으로
공포를 이용하여 피해자를 속여 대가를 지불
하거나 특정 행동을 유도하는 악성 소프트웨
어이다.
• 가짜 바이러스 경고나 시스템 문제를 표시하
여 사용자가 돈을 지불하거나 특정 소프트웨
어를 설치하도록 속이는 방식으로 작동한다.
[보기]
@ 컴포넌트웨어
© 셔블웨어
@ 안티스파이웨어
® 그룹웨어
© 유즈웨어
@스케어웨어
@ 네트웨어
© 애드웨어
2025년 기출문제 1회 243
## Page 244

0E 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int a=5,b=0;
04 try{
05 System.out.print(a /b);
06 }
07 catch(ArithmeticException e){
08 System.outprint(" 출력 1
09 }
10 catch(ArraylndexOutOfBoundsException e) {
11 System.outprint("출력 2");
12 }
13 catch(NumberFormatException e) {
14 System.out.print(" 출력 3");
15 }
16 catch(Exceptior)e){
17 System.out.print(" 출력 4");
18 }
19 finally{
20 System.oiitprint(" 출력 5");
21 }
22 }
23 스 }
0/ 다음 [emp], [sal] 테이블을 참고하여 [보기]
의 쿼리 실행 결과를 쓰시오.
[emp] 테이블
id name
1001 김철수
1002 홍길동
1004 강감찬
1008 이순신
[sal] 테이블
id incentive
1001 300
1002 300
1004 400
1008 1000
[SQL]
SELECT name, incentive
FROM emp, s게
WHERE emp.id=sal.id and incentive) =500
06 다음은 네트워크 프로토콜에 대한 설명이다.
괄호 ( ) 안에 알맞은 프로토콜을 쓰시오.
• ( ① )은/는호스트가 목적지 ip 주소는 알
고 있으나 MAC 주소를 모를 때, 이를 알아내
기 위해 사용하는 프로토콜이다.
• ( ② )은/는 디스크가 없는 호스트가 자신
의 MAC 주소를 통해 IP 주소를 할당받기 위
해 사용하는 프로토콜이다.
08 다음은 데이터베이스에 관련된 설명이다. 알
맞은 용어를 [보기]에서 골라 쓰시오.
• 릴레이션에서 속성의 개수를 의미:( ① )
• 릴레이션에서 튜플의 개수를 의미:( ② )
• 한 릴레이션의 컬럼이 다른 릴레이션의 기본
키로 이용되는 키: ( ③ ) Key
• 하나의 속성이 취할 수 있는 같은 타입의 원자
값들의집합:( ④ )
[보기]
Q)Domain
© Degree
@ Cardinality
® Foreign
© Primary
@ Candidate
@ Attribute
①
②
③
 @
①
 ②
244 수제비 정보처리기사 실기 FINAL 모의고사
## Page 245

IP 주소가 192.168.35.10, 서브넷 마스크는 255.
255.252.0인 PC에서 브로드캐스팅으로 다른 [확인 필요]
IP 정보를 전달한다고 할 때 수신할 수 있는
알맞은 IP를 [보기]에서 골라 모두 쓰시오. [확인 필요]
[보기]
@ 192.168.34.1 © 192.168.32.19
© 192.168.35.200 @ 192.168.33.138
@ 192.168.35.50
10 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 char Data[5]={'B', 'A', 'D', 'E'};
03 char c;
04 int main(){
05 int i, temp, temp2;
06 c='C';
07 printf("%d\n", Data[3]—Data[1]);
08 for(i=0;i<5;++i){
09 if(Data[i]>c)
10 break;
11 }
12 temp=Data[i];
13 Data[i]=c;
14 i + +;
15 for(; i<5; 十+i){
16 temp2=Data[i];
17 Data[i]=temp;
18 temp 너emp2; [확인 필요]
19 }
20 f0이=0;乂5刀十+){
21 printf("%c", Data[i]);
22 }
23 return 0;
24 }
다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 ffinclude <stdio.h>
02 ffinclude<stdlib.h>
03 void set(int **arr, int *data, int rows, int cols) {
04 int i;
05 for (i=0; i<rows * cols; + 十i) {
06 arr[((i+1)/rows)%rows][(i+1)%cols]=data[i];
07 }
08 }
09 int main() {
10 int rows=3, cols=3, sum 0;
11 int i;
12 int**arr;
13 int data[ ]={5, 2, 7,4,1, 8, 3, 6, 9};
14 arr=(int**)malloc(sizeof(int*) * rows);
15 for (i=0; i<cols; i十十){
16 arr[i]=(int *) malloc(sizeof(int) * cols);
17 }
18 set(arr, data, rows, cols);
19 for (i=0; i< rows * cols; i++) {
20 sum+=arr[i/rows][i%cols] * (i%2==0?1: -1);
21 }
22 for(i=0; i<rows; i十 十) {
23 free(arr[i]);
24 }
25 free(arr);
26 printf("%d", sum);
27 return 0;
28 }
2025년 기출문제 1회 245
## Page 246

다음은 자바 코드이다. 출력 결과를 쓰시오.다음 괄호 ( ) 안에 들어갈 알맞은 결합도
를 쓰시오.
• ( ① )은/는다른 모듈 내부에 있는 변수나
기능을 다른 모듈에서 사용하는 경우의 결합
도이다
• ( ② '은/는 모듈 간의 인터페이스로 배열
이나 오브젝트, 자료구조 등이 전달되는 경우
의 결합도이다.
• ( ③ )은/는파라미터가아닌모듈밖에선
언되어 있는 전역 변수를 참조하고 전역 변수
를 갱신하는 식으로 상호 작용하는 경우의 결
합도이다.
①____________________________________________
②____________________________________________
③____________________________________________
01 class Parent{
02 static int total=0;
03 int v=1;
04 public Parent(){
05 total+=(++v);
06 show();
07 }
08 public void show(){
09 total+=total;
10 }
11 }
12 class Child extends Parent{
13 int v너0;
14 public Child(){
15 v 十 =2;
16 totaH-=v+ + ;
17 show( );
18 }
19 ©Override
20 public void show(){
21 total+=total*2;
22 }
23 }
24 class Soojebi {
25 public static void main(String[ ] args) {
26 new Child( );
27 System.out.println(Parent.total);
28 }
29 }
246 수제비 정보처리기사 실기 FINAL 모의고사
## Page 247

16 다음은 자바 코드이다. 출력 결과를 쓰시오.다음이 설명하는 디자인 패턴은 무엇인지 쓰
시오.
• Wrapper라고도 불리며, 다른 클래스가 이용할 [확인 필요]
수 있도록 인터페이스 변환해주는 패턴이다.
• 기존에 생성된 클래스를 재사용할 수 있도록
중간에서 맞춰주는 역할을 하는 인터페이스를
만드는 패턴이다.
• 상속을 이용하는 클래스 패턴과 위임을 이용
하는 인스턴스 패턴의 두가지 형태로 사용되
는 디자인 패턴이다.
• 인터페이스가 호환되지 않는 클래스들을 함께
이용할 수 있도록 타 클래스의 인터페이스를
기존 인터페이스에 덧씌운다.
01 public class Soojebi {
02 static int fn(int[ ] a, int st, int end) {
03 if (st>=end) return 0;
04 int mid=(st+end)/2;
05 return a[mid]+Math.max(fn(a, st, mid), fn(a, mid+1, end));
06 }
07 public static void main(String[ ] args) {
08 int[ ] values={3, 5, 8,12,17};
09 System.out.println(fn(values, 0, values.length-1));
10 }
11 }
다음은 파이썬 코드이다. 출력 결과를 쓰시오.
다음은 화이트박스 테스트의 프로그램 제어
흐름이다. 다음 질문에 답하시오.
[코드] [순서도]
int test(int B[ ], int M, int X) {
int a=0;
while (a<M || B[a]<X) {
—I
if (B[a]<0) 『트승三厂
B[a]=—B[a]; 프기 드令>
a 十+;
}
return 1;
}
⑴ 순서도의 빈칸을 채우시오.
①________________________________________________
②________________________________________________
③________________________________________________
④________________________________________________
⑤________________________________________________
⑥________________________________________________
01 class Node:
02 def___________ __
03 s이f.v=v [확인 필요]
04 self.c 늬 ]
05
06 def tree(li):
07 n=[Node(i) for i in li]
08 for i in range(1, len(li)):
09 n[(i-1)/ /2].c.append(n[i])
10 return n[이
11
12 def calc(n, level=0):
13 return n.v if level % 2 else 0+\
sum(calc(n, level+1) for n in n.c) if n else 0
14
15 li늬3, 5, 8,12,15,17, 21] [확인 필요]
16 root=tree(li)
17 print(calc(root))
⑵ 문장 커버리지를 100% 만족하는 테스트
케이스를 쓰시오.
①—②—( )—( )—( )—( )—( )
2025년 기출문제 1회 247
## Page 248

18 다음은 c언어 코드이다. 출력 결과를 쓰시오. 19 다음은 c언어 코드이다. 출력 결과를 쓰시오.
ffinclude <stdio.h>
#include<stdlib.h>
typedef struct Data {
int value;
struct Data *next;
} Data;
Data *insert(Data *head, int value) {
Data *new_node=(Data *)malloc(sizeof(Data));
new_node —>value=value;
new_node- > next=NULL;
if(head = =NUI_l_)
return new_node;
new_node- > next=head;
head=new_node;
return head;
}
Data *reconnect(Data *head, int disconnect_count) {
Data *prev=head, *curr=head-)next;
while(curr&&curr->value !=disconnect_count) {
prev=curr;
curr=ci』rr—>next;
}
if(curr==NULI_) return head;
prev ->next=curr —>next;
curr-) next=head;
return curr;
}
int main(){
Data *head=NULL, *curr=NULL, *tmp=NULL;
int i;
for (i=1; i<= 5; i++)
head=insert(head, i);
head=reconnect(head, 3);
for (curr=head; curr !=NULL; curr=curr->next)
printf("%d", curr-)value);
while(head){
tmp=head;
head = head-) next;
free(tmp);
}
return 0;
01 #include<stdio.h>
02 typedef struct student{
03 char *name;
04 int score[3];
05 }Student;
06 int dec(int enc){
07 return enc & 0xA5;
08 }
09 int sum(Student *p){
10 return dec(p-)score[이)+dec(p->score[1])+dec(p->score[2]);
11 }
12 int main(){
13 Student $[2]={"Kim", {OxAO, OxA5, OxDB}, "Lee", {OxAO, OxED, 0x81}};
14 Student *p=s;
15 int result=0, i;
16
17 for(i=0; i<2; i十十){
18 result+=sum(&s[i]);
19 }
20 printf("%d", result);
21 return 0;
22 }
20 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 System.out.println(calc("5"));
04 }
05 static int calc(int value) {
06 if (value <=1) return value;
07 return calc(value-1)+calc(value-2);
08 }
09 static int calc(String str) {
10 int value=Integer.valueOf(str);
11 if (value <=1) return value;
12 return calc(value—1)+calc(value—3);
13 }
14 }
248 수제비 정보처리기사 실기 FINAL 모의고사
## Page 249

01 다음은 파일의 레코드(Record)를 물리적 저장
장치에 저장하기 위한 배치 방법인 파일 조직
에 대한 설명이다. 괄호 ( ) 안에 공통으로
들어갈 용어를 쓰시오.
• 파일 조직 방법은 레코드의 저장과 접근방법
을 결정해 주기 때문에 데이터 검색 성능 및
처리 효율성에 큰 영향을 준다.
• 파일 조직은 저장된 레코드들에 대한 어떤 접
근방법을 제공하느냐에 따라 크게 순차 방법,
( ) 방법, 해싱 방법이 있다.
•( ) 방법은 데이터 레코드에 접근하기
위해서 먼저 해당 ( )을/를 찾아서, 그
( )이/가 가리키는 주소를 따라가 원하는
레코드에 접근할 수 있도록 하는 저장 방법
이다.
02 데이터베이스에서 열(Column)을 의미하는 용
어로, 파일에서의 필드(Field)와 같은 의미를
가지는 데이터 구조 단위를 무엇이라고 하는
지 보기에서 골라 기호로 쓰시오.
[보기]
@ Relation © Tuple
© Attribute @ Cardinality
@ Degree @ Schema
® Instance
03 포트 번호 22번을 사용하고 인증, 암호화, 압
축, 무결성을 제공하며, Telnet보다 강력한 [확인 필요]
보안을 제공하는 원격 접속 프로토콜은 무엇
인지 쓰시오.
04 다음은 프로세스 스케줄링에 대한 설명이다.
괄호( )안에 들어갈 스케줄링 기법을 쓰
시오.
• ( ① ): 프로세스가 도착하는 시점에 따라
그 당시 가장 작은 서비스 시간을 갖는 프로세
스가 종료 시까지 자원을 점유하는 스케줄링
기법
• ( ② ): 가장 짧은 시간이 소요되는 프로세
스를 먼저 수행, 남은 처리시간이 더 짧다고
판단되는 프로세스가 준비 큐에 생기면 언제
라도 프로세스가 선점되는 스케줄링 기법으로
비선점 방식의 스케줄링 기법에 선점 방식을
도입한기법
①___________________________________________________________________________________
②___________________________________________________________________________________
2025년 기출문제 2회 249
## Page 250

다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi{
02 public static void fn(String[ ] data. String s){
03 data[이=s;
04 s="Z";
05 }
06
07 public static void main(String[ ] args) {
08 String data[ ]=〔"A"};
09 String s="B";
10 fn(data, s);
11 System.oulprint(data[0]+s);
12 }
13 }
07 실체 객체에 대한 대리 객체로 실체 객체에
대한 접근 이전에 필요한 행동을 취할 수 있
게 만들고, 이 점을 이용해서 미리 할당하지
않아도 상관없는 것들을 실제 이용할 때 할당
하게 하여 메모리 용량을 아낄 수 있으며, 실
체 객체를 드러나지 않게 하여 정보 은닉의
역할도 수행하는 디자인 패턴을 [보기]에서
찾아 쓰시오.
[보기]
• 생성 패턴: Builder, Prototype, Sin이eton, [확인 필요]
Abstract Factory
• 구조 i패턴: Bridge, Decorator, Facade,
Flyweight, Proxy, Composite, Adapter
• 행위 패턴: Observer, Mediator, Visitor,
Strategy
06 호스트 주소가 223.13.234.132이고, 서브넷
마스크는 255.255.255.192^ 때, ( ) 안에
들어가는 값을 쓰시오.
• O| 호스트의 네트워크 주소는 223.13.234.
( ① )이다.
• 이 네트워크 주소에서 사용 가능한 호스트 주
소의 개수는 네트워크 주소와 브로드캐스트
주소를뺀( ② )개이다.
①___________________________________________________________________________________
②___________________________________________________________________________________
08 다음 괄호( )안에 공통으로 들어갈 용어
를 쓰시오.
• ( )은/는 웹에서 Javascript, XML을 이용 [확인 필요]
하여 비동기식으로 웹 페이지의 일부 콘텐츠
만 리로드(Reload) 해오는 방식이다.
• ( ) 은/는 하이퍼텍스트 표기 언어(HTML)
만으로는 어려운 다양한 작업을 웹 페이지에
서 구현해서 이용자가 웹 페이지와 자유롭게
상호 작용할 수 있도록 구현하는 기법이다.
• Goo이e Maps와 Google ( )에서 이러한 [확인 필요]
방식을 사용한다.
250 수제비 정보처리기사 실기 FINAL 모의고사
## Page 251

09 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 static interface F {
03 int apply(int x);
04 }
05 public static int run(F f) {
06 try {
07 return f.apply(3);
08 }
09 catch (Exception e) {
10 return 7;
11 }
12 }
13 public static void main(String[ ] args) {
14 Ff=(x)—>{
15 if(x>2){
16 throw new RuntimeException( );
17 }
18 return x*2;
19 };
20 System.out.print(run(f)+run((int n)->n+9));
21 }
22 }
1 o 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static class Parent {
03 public int x(int i) {return i+2;}
04 public static String id() {return "P";}
05 }
06 public static class Child extends Parent {
07 public int x(int i) {return i+3;}
08 public String x(String s) {return s+"R";}
09 public static String id() {return "C";}
10 }
11 public static void main(String[ ] args) {
12 Parent ref=new Child( );
13 System.out.println(ref.x(2)+ref.id( ));
14 }
15 }
다음 제어흐름 그래프가 분기 커버리지를 만
족하기 위한 테스팅 순서를 쓰시오.
다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 #define SIZE 3
03 typedef struct {
04 int data[SIZ티; [확인 필요]
05 int front;
06 int rear;
07 }Queue;
08 void enq(Queue* q, int val) {
09 q-> data[q —>rear] 三 val;
10 q —>rea r=(q —>rear+1) % SIZE;
11 }
12 int deq(Queue* q) {
13 int val=q - > data[q - >front];
14 q —>front=(q—>front+1)%SIZE;
15 return val;
16 }
17 int main(){
18 Queue q={{0}, 0, 0};
19 int a, b;
20 enq(&q, 1);
21 enq(&q, 2);
22 deq(&q);
23 enq(&q, 3);
24 a=deq(&q);
25 b=deq(&q);
26 printf("%d 그리고 %d", b, a);
27 return 0;
28 }
2025년 기출문제 2회 251
## Page 252

다음은 자바 코드이다. 출력 결과를 쓰시오.프로세스의 도착시간과 서비스 시간은 다음
과 같다. RR 스케줄링을 적용할 때 평균 대기
시간을 구하시오. (단, 시간 할당량은 4ms이다.) [확인 필요]
프^11스 도착시간(ms) 서비스 시간(ms)
P1 0 8
P2 1 4
P3 2 9
P4 3 5
14 다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 struct dat {
03 int x;
04 int y;
05 };
06 int main() {
07 struct dat a[ ]={{1, 2}, {3, 4}, {5, 6}};
08 struct dat* ptr=a;
09 struct dat** pptr 三 &ptr;
10 (*pptr)[1]=(*pptr)[2];
11 printf("%d 그리고 %d", a[1].x, a[1].y);
12 return 0;
13 }
01 public class Soojebi {
02 public static class B0{
03 public int v;
04 public BO(int v) {
05 this.v=v;
06 }
07 }
08
09 public static void main(String[ ] args) {
10 BO a=new B0(1);
11 BO b=new BO(2);
12 BO c=new BO(3);
13 BO[ ] arr={a, b, c};
14 BO t = arr[이;
15 arr[이=arr[2];
16 arr[2]=t;
17 arr[1].v-arr[0].v;
18 System.out.println(a.v+"a"+b.v 十 "b"+c.v);
19 }
20 }
16 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 include<stdio.h>
02 ffinclude<stdlib.h>
03 struct node {
04 int p;
05 struct node* n;
06 };
07 int main() {
08 struct node a={1, NULL};
09 struct node b:三{2, NULL};
10 struct node c={3, NULL};
11 struct node* head=&c;
12 a.n=&b;
13 b.n=&c;
14 c.n=NULL;
15 c.n三&a;
16 a.n=&b;
17 b.n=NULL;
18 printf("%d %d %d", head-)p, head-)n-)p, head-)n->n-)p);
19 return 0;
20 }
252 수제비 정보처리기사 실기 FINAL 모의고사
## Page 253

다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 1st 늬1,2,3]
02 dst={i: i*2 for i in 1st}
03 s=set(dst.values())
04 1st[이=99
05 dst[2]=7
06 s.add(99)
07 print(len(s & set(dst.values())))
다음에서 설명하는 보안 공격 기법을 [보기]
에서 골라서 기호로 쓰시오.
• TCP 프로토콜의 3-Way Handshake를 악용 [확인 필요]
한 공격 기법으로 대표적인 자원 소진 공격
• 짧은 시간 대량의 패킷을 전송하여 서버의 백
로그 큐를 가득 채워 더 이상 신규 세션을 연
결할 수 없게 하는 공격
18 다음은 c언어 코드이다. 출력 결과를 쓰시오.
[보기]
O Slowloris © RUDY
© Tear Drop ® SYN Flooding
@ Land Attack @ UDP Flooding
® Smurfing @ Ping of Death
01 include <stdio.h>
02 #include<st에ib.h> [확인 필요]
03 struct node {
04 char c;
05 struct node* p;
06 };
07 struct node* func(char* s) {
08 struct node* h=NULL, *n;
09 while(*s) {
10 n=(struct node*)malloc(sizeof(struct node));
11 n—>c=*s 十+;
12 n—>p三 h;
13 h=n;
14 }
15 return h;
16 }
17 int main() {
18 struct node* n=func("BEST");
19 while(n) {
20 struct node* t=n;
21 putchar(n->c);
22 n=n—>p;
23 free(t);
24 }
25 return 0;
26 }
다음 [EMPLOYEE] 테이블에 대하여
(EMPLOYEE) 연산을 수행하면 나타나는 결과
를 채워 넣으시오.
[EMPLOYEE] 테이블
[결과]
EMPNO NAME DEPT TTL JOIN_DATE
1001 홍길동 총무 부장 2001.03.01
1002 강감찬 총무 대리 2017.09.01
1003 을지문덕 회계 과장 2012.03.01
1004 이순신 기획 차장 2004.03.09
①
②
¥
(4)
¥
①___________________________________________________________________________________
②___________________________________________________________________________________
③___________________________________________________________________________________
④___________________________________________________________________________________
⑤___________________________________________________________________________________
2025년 기출문제 2회 253
## Page 254

수제비 FINAL
Z025 기출문제3흐！
01 다음은 판매와 관련된 다이어그램이다. 해당
다이어그램의 명칭을 쓰시오.
다음은 리눅스/유닉스 운영체제의 명령어에
대한 설명이다. 다음 조건에 해당하는 명령어
를 쓰시오.
① 현재 작업 중인 디렉토리의 절대 경로를 출
력하는 명령어
② 자신이 속해있는 폴더 내에서의 파일 및 폴
더들을 표시하는 명령어
③ 디렉토리로 이동하는 명령어
④ 파일을 복사하는 명령어
①_________________________________________
②_________________________________________
③_________________________________________
④_________________________________________
02 전체 조건식의 영향은 고려하지 않고, 결정
포인트 내의 각 개별 조건식이 적어도 한 번
은 참(True)과 거짓(False)의 결과가 되도록 수
행하는 테스트 커버리지는 무엇인지 [보기]에
서 고르시오.
[보기]
O 구문 커버리지
© 결정 커버리지
© 조건 / 결정 커버리지
@ 다중 조건 커버리지
@ 변경 조건 / 결정 커버리지
@ 기본 경로 커버리지
© 조건 커버리지
© 제어 흐름 테스트
© 데이터 흐름 테스트
® 루프 테스트
254 수제비 정보처리기사 실기 FINAL 모의고사
## Page 255

04 다음은 오류 제어 방식에 대한 설명이다. 괄
호 ( ) 안에 들어갈 용어를 보기에서 찾아
서 쓰시오.
• 오류 제어 방식에는 크게( ① )방식과
( ② )방식이있다.
• ( ① )방식은 데이터 전송 과정에서 발생
한 오류를 검출하여 검출된 오류를 재전송 요
구 없이 A스루 수정하는 방식이다. 대표적인
유형인 ( ③ ) 코드 방식은 수신측에서 오
류가 발생한 비트를 찾아 재전송을 요구하지
않고 자신이 직접 오류를 수정하는 방식으로
1비트의 오류 수정이 가능하다.
• ( ② ) 방식은 데이터 전송 과정에서 오류
가 발생하면 송신 측에 재전송을 요구하는 방
식이다. 대표적인 유형에는 ( ④ ) 검사,
( ⑤ )등이있다.
• ( ④ ) 검사는 7~8개의 비트로 구성되는
전송 문자에 ( ④ ) 비트를 추가하여 오류
를 검출하는 방식이다.
• ( ⑤ )은/는 다항식을 통해 산출된 값을 토
대로 오류를 검사하는 방식으로 집단 오류를
해결하기 위한 방식이다.
[보기]
NAK, BEC, Hamming, MD5, Parity, BCD,
CRC, FEC
①____________________________________________
②____________________________________________
③____________________________________________
④____________________________________________
⑤____________________________________________
C 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 ffinclude<stdio.h>
02 struct Soo {
03 int x;
04 const char *y;
05 };
06 int main() {
07 struct Soo t[ ]={{1, "AB"}, {2, "DC"}, {3, "EB"}};
08 struct Soo *p= &t[1];
09 printf("%s", p—>y十(p—>x—1));
10 return 0;
11 }
06 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 int main(){
03 char str[]="REPUB니COFKOREA"; [확인 필요]
04 int a=0;
05 while (str[a] !='\0') +十a;
06 putchar(str[a—2]);
07 return 0;
08 }
2025년 기출문제 3회 255
## Page 256

다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 #include<stdio.h>
02 struct Node{
03 struct Node* next;
04 unsigned int x;
05 };
06
07 int main(){
08 struct Node t1 三 { 0, 5u };
09 struct Node t2={ 0, 7u };
10 struct Node t3=〔 0,11u };
11 struct Node* curr;
12 int sum=0;
13
14 t3.next=&t2;
15 t2.next=&tl;
16 curr=&t3;
17
18 while (curr){
19 sum=sum*3+cijrr—>x;
20 curr=curr-> next;
21 }
22
23 sum=(sumA42u)+100u;
24
25 printf("%u", sum);
26 return 0;
27 }
08 다음은 자바 코드이다. 빈칸에 들어갈 키워드
를 작성하시오.
01 interface Person {
02 void introduce( );
03 }
04 class Student_______ Person {
05 private String name;
06
07 public Student() {
08 this.name="Yuna";
09 }
10 public void introduce() {
11 System.out,println("Hello, my name is"+name);
12 }
13 }
14 public class Soojebi{
15 public static void main(String[ ] args) {
16 Student student=new Student();
17 studentjntroduce( );
18 }
19 }
09 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 data=[
02 [3, 5, 2, 4,1],
03 [4, 5,1],
04 [4, 4,1, 5, 4],
05 [4, 5]
06 ]
07
08 result={}
09
10 for index, lis in enumerate(data):
11 list_sum=sum(lis)
12 listjen 긔 en(lis)
13 result[index]=(list_sum, listjen)
14
15 print(result)
256 수제비 정보처리기사 실기 FINAL 모의고사
## Page 257

1 0 다음 SQL의 실행 결과를 쓰시오. [확인 필요]
[SOO] 테이블
NAME
SOPHIA
0 니 VIA
SEMA
[JEBI] 테이블
RULE
S%
%A%
SELECT COUNT(*) CNT FROM SOO CROSS
JOIN JEBI
WHERE SOO.NAME LIKE JEBI.RULE;
1 1 다음에서 설명하는 용어를 쓰시오.
• 은행 인증 등에 사용되며, 무작위 암호 생성과
HASH 함수를 이용해 매번 새로 발급되는 인
증 방식이다.
• 비밀번호가 캐시에만 존재하며, 서버나 클라
이언트에 장기적으로 저장되지 않기 때문에
공격자가 암호를 복제하거나 추출하기 어렵
고, 한 번 사용 후 만료되기 때문에 패스워드
탈취나 재사용 공격으로부터 시스템을 보호할
수 있다.
다음은 자바 코드이다. 빈칸에 들어갈 키워드
를 작성하시오.
01 class Rectangle {
02 int x, y;
03 Rectangle(int x, int y) {
04 this.x=x;
05 this.y=y;
06 }
07 int getArea() {
08 return x * y;
09 }
10 }
11
12 class Square extends Rectangle {
13 Square(int s) {
14 ___________________
15 }
16 int getSquareArea() {
17 return s* s;
18 }
19 }
20
21 public class Soojebi {
22 public static void main(String[ ] args) {
23 Square sq=new Square(10);
24 sq.getArea( );
25 }
26 }
다음에서 설명하는 용어를 쓰시오.
• 사용자가 비밀번호를 제공하지 않고 다른 웹
사이트나 애플리케이션의 접근 권한을 부여할
수 있게 하는 개방형 표준 기술이다 .
• 구글, 페이스북 등의 외부 계정을 기반으로 토
큰을 이용하여 간편하게 회원가입 및 로그인
할 수 있는 기술이다 .
2025년 기출문제 3회 257
## Page 258

다음과 같은 두 테이블 R과 S가 있다. 관계
대수식 R三s의 결과를 구하시오. (결과를 테이
블 형태로 작성하시오.)
[R] 테이블
[S] 테이블
A B
a1 b1
a2 b2
a1 b3
B
b1
b3
다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int x=7, y=4, z;
04 z=y%3<3 ? 2 : 1;
05 z=z&(z>>1);
06 z=(x>5&&z<=3) ? (z * x): (z/x);
07 System.out.printf("%d", z);
08 }
09 }
16 다음은 데이터베이스에 관련된 내용이다. 각
괄호에 들어갈 답을 [보기]에서 골라 쓰시오.
• ( ① )은/는 테이블 내의 행을 의미하며,
레코드(Record)라고도 한다. 어떤 요소의 집
합, 혹은 테이블에서의 행을 가리키지만, 일반
적인 집합과는 달리 중복이 허용될 수 있다.
• ( ② )은/는 릴레이션에 실제로 저장된 데
이터의 집합을 의미한다. 그리고 릴레이션 또
는 릴레이션 외연 (Relation Extension) 라고도
한다.
• ( ③ )은/는 특정 데이터 집합의 유니크
(Unique)한 값의 개수를 의미한다.
[보기]
튜플(Tuple), 릴레이션 스키마(Relation Schema),
릴레이션 인스턴스(Relation Instance), 카디널
리티(Cardinality), 디그리(Degree), 애트리뷰트
(Attribute)
다음은 자바 코드이다. 출력 결과를 쓰시오.
01 enum Tri {
02 A("A"), B("AB"), C("ABC");
03 private String code;
04 Tri(String code) {
05 this.code=code;
06 }
07 public String code() {
08 return code;
09 }
10 }
11 public class Soojebi{
12 public static void main(String[ ] args) {
13 Tri t=Tri.values( )[Tri.A.name( ).length( )];
14 System.out.print(t.code( ));
15 }
16 }
258 수제비 정보처리기사 실기 FINAL 모의고사
