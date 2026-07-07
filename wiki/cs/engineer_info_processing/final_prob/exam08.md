---
type: Study Note
title: "Final 모의고사 08회 (문제)"
description: "수제비 2026 정보처리기사 실기 final 모의고사 08회 문제 본문 추출본"
tags: [engineer-info-processing, final-mock-exam, exam-08]
timestamp: 2026-06-19
status: active
---

# Final 모의고사 08회 (문제)

## Page 77

10 다음은 C언어 코드이다. 실행 결과를 쓰시오.
01 #include<stdio.h>
02 include<st에ib.h> [확인 필요]
03 ffinclude <string.h>
04 int main() {
05 int i, j;
06 int row=4, col =4;
07 char (*arr)[4];
08
09 const char *str1="h이Io"; [확인 필요]
10 const char *str2="soojebi";
11 const char *src;
12 int offset=0;
13
14 arr=m 게 loc(row * sizeof(*arr));
15 if (arr==NULL) return 1;
16
17 for (i=0; i<row; i+十) {
18 if (i<2){
19 src=str1;
20 offset=i * (col-1);
21 }
22 else {
23 src 三 str2;
24 offset=(i-2) * (col-1);
25 }
26 for (j=0; j<col-1; j++) {
27 strncpy(&arr[i][j], &src[offset十j], 1);
28 if (src[offset+j]=='\0')
29 break;
30 }
31 arr[i][j]='\O';
32 }
33 for (i=0; i<row; i + +) {
34 for (j=0; j<col; j++) {
35 printf("%c", arr[i][j]);
36 }
37 printf("\n");
38 }
39 free(arr);
40 return 0;
41 }
다음 괄호 ( ) 안에 공통으로 들어갈 특징
을 영어로 쓰시오.
데이터베이스의 4가지 특징으로 Integrated
Data, Stored Data, Operational Data, ( )
이/가 있다. Integrated Data는 자료의 중복을 [확인 필요]
배제한 데이터의 모임이고, Stored Data는 저장 [확인 필요]
매체에 저장된 데이터이고, Operational Data는 [확인 필요]
조직의 업무를 수행하는 데 필요한 데이터이고,
( '은|는 여러 애플리케이션, 시스템들이 공 [확인 필요]
동으로 사용하는 데이터이다.
다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int[ ] arr={3, 5, 4, 2,1};
04 int i=0;
05 int temp=0;
06
07 do{
08 int j=i;
09 do{
10 if( arr[i]>arr[j]) {
11 temp=arr[i];
12 arr[i]=arr[j];
13 arr[j] 가emp; [확인 필요]
14 }
15 j++;
16 } while (j<5);
17 i++;
18 } while(i<4);
19
20 for(int i=0; i<5; i+十) {
21 System.out.printf(arr[i] + " ");
22 }
23 }
24 }
모의고사13회 77
## Page 78

다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 List (String) list=new LinkedList (String)();
04 list.add("Hello");
05 list.add("Hello");
06 list.add(1, "World");
07 System.out.print(list);
08 }
09 }
15 다음은 프로세스 스케줄링과 관련된 설명이
다. 괄호 ( ) 안에 들어갈 용어를 쓰시오.
프로세스 스케줄링 유형 중에서( ① )은/는
하나의 프로세스가 CPU를 차지하고 있을 때, 우 [확인 필요]
선순위가 높은 다른 프로세스가 현재 프로세스
를 중단시키고 CPU를 점유하는 스케줄링 방식 [확인 필요]
이다.
또한( ① )알고리즘중에서 ( ② )은/는
가장 짧은 시간이 소요되는 프로세스를 먼저 수
행하고, 남은 처리 시간이 더 짧다고 판단되는
프로세스가 준비 큐에 생기면 언제라도 프로세
스가 선점되는 방식이다.
14 다음은 보안 공격 기법에 대한 설명이다. 괄
호 ( ) 안에 들어갈 공격기법을 쓰시오.
•( ① )은/는 소프트웨어 개발사의 네트워크
에 침투하여 소스 코드의 수정 등을 통해 악의
적인 코드를 삽입하거나 배포 서버에 접근하여
악의적인 파일로 변경하는 방식을 통해 사용
자 pc에 소프트웨어를 설치 또는 업데이트 시 [확인 필요]
에 자동적으로 감염되도록 하는 공격기법이다.
•( ② )은/는 암호화 알고리즘의 실행 시기의
전력 소비, 전자기파 방사 등의 물리적 특성을
측정하여 암호 키 등 내부 비밀 정보를 부 채
널에서 획득하는 공격 기법이다.
①—_________________________________________________________________
②__________________________________________________________________
16 다음은 [학생] 테이블이다. 2학년부터 4학
년 학생의 학번, 이름을 검색하는 SQL 문을
BETWEEN 키워드를 사용하여 작성하시오.
[학생] 테이블
학번 이름 학년
200101 윤봉길 1
200102 안중근 3
200103 이순신 2
200104 홍범도 3
200105 김좌진 4
200106 유관순 3
200107 이봉창 2
200108 이광수 3
78 수제비 정보처리기사 실기 FINAL 모의고사
## Page 79

17 다음은 통합 인증과 관련된 내용이다. 괄호
( ) 안에 들어갈 용어를 쓰시오.
• 198이년대 중반 MIT의 Athena 프로젝트의 일 [확인 필요]
환으로 개발된 ( ① '은/는 클라이언트/서
버 모델에서 동작하며 대칭키 암호기법에 바
탕을 둔 프로토콜이다. ( ① '은/는 티켓
(Ticket)을 기반으로 동작호수는 컴퓨터 네트워크
인증 암호화 프로토콜로서 비보안 네트워크에
서 통신하는 노드가 보안 방식으로 다른 노드
에 대해 식별할 수 있게 허용한다.
• ( ② )은/는사용자가비밀번호를제공하지
않고 다른 웹사이트나 애플리케이션의 접근
권한을 부여할 수 있게 하는 개방형 표준기술
이다.
• ( ② )은/는 네이버, 카카오톡, Google과 [확인 필요]
Facebook 등의 외부 계정을 기반으로 토큰을
이용하여 간편하게 회원가입 및 로그인할 수
있게 해주는 기술이다 .
①____________________________________________
_________________________________________
18 다음은 c언어 코드이다. 출력 결과를 쓰시오.
' 다음은 데이터 링크 계층(2계층) 프로토콜에
대한 설명이다. 괄호 ( ) 안에 올바른 용어
를 쓰시오.
( ① )은/는 점대점 방식이나 다중방식의 통
신에 사용되는 iso에서 표준화한 동기식 비트 [확인 필요]
중심의 데이터 링크 프로토콜이고, ( ② )은/
는 네트워크 분야에서 두 통신 노드 간의 직접적
인 연결을 위해 일반적으로 사용되는 데이터 링
크 프로토콜이다.
①___________________________________________________________________________________
②___________________________________________________________________________________
20 테스트 하네스는 모듈의 테스트를 위한 코드
및 도구의 집합이다. 테스트 하네스의 구성요
소 중 다음 괄호 ( ) 안에 들어갈 요소를
쓰시오.
• ( ① ): 테스트 대상 컴포넌트나 모듈, 시스
템에 사용되는 테스트 케이스의 집합
• ( ② ): 애플리케이션에서 테스트 되어야 할
기능 및 특징, 테스트가 필요한 상황을 작성한
문서
01 include <stdio.h>
02 int main(){
03 int a[2][2]={{11, 22}, {44, 55}};
04 int i, sum=0;
05 int *p=a[이;
06 int length=sizeof(a)/sizeof(a[이);
07
08 for(i너; i< length; i + +)
09 sum+^lp+i);
10 printf("%d", sum);
11 return 0;
12 }
①___________________________________________________________________________________
②___________________________________________________________________________________
모의고사 13회 79
## Page 80

FINAL
모의고사 14 히
다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 include (stdio.h)
02 struct soojebi {
03 int x;
04 char y[16];
05 };
06 void fn(struct soojebi s){
07 s.y[s.x++]='><';
08 }
09 int main() {
10 struct soojebi s={ 1, "HELLO SOOJEBI" };
11 fn(s);
12 printf("%s", &s.y[s.x+ + -1]);
13 return 0;
14 }
다음은 보안에 대한 설명이다. 괄호( )안
에 들어갈 보안 관련 용어를 쓰시오.
( '은|는 독일 지멘스사의 원격 감시 제 [확인 필요]
어 시스템의 소프트웨어에 침투하여 시스템을
마비하게 하는 악성코드이다. 원자력 발전소와
송/배전망, 화학공장, 송유/가스관과 같은 산업
기반 시설에 사용되는 제어시스템에 침투하여
오동작을 유도하는 명령코드를 입력해서 시스템
을 마비시킨다.
02 다음은교환 방식에 대한 설명이다. 괄호( )
안에 들어갈 유형을 쓰시오.
• ( ① )은/는 데이터를 패킷 단위로 보내는
방식으로 회선 효율이 우수하고 비동기 전송
이 가능한 방식이다.
.( ① )의세부유형중( ② )은/는연결
경로를 확립하지 않고 각각의 패킷을 순서에
무관하게 독립적으로 전송하는 방식으로 헤더
를 붙여서 개별적으로 전달하는 비연결형 교
환 방식이다.
• ( ① )의세부유형중( ③ )은/는패킷
이 전송되기 전에 송 ■ 수신 스테이션 간의 논
리적인 통신 경로를 미리 설정하는 방식으로
목적지 호스트와 미리 연결 후 통신하는 연결
형 교환 방식이다.
04 다음 괄호( )안에 알맞은 옵션을 쓰시오.
테이블을 DROP 하려고 하는데 테이블에 외래
키(FOREIGN KEY)가 걸려 있다. 참조하는 테이블
까지 연쇄적으로 제거하려고 할 때는 ( ① )
옵션을 사용하고, 다른 테이블이 삭제할 테이블
을 참조 중이면 제거하지 않을 때는 ( ② )
옵션을 사용한다.
①____________________________________________
②____________________________________________
05 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 a=[''Hello", "Python", "World"]
02 for i in a:
03 print("abc")
①____________________________________________
②____________________________________________
③____________________________________________
80 수제비 정보처리기사 실기 FINAL 모의고사
## Page 81

06 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class A {
02 void show(int x) {System.out.print("A1 ");}
03 void show(String x) {System.out.print("A2 ");}
04 }
05 class B extends A {
06 ©Override
07 void show(int x) {System.out.print("B1 ");}
08 void show(double x) {System.out.print("B2 ");}
09 }
10 public class Soojebi {
11 public static void main(String[ ] args) {
12 A obj 三 new B( );
13 obj.show(10);
14 obj.show("test");
15 ((B)obj).show(10.5);
16 }
스 1》}______________________________________
07 다음은 운영체제와 관련한 용어 설명이다. 괄
호 ( ) 안에 들어갈 용어를 쓰시오.
• 교착상태는 다중프로세싱 환경에서 두 개 이
상의 프로세스가 특정 자원할당을 무한정 대
기하는 상태이다.
• 교착상태발생조건중( ① )은/는프로세
스가 자원을 배타적으로 점유하여 다른 프로
세스가 그 자원을 사용할 수 없는 상태를 말
한다.
• ( ② )은/는프로세스간( ① )의원리
를 보장하는 데 사용된다.
• ( ② )은/는 p(임계 구역 들어가기 전 수행),
V (임계 구역에서 나올 때 수행) 연산을 기반으로
구현한다.
①____________________________________________
②_______________________________________________
08 다음 괄호( )안에 들어갈 올바른 용어를
쓰시오.
배드 코드는 다른 개발자가 로직(Logic)을 이
해하기 어렵게 작성된 코드이다. 배드 코드 중
( ① )은/는 소스 코드가 복잡하게 얽혀 있어
이해하거 나 수정하기 어려운 코드이 다. ( ② )
은/는 아주 오래되거나 참고 문서 또는 개발자
가 없어 유지보수 작업이 어려운 코드를 말한다.
①_________________________________________
②_________________________________________
다음 그래프를 보고 맥케이브(McCabe)의 순
환 복잡도 측정 방식에 따른 복잡도를 구하
시오.
J三 _
모의고사 14회 81
## Page 82

다음은 자바 코드이다. 출력 결과를 쓰시오. : 다음은 C 프로그램이다. 출력 결과를 쓰시오.
01 public dass Soojebi{
02 public static void main(String[ ] args) {
03 try {
04 int result너0/0; [확인 필요]
05 System.out.println(result);
06 }
07 catch (ArithmeticException e) {
08 System.out.println("Cannot divide by zero");
09 }
10 catch (ArraylndexOutOfBoundsException e) {
11 System.out.println("lndex out of bounds");
12 }
13 catch (NullPointerException e) {
14 System.out.println("Null pointer exception");
15 }
16 finally {
17 System.out.println("No Problem");
18 }
19 }
20 }
잠재적 사용자의 다양한 목적과 관찰된 행동
패턴을 응집시켜 놓은 가상의 사용자를 의미
하는 용어는 무엇인지 쓰시오.
01 ffinclude<stdio.h>
02 int soojebi(char *x) {
03 int count=0, i;
04 char wordsf ]="aeiou";
05 while (*x) {
06 for(i=0; i<5; i十十) {
07 if(*x 三三 words[i]) {
08 count++;
09 break;
10 }
11 }
12 x 十+;
13 }
14 return count;
15 }
16 int main() {
17 char str[ ]="sooje";
18 int result=soojebi(str);
19 printf("%d\n", result);
20 return 0;
21 }
다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 ffinclude <stdio.h>
02 int fn(char* a){
03 int i=0;
04 for(i=0; a[i] !='\0'; i++);
05 return i;
06 }
07 int main() {
08 char a[1 이="H이o"; [확인 필요]
09 printf("%d", fn(a));
10 return 0;
11 }
82 수제비 정보처리기사 실기 FINAL 모의고사
## Page 83

1 4 다음은 EAI 구축 방식에 대한 설명이다. 괄호
( ) 안에 들어갈 방식은 무엇인지 쓰시오.
EAI의 구축 방식 중 가장 기초적인 애플리케이 [확인 필요]
션 통합방법으로 1:1 단순 통합방법을 의미하는
( ① ) 방식과 애플리케이션 사이 미들웨어
(버스)를 두어 연계하는 미들웨어 통합 방식인
( ② ) 방식이 있다.
①___________________________________________________________________________________
②___________________________________________________________________________________
15 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 interface A {
02 default void show() {
03 System.out.print("A");
04 }
05 }
06 interface B {
07 default void show() {
08 System.out.print("B");
09 }
10 }
11 class C implements A, B {
12 public void show() {
13 B.super.show( );
14 A.super.show( );
15 System.out.print("C");
16 }
17 }
18 class D extends C {
19 public void show() {
20 System.out.println("D");
21 super.show( );
22 System.out.println("E");
23 }
24 }
25 public class Soojebi {
26 public static void main(String[ ] args) {
27 C obj1=new C( );
28 obj1.show( );
29 }
30 }
16 다음 괄호( )안에 들어갈 대칭 키 알고
리즘을 쓰시오.
대칭 키 암호 방식은 암호화 알고리즘의 한 종
류로, 암호화와 복호화에 같은 암호 키를 쓰는
알고리즘이다. 대칭 키 암호 알고리즘의 종류 중
에서 ( ① )은/는 1999년 국내 한국인터넷진
흥원(KISAKI 개발한 블록 암호화 알고리즘으로,
128비트 비밀키로부터 생성된 16개의 64비트 라
운드 키를 사용하여 총 16회의 라운드를 거쳐
128비트의 평문 블록을 128비트 암호문 블록으
로 암호화하여 출력하는 방식이고, ( ② )은/
는 2001년 미국 표준 기술  연구소(NIST)에서 발
표한 블록 암호화 알고리즘으로, 블록 크기는
128비트이며, 키 길이에 따라 128비트, 192비트,
256비트로 분류되고, 라운드 수는 10, 12, 14라
운드로 분류되며, 한 라운드는 SubBytes, Shift-
Rows, MixColumns, AddRoundKey의 4가지 계 [확인 필요]
층으로 구성된다.
①___________________________________________________________________________________
②___________________________________________________________________________________
다음 괄호 ( ) 안에 들어갈 구성요소를 쓰
시오.
객체지향 모델링 시 클래스의 속성 및 연산과
클래스 간 정적인 관계를 표현한 다이어그램
인 클래스 다이어그램(Class Diagram)의 구성요
소 중 ( ① )은/는 클래스의 구조적 특성에
이름을 붙인 것으로 특성에 해당하는 인스턴스
가 보유할 수 있는 값의 범위를 기술한  것이고,
( ② )은/는 이름, 타입, 매개변수들과 연관
된 행위를 호출하는데 요구되는 제약사항들을
명시하는 클래스의 행위적 특징이다.
①___________________________________________________________________________________
②___________________________________________________________________________________
모의고사 14회 83
## Page 84

18 다음 괄호( )안에 들어갈 용어를 쓰시오.
( ① )은/는( ② )보다가벼운, 독립적으
로 수행되는 순차적인 제어의 흐름이며, 실행 단
위이고, ( ② '은/는 CPU에 의해 처리되는 [확인 필요]
사용자 프로그램, 시스템 프로그램, 즉 실행 중
인 프로그램을 의미하며, 작업(Job) 또는 태스크
(Task) 라고도 한다.
①_______________________________________________
②_______________________________________________
다음은 자바 코드이다. 출력 결과를 쓰시오.
01 abstract class Soojebi{
02 abstract String getName( );
03 }
04 class Soojebil extends Soojebi{
05 String getName(){
06 return "soojebil";
07 }
08 }
09 class Soojebi2 extends Soojebi{
10 String getName(){
11 return "soojebi2";
12 }
13 }
14 abstract class Si』perSoojebiFactory{
15 abstract Soojebi createSoojebi(String name);
16 }
17 class SoojebiFactory extends SuperSoojebiFactory {
18 Soojebi createSoojebi(String name){
19 switch(name){
20 case "soojebil":
21 return new Soojebil();
22 case "soojebi2":
23 return new Soojebi2( );
24 }
25 return null;
26 }
27 }
28 class SoojebiMain{
29 public static void main(String[ ] args){
30 SoojebiFactory sf=new SoojebiFactory( );
31 Soojebi s1 =sf.createSoojebi("soojebi1 ");
32 Soojebi s2=sf.createSoojebi("soojebi2");
33 System.oulprintln(s1.getName( )+s2.getName( ));
34 }
35 }
다음은 C언어 코드이다. 밑줄에 들어갈 가장
적합한 답을 쓰시오.
01 include <stdio.h>
02 #define MAX_SIZE 10
03 int stack[MAX_SIZ티; [확인 필요]
04 int top=-1;
05 void push(int item){
06 if (top 三 ① )
07 printf("stack is full\n");
08 else
09 sta 아<[ + 十 top]=item;
10 }
11 int pop() {
12 jf(top== _②_) {
13 printf("stack is empty\n");
14 return -1;
15 }
16 return sta아<[top——]; [확인 필요]
17 }
18 int is_empty(){
19 if(top= = -1)
20 return 1;
21 else
22 return 0;
23 }
24 int is_full() {
25 if(top>=MAX_SIZE)
26 return 1;
27 else
28 return 0;
29 }
30 int main() {
31 push(20);
32 push(30);
33 push(40);
34 while(!is_empty()){
35 printf("value=%d\n", pop());
36 }
37 return 0;
38 }
①_______________________________________________
②_______________________________________________
84 수제비 정보처리기사 실기 FINAL 모의고사
## Page 85

수제비
모의고사 15회
01 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 import java.util.Sta 아<;
02 public class Soojebi {
03 public static void main(String[ ] args) {
04 Stack<Integer>s=new Stack<>( );
05 s.push(10);
06 s.push(20);
07 System.out.print(s.pop()+" ");
08 s.push(30);
09 System.out.print(s.peek()十" ");
10 System.out.print(s.size( ));
11 }
12 }
02 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 typedef struct _soojebi{
03 char *str;
04 int num[3];
05 } soojebi;
06 int dec(int tmp){
07 return tmp A 0xA5;
08 }
09 int enc(int tmp){
10 return tmp A 0xA5;
11 }
12 int sum(soojebi *p){
13 return dec(enc(p—>num[2]));
14 }
15 int main(){
16 soojebi s[2]={
17 "Kim", {0xA0, 0xA5, OxDB},
18 "Lee", {0xA0, OxED, 0x81}
19 };
20 soojebi *p=s;
21 int result=0, i;
22 for(i=0;i<2;i + +){
23 result+=sum(&p[i]);
24 }
25 printf("%d", result);
26 return 0;
27 }
02 다음 괄호( )안에 들어갈 올바른 용어를
쓰시오.
• ( ① )은/는 AS(Autonomous System; 자치 시
스템; 자율 시스템) 내에서 사용하는 거리 벡터
알고리즘에 기초하여 개발된 내부 라우팅 프
로토콜이다.
• ( ① '은/는 거리 벡터 라우팅 기반 메트릭
정보를 인접 라우터와 주기적으로 교환하여
라우팅 테이블을 갱신하고 라우팅 테이블을
구성하고계산하는( ② )알고리즘을사용
한다. 또한 최대 홉 수(Hop Count)를 15개로 제
한한다.
①___________________________________________________________________________________
②___________________________________________________________________________________
모의고사15회 85
## Page 86

원거리 통신망(WAN; Wide Area Network)은
넓은 지리적 거리 ■ 장소를 넘나드는 네트워크
이다. 괄호 ( ) 안에 들어갈 원거리 통신망
연결 기술에  대해 쓰시오.
• ( ① )은/는 통신 사업자가 사전에 계약을
체결한 송신자와 수신자끼리만 데이터를 교환
하는 방식으로 점대점 프로토콜(PPP), HDLC
프로토콜이 쓰인다.
• ( ② '은/는 물리적 전용선을 활용하여 데
이터 전달 경로가 정해진 후 동일 경로로만 전
달되는 방식으로 데이터를 동시에 전송할 수
있는 양을 의미하는 대역폭이 고정되고 안정
적인 전송률을 확보할 수 있고, ISDN 프로토
콜이 쓰인다.
•( ③ )은/는 전체 메시지를 각 노드가 수용
할 수 있는 크기(패킷)로 잘라서 보내는 방식으
로 X.25, 프레임 릴레이 프로토콜이 쓰인다.
①____________________________________________
②____________________________________________
③____________________________________________
다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 ffinclude<stdio.h>
02 int main(){
03 char s[
04 if(s[O]){
05 printf("A");
06 }
07 else{
08 printf("B");
09 }
10 return 0;
11 }
06 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 import java.utiLArrays;
02 import java.util.List;
03 public class Soojebi {
04 public static void main(String[ ] args) {
05 LisKString>words=Arrays.asl_ist("alpha", "beta", "gamma");
06 words.replaceAII(s-)s.length( )%2= =0 ?
07 s.toUpperCase( ):new String Builder(s).
08 reverse( ).toString());
09 words.forEach(word - >
10 System.out.print (word+" "));
11 }
12 }
다음 괄호 ( ) 안에 들어갈 용어를 쓰시오.
소프트웨어 개발 보안 용어 중 ( ① )은/는
위협이 발생하기 위한 사전 조건으로 시스템
의 정보 보증을 낮추는 데 사용되는 약점이고,
( ② )은/는위협이( ① )을/를 이용하여
조직의 자산 손실 피해를 가져올 가능성이다.
①____________________________________________
②____________________________________________
08 다음이 설명하는 데이터베이스 기법을 쓰시오.
정규화된 엔터티, 속성, 관계에 대해 성능 향상
과 개발 운영의 단순화를 위해 중복, 통합, 분리
등을 수행하는 데이터 모델링 기법
86 수제비 정보처리기사 실기 FINAL 모의고사
