---
type: Study Note
title: "Final 모의고사 10회 (문제)"
description: "수제비 2026 정보처리기사 실기 final 모의고사 10회 문제 본문 추출본"
tags: [engineer-info-processing, final-mock-exam, exam-10]
timestamp: 2026-06-19
status: active
---

# Final 모의고사 10회 (문제)

## Page 97

09 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class Soojebi{
02 static private Soojebi instance=null;
03 private int count=0;
04 static public Soojebi get(){
05 instance=new Soojebi( );
06 return instance;
07 }
08 public void count(){ count++;}
09 public int getCount(){return instance.count;}
10 }
11
12 public class Soojebi2{
13 public static void main(String[ ] args){
14 Soojebi s1 =Soojebi.get();
15 s1.count( );
16 Soojebi s2=Soojebi.get( );
17 s2.count( );
18
19 System.out.print(s1 ,getCount( ));
20 }
21 }
1 o 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 a=list(range(1,10, 2))
02 for i in range(2, 4):
03 print(a.pop(i), end=")
04
05 print(sum(a))
다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 include <string.h>
03 int main() {
04 charf[6]="AC—5*";
05 char s[6]="";
06 int i, p=-1;
07 for(i=0; i<strlen(f); i++){
08 switch(f[i]){
09 case
10 s[p—1]=s[p]—s[p—1];
11 p—;
12 break;
13 case '*':
14 s[p—1]=s[p]*s[p—1];
15 p—;
16 break;
17 default:
18 s[++p]=f[i]—'O';
19 }
20 }
21 printf("%d", s[p]);
22 return 0;
23 }
과도한 GET 메시지를 이용하여 웹 서버의 과
부하를 유발시키는 공격으로 HTTP 캐시 옵
션을 조작하여 캐싱 서버가 아닌 웹 서버가
직접 처리하도록 유도, 웹 서버 자원을 소진
시키는 서비스 거부 공격기법은 무엇인지 쓰
시오.
모의고사 17회 9
## Page 98

13 다음은 스키마에 대한 설명이다. 괄호( )
안에 들어갈 용어를 쓰시오.
• ( ① )은/는 사용자나 개발자의 관점에서
필요로 하는 데이터베이스의 논리적 구조로
사용자 뷰를 나타낸다.
• ( ② '은/는 물리적 저장 장치의 관점에서
보는 데이터베이스 구조로 실제로 데이터베이스
스에 저장될 레코드의 형식을 정의한다.
다음은 키의 종류에 대한 설명이다. 괄호 ( )
안에 들어갈 키를 쓰시오.
• ( ① ): 후보 키 중에서 기본 키로 선택되
지 않은 키
• ( ② ): 릴레이션을 구성하는 모든 튜플에
대해 유일성은 만족하지만, 최소성은 만족하
지 못하는 키
①___________________________________________________________________________________
②___________________________________________________________________________________
①___________________________________________________________________________________
②___________________________________________________________________________________
다음은 자바 프로그램이다. 출력 결과를 쓰
시오.
16 다음은 [학생] 테이블이다. 3학년이 아닌 학
생의 학번을 출력하는 쿼리를 작성하시오.
[학생] 테이블
01 public class Soojebi{
02 public static void main(String[ ] args) {
03 try {
04 int x[ ]={10, 20, 30};
05 System.out.println(10+x[10]);
06 }
07 catch (ArithmeticException e) {
08 System.out.print("A");
09 }
10 catch(ArraylndexOutOfBoundsException e) {
11 System.out.print("B");
12 }
13 catch (NullPointerException e) {
14 System.out.print("C");
15 }
16 finally {
17 System.out.print("D");
18 }
19 }
20 }
[결과]
학번 이름 학년
202101 윤봉길 1
202102 안중근 3
202103 이순신 2
202104 홍범도 3
202105 김좌진 4
202106 유관순 3
202107 이봉창 2
학번
202101
202103
202105
202107
98 수제비 정보처리기사 실기 FINAL 모의고사
## Page 99

기억 공간 15K, 22K, 23K, 거K 순으로 빈 공
간이 있을 때 기억 장치 배치 전략으로 "First
Fit", "Best Fit", "Worst Fit"을 사용하여 17K
의 프로그램을 적재할 경우 내부 단편화의 크
기는 각각 얼마인지 쓰시오.
① First Fit 내부 단편화 크기:
② Best Fit 내부 단편화 크기:
③ Worst Fit 내부 단편화 크기:
18 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 interface Component {void op( );}
02 class Base implements Component {
03 public void op() {System.out.print("A");}}
04 abstract class Decorator implements Component {
05 protected Component c;
06 public Decorator(Component c) {this.c=c;}
07 public void op() { c.op( );}
08 }
09 class ConcreteDeco extends Decorator {
10 public ConcreteDeco(Component c) {super(c);}
11 public void op() {super,op( ); System.out,print("B");}
12 }
13 public class Soojebi {
14 public static void main(String[ ] args) {
15 Component obj=new ConcreteDeco(new Base( ));
16 obj.op( );
17 }
18 }
19 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 int Soojebi(int base, int exp){
03 int i, result=1;
04 for(i=0; i<exp; i++){
05 result *=base;
06 return result;
07 }
08 }
09
10 int main(){
11 printf("%d", Soojebi(2,10));
12 return 0;
13 }
20 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 def fn(n):
02 x=[True] * (n+1)
03 x[이=x[1]=False
04
05 P=2
06 while p*p<=n:
07 if><[p]:
08 for i in range(p*p, n 十 1, p):
09 x[i]=False
10 p+=1
11
12 primes=[i for i in range(n+1) if x[i]]
13 return primes
14
15 p=fn(11)
16 print(p)
모의고사 17회 99
## Page 100

수제비 E
모의고사 18회
다음은 C언어 코드이다. 출력 결과를 쓰시오. 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 ffinclude (stdio.h)
02 #define SIZE 3
03 enum level {LOW=80, MID=90, HIGH=100 };
04 struct soojebi {
05 int a, b, c;
06 enum level Iv;
07 };
08 enum level fn3(int a) {
09 switch (a/10) {
10 case 10:
11 return HIGH;
12 case 9:
13 return MID;
14 default:
15 return LOW;
16 }
17 }
18 void fn1 (struct soojebi *p) {
19 int i;
20 for (i=0; i<SIZE; i + +){
21 (p+i)—>a=80+i*SIZE;
22 (p+i)—>b=90十i *SIZE;
23 (p+i)->c=100-i * SIZE;
24 (p+i) —>Iv=f n3((p+i)-> a);
25 }
26 }
27 void fn2(struct soojebi *p) {
28 int i;
29 for (i=0; i<SIZE; i + +){
30 printf("%d", p->a+p->b>p->lv?p->lv:p~)c);
31 p+ + ;
32 }
33 }
34 int main() {
35 struct soojebi s[SIZE], *p, *q;
36 p=s;
37 q=s;
38 fn1(p);
39 fn2(q);
40 return 0;
41 }
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int x=10, y=20;
04 x=x A y;
05 y=x Ay;
06 x=x A y;
07 System.out.println(x+","+y);
08 }
09 }
다음은 [급예 테이블에 대한 명세이다. [급
예 테이블에서 부서명이 '마케팅부'이고, 직
책은 '부장', 급여는 '100'인 데이터를 입력하
시오.(전화번호는 INSERT 문에 따로 입력하지 않
는다.)
[급예 테이블 명세
속성명 데이터 타입
부서명 VARCHAR(20)
직책 VARCHAR(20)
급여 VARCHAR(20)
전화번호 VARCHAR(11)
정점이 5개인 방향 그래프가 가질 수 있는 최
대 간선 수는 얼마인지 쓰시오. (단, 자기 간선
과 중복 간선은 배제한다.)
1 00 수제비 정보처리기사 실기 FINAL 모의고사
## Page 101

05 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main (String[ ] args){
03 List a=new ArrayList( );
04 a.add(2);
05 System.out.print(a);
06 a.add(1);
07 System.out.print(a);
08 a.add(1);
09 System.out.print(a);
10 a.add(1,3);
11 System.out.print(a);
12 a.remove(2);
13 System.out.print(a);
14 System.out.print(a.get(2));
15 System.out.print(a.size( ));
16 }
17 }
06 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 #include<stdio.h>
02 int main(){
03 int a=0, i=3;
04 for(;i<100;i*=3)
05 a+=i;
06 printf("%d", i);
07 return 0;
08 }
07 다음은 보안 솔루션에 대한 설명이다. 괄호
( ) 안에 들어갈 용어를 쓰시오.
• ( ① 足/는 단말기가 내부 네트워크에 접속
을 시도할 때 이를 제어하고 통제하는 기능을
제공하는 솔루션으로 바이러스나 웜 등의 보
안 위협뿐만 아니라 불법 사용자에 대한 네트
워크 제어 및 통제기능을 수행하는 장비이다.
• ( ② )은/는 네트워크에서 발생하는 이벤트
를 모니터링하고 비인가 사용자에 의한 자원
접근과 보안정책 위반 행위(침입)를 실시간으
로 탐지하는 시스템이다.
①____________________________________________
②_______________________________________________
08 전송 계층과 응용 계층 사이에서 클라이언트
와 서버 간의 웹 데이터 암호화(기밀성), 상호
인증 및 전송 시 데이터 무결성을 보장하는
보안 프로토콜은 무엇인지 쓰시오.
09 다음은 테스트 목적에 따른 분류이다. 괄호
( )안에 들어갈 테스트 유형을 쓰시오.
• ( ① '은/는 시스템에 고의로 실패를 유도
하고, 시스템의 정상적 복귀 여부를 테스트하
는기법이다.
• ( ② '은/는 오류를 제거하거나 수정한 시
스템에서 오류 제거와 수정에 의해 새로이 유
입된 오류가 없는지 확인하는 일종의 반복 테
스트 기법이다.
①____________________________________________
②_______________________________________________
모의고사18회 101
## Page 102

10 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 print(sum([ i for i in range(-1, -10, -4) ]))
다음은 0U\P 연산이다. 괄호 ( ) 안에 알
맞은 연산을 쓰시오.
다음 괄호 ( ) 안에 들어갈 용어를 쓰시오.
객체지향 소프트웨어 개발 과정에서 산출물
을 명세화, 시각화, 문서화할 때 사용되는 모델
링 기술과  방법론을 통합해서 만든 표준화된 언
어는 ( ① )이다. ( ① )의 구성요소 중
( ② )은/는 추상적인 개념으로, 주제를 나타
내는 요소이고 단어 관점에서 '명사' 또는 '동사'
를 의미한다.
①___________________________________________________________________________________
②___________________________________________________________________________________
• ( ① ): 분석할 항목에 대해 구체적인 데이
터로부터 요약된 형태의 데이터로 접근하는
연산
• ( ② ): 분석할 항목에 대해 요약된 형태의
데이터로부터 구체적인 데이터로 접근하는
연산
. ( ③ ): 온라인 분석처리를 위한 자료 구조
인 데이터 큐브의 한 조각을 볼 수 있게 해주
는 연산
• ( ④ ): 고정된 다차원 값에 대한 연산
①____________________________________________
②____________________________________________
③____________________________________________
④____________________________________________
다음은 C언어 코드이다. 출력 결과를 쓰시오.
다음은 보안 암호 알고리즘에 대한 설명이
다. 괄호 ( ) 안에 들어갈 암호화 알고리즘
종류를 쓰시오.
• ( ① ): 국내 한국인터넷진흥원(KISAKI 개
발한 블록 암호화 알고리즘으로 128bit 비 밀키
로부터 생성된 16개의 64bit 라운드 키를 사용
하여 총 16회의 라운드를 거쳐 128bit 암호문
블록으로 암호화하는 대칭키 알고리즘
• ( ② ): 유한체 위에서 정의된 타원곡선 군
에서의 이산대수 문제에 기초한 암호화 알고
리즘으로 RSA보다 키의 비트 수를 적게하면 [확인 필요]
서 동일한 성능을 제공하는 비대칭키 암호화
알고리즘
01 ffinclude<stdio.h>
02 int main(){
03 int i=1;
04 int sum=0;
05 for(;i<10;){
06 switch(i%2){
07 case 0 :
08 sum+=1;
09 default:
10 sum+=2;
11 }
12 i 十 =3;
13 }
14 printf("%d", sum);
15 return 0;
16 : }
①___________________________________________________________________________________
②___________________________________________________________________________________
1 02 수제비 정보처리기사 실기 FINAL모의고사 [확인 필요]
## Page 103

소프트웨어 개발 주기의 단계별로 요구할 인
력의 분포를 가정하는 모형으로 시간에 따른
함수로 표현되는 Rayleigh - Norden 곡선의
노력 분포도를 기초로 하는 비용산정 모형은
무엇인지 쓰시오.
16 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 ffinclude <stdio.h>
02 int main(){
03 char a[ ]="ABC";
04 int i;
05
06 for(i=0; a[i]!=\0'; a[i]-='C'){
07 printf("%d", *(a+i));
08 i++;
09 }
10 return 0;
11 }
다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int sum:더act(3, 5); [확인 필요]
04 System.out.println(sum);
05 }
06 public static int fact(int a, int b) {
07 if (b<a){
08 return 1;
09 }
10 else {
11 return b * fact(a, b-1);
12 }
13 }
14 }
18 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int[ ] numArr=new int[5];
04 int result=0;
05
06 for(int i=0; i<5; i + +)
07 numArr[i]= + +i;
08
09 for(int i: numArr)
10 result+=i;
11
12 System.out.printf("%d", result);
13 }
14 }
19 다음은 신기술에  대한 설명이다. 괄호( )
안에 들어갈 용어를 쓰시오.
최근 현실 세계를 가상화하여 비즈니스에 사용
하는 기술이  부각되고 있다. 그 중( ① )은/
는 가상 물리 시스템으로 인간의 개입 없이 대
규모 센서 • 액추에이터를 갖는 물리적인 요소
들과 통신 기술 , 응용 • 시스템 소프트웨어 기술
을 활용하여 실시간으로 물리적 요소들을 제어
하는 컴퓨팅 요소가 결합된 복합 시스템이고,
( ② 물리적인 사물과 컴퓨터에 동일
하게 표현되는 가상 모델로 실제 물리적인 자산
대신 소프트웨어로 가상화함으로써 실제 자산의
특성에 대한 정확한 정보를 얻을 수 있고, 자산
최적화, 돌발사고 최소화, 생산성 증가 등 설계
부터 제조, 서비스에 이르는 모든 과정의 효율성
을 향상시킬 수 있는 모델이다.
①___________________________________________________________________________________
②___________________________________________________________________________________
모의고사 18회 103
## Page 104

20 다음 괄호( )안에 들어갈 디자인 패턴
유형을 쓰시오.
소프트웨어 공학의 소프트웨어 설계에서 공통으
로 발생하는 문제에 대해 자주 쓰이는 설계 방
법을 정리한 패턴인 디자인 패턴의 유형 중 구조
패턴에속하는( ① )은/는기능의클래스계
층과 구현의 클래스 계층을 연결하고, 구현부에
서 추상 계층을 분리하여 추상화된 부분과 실제
구현 부분을 독립적으로 확장할 수 있는 디자인
패턴이고,( ② )은/는 기존에 생성된 클래스
를 재사용할 수 있도록 중간에서 맞춰주는 역할
을 하는 인터페이스를 만드는 패턴으로, 상속을
이용하는 클래스 패턴과 위임을 이용하는 인스
턴스 패턴의 두 가지 형태로 사용되는 디자인 패
턴이다.
①___________________________________________________________________________________
②___________________________________________________________________________________
1 04 수제비 정보처리기사 실기 FINAL 모의고사
## Page 105

수제비
모의고사 19히
01 다음은 자바 코드이다. 출력 결과를 쓰시오. 02 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 class Animal {
02 void sound() {
03 System.out.print("?");
04 }
05 }
06 class Dog extends Animal {
07 void sound() {
08 System.out.print("Bark");
09 }
10 }
11 class Cat extends Animal {
12 void sound() {
13 System.out.print("Meow");
14 }
15 }
16 public class Soojebi {
17 public static void main(String[ ] args) {
18 Animal[ ] zoo={new Dog(), new Cat( )};
19 for (Animal a : zoo) {
20 if (a instanceof Dog) ((Dog) a).sound( );
21 else a.sound( );
22 }
23 }
24 }
01 ffinclude <stdio.h>
02 struct soojebi {
03 int x;
04 int y;
05 };
06 int main() {
07 struct soojebi s[ ]={
08 {1, 2},
09 {3, 4},
10 {5, 6}
11 };
12 struct soojebi *ptr=s;
13 struct soojebi **pptr=&ptr;
14 ptr[1]=(*pptr)[2];
15 printf("%d%d", s[1].x, s[1].y);
16 printf("%d%d", ptr[1].x, ptr[1].y);
17 printf("%d%d", (*pptr)[1].x, (*pptr)[1].y);
18 return 0;
19 }
03 다음은 시퀀스 다이어그램에 대한 설명이다.
괄호( )안에 들어갈 용어를 쓰시오.
객체 간 상호작용을 메시지 흐름으로 표현한 다
이어그램인 시퀀스 다이어그램의 구성요소 중
( ① '은/는 위쪽에 표시되며 사각형 안
에 밑줄 친 이름으로 명시한다.( ② )은/는
( ① )(으로부터 뻗어 나가는 점선으로 실제
시간이 흐름에 따라( ① )의 생명주기 동안
발생하는 이벤트를 명시한다.
①___________________________________________________________________________________
②___________________________________________________________________________________
모의고사19회 105
## Page 106

04 HONG이라는 사용자에게 STUDENT 테이블 [확인 필요]
에 SELECT 할 수 있는 권한을 부여하는 DCL
을 작성하시오.
05 다음 괄호( )안에 공통으로 들어갈 용어
를 쓰시오.
UML의 ( '은/는 UML의 기본적 요소 이외의 [확인 필요]
새로운 요소를 만들어 내기 위한 확장 매커니즘
이다. 형태는 기존의 UML의 요소를 그대로 사용 [확인 필요]
하지만 내부 의미는 다른 목적으로 사용하도록
확장한다. 또한 UML의 ( )은 '«>>'(길러멧; [확인 필요]
Guillemet) 기호를 사용하여 표현한다.
06 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 def soojebi(s, char):
02 return s.replace(char, ")
03
04 string="Hello, Soojebi!"
05 chr='o'
06 result=soojebi(string, chr)
07 print(result)
다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main (String[ ] args){
03 TreeMap<hteger, String) map=newTreeMap<>();
04 map.put(4, "D");
05 map.put(3, "C");
06 map.put(1, "A");
07 map.put(2, "B");
08 System.out.println(map);
09 }
10 }
08 다음은 데이터베이스 회복 기법에 대한 설명
이다. 괄호 ( ) 안에 들어갈 용어를 쓰시오.
데이터베이스 회복 기법의 종류 중( ① )은/
는 장애 발생 시 검사점 이후에 처리된 트랜잭션
에 대해서만 장애 발생 이전의 상태로 복원시키
는회복기법이고,( ② )은/는데이터베이스
트랜잭션 수행 시 복제본을 생성하여 데이터베
이스 장애 시 이를 이용해 복구하는 기법이다.
①_____________________________________________
②_____________________________________________
09 다음 [부세 테이블에서 'DT부'와 '보안부'를 [확인 필요]
삭제하는 쿼리를 작성하시오.
[부세 테이블
부서 번호 부서명 전화번호
1 마케팅부 111-2222
2 영업부 333—4M4
3 전략부 555-6666
4 보안부 777-8888
5 DT 부 999-0000
1 06 수제비 정보처리기사 실기 FINAL 모의고사
