---
type: Study Note
title: "Final 모의고사 13회 (문제)"
description: "수제비 2026 정보처리기사 실기 final 모의고사 13회 문제 본문 추출본"
tags: [engineer-info-processing, final-mock-exam, exam-13]
timestamp: 2026-06-19
status: active
---

# Final 모의고사 13회 (문제)

## Page 127

13 다음 괼■호( )안에 알맞은 특성을 쓰시오.
보안의 3대 요소 중 ( ① '은|는 정당한 방법 [확인 필요]
을 따르지 않고서는 데이터가 변경될 수 없으며,
데이터의 정확성 및 완전성과 고의/악의로 변경
되거나 훼손 또는 파괴되지 않음을 보장하는 특
성이고,( ② )은/는 인가되지 않은 개인 혹은
시스템 접근에 따른 정보 공개 및 노출을 차단하
는 특성이다.
①_______________________________________________
②_______________________________________________
14 다음 괄호( )안에 알맞은 값 및 클래스를
쓰시오.
• IPv4는 길이가 32bit이며, ( ① )비트씩 네 [확인 필요]
부분으로 나눈다.
• ( ② ) 클래스는 128.0.0.0 〜 191.255.255.
255의 IP 범위를 갖고, ( ③ ) 클래스는 224.
0.0.0〜239.255.255.255의 IP 범위를 갖는다.
①_______________________________________________
②_______________________________________________
③_______________________________________________
다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 #include (stdio.h)
02 int fn(char *p){
03 int s=1, num 三0;
04 jf(*p 三 ='\n')
05 return 0;
06 if(*p= = '—')
07 s=-1;
08 while(*p){
09 if(*p>='0'&&*p<='9)
10 num=num*8+*p—'O';
11 }
12 p+十;
13 }
14 return num*s;
15 }
16 int main(){
17 char *x="hi52";
18 int a=fn(x);
19 printf("%d", a);
20 return 0;
21 }
16 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 String str="Soojebi_Java";
04 str=str.trim( ).replace("_", " ").tol_owerCase( );
05 String result三str.substring(str.indexOf("j"), str.lengthf ));
06 System.out.println(result);
07 }
08 }
모의고사23회 127
## Page 128

다음은 C언어 코드이다. 출력 결과를 쓰시오.
(단, int 형은 4바이트로 가정한다.)
01 #include<stdio.h>
02 int main(){
03 int a[10];
04 int b[10][10];
05
06 printf("%d", sizeof(a));
07 printf("%d", sizeof(b));
08 printf("%d", sizeof(b[1]));
09 printf("%d", sizeof(b[1][0]));
10 return 0;
11 }
18 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi{
02 public static void main(String[ ] args){
03 int[ ] arr={1,2,3,4,5};
04 int[ ] temp={1,2,4,6,8};
05 int idx=0;
06 boolean flag;
07
08 for(int i=O;i<arr.length;i++){
09 flag=false;
10 if(arr[i]==temp[i]){
11 flag=true;
12 }
13
14 if(!flag){
15 temp[idx++]=arr[i];
16 System.out.print(temp[idx]);
17 }
18 }
19 }
20 }
19 다음은 시스템 보안 공격과 대응 방안에 대한
설명이다. 괄호 ( ) 안에 들어갈 용어를 쓰
시오.
버퍼 오버플로우 공격은 스택 영역에 할당된 버
퍼 크기를 초과하는 양의 데이터(실행 가능 코드)
를 입력하여 복귀 주소를 변경하고 공격자가 원
하는 임의의 코드를 실행하는 공격 기법이다.
버퍼 오버플로우 공격 기법에 대한 대응 방안
에는( ① )와/과( ② )이/가 있다. 먼저
( ① )은/는 카나리(Canary)라고 불리는 무결
성 체크용 값을 복귀 주소와 변수 사이에 삽입
해 두고, 버퍼 오버플로우 발생 시 카나리 값을
체크, 변할 경우 복귀 주소를 호출하지 않는 방
식으로 대응하는 기법이고, ( ② )은/는 함수
시작 시 복귀 주소를 Global RET라는 특수 스택 [확인 필요]
에 저장해 두고, 함수 종료 시 저장된 값과 스택
의 RET 값을 비교해 다를 경우 오버플로우로 간
주하고 프로그램 실행을 중단하는 기법이다.
①___________________________________________________________________________________
②___________________________________________________________________________________
20 다음은 아키텍처를 설계할 때 참조할 수 있는
전형적인 해결 방식인 아키텍처 패턴(Patterns)
의 유형에 대한 설명이다. 괄호 ( ) 안에 들
어갈 유형을 쓰시오.
( ① )은/는 각각의 서브 시스템들이 계층 구
조를 이루며 서로 마주 보는 두 개의 계층 사
이에서만 상호작용이 이루어지는 패턴이고,
( ② )은/는 데이터 스트림을 생성하고 처리
하는 시스템에서 사용 가능한 단방향 패턴으로
서브 시스템이 입력 데이터를 받아 처리하고, 결
과를 다음 서브 시스템으로 넘겨주는 과정을 반
복한다.
①___________________________________________________________________________________
②___________________________________________________________________________________
1 28 수제비 정보처리기사 실기 FINAL 모의고사
## Page 129

수제비 FINAL
모의고사 24히
01 다음은 C 언어 코드이다. 출력 결과를 쓰시오. 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 int main(){
03 int i=2;
04 while (i——
05 printf("%d", i);
06 }
07 printf("%d", i);
08 return 0;
09 }
02 다음 괄호( )안에 공통으로 들어갈 용어
를 쓰시오.
( '은/는 수집된 후 저장은 되어 있지만, 분
석에 활용되지는 않는 다량의 데이터를 의미한
다.( )은/는 향후 사용될 가능성이 있다는
이유로 삭제되지 않아 공간만 차지하고 있으며,
보안 위협을 초래하기도 한다.
01 class A {
02 int count=1;
03 void displayf) {System.out.print("A" + count+" ");}
04 }
05 class B extends A {
06 int count=2;
07 void display() {System.out.print("B"+count);}
08 }
09 public class Soojebi {
10 public static void main(String[ ] args) {
11 A obj 三 new B( );
12 obj.display( );
13 System.out.print(obj.count);
14 }
15 }
0E 다음 [정처기] 테이블에서 쿼리를 실행했을
때 결과는 [결과] 테이블과 같다. [결과] 테이
블의 밑줄 친 곳에 들어갈 값을 쓰시오.
[정처기] 테이블
03 사설 네트워크에 속한 여러 개의 호스트가 하
나의 공인 ip 주소를 사용하여 인터넷에 접속
하기 위한 네트워크 주소 변환 기술은  무엇인
지 쓰시오.
[쿼리]
이름 필기 실기
엑소 80 NULL
BTS NULL 100
세븐틴 NULL NULL
SELECT COUNT(필기*실기) FROM 정처기;
[결과]
COUNT(필기*실기)
모의고사24회 129
## Page 130

06 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 int main(){
03 char A='A';
04 char B=66;
05 char c[3]={A, B};
06
07 if(c[2]);
08 printf("%c%d", A, B);
09
10 printf("%s", c);
11
12 if(c[1]= = 'B');
13 printf("%c%c", A十 1, B十 1);
14
15 return 0;
16 }
08 다음이 설명하는 개발 도구는 무엇인지 쓰시오.
• 소프트웨어 변경 사항을 관리하기 위해서 형
상 식별, 통제, 감사, 기록을 수행하는 도구
• 개발자들이 작성한 코드와 리소스 등 산출물
에 대한 관리를 위한 도구
• 프로젝트 진행 시 필수로 포함되는 도구
• 대표적으로 CVS, Subversion, Git가 있음 [확인 필요]
다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 x=[65, 66, 97, 98]
02 print(all(x))
03 print(any(x))
04 print(chr(x[이))
05 print(divmod(x[1], x[이))
다음은 소프트웨어 개발 방법론에 대한 설명
이다. 괄호 ( ) 안에 들어갈 방법론을 보기
에서 골라 기호로 쓰시오.
• ( ① . )는 정보시스템 개발에 필요한 관리
절차와 작업 기법을 체계화한 방법론으로 대
형 프로젝트를 수행하는 체계적인 방법론이다.
• ( ② )는 특정 제품에 적용하고 싶은 공통
된 기능을 정의하여 개발하는 방법론으로 임
베디드 소프트웨어를 작성하는 데 유용한 방
법론이다.
[보기]
@ Structured Development
@ Information Engineering Development
© Object-Oriented Development
@ Agile Development
@ Product Line Development
(D Spiral Development
⑨ Prototyping Development
10 다음은 [사전] 테이블이다. [결과] 테이블처럼
'sy'로 시작되고, 'm'으로 끝나는 문자열을 찾
기 위한 쿼리를 작성하시오.
[사전] 테이블
단어 뜨
system 체계
symbol 상징
symmetry 대칭
[결과]
단어 뜨
system 체계
①___________________________________________________________________________________
②___________________________________________________________________________________
130 수제비 정보처리기사 실기 FINAL 모의고사
## Page 131

다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class Parent{
02 int compute(int num){
03 if(num<=1){
04 return 1;
05 }
06 return num*compute(num-1);
07 }
08 }
09 class Child extends Parent{
10 int compute(int num){
11 if(num<=1){
12 return 1;
13 }
14 return num*compute(num-2);
15 }
16 }
17 public class Soojebi {
18 public static void main(String[ ] args) {
19 Parent obj=new Child( );
20 System.out.print(obj.compute(4));
21 }
22 }
다음은 접근 통제와 관련한 용어이다. 괄호
( )안에 들어갈용어를쓰시오.
• ( ① )은/는 자신이 누구라고 시스템에 밝
히는 행위로 객체에게 주체가 자신의 정보를
제공하는 활동이다.
• ( ② )은/는 주체의 신원을 검증하기 위한
활동으로 주체의 신원을 객체가 인정해 주는
행위이다.
• ( ③ '은/는 인증된 주체에게 접근을 허용
하는 활동으로 특정 업무를 수행할 권리를 부
여하는 행위이다.
①_______________________________________________
②_______________________________________________
③_______________________________________________
13 다음은 결합도의 종류에 대한 설명이다. 괄호
( )안에들어갈용어를쓰시오.
•( ① '은/는 모듈 간의 인터페이스로 전달
되는 파라미터를 통해서만 모듈 간의 상호 작
용이 일어나는 경우의 결합도이다.
•( ② )은/는 모듈 간의 인터페이스로 배열
이나 객체, 구조 등이 전달되는 경우의 결합
도로 두 모듈이 동일한 자료 구조를 조회하는
경우의 결합도이다.
①____________________________________________
②_______________________________________________
요청 헤더의 Content-Length# 비정상적으
로 크게 설정하여 메시지 바디 부문을 매우
소량으로 보내 계속 연결 상태를 유지시키는
공격은 무엇인지 쓰시오.
1 5 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 String str="soojebiisgood";
04 System.out.println(sjbMethod(str));
05 }
06 static String sjbMethod(String str) {
07 String result="";
08 for(int i=0; i<str.length( ); i++) {
09 char c=str.charAt(i);
10 if (result.indexOf(c)= = — 1) {
11 res니t+=c; [확인 필요]
12 }
13 }
14 return res니t; [확인 필요]
15 }
16 }
모의고사24회 131
## Page 132

16 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 include<stdio.h>
02 int isPrime(int number) {
03 int i;
04 for (i=2; i< number; i++) {
05 if (number%i==0) return 0;
06 }
07 return 1;
08 }
09 int main(){
10 int number=88711, max_div=0, i;
11 for (i=2; i<number; i++)
12 if (isPrime(i)==1 & & number%i = =0)
13 max_div=i;
14 printf("%d", max_div);
15 return 0;
16 }
다음 괄호 ( ) 안에 들어갈 공격 기법을 쓰
시오.
사용자들에게 랜섬웨어를 감염시키기 위한 다양
한 공격 기법들을활용하고있다.그 중 ( ① )
공격 기법은 악의적인 해커가 불특정 웹 서버와
웹 페이지에 악성 스크립트를 설치하고, 불특정
人요자 접속 시 사용자 동의 없이 실행되어 의도
된 서버(멀웨어 서버)로 연결하여 감염시키는 공
격 기법이고,( ② )은/는특정인에대한 표적
공격을 목적으로 특정인이 잘 방문하는 웹 사이
트에 악성 코드를 심거나 악성 코드를 배포하는
URL로 자동으로 유인하여 감염시키는 공격 기 [확인 필요]
법이다.
①_____________________________________________
②_____________________________________________
18 논리의 기술에  중점을 둔 도형식 표현 방법으
로 조건이 복합되어 있는 곳의 처리를 시각적
으로 명확히 식별하는 데 사용되는 구조적 방
법론 도구를 무엇이라고 하는지 쓰시오.
다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int n=5;
04 for (int i=1; i<n; i + +) {
05 System.out.print(soo(i)+"
06 }
07 }
08 static int soo(int n) {
09 if (n<=1) return n;
10 return soo(n—1)十soo(n—2);
11 }
12 }
다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 #include <stdio.h>
02 int main(){
03 char *p="hello";
04 int i;
05 for(i=0; i<3; i+十){
06 printf("%c", *p);
07 p++;
08 }
09 return 0;
10 }
1 32 수제비 정보처리기사 실기 FINAL 모의고사
## Page 133

모의고사 25회
01 다음은 파이썬 코드이다. 출력 결과를 쓰시오. 0Z 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 x=[1, 2, 3, 4, 5]
02 x=list(map(lambda num: num*3 if num % 2=0 else num*2, x))
03 print(x)
02 프로세스 관련 용어에 대한 설명이다. 괄호
( )안에들어갈용어를쓰시오.
( ① )은/는 초당 처리건수를 의미하며, 초당
몇 개의 트랜잭션을 처리할 수 있는지 나타내는
서비스성능지표이다. 또한( ② )은/는 프로
세스들이 입력되어 수행하고 결과를 산출하기까
지 소요되는 시간이다.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int n=30;
04 String result="";
05 for (int i=2; i<=n; i++) {
06 while (n%i==0) {
07 result+=i;
08 n/=i;
09 }
10 }
11 System.out.println(result);
12 }
13 }
①___________________________________________________________________________________
②___________________________________________________________________________________
0E 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 print(('dog'*2)[: -4 : -1])
02 print('ant'+'cat'*2)
02 다음 괄호( )안에 들어갈 용어를 쓰시오.
( ① )은/는 AS 상호 간(Inter-AS 또는 Inter-
Domain)에 경로 정보를 교환하기 위한 라우팅 프
로토콜로 변경 발생 시 대상까지의 가장 짧은 경
로를 ( ② ) 알고리즘을 통해 선정하고, TCP
연결(Port 179)을 통해 자치 시스템(AS)으로 라우
팅 정보를 신뢰성 있게 전달하는 특징이 있다.
①____________________________________________
②____________________________________________
06 다음이 설명하는 용어를 쓰시오.
• 군중과 아웃소싱의 합성어로 클라우드 컴퓨팅
이 실용화되면서 가능하게 된 정보 기술 (IT) 아
웃소싱 전략의 하나이다.
• 기업 활동의 전 과정에 소비자 또는 대중이 참
여할 수 있도록 일부를 개방하고 참여자의 기
여로 기업 활동 능력이 향상되면 그 수익을 참
여자와 공유하는 방법이다.
모의고사 25회 1 3:
## Page 134

다음은 자바 코드이다. 출력 결과를 쓰시오. 08 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 class A {
02 void display(int x) {
03 System.out.print("A1");
04 }
05 void display(String x) {
06 System.out.print("A2");
07 }
08 void show() {
09 System.out.print("A3");
10 }
11 }
12 class B extends A {
13 void display(int x) {
14 System.out.print("B1 ");
15 }
16 void display(double x) {
17 System.out.print("B2");
18 }
19 void show() {
20 System.out.print("B3");
21 }
22 }
23 public class Soojebi {
24 public static void main(String[ ] args) {
25 A obj1=new B( );
26 B obj2=new B( );
27 obj1.display(10);
28 obj1.display("test");
29 obj2.display(10.5);
30 obj2.show( );
31 }
32 }
01 include <stdio.h>
02 void Soojebi(int n) {
03 if(n<=1){
04 return;
05 }
06 printf("%d", n);
07 Soojebi(n-I);
08 printf("%d", n);
09 }
10 int main(){
11 Soojebi(3);
12 return 0;
13 }
다음이 설명하는 보안 공격 기법은 무엇인지
쓰시오.
공격자는 출발지 IPS 공격 대상 IP로 위조하여 [확인 필요]
다수의 반사 서버로 요청 정보를 전송, 공격 대
상자는 반사 서버로부터 다량의 응답을 받아서
서비스 거부(DoS)가 되는 공격 기법
다음이 설명하는 보안 관련 용어를 쓰시오.
• 온라인상에서 범죄와 같은 불법적인 행위를
수행하기 위해 제작된 컴퓨터 프로그램으로,
공격용 툴킷으로 불림
• 악성 코드로 구성된 프로그램이 사용자를 속
여 PC에 설치되면 불법적으로 정보를 수집하 [확인 필요]
거나 PC의 자원을 사용하여 원하는 대상을 공 [확인 필요]
격하는 용도로 사용
• 키로거, 스파이웨어, 브라우저 하이재커 등이
속함
134 수제비 정보처리기사 실기 FINAL 모의고사
## Page 135

다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 x=0
02 a=[1, 2, 3, 4, 5, 6, 7, 8]
03 b=a[:: 2]
04 for i in range(0, 3):
05 x+=b[i]
06 print(x)
다음은 인증 기술의  유형이다. 괄호 ( ) 안
에 들어갈 인증 기술의  유형을 쓰시오.
• ( ① )은/는 사용자가 기억하고 있는 것으
로 Something You Know라고 표현할 수 있다. [확인 필요]
• ( ② '은/는 사용자의 특징을 활용한 것으
로 Something You Do라고 표현할 수 있다. [확인 필요]
①__________________________________________________________________
②__________________________________________________________________
다음은 블랙박스 테스트 기법에 대한 설명이
다. 괄호 ( ) 안에 들어갈 유형을 보기에서
골라서 기호로 쓰시오.
• ( ① )는 테스트 대상 •시스템이나 객체의
상태를 구분하고, 이벤트에 의해 어느 한 상태
에서 다른 상태로 전이되는 경우의 수를 테스
트하는 기법이다.
• ( ② )는 테스트 데이터값들 간에 최소한
한 번씩을 조합하는 방식이며, 이는 커버해야
할 기능적 범위를 모든 조합에 비해 상대적으
로 적은 양의 테스트 세트로 구성하기 위한 테
스트기법이다.
[보기]
@ Equivalence Partitioning Testing
© Decision Table Testing
© State Transition Testing
@ Use Case Testing
@ Classification Tree Method Testing
@ Cause-Effect Graph Testing
® Pairwise Testing
①___________________________________________________________________________________
②___________________________________________________________________________________
다음 각각의 지문에서 설명하는 공격기법 및
보안 용어를 보기에서 골라서 기호로 쓰시오.
① printf 등의 함수에서 문자열 입력 형식을 잘
못 입력하는 경우에 나타난다. 이전까지 입력
된 문자열의 길이만큼 해당 변수에 저장시키
기 때문에 메모리의 내용도 변조 가능하다.
② 한정된 자원을 동시에 이용하려는 여러 프로
세스가 자원의 이용을 위해 경쟁을 벌이는
현상을 이용하는 공격 기법이다.
③ 바이러스나 명백한 악성 코드를 포함하지 않
는 합법적 프로그램이면서도 사용자를 귀찮
게 하거나 위험한 상황에 빠뜨릴 수 있는 프
로그램이 다.
[보기]
@ 키로거 공격(Key Logger Attack)
® 루트킷(Rootkit)
© 포맷 스트링 공격 (Format String Attack)
@ ROP(Return Oriented Programming)
© 스미싱(Smishing)
(D 봇넷(Botnet)
⑨ 레이스 컨디션 공격(Race Condition Attack)
@ 스피어 피싱(Spear Phishing)
(D 그레이웨어(Grayware)
(D APT 공격(Advanced Persistent Threat)
® 제로데이 공격(Zero Day Attack)
① SQL 인젝션 공격(SQL Injection Attack)
①___________________________________________________________________________________
②___________________________________________________________________________________
③___________________________________________________________________________________
모의고사 25회 135
## Page 136

[성적] 테이블을 이용하여 쿼리를 실행한 결
과는 [결과] 테이블과 같다. [결과] 테이블에
밑줄친 곳에 들어갈 값을 쓰시오.
[성적] 테이블
[쿼리]
이름 과목
지기쌤 DB
두음쌤 DB
수제비쌤 알고리즘
보안쌤 알고리즘
클라우드쌤 알고리즘
빅데이터쌤 알고리즘
정보 주체가 기관으로부터 자기 정보를 직접
내려받아 이용하거나 제 3자 제공을 허용하
는 방식으로 정보 주체 중심의 데이터 활용
체계이자 개인이 정보 관리의 주체가 되어 능
동적으로 본인의 정보를 관리하고, 본인의 의
지에 따라 신용 및 자산관리 등에 정보를 활
용하는 일련의 과정을 무엇이라고 하는지 쓰
시오.
SELECT COUNT(DISTINCT 과목) FROM 성적;
[결과]
COUNT(DISTINCT 과목)
16 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int x=8;
04 int y=3;
05 int z=5;
06 int result=(x|y)&(z<<y)%x+z*y-(xAz)/y;
07 System.out.println(result);
08 }
09 }
18 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 #include <stdio.h>
02 include<string.h>
03 #define MAX_RECORDS 4
04 #define MAX_DIVISION_LENGTH 20
05 typedef struct {
06 int id;
07 int subid;
08 char division[MAX_DIVISION_LENGTH];
09 int score;
10 } Record;
11
12 int main() {
13 int i, sum1=0, sum2=0;
14 Record r[MAX_RECORDS]={
15 {1,101, "computer", 100},
16 {2,101, "computer", 80},
17 {3, 201, "marketing", 90},
18 {4, 202, "marketing", 80}
19 };
20 for(i=0;i<MAX_RECORDS;i+十) {
21 if (strcmp(r[i].division, "computer") ==0) {
22 sum1 +=r[i].score;
23 }
24 else if(strcmp(r[i].division, "marketing")==O) {
25 sum2 +=r[i].score;
26 }
27 }
28 printf("%d %d\n", sum1, sum2);
29 return 0;
30 }
136 수제비 정보처리기사 실기 FINAL 모의고사
