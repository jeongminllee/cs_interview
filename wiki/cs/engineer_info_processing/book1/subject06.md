---
type: Study Note
title: "[6과목] 프로그래밍 언어 활용"
description: "정보처리기사 실기 기본서 1권 6과목 프로그래밍 언어 활용 본문 텍스트 추출본"
tags: [engineer-info-processing, 기본서1권, 과목6]
timestamp: 2026-06-19
status: active
---

# 6과목 프로그래밍 언어 활용

## Page 351

개 념 박살내기 자바문자열 연결
[소스코드
01
02
03
04
05
06
07
08
public class Soojebi {
public static void main(String[ ]args){
System.out.println("5+2="+3+4);
System.out.println("5+2="+3.1+4);
System.out.println("5+2그"+(3+4));
System.out.println(5+2+"三3+4");
}
}
출력
5+2=34
5+2=3.14
5+2=7
7=3+4
[코드 해설]
03
• 문자열인 "5+2="와 3을 더하므로 "5+2=3"이 되고, "5+2=3"에 4를 더
하므로 "5+2=34"가 되어 5+2=34가 출력
04
• 문자열인 "5+2="와 3.1 을 더하므로 "5十2=3.1"이 되고, "5+2=3.1"에 4를
더하므로 "5+2=3.14"가 되어 5+2=3.14가 출력
05
• 괄호가 우선순위가 높으므로 3+4가 먼저 계산되어 701 됨
• 문자열인 "5+2="와 7을 더하므로 "5+2=7"이 되어 5十2=7이 출력
06
• 5+2를 계산하면 701 되고, 7과 "=3+4"를 더하면 "7=3+4"이 되어 7=3+4
가 줄력
휴乂우 요》
津흐n+⑤
숫자와 문자열이 함께
포함된 덧셈 연산은 왼
쪽부터 순차적으로 평가
됩니다. 예를 들어 문자
열+정수+정수는 먼저
문자열+정수가 계산되
고, 그 결과가 다음 정수
와 다시 연산됩니다. 반
대로 정수+정수+문자
열은 앞의 두 정수가 먼
저 더해진 뒤, 그 결과가
문자열과 결합됩니다.
r2오 S
⑶ 문자열 비교
D equals 메서드 座圓困1 mm
• equals 메서드는 문자열 자체를 비교하는 메서드이다.
boolean equals
(anObject);
• anObject 문자열과 같으면 true를, 다르면 false를 [확인 필요]
반환
• equals 메서드는 대소문자를 구분한다.
0 equal이gnoreCase 메서드 [확인 필요]
• equalsIgnoreCase 메서드는 대소문자를 무시하고 문자열을 비교하는
메서드이다.
b -
둑
 v
C
## Page 352

boolean equalsIgnoreCase • anObject 대소문자를 무시했을 때 문자열과 같으면
(anObject); true를, 다르면 false를 반환 [확인 필요]
酷取世 쏘
char 형 배열에서 [ ]를
이용해 해당 번지의 문
자에 접근할 수 있으나
String 형은 참조형으로
[ ]를 이용해 해당 번지
의 문자에 접근할 수 없
습니다. 그래서 charAt
메서드를 통해서 해당
번지의 문자를 가지고
옵니다.
EJ charAt 메서드
• charAt 메서드는 문자열에서 해당 번지의 문자를 반환하는 메서드이다.
char charAt(index); • 문자열에서 index 번지의 문자를 반환
□ substring 메서드
• substring 메서드는 문자열에서 특정 부분을 잘라서 새로운 문자열을
반환하는 메서드이다.
String substring
(beginlndex);
• 문자열에서 beginlndex 번지부터 끝까지 잘라낸 문
자열을 반환
String substring
(beginlndex, endindex);
• 문자열에서 beginlndex 번지부터 end-Index 직전
까지 잘라낸 문자열을 반환
同 toUpperCase 메서드
• toUpperCase 메서드는 문자열의 알파벳을 모두 대문자로 변경한 문자
열을 반환하는 메서드이다.
_ . , ,, 스 수. • 문자열의 알파벳을모두 대문자로 변경한문자열을
String tollpperCase(),
0 toLowerCase 메서드
• toLowerCase 메서드는 문자열의 알파벳을 모두 소문자로 변경한 문자
열을 반환하는 메서드이다.
String toLowerCase( );
• 문자열의 알파벳을 모두 소문자로 변경한 문자열을
반환
Ei replace 메서드
• replace 메서드는 주어진 문자열을 새로운 문자열로 교체하는 메서드
이다.
String replace
(이d, new);
• 문자열 내에서 old와 일치하는 문자열을 포함된 부 [확인 필요]
분을 new로 변경 [확인 필요]
프로그래밍 언어 활용
## Page 353

El replaceAII 메서드
• replaceAII 메서드는 주어진 정규 표현식에 매칭되는 부분을 새로운 문
자열로 교체하는 메서드이다.
String replaceAII • 문자열에서 regex와 일치하는 패턴을 replacement [확인 필요]
(regex, replacement); 문자열로 변경
0 split 메서드
• split 메서드는 구분자를 기준으로 문자열을 나누어 문자열 배열로 반
환하는 메서드이다.
String[ ] split • 문자열에서 regex와 일치하는 패턴을 기준으로 문 [확인 필요]
(regex); 자열을 분리
문자열을 분리한 결과를
문자열 배열에 저장합니
다. 예를 들어 a="x,y,z"
일 때 a.splie(",")을 하게
되면 a[이에 "x", a[1]에
"y", a[2]에 "z"가 저장
됩니다.
[0 trim 메서드
• trim 메서드는 문자열에서 앞뒤 공백을 제거한 문자열을 반환하는 메
서드이다.
String trim( ); • 문자열에서 앞뒤 공백을 제거한 문자열을 반환
DO length 메서드
• length 메서드는 문자열의 길이를 반환하는 메서드이다.
int length( ); • 문자열의 길이를 반환
두J 개 념 박살내기 자바 문자열 비교
[소스코드]
01 public class Soojebi {
02 public static void main(String[ ] args){
03 String a="abc";
04 String b="abc";
05 String c=new String("abc");
06 String d=new String("abc");
07 String e=a;
08 System.out.println(a==b);
09 System, out. pri ntl n(a==c);
10 System.out.println(b==e);
Chapter 03 자바 6-167
## Page 354

11 System.out.println(c=d);
12 System.out.println(d==e);
13 System.out.println(a.equals(b));
14 System.out.println(a.equals(c));
15 System.out.println(b.equals(e));
16 System.out.println(c.equals(cl));
17 System.out.println(d.equals(e));
18 }
19 }
true
false
true
false
춤려 false
거 true
true
true
true
true
[메모리 구조]
[코드 해설]
V • /
혜."나''u』" 혀^i
if 문, for 문, whil© 문,
do while 문은 C언어와
문법이 동일합니다. 생
각나지 않으시면 C언어
부분 참고해주세요.
02 • main 메서드부터 실행
• a, b라는 이름의 문자열 변수에 "abc" 문자열이 가리키고 있는 주소를 저장
03~04 • a, b는 리터럴 방식이고, 같은 문자열을 가지고 있0므루 문자열 풀의 같
은 곳을 가리킴
• c, d라는 이름의 문자열 변수에 "abc" 문자열이 가리키고 있는 주소를 저장
05~0b • c, d는 각각의 인스턴스를 가지므로 서로 다른 주소값을 가짐
06~07 • e라는 이름의 문자열 변수에 a의 주소값을 저장
08 • a와 b는 같은 주소값을 가지므로 true가 출력됨 [확인 필요]
6-168 VI 프=그래밍 언어 활용
## Page 355

VIS
HlJ
IJ2=
0°
r2오 W
OIO
09
• a는 문자열 풀에 저장되어 있고, c는 힙에 저장되어 있0므루 주소가 달라
false 가 출력됨
10
• b는 문자열 풀에 저장되어 있고, e도 문자열 풀에 저장되어 있0므.루 주소
가 같아 true가 출력됨 [확인 필요]
11 • c, d는 각각 다른 인스턴스를 가지므로 주소가 달라 false가 출력됨 [확인 필요]
12
• d는 힙에 저장되어 있고, e는 문자열 풀에 저장되어 있으므로 주소가 달라
false 가 출력됨
13~17 • a, b, c, d, e 모두 "abc"라는 동일한 문자열을 가지고 있으므로 결과는 true
개념 박살내기 자바문자열메서드
[소스코드
public class Soojebi {
public static void main(String[ ] args){
String a="hello";
String b="HELLO";
String c="1,2,3,,4";
String d=" HELLO ";
System.out.println(a=b);
System.out.println(a.equals(b));
System.out.println(a.equalslgnoreCase(b));
System.out.println(a.charAt(0));
System.out.println(a.substring(2));
System.out.println(a.toUpperCase( ));
System.oulprintln(b.toLowerCase( ));
System.out.println(a.replace("lo", "II"));
System.out.println(a.replaceAII("lo", "II"));
System.out.println(c.split(",")[1]);
System.out.println(d.trim( ));
System.out.println(d.trim( ).length( ));
}
}
false
false
true
h
llo
출력 HELLO
hello
helll
helll
2
HELLO
5
Chapter 03 자바 6-169
## Page 356

[코드 해설
02 • main 메서드부터 실행
03 〜 06
• a 문자열 변수를 "hello"로 초기화, 문자열 변수를 "HELLO"로 초기화, 문
자열 변수를 "1,2,3,,4"로 초기화, d 문자열 변수를 " HELLO "로 초기화
07
08
• a와 b는 값이 다르므로 false를 출력 [확인 필요]
• a와 b는 값이 다르므로 false를 출력 [확인 필요]
09 • a와 b는 대소문자를 무시하면 값이 같으므로 true를 출력 [확인 필요]
10
• a에서 0번지에 위치한 문자는 h이므로 h를 출력
0 1 2 3 4
h e । 0
11
• a에서 2번지에 위치한 I부터 끝까지 문자열을 자르므로 llo가 되어 llo를 출력 [확인 필요]
• a 값을 바꾸려면 a=a.substring(2)와 같이 대입 연산자를 이용해서 대입을
해야하는데 대입을 하지 않0므루 a 값은 바뀌지 않음
12 • a 문자열을 전부 대문자로 변경하여 HELLO가 출력됨 [확인 필요]
13 • b 문자열을 전부 소문자로 변경하여 h에o가 출력됨 [확인 필요]
14 • a 문자열에서 Io를 전부 I로 변경 [확인 필요]
15 • a 문자열에서 Io를 전부 I로 변경 [확인 필요]
16
• c 문자열을 콤마(,) 기준으로 분리하고, 배열의 1번지 값을 출력하여 2가 출
력됨
[0] [1] [2] [3] [4]
"1" "3" "4"
• 콤마(,) 사이에 아무 값도 없는 경우는 빈 문자열이 됨
17 • d 문자열의 앞뒤 공백을 모두 제거하여 HELLO만 남게 되어 HELLO를 출력 [확인 필요]
18
• d 문자열의 앞뒤 공백을 모두 제거한 HELLO의 글자수를 반환하므로 5가 [확인 필요]
되어 5를 줄력
6-170 VI 프=그래밍 언어 활용
## Page 357

守 반복문 -for each 문 ★
(1) for each 문의 개념
• for each 문은 배열이나 리스트의 크기만큼 반복하는데, 반복할 때마다
배열이나 리스트의 항목을 순차적으로 변수에 대입하는 반복문이다.
⑵ for each 문의 구조
for( 제어변수:배열 ) {
문장;
}
VI
IB
HlJ
lJa=
0°
n2오
#
두J、개 념 박살내기 자바 for each 문 예시
[소스코드]
01
02
03
04
05
06
07
08
public class Soojebi {
public static void main(String[ ]args){
String[ ] name={"S00", "JE", "Bl"};
for(String nm: name){
System.out.println(nm);
}
}
}
출력
SOO
JE
Bl
[코드 해설]
03 • "SOO", "JE", "Bl" 값을 갖는 name 배열을 선언
04 • name 배열의 첫 번째 요소인 "S00"를 nm 변수에 전달
05 • nm의 값인 S00를 출력 [확인 필요]
04 • name 배열의 두 번째 요소인 "JE"를 nm 변수에 전달
05 • nm의 값인 JE를 출력 [확인 필요]
04 • name 배열의 세 번째 요소인 "BI"를 nm 변수에 전달
05 • nm의 값인 비를 출력 [확인 필요]
Chapter 03 자바 6-171
## Page 358

세 메서드 ★★★
(1) 사용자 정의 함수(메서드)
E1 사용자 정의 함수(User—Defined Function) 개념
• 사용자 정의 함수는 사용자가 직접 새로운 함수를 정의하여 사용하는
방법이다.
• 사용자 정의 함수에서 매개변수나 생성된 변수는 사용자 정의 함수가
종료되면 없어진다.
Q 사용자 정의 함수 문법
자료형 함수명(자료형 변수명, •••){
명령어;
return 반환값;
재 - 박살내기 자바사용자정의 함수
[소스코드]
01 public class Soojebi {
02 static char fn(int num){
03 if(num % 2==0)
04 return Y;
05 else
06 return 'N';
07 }
08 public static void main(String[ ] args){
09 char a=fn(5);
10 System.out.print(a);
11 }
12 } _____________
출력 N
힣 아
類
자바도 C 언어처럼 재귀
함수를 사용할 수 있습
니다.
[코드 해설]
• a라는 이름의 char(문자)형 변수를 선언, a는 fn(5)가 실행한 후에 반환되는
return 값으로 초기화
• fn(5)에 의해 fn 함수를 실행
02 • fn(int num) 함수를 fn(5)로 호출했으므로 num의 값은 5 [확인 필요]
• num은 사용자 정의 함수가 끝나면 없어짐 [확인 필요]
6-172 VI 프로그래밍 언어 활용
## Page 359

03
05
06
09
10
• num은 5이므로, num % 2는 5%2인 10| 때문에 num % 2==0은 거짓이 되 [확인 필요]
어 if 문을 실행하지 않음
• if 문이 거짓이므로 else 문을 실행
• N을 fn(5) 호출한 곳으로 전달
• return을 만났0므로 fn 함수는 종료 [확인 필요]
• fn(5)는 N 이므로 a는 N이라는 문자로 초기화
• a 의 값인 N을 출력
(2) static 메서드 21 년 2회 . 3회
• static 메서드는 클래스가 메모리에 올라갈 때 자동적으로 생성되는 메
서드이다.
• 인스턴스를 생성하지 않아도 호출이 가능하게 된다.
E2오 W
OIO
인스턴스 Instance
클래스로부터 만들어진
객체이다.
'내기 자바 static 메서드
[소스코드]
01 class Soojebi {
02 static void print(){
03 System.out.println("static method");
04 }
05 }
06 public class SoojebiMain {
07 public static void main(String[ ] args){
08 Soojebi.print( );
09 }
10 }
출력 static method
[코드 해설]
07 • main 메서드부터 시작
08
• 인스턴스(Soojebi soo와 같은 변수 선언)를 생성하지 않고, "클래스명.메서드 [확인 필요]
명" 형태로 호출
02 • static으로 print 메서드 선언해서 인스턴스 없이 호출 가능 [확인 필요]
03 • static method 출력
Chapter 03 자바 6-173
## Page 360

익명 함수를 1줄로 표현
할 때는 중괄호가 없습니
다. 익명 함수를 사용자
정의 함수처럼 여러 줄로
표현할 때는 중괄호가 있
습니다.
⑶ 익명 함수 =폐
BI 익명 함수(Anonymo니s Function) 개념 [확인 필요]
• 익명 함수는 함수 이름 없이 동작하는 함수이다.
• 매개변수에 값을 전달하면 표현식에서 연산을 수행한다.
Q 익명 함수 문법
(매개변수) -> 표현식;
(매개변수) -> {
명령문;
return 반환값;
}
• 하나의 추상 메서드만 가진 인터페이스를 기반으로 동작한다.
( 개뎌 박살내기 자바익명 함수
[소스코드]
01
02
03
04
05
06
07
08
09
interface ISoo {int fn(int x, int y);}
public class Soojebi {
public static void main(String[ ] args) {
ISoo a=(x, y)—>x+y;
System.out.println(a.fn(2, 3));
ISoo b=(x, y)->{ return x+y; };
System.out.println(b.fn(2, 3));
}
}
출력 5
5
[코드 해설]
01 • 함수형 인터페이스 ISoo 선언 및 fn() 메서드 정의
02 • Soojebi 클래스 선언
03 • main 메서드 시작
04 • 익명 함수를 이용해 ISoo 인터페이스의 fn() 구현 생성
05 • a.fn(2, 3) 호출, x+y의 값인 5를 출력
06 • 또 다른 익명함수로 ISoo 구현 생성
07 • b.fn(2, 3) 호출, x+y의 값인 5를 출력
6-174 VI 프로그래밍 언어 활용
## Page 361

⑷ 자바 클래스 호줄 순서
• 자바에서 클래스가 처음 로드될 때, static 변수 선언 및 초기화문 一
static 블록 -* main 메서드 순서로 실행된다.
자바 클래스 호출 순서
[소스코드]
public class Soojebi {
static int x=fn( );
static int fn() {
System.out.print("A"+x);
return 1;
}
static {
x+=2;
System.out.print("B"+x);
}
static {
x++;
System.out.print("C"+x);
}
public static void main(String[ ] args) {
System.out.print(x);
}
}
출력 A0B3C44
[코드 해설
15 • main 메서드 호출
02 • 클래스 로딩 시 static int x=fn( );이 실행되기 위해 fn() 메서드를 호출
• fn()을 실행하고 "A"+x 출력
(Jd 〜 Ub • x는 아직 초기화되지 않아 0으로 간주되어 "A0" 출력하고 이후 1을 반환
02 • 반환된 값인 1을 X에 대입하여 X는 1이 됨
07〜 09 • 첫 번째 static 블록 실행하고 x에 2를 더해 x=3, 이후 "B3" 출력
11-13 • 두 번째 static 블록 실행하고 x를 1 증가시켜 x=4, 이어 "C4" 출력
15 • 클래스 초기화 완료 후 main 실행
16 • System.out.print(x); 실행하고 현재 x 값 4를 출력
M 談
胎 P애 K |^|
static 이 여러 개 있을 때
는 01번 라인부터 차례
대로 처리됩니다.
V
I
H
B
a
H
OE
rs오 W [확인 필요]
OIO
Chapter 03 자바 6-175
## Page 362

Q 클래스 ★★★
(1) 클래스(Class) 개념
• 클래스는 객체 지향 프로그래밍(OOP;Object—Oriented Programming)에
서 특정 객체를 생성하기 위해 변수와 메서드를 정의하는 틀이다.
⑵ 클래스 접근 제어자
① 클래스 접근 제 어자(Access Modifier) 개념
• 접근 제어자는 지정된 클래스, 변수, 메서드를 외부(같은 패키지이거나
다른 패키지)에서 접근할 수 있도록 권한을 설정하는 기능이다.
② 클래스 접근 제어자 종류
齡허L—
default는 자바에만 존 [확인 필요]
재하는 접근 제어자입
니다.
▼ 클래스 접근 제어자 종류
종류 설명
public • 외부의 모든 클래스에서 접근이 가능한 접근 제어자
protected
• 같은 패키지 내부에 있는 클래스, 하위 클래스(상속받은 경우)에서 접
근이 가능한 접근 제어자
• 자기 자신과 상속받은 하위 클래스 둘 다 접근이 가능한 접근 제어자
default
• 접근 제어자를 명시하지 않은 경우로 같은 패키지 내부에 있는 클래
스에서 접근이 가능한 접근 제어자
private • 같은 클래스 내에서만 접근이 가능한 접근 제어자
잠깐! 알고가기
정보 은닉
Information Hiding
코드 내부 데이터와 메
서드를 숨기고 공개 인
터페이스를 통해서만 접
근이 가능하도록 하는
코드 보안 기술이다.
⑶ 클래스 정의 MB
• 클래스에서 변수는 변수 선언과 동일하고, 메서드는 사용자 정의 함수
와문법이 동일하다.
• 일반적으로 변수는 private 접근 제어자를 사용하여 외부에서 접근하
지 못하게 하며, 메서드는 외부에 공개할 것만 public 접근 제어자를,
그렇지 않으면 protected나 private 접근 제어자를 사용하여 정보 은 [확인 필요]
닉을 한다.
6-176 VI 프로그래밍 언어 활용
## Page 363

public class 클래스명{
private 자료형 변수명;
public 반환_자료형 메서드명(자료형 변수명, •■•){
명령어;
return 반환값;
}
}
(4) 클래스 변수 생성 @폐！
• 클래스는 객체를 생성하기 위해 변수와 메서드를 정의하는 틀이므로
실제 변수에 들어갈 인스턴스를 new 키워드로 생성해주어야 한다.
• 변수를 이용해 클래스의 메서드에 접근한다.
클래스명 변수명 = new 클래스명(파라미터);
변수명.메서드명();
(5) 클래스 this*!圓 @固
• this는 현재 객체를 가리키는 키워드이다. [확인 필요]
• 클래스 내부의 변수와 메서드를 가리킬 수 있다.
클래스 내부 변수 접근 this. 변수;
클래스 내부 메서드 접근 this. 메서드(매개변수);
클래스 내부 생성자 호출 this(매개변수);
예오*t쏘!
오버라이딩에 대해서 뒤
에서 다루는데. 만약 오
버라이딩 관계에 있다면
this. 메서드(매개변수);를
호출하더라도 자식 클
래스의 메서드를 실행합
니다.
■그념 박살나기 자바 this
[소스코드]
01 public class Soojebi {
02 private int a;
03 public void setA(int a){
04 this.a=a;
05 }
06 public int getA(){
07 return a;
08 }
09 public static void main(String[ ] args){
10 Soojebi soo 三 new Soojebi( );
Chapter 03 자바 6-177
## Page 364

setA 함수에서 a라고 하
면 파라미터로 받은 int
a일 수도 있고, 클래스
내에 저장된 private int
a의 a일 수도 있습니다.
프로그램에서는 같은
이름일 경우 가장 가까
이에 있는 변수를 지칭
하게  되는데, 파라미터
로 받는 int a는 함수 내
에 있어서 함수 밖에 있
는 private int a보[자' 가'
까우므로 a라고 지칭하
면 파라미터로 받는 int
a를 가리키게  됩니다. 그
러면 클래스 내에 있는
private int a의 a를 가리
킬 방법이 없으므로 this
를 써서 가리킬 수 있습
니다.
11 soo.setA(5);
12 System.out.print(soo.getA( ));
13 }
14 }
출력 5
[코드 해설]
09 • main 메서드부터 시작
10 • soo라는 변수에 Soojebi 클래스 생성 [확인 필요]
11 • soo 클래스 변수 내의 setA라는 함수를 호출할 때 5를 넘김 [확인 필요]
03 • setA 함수에서 a라는 매개변수 받음
04
• this.a는 class 내의 a 변수, 그냥 a는 매개변수로 받은 변수
• 클래스 내의 private int a의 a에 파라미터로 받은 a 값인 5를 대입
12
• soo.getA의 반환 값을 출력 [확인 필요]
• 반환 값은 getA 메서드를 실행해야 알 수 있음
06 • getA 함수는 클래스 내의 a 변수에 저장된 5를 반환
12 • soo.getA의 반환 값은 5이므로 System.out.println(5)가 되어 5를 출력 [확인 필요]
(6) 생성XKConstructor) Hi [확인 필요]
• 생성자는 해당 클래스의 객체가 생성될 때 자동으로 호출되는 특수한
종류의 메서드이다.
• 생성자는 일반적으로 클래스의 멤버 변수를 초기화하거나 클래스를 사
용하는 데 필요한 설정이 필요한 경우 사용한다.
• 생성자는 클래스 명과 동일한 메서드명을 가지고, 반환 값이 없다.
• 생성자가 없을 경우 public 클래스명( ){ }이라는 아무 일도 하지 않는
생성자가 있는 것처럼 동작한다.
▼ 생성자
구분 코드
public class 클래스명{
public 클래스명(매개변수){
생성자 정의 명령어;
}
}
생성자 호출 클래스명 클래스변수=new 클래스명(매개변수);

6-178 VI 프로그래밍 언어 활용
## Page 365

자바 생성자
[소스코드]
public class Soojebi{
public Soojebi(){
System.outprintln("A");
}
public Soojebi(int a){
System.out.println("B:"+a);
}
public void fn(){
System.out.println("C");
}
public static void main(String[ ] args){
Soojebi s1=new Soojebi( );
Soojebi s2=new Soojebi(5);
s1.fn( );
}
}
A
출력 B:5
C
[코드 해설]
11 • main 메서드부터 시작
12 • new Soojebi( )에서 파라미터가 없01그루 Soojebi() 생성자를 호출
02 • 매개변수가 없는 생성자를 호출
03 • A를 줄력
13 • new Soojebi(5)에서 파라미 터가 정수이므로 Soojebi(int a) 생성자를 호출
05 • 정수 값을 매개변수로 받는 생성자를 호출
06 • a는 5이므로 "B:"+5가 되어 B:5가 출력
14 • S1 의 fn 메서드를 호출
08 • fn 메서드 실행
09 •C를 출력
(7) 내부 클래스(Inner Class)
• 내부 클래스는 다른 클래스 내부에 정의된 클래스이다.
Chapter 03 자바 6-179
## Page 366

:하:
齡 Wnl 여
클래스명. 내부_클래스명
를 통해서 내부 클래스
에 접근할 수 있습니다.
class 클래스명 {
class 내부_클래스명 {
// 내무 클래스
}
}
클래스명.내부_클래스명= 클래스명내부_클래스명();
C언어와 자바에서 //는
주석이라고 해서 // 뒤
에 코드는 무시합니다.
輕 어 벼 박살내기 자바내부클래스
[소스코드]
01 class Outer {
02 static class Inner {
03 void fn() {
04 System.out.print("A");
05 }
06 }
07 }
08 public class Soojebi {
09 public static void main(String[ ] args){
10 Outer.lnner a=new Outer.lnner();
11 a.fn( );
12 }
13 }
출력 A
[코드 해설
9 • main 메서드 시작
10 • Outer.lnner를 통해 내부 클래스 Inner에 접근 [확인 필요]
11 • a.fn()을 호출하고 fn() 실행하여 "A"를 출력
(8) 래퍼 클래스
Q 래퍼 클래스(Wrapper Class) 개념
• 래퍼 클래스는 기본 자료형을 객체로 다루기 위해서 사용하는 클래스
이다.
• 래퍼 클래스는 기본형 데이터를 객체로 감싸서 사용할 수 있도록 해주
는 클래스이다.
6-180 VI 프로그래밍 언어 활용
## Page 367

▼ 기본 자료형과 래퍼 클래스 매핑
기본 자료형 래퍼 클래스
■'W스 絲
해여 Point 톄boolean Boolean [확인 필요]
byte Byte 기본 자료형과 래퍼 클
short Short
래스 이름을 보시면 첫
글자가 소문자이냐 대문
int Integer 자이냐 차이입니다. 대
소문자를 제외하고 int,
사》빼고는 기본 자료long Long [확인 필요]
float Float
형과 래퍼 클래스의 이
름이 전부 동일합니다.
double Double
char Character
厂J 박살내기 자바래퍼클래스
[소스코드]
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 Integer num=new lnteger(2);
04 int n=num.intValue( );
05 System.out.println(n);
06 }
07 }
출력 2
[코드 해설
02 • main 메서드 시작
03 • Integer 객체를 생성하고 변수 num에 2를 저장 [확인 필요]
04 • Integer 객체의 값을 기본형 int로 변환하여 n에 대입 [확인 필요]
05 •n 값인 2를 줄력
Q 래퍼 클래스 메서드 ^3
▼ 래퍼 클래스 메서드
메서드
valueOf
설명
• 기본 타입 값을 해당 래퍼 클래스 객체로 변환하는 메서드
parseXXX
• 문자열을 기본 타입의 값으로 변환하는 메서드
ED parseInt, parseDouble
Chapter 03 자바 6-181
## Page 368

메서드 설명
toString • 래퍼 클래스 객체의 값을 문자열로 변환하는 메서드
equals • 래퍼 클래스 객체 간의 값을 비교하는 메서드
a
념 박살내기 자바 래퍼 클래스 메서드
•하
[소스코드]
public class Soojebi {
public static void main(String[ ] args) {
String str1 = "1O";
String str2="10.0";
String str3="true";
byte a1=Byte.parseByte(str1);
int b1 긔nteger.parselnt(strl); [확인 필요]
short d =Short.parseShort(str1);
long d1=Long.parseLong(str1);
float e1=Float.parseFloat(str2);
double fl=Double.parseDouble(str2);
boolean g1=Boolean.parseBoolean(str3);
System.out.println(""+a1+b1+c1+d1+e1 +f1+g1);
Byte a2 三 Byte.vahjeOf(strl);
Integer b2=lnteger.v기ueOf(strl); [확인 필요]
Short c2=Short.valueOf(strl);
Long d2=Long.valueOf(str1);
Float e2=Float.valueOf(str2);
Double f2=Double.valueOf(str2);
Boolean g2=Boolean.valueOf(str3);
System.out.println(""+a2+b2+c2+d2+e2+f2+g2);
System.out.println(b2.toString( ));
System.out.println(b2.equals(10));
}
}
1010101010.010.0true
출력 1010101010.010.0true
10
true
6-182 vi 프=그래밍 언어 활용
## Page 369

[코드 해설
V-
IH
H11Z12=
O°
R2오
02 • main 메서드부터 프로그램 시작
03 • 문자열 변수 str1 을 "10"으로 초기화
04 • 문자열 변수 str2를 "10.0"으로 초기화
05 • 문자열 변수 str3을 "true"로 초기화
07 • a1 변수는 str1 문자열을 byte 형으로 변환하여 10이 됨
08 • b1 변수는 str1 문자열을 int 형으로 변환하여 10이 됨
09 • c1 변수는 str1 문자열을 short 형으로 변환하여 10이 됨
10 • d1 변수는 str1 문자열을 long 형으로 변환하여 10이 됨
11 • e1 변수는 str2 문자열을 float 형으로 변환하여 10.0이 됨
12 • f1 변수는 str2 문자열을 double 형으로 변환하여 10.0이 됨
13 • g1 변수는 str3 문자열을 boolean 형으로 변환하여 true가 됨 [확인 필요]
14
• " "는 문자열이고, 문자열十정수=문자열이 되기 때문에 a1 ~g1 값들은 전
부 문자열 연결이 됨
16~22 • 문자열을 각 래퍼 클래스에 맞는 값으로 변환
23
• " "는 문자열이고, 문자열+정수=문자열이 되기 때문에 a2~g2 값들은 전
부 문자열 연결이 됨
25 • b2는 10이므로 문자열로 변환하면 "10"이 되어 10을 출력
26 • b2는 10과 같으므로 true를 반환하기 때문에 true가 출력됨 [확인 필요]
(9) 기타 클래스—Math 클래스
• Math 클래스는 수학적 계산과 관련된 다양한 정적 메서드를 제공하는
클래스이다.
▼ Math 클래스
메서드 설명
Math.signum(a)
• 부호를 확인하는 메서드(양수이면 1.0, 음수이면 -1.0 반환)
GD Math.signum(5)=1.0
Math.max(a, b)
• 두 수 중 큰 값을 반환하는 메서드
ED Math.max(3,5)=5
Math.min(a, b)
• 두 수 중 작은 값을 반환하는 메서드
0] Math.min(3, 5)=3
Chapter 03 자바 6-183
## Page 370

제 박살내기 자바기타클래스
[소스코드]
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 System.out.println(Math.signum(-2.0));
04 System.out.println(Math.max(1, 6));
05 System.out.println(Math.min(2, 3));
06 System.o니t.println(Math.pow(5, 2)); [확인 필요]
07 System.out.println(Math.abs(-2));
08 System.out. pri ntln(Math.ceil(1.5));
09 System.out.println(Math.floor(1.5));
10 System.outprintln(Math.round(1.5));
11 System.out.println(Math.sqrt(4));
12 }
13 }
-1.0
6
2
25.0
출력 2
2.0
1.0
2
2.0
6-184 VI 프=그래밍 언어 활용
## Page 371

[코드 해설]
02 • main 메서드부터 실행
03 •-2.0 은음수이므로 -1.0 을출력
04 • 두 수중 큰 값인 6을 출력
05 • 두 수중 작은 값인 2를 출력
06 • 5의 2승은 25가 되어 실수 형태인 25.0을 출력
07 • -2의 절댓값 2를 출력
08 • 1.5를 올림한 값인 2.0을 출력
09 • 1.5를 내림한 값인 1.0을 출력
10 • 1.5를 반올림한 값인 2을 출력
11 • v조=2.0를 출력
r2오 眠
Oto
파 클래스 상속 ★★★
⑴ 클래스 상속(Inheritance) 개념
• 상속은 어떤 객체가 있을 때 그 객체의 변수와 메서드를 다른 객체가
물려받는 기능이다.
(2) 클래스 상속 문법 @1圓
▼ 클래스 상속 문법
이ass 부모_클래스명{ [확인 필요]
}
class 자식_클래스명 extends 부모_클래스명{
}
부모 클래스는 상위 클
래스, 슈퍼 클래스라고도
하고, 자식 클래스는 하
위 클래스, 서브 클래스
라고도 합니다.
나중에 인터페이스를 공
부하면 상속할 때 키워드
가 헷갈립니다. 일반 클
래스, 추상 클래스를 상
속할 때는 extends, 인
터페이스를 상속할 때는
implements라는 것을 [확인 필요]
꼭 기억해두세요.
Chapter 03 자바 6-185
## Page 372

자바는 자식 클래스를
J 박살내기 자바클래스상속
생성하면 부모 클래스
생성자를 먼저 방문하
고, 그다음에 자식 클래
스 생성자를 방문합니
다. 파이썬은 자식 클래
스를 생성하면 자식 클
래스의 생성자만 방문합
니다. 차이점을 기억해
두세요.
[소스코드
public class A{
public void fnA(){
System.out.println("A");
}
}
public class B extends A{
public void fnB(){
System.out.println("B");
}
}
public class Soojebi {
public static void main(String[ ] args){
B b:三 new B( );
b.fnA( );
b.fnB( );
}
}
출력 A
B
[코드 해설]
12 • main 메서드부터 시작
13 • B 클래스를 b라는 변수로 생성
14
• b의 fnA() 함수를 호출하면 B 클래스에 fnA() 메서드가 없으므로 부모 클래
스인 A 클래스의 fnA() 메서드를 실행
02 • fnA() 메서드를 실행
03 • A를 출력
15 • b의 fnB() 함수를 호출하면 B 클래스의 fnB()를 호출
07 •fnB() 메서드를 실행
08 • B를 출력
(3) 오버로딩(Overloading)
• 오버로딩은 동일 이름의 메서드를 매개변수만 다르게 하여 여러 개 정
의할 수 있는 기능이다.
• 오버로딩 특징은 다음과 같다.
6-186 VI 프로그래밍 언어 활용
## Page 373

• 메서드 이름이 같아야 한다.
• 매개변수 개수가 달라야 한다.
• 매개변수 개수가 같을 경우 데이터 타입이 달라야 한다.
• 반환형은 같거나 달라도 된다.
g 유 나네昌배세네세山리베세세서세江
채、硬 박살내기 자바오버로딩
廳째關■HI廳廳^^퓨廳羅해^調廳^^쬬쮀톄
[소스코드
public class A {
public void fn(){
System.out.println("A");
}
public void fn(int i){
System.out.println(i);
}
public void fn(double d){
System.out.println(d);
}
public int fn(int a, int b){
return a+b;
,
public class Soojebi{
public static void main(String args[ ]){
A a=new A( );
a.fn( );
a.fn(7);
a.fn(10.0);
System.out.println(a.fn(2, 3));
''
출력
厂
10.0
5
1
[코드 해설]
16 • main 메서드부터 시작
17
• A 클래스를 a라는 변수로 생성
• A 클래스를 a 변수에 생성하므로 A의 생성자 A()를 호출해야 하지만, 생성
자가 없으므로 클래스 생성 시 아무 일도 일어나지 않음
18 • a의 fn() 메서드 호출(파라미터가 없는 fn 메서드를 호출)
02 • 매개변수가 없고 반환 값도 없는 fn 메서드
03 • A를 출력
생성자와 오버라이딩을
헷갈려하는데, 생성자는
클래스명과 동일한 이름
의 메서드이고, 오버라
이딩은 부모, 자식 간 동
일한 이름의 메서드입니
다.(생성자는 오버라이딩이
안 됩니다.)
VI
IH
Hll
IJ2=
0°
r2오 S
Chapter 03 자바 6-187
## Page 374

• a의 fn() 메서드 호출(하나의 정수형 매개변수를 갖고 반환 값이 없는 fn 메서드
19 _ _、호줄)
05 • fn(int i)메서드의 에 7을 전달
06 • i 값인 7을 출력
• a의 fn() 메서드 호출(하나의 실수형 매개변수를 갖고 반환 값이 없는 fn 메서드
호출)
08 • fn(double d)메서드의 d에 10.0을 전달
09 • d 값인 10.0을 출력
21 • a의 fn() 메서드 호출(두 개의 매개변수를 갖고 반환 값을 갖는 fn 메서드를 호출)
11 • fn(int a, int b)에서 a에 2를, b에 3을 전달
12 • a+b 인 5를 반환
21 • printin 메서드는 반환값 5를 출력
(4) 오버라이딩(Overriding) aw MB
• 오버라이딩은 하위 클래스에서 상위 클래스 메서드를 재정의할 수 있
는 기능이다.
• 오버라이딩 특징은 다음과 같다.
• 오버라이드하고자 하는 메서드가 상위 클래스에 존재하여야 한다.
• 메서드 이름은 같아야 한다.
• 메서드 매개변수 개수, 데이터 타입이 같아야 한다.
• 메서드 반환형이 같아야 한다.
▼ 오버라이딩 구문
class 부모_클래스명{
public 반환_자료형 메서드명(자료형 변수명){ }
}
class 자식_클래스명 extends 부모_클래스명{
public 반환J다료형 메서드명(자료형 변수명){
// 부모 클래스의 메서드명, 매개변수가 동일해야 함
} 「 으 • < . 스 느 三三
}
6-188 VI 프로그래밍 언어 활용
## Page 375

go?뎔 박살내기 자바오버라이딩
[소스코드]
01 public class A{
02 public void fn(){
03 System.out.println("A");
04 }
05 }
06 public class B extends A{
07 public void fn(){
08 System.out.println("B");
09 }
10 }
11 public class Soojebi{
12 public static void main(String args[ ]){
13 A a=new B();
14 a.fn( );
15 }
16 } _______________________________ __________________________
출력 B
[코드 해설]
12 • main 메서드부터 시작
• B 클래스를 a라는 변수로 생성
-B 클래스를 a 변수에 생성하므로 B의 생성자 B()와 B의 부모인 A의 생성
자 A()를 호출해야 하지만, 둘 다 없으므로 클래스 생성 시 아무 일도 일어
나지 않음
14 • a는 B 클래스이므로 B 클래스의 fn()을 호출
07 • B 클래스의 fn()을 호출
08 • B를 출력
VIH
l<lJM2=
a°
rJ2오 s
oto
Chapter 03 자바 6-189
## Page 376

두J 박살내기 자바생성자,오버라이딩
[소스코드]
class Parent{
public Parent(){
System.out.print("A");
}
public Parent(int a){
System.out.print("B");
}
public void fn(){
System.out.print("C");
}
}
class Child extends Parent{
public Child(){
System.out.print("D");
}
public Child(int a){
super(a);
Systenout.print("E");
}
public void fn(){
System.out.print("F");
}
}
public class Soojebi{
public static void main(String args[ ]){
Parent a=new Parent();
Parent b 三 new Parentd);
Parent c=new Child( );
Parent d=new Child(1);
Child e=new Child( );
Child f=new Child(2);
a.fn( );
e.fn();
}
}
출력 ABADBEADBECF
6-190 VI 프로그래밍 언어 활용
## Page 377

[코드 해설]
25 • main 함수의 시작 부분(프로그램이 제일 처음 실행되는 부분)
26 • new Parent()에 의해 파라미터가 없는 Parent 생성자 호출
02 〜 04 • Parent 생성자를 실행하여 A를 출력
27 • new Parent(1)에 의해 정수형 파라미터를 받는 Parent 생성자 호출
05~07
•a 변수에 1이 전달
• Parent 생성자를 실행하여 B를 출력
28 • new Child()에 의해 파라미터가 없는 Child 생성자 호출
13
• Child 생성자에서 부모 클래스의 생성자에 대한 명령어가 따로 없으므로
Parent 생성자는 파라미터가 없는 생성자가 호출
02~04 • 부모 클래스 생성자를 실행하여 A를 출력
13~15 • 자식 클래스 생성자를 실행하여 D를 출력
29 • new Child(1)에 의해 정수형 파라미터를 받는 Child 생성자 호출
16~17
•a 변수에 1이 전달
• Child 생성자에서 부모 클래스의 생성자에 대한 명령어 super(a)가 있으므
로 Parent 생성자는 정수형 파라미터를 가지는 생성자가 호출
05 〜 07
•a 변수에 1이 전달
• 부모 클래스 생성자를 실행하여 B를 출력
18~19 • 자식 클래스 생성;다를 실행하여 E를 출력
30 • new Child()에 의해 파라미터가 없는 Child 생성자 호출
13
• Child 생성자에서 부모 클래스의 생성자에 대한 명령어가 따로 없으므로
Parent 생성자는 파라미터가 없는 생성자가 호출
02~04 • 부모 클래스 생성자를 실행하여 A를 출력
13~15 • 자식 클래스 생성자를 실행하여 D를 출력
31 • new Child(2)에 의해 정수형 파라미터를 받는 Child 생성자 호출
16~17
•a 변수에 10| 전달
• Child 생성자에서 부모 클래스의 생성자에 대한 명령어 super(a)가 있으므
로 Parent 생성자는 정수형 파라미터를 가지는 생성자가 호출
05 〜 07
•a 변수에 10| 전달
• 부모 클래스 생성자를 실행하여 B를 출력
18~19 • 자식 클래스 생성자를 실행하여 e를 출력
32
• a 변수는 Parent 클래스를 인스턴스로 가지므로 Parent 클래스의 fn 메서
드를 실행
08〜10 • fn 메서드를 실행하여 C를 출력
33
• e 변수는 Child 클래스를 인스턴스로 가지므로 Child 클래스의 fn 메서드
를 실행
20~22 • fn 메서드를 실행하여 F를 출력
new Parent( );코드에
서 Parent만 봤을 때는 [확인 필요]
Parent의 부모 클래스 [확인 필요]
가 없기 때문에 Parent
생성자만 호출합니다.
new Child( );코드에서
Child 를 봤을때 부모가
Parent이므로 Parent [확인 필요]
생성자와 Child 생성자
모두호출합니다.
Parent x 三 new Child( );
와 Child x=new Child
();의 차이를 묻는 질문
이 많습니다. 제대로 이
해하려면 업캐스팅, 다
운캐스팅 개념을 알아야
하지만, 결론만 말하자
면 메서드의 동작 방식
은 차이가 없습니다.
vlm
HlJ
IJ무 [확인 필요]
0°*』오 e
oto
Chapter 03 자바 6-191
## Page 378

• 자바에서 static 메서드는 오버라이딩할 수 없다.
1、개념 자바 오버라이딩, static 메서드
[소스코드
class Parent {
public String fn1() {return "A";}
public static String fn2() {return "B"; };
}
class Child extends Parent {
public String fn1() {return "C";}
public static String fn2() {return "D"; };
}
public class Soojebi {
public static void main(String [ ] args) {
Parent x=new Child( );
Child y=new Child();
System.out.println(x.fn1());
System.out.println(x.fn2( )+y.fn2( ));
System.out.println(Parent,fn2( )+Child.fn2( ));
}
}
C
출력 BD
BD
[코드 해설
11 • main 메서드 시작
12 • Child 객체 생성, 부모 타입 참조 변수 x에 저장
13 • Child 객체 생성, 자식 타입 변수 y에 저장
14 • x.fn1() 호출, Child의 fn1() 실행, "C" 반환/출력 [확인 필요]
• x.fn2() 호출, Parent.fn2() 실행, "B"를 반환
15 • y.fn2() 호출, Child.fn2() 실행, "D"를 반환
• 반환 결과를 합친 "BD"를 출력
16 • Parent.fn2() 및 Child.fn2()을 호출하여 "BD"를 출력
(5) 부모 클래스 접근
• 자바는 super 키워드를 이용하여 상위 클래스의 변수나 메서드에 접근
할수있다.
6-192 VI 프로그래밍 언어 활용
## Page 379

부모 클래스 내부 변수 접근 super. 변수;
부모 클래스 내부 메서드 접근 super. 메서드(매개변수);
부모 클래스 내부 생성자 호출 super(매개변수);
VIm
KU
IJ무 [확인 필요]
0°
r2오 w
oto
도
재 박살내기 자바상위클래스접근
[소스코드
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
public class A{
public void fn(){
System.out.println("A");
}
}
public class B extends A{
public void fn(){
super.fn( );
System.out.println("B");
}
}
public class Soojebi {
public static void main(String args[ ]){
A a=new B( );
a.fn( );
}
}
출력 A
B
[코드 해설]
13 • main 메서드부터 시작
14
• B 클래스를 a라는 변수로 생성
• B 클래스를 a 변수에 생성하므로 B의 생성자 B()와 B의 부모인 A의 생성
자 a( )를 호출해야 하지만, 둘 다 없으므로 클래스 생성 시 아무 일도 일어
나지 않음
15 • a라는 변수는 B 클래스이므로 B 클래스에 있는 fn() 메서드를 호출
07 • B 클래스의 fn() 메서드 호출
08 • super 키워드가 있으므로 부모 클래스의 fn() 메서드를 호출
02 • A 클래스의 fn() 메서드 호출
03 • A 를 줄력
09
• super.fn( )01 끝났으므로 그 다음 코드를 실행
•B를 출력
Chapter 03 자바 6-193
## Page 380

(6) 업 캐스팅(Upcasting)
• 업 캐스팅은 하위 클래스 객체를 상위 클래스 타입으로 변환하는 과정이다.
• 하위 클래스 객체를 상위 클래스 타입으로 변환하는 것이 자동으로 이
루어지며, 이를 암시적 캐스팅이라고도 한다.
• 자식 클래스가 부모 클래스의 메서드를 오버라이딩한 경우, 부모 클래
스 타입으로 호출해도 자식 클래스의 메서드가 호출된다.
• 자식 클래스와 부모 클래스의 변수 이름이 같을 경우는 자식 클래스의
변수에 접근할 수 없다.
懸 개 념 박살내기 자바업 캐스팅
[소스코드]
01 class A{
02 int a=3;
03 A(){
04 System.oulprintln("A");
05 }
06 public void fn(){
07 System.out.println("C"+a);
08 }
09 }
10 class B extends A{
11 int a=5;
12 B(){
13 System.out.println("B");
14 }
15 public void fn(){
16 System.out.println("D"+a);
17 }
18 }
19 public class Soojebi {
20 public static void main(String args[ ]){
21 A a=new B( );
22 System.out.println(a.a);
23 a.fn();
24 }
25 }
A
출려 B
3
D5
—
6-194 VI 프로그래밍 언어 활용
## Page 381

[코드 해설
19 • main 메서드부터 시작
20
• B 클래스를 a라는 변수로 생성하고, a 변수의 타입은 A 클래스(업 캐스팅)
• B 클래스 생성했으므로 생성자를 호출
03~05 • A 클래스의 생성자를 실행하여 A를 출력
12~14 • B 클래스의 생성자를 실행하여 B를 출력
22
• 업 캐스팅 관계에서 변수를 출력하므로 자식 클래스의 변수에 접근할 수 없
기 때문에 부모 클래스의 a 변수인 3을 출력
23 • 오버라이딩 관계이므로 자식 클래스의 fn 메서드를 호출
15
• 자식 클래스의 fn 메서드에서는 변수에 접근할 수 있으므로 a는 5가 되어
"D"+5인 D5를 출력
r2오 w
oto
© 추상클래스 *
(1) 추상 클래스(Abstract Class) 개념
• 추상 클래스는 미구현 추상 메서드를 한 개 이상 가지며, 자식 클래스
에서 해당 추상 메서드를 반드시 구현하도록 강제하는 기능이다.
(2) 추상 클래스 구문 SB
▼ 추상 클래스 구문
abstract class 추상_클래스명 {
abstract 자료형 메서드명();// 메서드 내부는 정의하지 않음
}
이ass 자식_클래스명 extends 추상_클래스명{ [확인 필요]
자료형 메서드명(){
명령어;// 메서드를 상속받아 메서드 내부를 정의
}
^^9^1 頭
메서드 내부를 정의하지
않는다는 의미는 메서드
내부에 소스 코드를 이
용해서 구현하지 않는다
는 의미이고, 메서드 내
부를 정의한다는 의미는
메서드 내부를 소스 코
드를 이용해서 구현한다
는 의미입니다.
예%f으世 히！_
앞에서 강조했던 것 기
억하시나요? 일반 클래
스, 추상 클래스를 상속
할 때는 extends, 인터
페이스를 상속할 때는
implements라는 것을 [확인 필요]
꼭 기억해두세요.
Chapter 03 자바 6-195
## Page 382

]、개 념,박살내기 자바 추상 클래스
[소스코드
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
abstract class A {
abstract void fn( );
}
class B extends A {
void fn(){
System.out.print("B");
}
}
class C extends A{
void fn(){
System.out.print("C");
class Soojebi {
public static void main(String[ ] args){
A b=new B( );
A c=new C( );
b.fn( );
c.fn( );
출력 BC
[코드 해설
15 • main 함수의 시작 부분(프로그램이 제일 처음 실행되는 부분)
16
• B 클래스를 생성하여 b 변수에 저장(생성자가 없으= 생성자는 따로 호출하
지 않음)
17
• C 클래스를 생성하여 c 변수에 저장(생성자가 없으므로 생성자는 따로 호출하
지 않음)
18
•fn 메서드는 오버라이딩 관계이므로 자식 클래스인 B 클래스의 fn 메서드
실행
05~07 • fn 메서드에 의해 B를 출력
19
•fn 메서드는 오버라이딩 관계이므로 자식 클래스인 C 클래스의 fn 메서드
실행
10~12 • fn 메서드에 의해 C를 출력
6-196 VI 프로그래밍 언어 활용
## Page 383

⑫ 인터페이스 ★
(1) 인터페이스(Interface) 개념
• 인터페이스는 클래스가 구현해야 하는 메서드의 선언만을 포함하는 형
태이다. (인터페이스는 일종의 추상 클래스이다.)
• 오직 추상 메서드와 상수만을 멤버로 가질 수 있으며, 그 외의 다른 어
떠한 요소도 허용하지 않는다.
• 인터페이스는 구현된 것은 아무것도 없고 밑그림만 그려져 있는 '기본
설계도'라고 할수있다.
VIH
HU
IJ또 [확인 필요]
OEW-오 e
s
(2) 인터페이스 구문
▼ 인터페이스 구문
interface 인터페이스_클래스명 {
자료형 메서드명();// 메서드 내부는 정의하지 않음
}
class 자식_클래스명 .:ients 인터페이스_클래스명{
자료형 메서드명(){
// interface의 메서드를 상속받아 내두를 정의 [확인 필요]
}
、• / 짜 져
interface를 상속받을 [확인 필요]
때는 일반 상속을 받을
때 사용하는 extends가 [확인 필요]
아니라 implements 키
워드를 사용한다는 것을
챙겨가시기 바랍니다.
궤。박살내기 자바인터페이스
[소스코드]
01
02
03
04
05
06
07
08
09
10
11
12
interface A{
void fn();
}
class B implements A{
public void fn(){
System.outprint("B");
}
}
class C implements A{
public void fn(){
System.out.print("C");
談혜%뎌
소스 코드 동작하는 것을
자세히 보시면 abstract
클래스와 차이가 없습
니다.
Chapter 03 자바 6-197
## Page 384

13
14
15
16
17
18
19
20
21
}
class Soojebi{
public static void main(String args[ ]){
A b=new B( );
A c 三 new C( );
b.fn( );
c.fn( );
}
}
줄력
[코드 해설
BC
]
15 • main 메서드부터 시작
16
• B 클래스를 b라는 변수로 생성
• B 클래스를 b 변수에 생성하므로 B의 생성자 B()와 B의 부모인 A의 생성
자 A()를 호출해야 하지만, 둘 다 없으므로 클래스 생성 시 아무 일도 일어
나지 않음
17
• C 클래스를 c라는 변수로 생성
• C 클래스를 c 변수에 생성하므로 C의 생성자 C()와 B의 부모인 A의 생성
자 A()를 호출해야 하지만, 둘 다 없으므로 클래스 생성 시 아무 일도 일어
나지 않음
18 • 으라는 변수는 B 클래스이므로 B 클래스에 있는 fn() 메서드를 호출
05 • B 클래스의 fn() 메서드 호출
06 •B를 출력
19 • c라는 변수는 C 클래스이므로 C 클래스에 있는 fn() 메서드를 호출
10 • C 클래스의 fn() 메서드 호출
11 • C 를 줄력
曾g Point
enum은 상수 모음이고, [확인 필요]
문법은 클래스와 비슷합
니다.
® 열거형 ★★
(1) 열거형(En니meration) 개념 [확인 필요]
• 열거형은 서로 관련 있는 상수들의 집합을 정의할 때 사용하는 형태
이다.
6-198 VI 프로그래밍 언어 활용
## Page 385

enum 열거형명{
상수명1(매개변수값 1). 상수명2(매개변수값2), … ;
자료형 변수명;
열거형명(){ // 생성자
}
반환_자료형 메서드명(자료형 변수명, ••■){
명령어;
return 반환값;
}
VIH
HU:lm=
0°
r2오 w
olo
⑶ 열거형 메서드
▼ 열거형 메서드
메서드 설명
name() • 열거 객체의 문자열을 반환하는 메서드
ordinal() • 열거 객체의 순번을 반환하는 메서드
compareTo() • 열거 객체를 비교해서 순번의 차이를 반환하는 메서드
values() • 모든 열거 객체들을 배열로 반환하는 메서드
뿨!흐 박살내기 자바열거형메서드
[소스코드]
01 enum Alpha{
02 B("2"), C("3");
03 String n;
04 Alpha(String n){ this.n=n;}
05 public String get() {return n;}
06 }
07 public class Soojebi {
08 public static void main(String[ ] args) {
09 Alpha n=Alpha.C;
10 System.out.println(n.name( ));
11 System.out.println(n.ordinal( ));
12 System.out.println(n.compareTo(Alpha.A));
13 System.out.println(n.get( ));
14 for(int i三0; i<3; i++) {
15 System.out.print(Alpha.values( )[i]);
Chapter 03 자바 6-199
## Page 386

C
2
출력 2
3
ABC
P、心 三 박살내기 자바열거형 메서드
[소스코드]
enum Alpha{
A("1"), B("2"), C("3");
String n;
Alpha(String n){ this.n=n;}
public String get() {return n;}
}
public class Soojebi {
public static void main(String[ ] args) {
Alpha n三Alpha.C;
System.out.println(n.name( ));
System.out.println(n.ordinal( ));
System.out.println(n.compareTo(Alpha.A));
System.out.println(n.get( ));
for(int i=0; i<3; i++) {
System.out.print(Alpha.values( )[i]);
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
C
2
출력 2
3
ABC
[코드 해설]
08 • main 메서드 시작
09 • 열거형 상수 C를 변수 n에 저장
10 • 열거형 상수의 이름 "C"를 반환 및 출력
11 • 상수의 순서값 "2"를 반환 및 출력
12 • C와 A의 순번 차이인 "2"를 반환 및 출력
13 • 생성자에서 저장된 문자열 "3"을 반환 및 출력
14~16 • for 문 실행, i=0부터 i<3까지 반복하면서 순서대로 "ABC"를 출력
6-200 VI 프로그래밍 언어 활용
## Page 387

0 제네릭 ★★
⑴ 제네릭(Generic) 개념
• 제네릭은 클래스나 메서드가 다양한 타입을 처리할 수 있도록 일반화
하는 기능이다.
(2) 제네릭 문법
class 클래스명<T>{
}
클래스명<타입>변수명 = nw 클래스명<타입>();
•<T>는 타입 매개변수로, 이 자리에 실제 타입이 들어간다.
•<타입>자리에 실제 사용하고자 하는 타입 (Integer, String 등)을 넣는다.
[ok) . .
汗잠간! 알고가기
두후 개 념 박살내기 자바제네릭
[소스코드
class A<T> {
Tx;
public void setA(T x) {
this.x=x;
}
public T getA() {
return x;
}
}
public class Soojebi {
public static void main(String args[ ]){
A<String> a=new A< >( );
a.setA("H©llo");
System.out.println(a.getA( ));
A<lnteger>b=new A<>();
b.setA(100);
System.out.println(b.getA( ));
Integer
int 형의 래퍼 클래스
(Wrapper Class)로, int 데
이터 타입을 객체로 다
룰 수 있도록 제공하는
클래스이다.
Integer a=5;
Integer b=4;
System.out.
println(a+b);
 9 가 출력됨
Hello
100
Chapter 03자바 6-201
## Page 388

[코드 해설]
11 • main 메서드부터 시작
12
• 제네릭 클래스 A의 인스턴스를 String 타입으로 생성하여 a 변수에 대입
• A 클래스의 타입 매개변수 t는 String으로 지정되므로, A 클래스는 String [확인 필요]
타입으로 동작
13 • setA 메서드의 매개변수 x는 String 타입이 되며, 문자열형 "Hello"를 전달
03~04
• A 클래스의 x 변수에 "Hello"를 대입
• x는 String 타입으로 동작
14 • a.getA 메서드를 호출
06~08
• A 클래스의 丁는 String이므로 public String getA() 형태 [확인 필요]
• x 변수의 값이 "Hello"이므로 "Hello"를 반환
14 • a.getA() 반환 값인 "Hello"를 출력
16
• 제네릭 클래스 A°| 인스턴스를 Integer 타입으로 생성하여 b 변수에 대입
• A 클래스의 타입 매개변수 丁는 Integer로 지정되어, A 클래스는 Integer 타 [확인 필요]
입으로 동작
17 • setA 메서드의 매개변수 x는 Integer 타입이 되며, 정수형 100을 전달
03~04
• A 클래스의 x 변수에 100을 대입
• 여기서 x는 Integer 타입으로 동작
18 • b.getA 메서드를 호출
06 〜 08
• A 클래스의 丁는 Integer이므로 public Integer getA() 형태 [확인 필요]
• x 변수의 값이 100이므로 100을 반환
18 • a.getA() 반환 값인 100을 출력
⑶ 제네릭 오버로딩 관계 @^國
• 제네릭 변수를 매개변수로 전달할 때 제네릭이나 Object 타입으로 전
달한다.
6-202 VI 프로그래밍 언어 활용
## Page 389

개념 박 자바 제네릭 오버로딩⑴
[소스코드]
class A{
<T>void fn(T x) {
System.out.print("A"+x);
}
void fn(lnteger x) {
System.out.print("B"+x);
}
}
class B<T>{
T value;
public B(T t) {
value=t;
}
public void fn() {
new A( ).fn(value);
}
}
class Soojebi {
public static void main(String[ ] args) {
B x=new B<>(0);
x.fn( );
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23*
AO
[코드 해설
19 • main 메서드부터 시작
20 • B 클래스를 생성하고, 생성자 B<>(0)을 호출하여 x 변수에 대입
11~13
• public B(T t)에서 생성자에서 매개변수 t로 0을 전달받음
• 丁는 Integer 타입으로 결정되며, value 변수에 00| 대입
21 • x.fn()을 호줄
14~16
• A 클래스를 생성하고, fn(value) 메서드를 호출
• value은 타입이 제네릭 [확인 필요]
• 제네릭은 오버로딩 관계일 때 제네릭이나 Object 타입을 매개변수로 받는
메서드를 호출하므로 <T> void fn(T x) 메서드를 호출
02 〜 04 • x=0이므로 "A"+0이 되어 AO을 출력 [확인 필요]
Chapter 03 자바 6-203
## Page 390

제 박살내기 자바제네릭오버로딩⑵
[소스코드]
01 class A{
02 void fn(Object x) {
03 System.out.print("A''+x);
04 }
05 void fn(lnteger x) {
06 System.out.print("B"+x);
07 }
08 }
09 class B<T>{
10 T value;
11 public B(T t) {
12 value=t;
13 }
14 public void fn() {
15 new A( ).fn(value);
16 }
17 }
18 class Soojebi {
19 public static void main(String[ ] args) {
20 B x=new B<>(0);
21 x.fn( );
출력 A0
[코드 해설]
19 • main 메서드부터 시작
20 • B 클래스를 생성하고, 생성자 B<>(0)을 호출하여 x 변수에 대입
• public B(T t)에서 생성자에서 매개변수 t로 0을 전달받음
1改어3 • t는 Steger 타입으로 결정되며, value 변수에 0이 대입
21 • x.fn()을 호출
• A 클래스를 생성하고, fn(value) 메서드를 호줄
• v기니e은 타입이 제네릭
14〜1b • 제네릭은 오버로딩 관계일 때 제네릭이나 Object 타입을 매개변수로 받는
메서드를 호출하므로 void fn(Object x) 메서드를 호출
02~04 • x=0이므로 "A"+00| 되어 A0을 출력
6-204 VI 프로그래밍 언어 활용
## Page 391

O 예외 처리 ★ SHHHHHHHB
(1) 예외 처리(Exception Handling) 개념
• 예외 처리는 프로그램 실행 중 발생할 수 있는 예외적인 상황에 대해
적절히 대처하기 위한 기법이다.
(2) 예외 종류
VIS
而
Mm=
o°오오 S
• 예 외 종류는 ArraylndexOutOfBoundsException, Arithmetic -
Exception 등이 있다.
▼ 예외 종류
조 S OTT 설명
ArraylndexOutOfBoundsException
• 배열의 범위를 벗어난 인덱스에 접근하려고 할
때 발생하는 예외
ArithmeticException
• 수학적인 연산 중 오류가 발생할 때 발생하는
예외
NullPointerException
• 객체가 null인 상태에서 메서드나 필드에 접근하 [확인 필요]
려고 할 때 발생하는 예외
NumberFormatException
• 문자열을 숫자 타입으로 변환하려 할 때 형식이
맞지 않으면 발생하는 예외
IndexOutOfBoundsException
• 리스트나 문자열의 유효하지 않은 인덱스에 접근
할 때 발생하는 예외
(3) 예외 처리 구문
• 예외 처리 구문에 try, catch, finally기- 있다. [확인 필요]
▼ 예외 처리 구문
try {
// 예외 발생할 가능성이 있는 코드
}
catch (예외) {
// 예외가 발생할 때 실행하는 코드
}
finally {
// 예외 발생 여부와 관계없이 항상 실행되는 코드
}
try에서 예외가 발생하지 [확인 필요]
않을 경우 try 문이 끝나
고 finally 문을 실행합니
다. 반면에 try에서 예외 [확인 필요]
가 발생할 경우 예외 사항
이 발생하자마자 catch
문을 실행하고, catch 문
이 끝나면 finally 문을 실
행합니다.
Chapter 03자바 6-205
## Page 392

▼ 예외 처리 구조
블록 설명
try
• 예외가 발생할 수 있는 코드를 작성하는 블록
• try 블록 내에서 발생한 예외는 catch 블록으로 전달
catch • try 블록에서 발생한 예외를 처리하는 블록
finally
• 예외 발생 여부와 상관없이 항상 실행되는 블록
• finally는 있을 수도 있고, 없을 수도 있음 [확인 필요]
개 념 자바 예외 처리
04라인에서 10/0에서 에
러가 나면 곧바로 catch
문으로 이동합니다. 10/0
이 되는 순간 에러가 발
생하므로 result에 값 [확인 필요]
을 대입하기 전에 에러
가 발생하여 result에 값 [확인 필요]
이 대입되지 않은 상태
로 catch 문으로 이동하
고, catch 문이 끝나면
finally 문으로 이동합니
다. catch를 실행했는지 [확인 필요]
여부랑 상관없이 finally
를 실행한다는 부분은
헷갈리는 부분이니 꼭
기억해두세요.
[소스코드]
01 p니blic class Soojebi { [확인 필요]
02 public static void main(String[ ] args) {
03 try {
04 int result=10 / 0;
05 }
06 catch (ArithmeticException e) {
07 System.out.print("A");
08 }
09 finally {
10 System.out.printC'B");
11 }
12 }
13 }
출력 AB
[코드 해설]
02 • main 메서드부터 시작
03 • try〜catch 문 실행
04 • 10 / 0은 수학적 오류이므로 ArithmeticException 오류 발생
06 • ArithmeticException 오류 처리
07 • A를 출력
09 • try~catch를 처리하고 finally 문을 실행 [확인 필요]
10 • B를 출력
(4)throw, throws
• throw는 메서드 내부에서 직접 예외를 발생시킬 때 사용한다. [확인 필요]
• throws는 메서드 선언부에 이 메서드가 예외를 던질 수 았음을 선언할 [확인 필요]
6-206 VI 프로그래밍 언어 활용
## Page 393

때 사용한다.
자바 throw, throws
[소스코드]
01 class SoojebiException extends Exception {
02 public SoojebiExceptiorY ) {
03 System.out.print("A");
04 }
05 }
06 public class Soojebi {
07 public static void fn() throws SoojebiException {
08 System.out.print("B");
09 throw new SoojebiException( );
10 }
11 public static void main(String[ ] args) {
12 try {
13 System.out.print("c");
14 fn( );
15 System.out.print("D");
16 }
17 catch (SoojebiException e) {
18 System.out.print("E");
VI
IH
HU
IJ
nJH
oa
r5오 w
olo
출력 CBAE
[코드 해설]
11 • main 메서드부터 시작
12 • try 문을 실행
13 • C를 출력
14 • fn 메서드 호출
• fn 메서드는 SoojebiException을 던질 수 있다고 선언(throws Soojebi [확인 필요]
Exception)되어 있으므로, 호출한 try 블록 내에서 예외 처리가 필요
08 • B를 줄력
• fn() 메서드 내에서 SoojebiException 예외가 발생
• 예외를 발생시키며 SoojebiException 생성자를 호출
02~04》를출력
• 예외가 발생했으므로 try 블록을 종료하고 SoojebiException 예외를 처리
09 하는 catch 블록으로 이동
17~19 • SoojebiException 예외를 처리하는 catch 블록에서 E를 출력
Chapter 03 자바 6-207
## Page 394

지피지기 기출문제
► 20 년 1 회 ► 20 년 1s|
01 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi{
02 public static void main(String[ ] args){
03 int i ;
04 int [ ]a={0, 1, 2, 3};
05 for(i=0;i<4;i++){
06 System.out.print(a[i]+"
07 }
08 }
09 }
1=1______________ _ ____
우''5 02 • main 메서드부터 실행
03 • 누라는 이름의 정수형 변수를 선언
04
• a라는 이름의 정수형 배열을 선언하고, {0,
1, 2, 3}을 초깃값으로 저장
05 〜 06 • i=0일 때 a[이이므로 0번째 요소인 0이 출력
05 〜 06 • i=1 일 때 a[1]이므로 1번째 요소인 1이 출력
05 〜 06 • i=2일 때 a[2]이므로 2번째 요소인 2가 출력
05 〜 06 • i=3일 때 a[3]이므로 3번째 요소인 301 출력
다음은 자바 코드이다. 출력 결과를 쓰시오.
public class Soojebi{
public static void main(String[ ] args){
int i=3;
int k=1;
switch(i){
case 0:
case 1:
case 2:
case 3:k=0;
case 4:k+=3;
case 5:k—=10;
default :k—-;
}
System.out.print(k);
}
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
서 ___
「"리 02 • main 메서드부터 실행
03
• 너라는 이름의 정수형 변수를 선언하고, 3으
로 초기화
04
• k라는 이름의 정수형 변수를 선언하고, 1로
초기화
05 • 너는 3이므로 case 3으로 진입
09
• k=0에 의해 k는 0이 됨
• break가 없으므로 다음 명령어 실행 [확인 필요]
10
•k+=3을 실행하여 k는 3이 됨
• break가 없으므로 다음 명령어 실행 [확인 필요]
11
• k-=10을 실행하여 k는 一7이 됨
• break가 없으므로 다음 명령어 실행 [확인 필요]
12 • k--를 실행하여 k는 —8이 됨
14 • k 값인 —8을 출력
01. 0 1 23 02. -8
6-208 VI 프로그래밍 언어 활용
## Page 395

► 20년 3회 ► 20년 3회
()3 다음은 자바 코드이다. 다음 밑줄에 들어갈 키
워드를 쓰시오.
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
class Parent{
public void show(){
System.out.println("Parent");
}
}
class Child extends Parent{
public void show(){
System.out.println("Child");
}
}
public class Soojebi{
public static void main(String[ ] args){
Parent pa=Child( );
pa.show();
04 다음은 자바 코드이다. 출력 결과를 쓰시오,
class A{
private int a;
public A(int a){
this.a=a;
}
public void display(){
System.out.println("a="+a);
}
}
class B extends A{
public B(int a){
super(a);
super.display( );
}
}
public class Soojebi{
public static void main(String[ ] args){
B obj=new B(10);
}
0
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
• 자바에서 클래스를 생성하기 위해서는 new라는 키워 [확인 필요]
드를 써야 한다.
• main 메서드부터 실행
• new B(10);에 의해 생성자를 호출
• B 생성자는 10을 넘겨받았으므로 a=10
• 자식 클래스의 생성자의 첫 번째 명령어가
super가 있는 경우 부모 클래스에서 어떤 [확인 필요]
생성자를 호출하는지 결정
• B(int a) 안에 첫 번째 명령어는 super(10);
이므로 부모 클래스의 생성자는 파라미터
로 정수형을 받는 생성자인 A(int a)를 호출
03 • A 생성자는 10을 넘겨받았으므로 a=10
04 • 클래스 내부 필드인 this.a 에 a 값인 10을 대입
13 • 부모 클래스의 display 메서드를 호출
06 • display 메서드 호출
07
• 클래스 내부 필드인 a에 100| 저장되어 있으
므로 "a="+10인 "a너0"을 출력
03. new 04. a=10
지피지기 기출문제 6-209
## Page 396

► 20년 3회 ► 20년 3회 , 23년 1회
05 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 p니blic class Soojebi{ [확인 필요]
02 public static void main(String[ ] args){
03 int i=0;
04 int sum=0;
05 while(i<10){
06 i++;
07 if(i%2=l)
08 continue;
09 sum+=i;
10 }
11 System.out.println(sum);
12 }
13 }
r" 리 02 • main 메서드부터 실행
03 〜 04 • i, sum이라는 정수형 변수에 0을 초기화 [확인 필요]
05 • i=0 이므로 i<10 은참
06 • i++에 의해 i=i 이 됨
07 〜 08
• 를 2로 나눴을 때가 1이면(i가 홀수이면) 참
• i=1 이므로 if 문이 참이기 때문에 continue
를 실행
05 •i=1 이므로 i<10은 참
06 •i++에 의해 i=2가 됨
07 〜 08 • i=2이므로 if 문이 거짓이므로 if 문 안의 명
령어인 continue를 실행하지 않음 [확인 필요]
09 • sum 변수에 i 값인 2를 더해 sum은 2가 됨 [확인 필요]
• sum 변수는 i 값이 짝수일 때 더해지게  됨
06 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 abstract class Vehicle {
02 String name;
03 abstract public String getName(String val);
04 public String getName() {
05 return "Vehicle name:"+name;
06 }
07 public void setName(String val){
08 name=val;
class Car extends Vehicle {
public Car(String val) {
setName(val);
}
public String getName(String val) {
return "Car name:"+val;
}
public String getName(byte val[ ]) {
return "Car name:"+val;
public class Soojebi {
public static void main(String[ ] args) {
Vehicle obj 三 new Car("Spark");
System.out.println(obj.getName( ));
05 •i=9이므로 i<10은 참
06 •i+十에 의해 i=10이 됨
07〜 08 • i=10이므로 if 문이 거짓이므로 if 문 안의
명령어인 continue를 실행하지 않음 [확인 필요]
09
• sum 변수에 i 값인 10을 더함
• 누가 2, 4, 6, 8,10일 때 sum+=i;를 실행하
게  되므로 2+4+6+8+10=30이 됨
05 •i=10이므로 i<10은 거짓
11 • sum 변수의 값인 30을 출력
06. Vehicle name:Spark
6-210 vi 프로그래밍 언어 활용
## Page 397

► 20년 4회
r—1
1믜리 25
• main 메서드부터 실행
26
• Car라는 생성자를 실행하면서 매개변수로 [확인 필요]
"Spark"를 전달
• obj 변수에 Car 클래스가 생성됨
13 • Car 클래스의 생성자인 Car(String val)에
"Spark"를 넘겨주면 val="Spark"이 됨
14
• setName("Spark"); 으로 호출
•setName은 Vehicle 클래스에 있으므 [확인 필요]
로 Vehi이e 클래스의 setName 메서드에 [확인 필요]
"Spark" 값을 전달
07 •setName 메서드에서 매개변수로 받은
"Spark"를 val 변수에 저장
08 •val 값인 "Spark"를 name이라는 변수에 [확인 필요]
저장
27 • obj 변수의 getName 메서드를 호출
04
• getName에 파라미터가 없으므로 부모 클 [확인 필요]
래스의 getName() 메서드를 실행하게  되
고, Vehi이e의 getName에 있는 "Vehicle [확인 필요]
name:"+name;을 반환
• name은 이미 new Car("Spark")라는 생성 [확인 필요]
자에 의해서 "Spark"라는 값으로 대입이
되었기 때문에 getName에서는 "V이이이e [확인 필요]
name:"+"Spark"인 "Vehicle name:Spark"
를받게됨
27
• getName에서 반환받은 "Vehi이e name: [확인 필요]
Spark"를 System.out.println 함수를 이용
하여 출력
08 다음은 nO| 10일 때, 10을 이진수로 변환하는
자바 소스 코드이다. ①, ②에 알맞은 값을 적
으시오.
[출력 결과]
00001010
01 class Soojebi{
02 public static void main (String[ ] args) {
03 int [ ]a=new int[8];
04 int i=0;
05 int n=10;
06 while( ① ){
07 a[i++]= ② ;
08 n /=2;
09 }
10 for(i=7;i>=0;i--){
11 System.out.print(a[i]);
12 }
13 }
14 }
①__________________________________________________________________
②__________________________________________________________________
| 卜 20년 3회
07 C++에서 생성자란 무엇인지 쓰시오.
• 생성자는 일반적으로 클래스의 멤버 변수를 초기화하
거나 클래스를 사용하는 데 필요한 설정이 필요한 경우
사용한다.
• C++, 자바에서는 클래스 명과 동일한 메서드명을 가
지고, 반환 값이 없다.
허너스
『 07. :||당 클래스의 객체가 생성될 때 자동으로 호출되는 특수 [확인 필요]
한 종류의 메서드이다. 08. ① n>0 또는 n>=1 또는 i<8
또는 i<=7, ② n%2 또는 n&1
지피지기 기출문제 6-211
## Page 398

I지 • 십진수 n을 a의 배열을 이용해 2진수 값으로 저장한 후
출력을 하는 프로그램이다.
• 코드의 for 문을 보면 a[7] 번지부터 a[이 번지 순으로
출력하기 때문에 a[이 번지가 1의 자리가 된다.
02 • main 메서드부터 실행
03
• 정수형 8개짜리 a 배열 생성
• a 배열 안의 값은 전부 0으로 초기화
04 • i라는 이름의 변수를 선언 및 0으로 초기화
05 • n이라는 이름의 변수를 선언 및 10으로 초
기화
06
• while 문 안에서 a[i++]이라는 코드를 보
면 while 문이 a의 개수인 8번 이내로 반
복해야 하므로 조건식은 i<8이 가능
• n 값으로 a[i] 값을 계산하므로 n이 0보다 클
때 반복할 수 있도록 조건식은 n>0이 가능
07
• a[i]에는 0과 1°| 값이 들어가야 함(a는 2진수
값을 저장하기 때문에 0과 1만 값이 있어야 함)
• 2로 나눴을 때 나머지가 이진수 변환하
는데 필요로 하는 값이므로 ②에는 n%2가 됨
08 • n 을 2로 나눔
10〜12 • a[7] 번지부터 a[이 번지 순으로 출력
丄u서 [확인 필요]
1미, 리 02 • main 메서드부터 실행
03
•a 배열은 2차원 배열
• for 문에서 a[i][j]에서 느 0,1, 2이고, j는 0,
1, 2, 3, 4이므로 int[3개][5개]가 되어야 하
므로 int [ ]a=new int[3][5];가 되어야 함
04 •i=0,1, 2일 때 반복
05 • j=0,1, 2, 3, 4일 때 반복
j=0 i = 1 j=2 j=3 j=4
a[이이=
i=0 0*3+0+1
=1
a[이[1]=
1*3+0 뉘
=4
a[0][2]=
2*3+0 뉘
-1
a[이[3]=
3*3+0+1
긔 0
a[0][4]=
4*3+0 뉘
=13
06 a[1][이=
i=1 0*3 뉘+1
=2
a[1][1]=
1*3 뉘+1
=5
a[1][2]=
2*3+1 뉘
=8
a[1][3]=
3*3+1+1
=11
a[1][4]=
4*3+1+1
=14
a[2][0]=
i=2 0*3+2+1
=3
a[2][1]=
1*3+24-1
=6
a[2][2]=
2*3+2+1
=9
a[2][3]=
3*3+2뉘
=12
a[2][4]=
4*3+2+1
=15
07 • a[i][j] 값 출력
09 •개행
► 20 년 4 회
► 20 년 4 회 10 다음은 자바 소스 코드이다. 출력 결과를 쓰시오.
09 다음은 자바 소스코드이다. 출력 결과를 보고,
①, ②에 알맞은 값을 적으시오.
[출력 결과]
1 4710 13
2 5 8 11 14
36 9 12 15
01 class Soojebi{
02 public static void main (String[ ] args) {
03 int[ ][ ] a=new int[ ① ][ ② ];
04 for(inti=0;i<3;i++){
05 for(int j=0;j<5;j++){
06 a[i][j]듸*3+(i+1);
07 System.out.print(a[i][j]+"
08 }
09 System.out.println();
10 }
11 }
12 }
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
class Parent!
public int compute(int num){
if(num<=1) return num;
return compute(num—1)+compute(num - 2);
}
}
class Child extends Parent{
public int compute(int num){
if(num <=1) return num;
return compute(num—1)+compute(num-3);
}
}
class Soojebi{
public static void main(String[ ] args){
Parent obj=new Child();
System.out.print(obj.compute(4));
①
②
토후
『 09.2)3, ② 5 10. 1
6-212 VI 프로그래밍 언어 활용
## Page 399

1X.. 서!______________
ri 리 14 • main 함수부터 실행
15 • Child 클래스의 인스턴스를 생성하고, obj
변수에 저장
11
• obj의 compute 메서드 호출 [확인 필요]
• compute 메서드는 오버라이딩 관계이므로
자식 클래스인 Child 클래스의 compute
메서드가 실행
08 〜 12 • numO| 4일 때 if 문이 거짓이므로 compute
(3)+compute(1); 를 실행
08 〜 12 • numO| 3일 때 if 문이 거짓이므로 compute
(2)+compute(0); 를 실행
08 〜 12 • numO| 2일 때 if 문이 거짓이므로 compute
(1)+compute(-1);를 실행
08 〜 12 • num이 1일 때 if 문이 참이므로 1을 반환 [확인 필요]
C르I 02 • main 함수부터 실행 [확인 필요]
03
• arr이라는 이름의 2차원 배열 생성 [확인 필요]
45 arr[O][이
arr[O]50 arr•[이 [1]
75 arr[0][2]
89 arr[1][0] arr[1]
04 • arr[이은 {45, 50, 75} 3개이므로 301 출력됨
05 • arr[1]은 {89} 1개이므로 10| 출력됨
06 • arr[이[이의 값인 45가 출력
07 • arr[0][1]의 값인 50이 출력
08 •arr[1][이의 값인 89가 출력
16 • computed)의 반환값은 1 이므로 1을 출력 ► 21년 1회
4를 매개변수로 넘겨주어 soojebi 함수를 호출하고,
매개변수에 n-1 값과 n-3값을 각각 재귀 호출한 값을
더하여 화면에 출력한다.
compute(n) 리턴값
compute(4) compijte(3)+compiite(1)=0+1 =1
compute(3) compute(2) 十 compute(O)=0+0=0
compute(2) com pute(1)+com pute( -1)=1 — 1=0
computed) 1
compute(O) 0
compute(-l) -1
최종적으로 computed)은 compute⑶+compute(l)
이고, computed)은 0, compute⑴는 10| 되어 0과
1을 더한 1이 화면에 출력된다.
► 21년 1회
12 다음은 자바소스 코드이다. 출력 결과를쓰시오.
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
public class Soojebi{
public static void main(String[ ] args){
int i, j;
for(j=0, i=o;i<=5;i++) {
j+늬;
System.out.print(i);
if(i=5){
System.out.print("=");
System.out.print(j);
}
else {
System.outprint("+");
11 다음은 자바 소스 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi{
02 public static void main(String[ ] args){
03 int[ ][ ] an=new int[ ][ ]{{45, 50,75}, {89} };
04 System,out.println(arr[0],length);
05 System.out.println(arr[1].length);
06 System.out.println(arr[0][0]);
07 System.out.println(arr[이[1]);
08 System.out.println(arr[1][이);
09 }
10 } 12. 0+1+2+3+4+5=15
45
50
89
지피지기 기출문제 6-213
## Page 400

► 21년 2회l햇리 02 [확인 필요]
• main 메서드부터 실행
03 • 정수형 변수 i, j 를 선언
04
• for 문에서는 j=0, i=0으로 초깃값을 설정
하고 i가 5보다 작거나 같을 때까지 i 값을
1씩 증가하며 반복
• i=0이므로 i<=5를 만족하여 반복문 실행
05 • i=0이므로 j에 0을 더해서 j=0이 됨
06 • 너는 0이므로 0을 출력
07 • i=0이므로 if 문은 거짓이므로 else 문 안의
명령어 실행
12 • +를 출력
04 • i+十에 의해 i=l이 되고, i=1 이므로 i<=5
를 만족하여 반복문 실행
05 •i=1 이므로 j에 1을 더해서 j너이 됨
06 니는1이므로1을 출력
07 • i=1 이므로 if 문은 거짓이므로 else 문 안의
명령어 실행
12 •+를 출력
04 • i+十에 의해 i=2가 되고, i=2이므로 i<=5
를 만족하여 반복문 실행
05 • i=2이므로 j에 2를 더해서 j=3이 됨
06 • 누는 2이므로 2를 줄력
07 • i=2이므로 if 문은 거짓이므로 else 문 안의
명령어 실행
12 • +를 출력
04 • i++에 의해 i=3이 되고, i=3이= i<=5
를 만족하여 반복문 실행
05 • i=3이므로 j에 3을 더해서 j=6이 됨
06 • 더는 3이므로 3을 출력
07 • i=3이므로 if 문은 거짓이므로 else 문 안의
명령어 실행
12 • +를 출력
04 • i++에 의해 i=4가 되고, i=4이므로 i<=5
를 만족하여 반복문 실행
05 • i=4이므로 너에 4를 더해서 j=10이 됨
06 • 더는 4이므로 4를 출력
07 • i=4이므로 if 문은 거짓이므로 else 문 안의
명령어 실행
12 • +를 출력
05 • i=5이므로 j에 5를 더해서 j=15가 됨
06 • 더는 5이므로 5를 출력
07 • i=5이므로 if 문은 참이므로 if 문 안의 명령
어 실행
08 •=을 출력
09 • j 값인 15를 출력
13 다음은 자바 소스 코드이다. 출력 결과를 쓰시오.
01 class ovr1{
02 public static void main (String[ ] args){
03 ovr1 a1 三 new ovr1( );
04 ovr2 a2=new ovr2( );
05 System.out.print(a1.san(3, 2)+a2.san(3, 2));
06 }
07 int san(int x, int y){
08 return x+y;
09 }
10 }
11 class ovr2 extends ovr1{
12 int san(int x, int y){
13 return><一y+super.san(x, y);
14 }
15 }
12르1 02 • main 메서드부터 실행
03 • ovr1 클래스의 인스턴스를 생성해서 a1 변
수에 저장
04 • ovr2 클래스의 인스턴스를 생성해서 a2 변
수에 저장
05
• a1 변수는 ovr1 클래스이므로 ovr1 클래스
의 san 메서드를 호출
• a1.san(3, 2)이므로 x에 3을 y에 2를 전달
07 〜 08 • x=3, y=2이므로 3+2°1 5를 반환
05
• a2 변수는 ovr2 클래스인데, ovr2 클래스
는 ovr1 클래스를 상속받고 있으므로 san
메서드는 오버라이딩 관계
• 오버라이딩 관계이므로 자식 클래스인 ovr2
클래스의 san 메서드를 호출
• a2.san(3, 2)이므로 x에 3을 y에 2를 전달
12 • x=3, y=2를 전달
13
• s니per.san(x, y)는 부모 클래스의 san 메서 [확인 필요]
드를 호출하므로 super.san(3, 2)는 5가 됨
• x-y+super.san(3, 2)은 3—2+5이므로 6
이 반환됨
05 • a1.san(3, 2)은 5, a2.san(3, 2)은 6이므로
5+6인 11을 출력
6-214 VI 프로그래밍 언어 활용
## Page 401

► 21년 3회
14 다음은 자바 소스 코드이다. 출력 결과를 쓰시오
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
class Soojebi{
static private Soojebi instance=null;
private int counted;
static public Soojebi get(){
if(instance==null){
instance=new Soojebi( );
}
return instance;
}
public void co니nt( ){count++;} [확인 필요]
public int getCount( ){return count;}
}
public class Soojebi2{
public static void main(String[ ] args){
Soojebi s1=Soojebi.get();
s1.count( );
Soojebi s2=Soojebi.get( );
s2.count();
Soojebi s3=Soojebi.get();
s3.count( );
System.out.print(s1.getCount( ));
17
• instance는 Soojebi 클래스를 저장하고 있 [확인 필요]
기 때문에 만들어놨던 instance 변수를 s2
에 반환(S1 에 저장된 것과동일함)
18
• s2의 count 메서드를 실행하면 Soojebi 클
래스의 count 값이 1 증가하여 count 값이
2가됨
19 • Soojebi.get() 메서드를 호출
04 〜 07
• instance에 Soojebi 객체가 저장된 상태이 [확인 필요]
므로 instance가 null이 아니게  되어 if 문의 [확인 필요]
조건이 거짓
08 • instance 변수에는 기존에 저장했던 Soojebi
객체가 있으므로 Soojebi 객체를 반환
19
• instance는 Soojebi 클래스를 저장하고 있 [확인 필요]
기 때문에 만들어놨던 instance 변수를 s3
에 반환(S1 에 저장된 것과 동일함)
20
• S3의 count 메서드를 실행하면 Soojebi 클
래스의 count 값이 1 증가하여 count 값이
301 됨
21 •s1 의 count 값은 3이므로 getCount 메서
드를 실행하면 301 반환되어 301 출력됨
• Soojebi.get( ) 메서드를 호출하면 반환되는 값이
instance0|7| 때문에 s1, s2, s3에 저장되는 변수는 모
두 instance에 저장된 값을 저장하게  되어 s1.count(), [확인 필요]
s2.count(), s3.count()를 하게  되면 instance에 저장 [확인 필요]
된 Soojebi 객체의 count 값을 1 증가시키게  된다.
► 21년 2회
|해;| • get 함수에서 instance가 nulio| 아니면 instance에 [확인 필요]
Soojebi 객체가 저장된 상태이므로 기존에 저장했던
Soojebi 객체를 반환해준다.
15
14 • main 메서드부터 실행
15 • Soojebi.get() 메서드를 호출
04〜 07
• instance는 null인 상태이므로 instance: [확인 필요]
new Soojebi( );를 실행하여 instance 변수
에 Soojebi 클래스를 저장
08 • instance 변수를 반환
15 • get 메서드의 instance 반환 값을 s1 에 저장
16
•s1 의 count 메서드를 실행하면 Soojebi 클
래스의 count 값이 1 증가하여 count 값이
1이 됨
17 • Soojebi.get() 메서드를 호출
04〜 07
• instance에 Soojebi 객체가 저장된 상태이 [확인 필요]
므로 instance가 nullO| 아니게  되어 if 문의 [확인 필요]
조건이 거짓
08 • instance 변수에는 기존에 저장했던 Soojebi
객체가 있으므로 Soojebi 객체를 반환
다음은 자바 코드이다. 밑줄 친 곳에 들어갈 키
워드를 쓰시오.
[소스코드]
public class Soojebi{
public static void main(String[ ] args){
System.out.print(Soojebi.check(1));
}
String check(int num){
return (num>=0) ? "positive" : "negative";
}
}
01
02
03
04
05
06
07
08
[출력값]
positive
15. static
지피지기 기출문제 6-215
## Page 402

Li•.•서 ii
1°"리 02 • main 메서드부터 실행
03
• Soojebi 클래스의 check 메서드를 호출
• 일반적으로 다음과 같이 인스턴스(new
Soojebi( ))를 생성해서 접근해야 하지만,
Soojebi 클래스의 인스턴스 없이 Soojebi.
check와 같이 check 메서드를 호출하려 [확인 필요]
면 check 메서드는 static이어야 함 [확인 필요]
Soojebi a 三 new Soojebi( );
a.check(l);
05 • check(l)에 의해 num=1 이 됨
06
•num = 1 이므로 (num>= O)은 참이 되어
"positive"를 반환
03 • 반환받은 "positive"를 출력
► 21년 3회
16 다음은 자바 소스 코드이다. 출력 결과를 쓰시오.
public class Soojebi{
public static void main(String[ ] args){
int a=3, b=4, c=3, d=5;
if((a==:2 | a-=c) & !(c>d)
& (1==bAc!=d)) {
a=b+c;
if(7==bAc!三a) {
System.out.println(a);
}
else {
System.out.println(b);
}
}
else {
a=c+d;
if(7==cAd!=a) {
System.out.println(a);
}
else {
System.out.println(d);
}
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
r—1
1핵비 02
• main 메서드부터 실행
03
• 정수형 변수를 a=3, b=4, c=3, d=5로
초기화
04 〜 05
• a==2는 거짓이므로 0이 되고, a==c는
3==3이기 때문에 참이므로 1이 됨
• c>d는 3>5이므로 거짓이기 때문에 001 되
지만, 앞에 !(not 연산)이 있어 !0인 1이 됨
• l==b는 거짓이므로 0이 되고, c!=d는
3!=5(3과 5는 다름)이 참이므로 10| 되기 때
문에 0Al은 XOR 연산에 의해 참이 되어 [확인 필요]
1이 됨
• if((a==2 I a==c)&!(c>d)&(1==bAc!=d))
는 ifd&i&D과 같은데, (1&D&1 에서 앞의
(1&1)은 2진수로 바꿨을 때 같은 자릿수 간
에 AND 연산을 하면 101 되고, 1&1은 10|
므로 ifd&i&D은 if(D이 되어 참이 됨
06 • b는 4, c는 3이므로 a는 4+3인 701 됨
07
• if 문에서 7 = = b는 거짓이라 0이 되고,
c!=a는 3!=7이므로 참이라 1이 되므로 if
(7=bAc!=a)는 if(0A1)과 같고, 0과 1을 2진
수로 바꿨을 때 같은 자리끼리 XOR 연산
하면 1이므로 if(1)0| 되어 if 문 조건을 만족
08 • a 값인 7을 출력
6-216 VI 프로그래밍 언어 활용
## Page 403

► 22년 1회 ► 22년 1회
17 다음은 자바 코드이다. 출력 결과를 쓰시오.
class A {
int a;
int b;
}
public class Soojebi {
static void func1(A m){
m.a *=10;
}
static void func2(A m){
m.a+=m.b;
}
public static void main(String args[ ]){
A m=new A();
m.a=100;
func1(m);
m.b=m.a;
func2(m);
System.out.printf("%d", m.a);
}
5
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
C2르J 12 • main 메서드부터 실행 [확인 필요]
13 • A 클래스 타입의 m 변수에 A 클래스를 생성
14 • m 변수의 a 필드에 100을 저장
15 • fund 메서드 호출
06 〜 08 • fund 호출될 때 m.a 값이 100이므로 m.a
*=10에 의해 m.a 값이 1000이 됨
16 • m.b에 m.a 값인 1000을 저장
17 • func2 메서드 호출
09 〜 11
• func2 호출될 때 m.a 값이 1000이고, m.b
의 값이 1000이므로 m.a+=m.b에 의해
m.a 값이 200001 됨
18 • m 의 a 변숫값인 2000을 출력
18 다음은 스레드에 관한 코드이다. 다음 밑줄에
알맞은 코드를 쓰시오.
class Car implements Runnable{
int a;
public void run(){
System.out.println("run");
}
}
public class Soojebi{
public static void main(String args[ ]){
Thread t1=new __________________ ));
t1.start( );
01
02
03
04
05
06
07
08
09
10
11
12
|忌| • Runnable 인터페이스 상속하여 스레드를 구현할 수
있다.
public class Car implements Runnable{
public void run(){
// 스레드 동작 시 수행할 코드
}
}
public class Soojebi{
public static void main(String[ ] args){
Thread t=new Thread(new Car( ));
t.start( );
}
• 스레드를 만들기 위해서는 Runnable 인터페이스 상속
받고, 스레드를 생성하기 위해서 new 뒤에 Runnable
인터페이스를 상속받은 스레드 클래스를 선언해준다.
Thread 스레드변수=new Thread(new 상속받은 스레드
클래스());
18. Car
지피지기 기출문제 6-217
## Page 404

► 22년 2회 ► 22년 3회
19 다음은 자바 코드이다. 출력 결과를 쓰시오. 20 다음은 자바 코드이다. 출력 결과를 쓰시오.
H
2
3
4
5
6
7
8
9
O
1
2
3
4
5
6
7
8
9
O
O
O
O
O
O
O
O
O
1
1
1
1
1
1
1
1
1
1
public class Soojebi{
int a;
public Soojebi(int a) {
this.a=a;
}
int func() {
int b=1;
for (int i=1;i<a;i++){
b=a * i+b;
}
return a+b;
}
public static void main(String[ ] args){
Soojebi obj=new Soojebi(3);
obj.a=5;
int b=obj.func( );
System.out.print(obj.a+b);
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
O
O
O
0
O
0
O
O
O
1
1
1
1
1
1
class Soojebi{
public static void main(String[ ] args) {
int[ ] result=new int[5];
int[ ] arr={79, 34,10, 99, 50};
for(int i=0;i<5;i++) {
result[i]=l;
for(int j=0;j<5;j++) {
if(arr[i]<arr[j]) result[i]++;
}
}
for(int k=0;k<5;k++) {
System.out.print(result[k]);
02
03
r—n
I 리 13 • main 메서드부터 실행
14
• Soojebi 클래스의 인스턴스를 생성하고, obj
변수에 저장
• new Soojebi(3)을 통해 생성자 호출
03 〜05
• 파라미터 a에 3을 전달
• 클래스 내의 필드 a에 파라미터 a 값인 3을
대입
15 • obj 변수의 a 필드에 값을 5로 변경
16 • obj 변수의 func 메서드를 호출
06 • func 메서드 실행
07 • b라는 이름의 정수형 변수를 생성하고, 1로
초기화
08 〜 10
• a는 5이= i<5 조건이 참인 동안 반복문
을수행
• i너일 때 b는 a*i+b=5*1 十1=6
• i=2일 때 b는 a*i+b=5*2+6=16
• i=3일 때 b는 a*i+b=5*3+16=31
• i=4일 때 b는 a*i+b=5*4+31=51
11 • a는 5이고, b는 51이므로 a+b=5+51=56
을 반환
16 • b 변수에 obj.func 메서드의 반환값인 56
을 저장
17 • obj.a는 5이고, b는 56이므로 5+56=61을
출력
04
11~13
• main 메서드부터 실행
• 정수형 배열로 5칸의 공간을 갖는 result를 [확인 필요]
선언
• [79, 34, 10, 99, 50] 값을 갖는 정수형 배
열 arr을 선언 [확인 필요]
• 이중 for 문의 구조에서 res니t[i]의 초기값 [확인 필요]
은 1이며, arr 배열에 자기 자신보다 큰 수
의 개수를 찾으면 result[i]의 값을 1씩 늘
려 감
• 이중 for 문에 따른 result[i]의 값은 다음과
같이 변경
이중 for 문이 종료되고 새롭게  for 문이 실
행되며, result 배열에 가장 마지막으로 저
장된 값인 24513을 출력
i=0 i=1 i=2 i=3 i=4
j=0 1 2 2 1 2
i=1 1 2 3 1 2
j=2 1 2 3 1 2
j=3 2 3 4 1 3
j=4 2 4 5 1 3
20. 24513
6-218 VI 프=그래밍 언어 활용
## Page 405

► 22년 3회 ► 22년 3회
다음은 자바 코드이다. 출력 결과를 쓰시오.
public class Soojebi {
static int[ ] MakeArray(){
int[ ] tempArr=new int[4];
for(int i=0;i<tempArr.length;i++){
tempArr[i]=i;
}
return tempArr;
}
public static void main(String[ ] args){
int[ ] intArr;
intArr=MakeArray( );
for(int i=0;i<intArr.length;i++){
System.out.print(intArr[i]);
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
1
[買리 09 • main 메서드부터 실행
10 • 정수형 배열 intArr을 선언 [확인 필요]
11 • MakeArray 메서드를 통해 도출된 결과를
intArr에 저장 [확인 필요]
02 • 크기가 4인 정수형 배열 tempArr을 선언 [확인 필요]
03 〜 06
• for 문을 통해 배열의 크기인 4만큼 반복하
며, tempArr[i]에 i의 값을 넣고 반환
• for 문에 따른 tempArr 배열의 값은 다음과
같이 변경
i=0 i:더 i=2 i=3
tempArrfi] 0 1 2 3
07 • tempArr을 반환 [확인 필요]
11 • tempArr의 값을 그대로 intArr에 저장 [확인 필요]
12 〜 14 • for 문을 통해 순차적으로 출력하면 0123
이 출력
22 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args){
03 int a=0;
04 for(int i=1;i<999;i++){
05 if(i%3==0 && i%2!=0)
06 a긔;
07 }
08 System.out.print(a);
09 }
10 }
E3 02 • main 메서드부터 실행
03 • a라는 이름의 정수형 변수를 0으로 초기화
04 • for 문을 통해 i7^ 1부터 998까지 반복
05 〜 06
• if 문을 통해 의 값이 3으로 나누어 떨어지
고, = 나누어 떨어지지 않는 결과에 대해
서만 a의 값에 대입
• 3의 배수 [3, 6, 9, 12, 15, 18, 21, 24, 27,
30, 996]에서 짝수를 제외한 나머지 값
인 [3, 9, 15, 21, 27, … 993]0| 순서대로
a에 대입되고, a=993 이후에 if 문을 만족
하는 i 값이 없음
08 • a 값인 993을 줄력
22. 993
지피지기 기출문제 6-219
## Page 406

► 23년 1회 ► 23년 1회
23 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class Static {
02 public int a=20;
03 static int b=0;
04 }
05 public class Soojebi{
06 public static void main(String[ ] args) {
07 int a;
08 a=10;
09 Static. b=a;
10 Static st=new Static( );
11 System.out.println(Static.b++);
12 System.out.println(st.b);
13 System.out.println(a);
14 System.out.print(st.a);
24 다음은 자바 코드이다. 빈칸에 들어갈 코드를
쓰시오.(단, 변수명으로 쓰시오.)
class Soojebi{
static void swap(int[ ] a, int idx1, int idx2){
int t=a[id><1];
a[idx1]=a[idx2];
a[ ① ]=t;
}
static void Usort(int[ ] a, int len){
for(int i=0;i<len;i++){
for(int j=0;j<len-i-1;j++){
if(a[j]>a[j+1]) {
swap(a, j, j+1);
}
}
}
03
06
• 자바에서 main 메서드 실행 전에 static 변
수가 먼저 실행
• Static 클래스 내에 static int b=0;에 의해
븨트 static 변수에 0을 대입
• main 메서드 실행
• main 내부의 a 변수에 10을 대입한다.
public static void main(String[ ] args){
int [ ]item={5, 4, 9,1, 3, 7};
int nx=6;
Usort(item, ② );
for(int data:item) {
System, out. print(data+"
12 〜 14
07〜 08 0 Static.b
a10
09
main 내부의 a 변수값 10을 Static.b 변수
에 대입
10 Static.b
a10
10
Static 클래스가 st 변수에 할당
20 st.a
Static.b(또는 st.b)
a
10
10
11
System.out.println(Static.b++);에 의해
Static.b 값인 10이 출력되고, Static.b의 값
이 1 증가
20 st.a
Static.b(또는 st.b)
a
11
10
• st.b는 11, a는 10, sla는 20이므로 11, 10, [확인 필요]
2001 출력
①___________________________________ __________
②_______________________________________________
23.10 24. ① idx2, ② nx
11
10
20
6-220 vi 프로그래밍 언어 활용
## Page 407

• 정수형 배열을 버블 정렬을 사용해 오름차순으로 정렬
하는 함수를 구현하는 코드이다.
•프로그램에서 교환할 때 구문은 a=b;b=c;c=a;형
태가 되어야 하므로 t=a[idx1];a[idx1]=a[idx2];
a[ ① 1긔; 에서 ①은 idx2가 되어야 한다.
• Usort 메서드 호출하는 부분은 Usort(item, ② );이고,
전달받는 부분은 Usort(int[ ] a. int len)이므로 ②는 int
len에 전달하는 값이다. [확인 필요]
22 〜24
Usort 메서드가 끝나면 item 배열은 다음
과 같음
item[0] | item[1] item[2] item[3] item[4] item[5]
1 1 3 4 5 7 9
for 문을 반복하면서 item[이~item[5]의 값
인 1, 3, 4. 5, 7, 9를 차례대로 data에 대입 [확인 필요]
하고, data 값을 출력
main 메서드에서 int 형 변수는 nx 밖에 없..0므루 ②는
nx 가 되어야 한다.
18 • main 함수부터 시작
19
• item이라는 정수형 배열에 5, 4, 9, 1, 3, 7 [확인 필요]
값으로 초기화
item[이 item[2] item[3] item[4] item[5]
5 4 9 1 3 7
20 • 아라는 이름의 정수형 변수를 6으로 초기화
21 • Usort 메서드 호출
• item 배열과 ②라는 정수형 변수를 전달
08
• Usort 메서드에서 item 배열을 a라는 이름
으로 전달받고, ②라는 값을 len이라는 변 [확인 필요]
수로 전달받음
a[이 a[1] a[2] a[3] a[4] a[5]
5 4 9 1 3 7
09 • 바깥쪽 for 문은 i=0부터 시작
10 • 안쪽 for 문은 j=0부터 시작
11 • j=0이므로 a[이인 5와 a[1]인 4를 비교하면
if 문은 참이므로 if 문 안의 명령어를 실행
12 • swap 메서드 호출
• a 배열, j 값인 0, j+1 값인 1을 전달
02 • swap 메서드에서 a 배열을 전달받고, idx
1=0, idx2=1을 전달받음
03 • t라는 변수에 a[id><1]==a[이:=5를 대입
04
•a[id><1]인 a[이에 a[idx2]=a[1]==4를
대입
a[이 a[1] a[2] a[3] a[4] a[5]
4 4 9 1 3 7
05
• swap 메서드를 통해 a[이과 a[1] 값을 교환
해야하므로 t 값을 a[1] 번지에 대입해야 함
• t는 5이므로 a[idx2]=a[1]에 t 값인 5를 저
장
a[이 a[1] a[2] a[3] a[4] a[5]
4 _ 5 9 1 3 7
10 • j++에 의해 j=1 이 됨
11
• j=l이므로 a[1]인 5와 a[2]인 9를 비교하면
if 문은 거짓이므로 if 문 안의 명령어를 실
행하지 않음
► 23년 1회
25 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class Parent {
02 int x=100;
03 Parent() {
04 this(500);
05 }
06 Parent(int x) {
07 this.x=x;
08 }
09 int getX() {
10 return x;
class Child extends Parent {
int x=4000;
Child() {
this(5000);
}
Child(int x) {
this.x=x;
public class Soojebi {
public static void main(String[ ] args) {
Child obj=new Child( );
System.out.println(obj.getX( ));
}
}
25. 500
지피지기 기출문제 6-221
## Page 408

리 25 • main 메서드부터 실행
26
, new Child( )에 의해 클래스 생성하고, 클
래스를 생성하면서 생성자를 호출
• 생성자는 자식 클래스(Child) 생성자의 첫
번째 명령어에서 생성자를 호출하지 않으므
로 부모 클래스(Parent)의 생성자 중 파라미
터가 없는 생성자인 Parent() 호출하고, 그
다음에 자식 클래스(Child) 생성자를 호출
03
• 부모 클래스인 Parent 클래스의 생성자인
Parent()를 호출
04
• this(500)로 Parent 클래스에서 매개변수를
1개 가지는 Parent(int x) 생성자를 호출하
고 x에 500을 매개변수로 전달
06 〜 07
• this(500)에 의해 호출되고, this.x=x;에 의
해 x 값인 500을 this.x인 Parent 클래스의
변수 X에 대입
16
• 자식 클래스인 Child 클래스의 생성자인
Child()를 호출
17
• this(5000)로 Child 클래스에서 매개변수를
1개 가지는 Child(int x)생성자를 호출하고 x
에 5000을 매개변수로 전달
19 〜 20
•this(5000)에 의해 호출되고, this.x=x;에
의해 x 값인 5000을 this.x인 Child 클래스
의 변수 x에 대입(Parent 클래스 변수 x에는
500, Child 클래스 변수 x에는 500001 저장)
27 • getX() 메서드 호출
09 〜 10 • Parent 클래스에 있으므로 Parent 클래스
의 x값인 500을 반환
27 • 반환값 500을 출력
► 23년 2회
26 다음은 자바 소스 코드이다. 출력 결과를 쓰시오.
01 class Soojebi {
02 public static void main(String[ ] args) {
03 String str1="soojebi";
04 String str2="soojebi";
05 String str3=new String("soojebi");
06
07 System .out. pri nt I n(strl =str2);
08 System.out.println(str1 =str3);
09 System.out.println(str1.equals(str3));
10 System.out.println(str2.equals(str3));
11 }
12 }
자바에서 '==' 연산자는 객체의 주소값을 비교하고,
equals 메서드는 비교하는 두 대상의 값을 비교하는
메서드이 다.
02 • main 메서드부터 시작
03 •String 타입 변수 str1 선언 및 문자열
"soojebi"를 대입
04 •String 타입 변수 str2 선언 및 문자열
"soojebi"를 대입
05
• String 타입 객체 str3 선언 및 생성자 호출
하여 "soojebi"로 초기화
07 • strl과 str2가 같으므로 true를 출력 [확인 필요]
08 • strl 과 str3가 같지 않으므로 false를 출력 [확인 필요]
09 • strl의 equals에 str3을 전달하여 true를 출력 [확인 필요]
10 • str2의 equals에 str3을 전달하여 true를 [확인 필요]
출력
26. true
false
true
true
6-222 VI 프로그래밍 언어 활용
## Page 409

27 다음은 자바 코드이다. 출력 결과를 쓰시오.
► 23년 3회
01 public class Soojebi {
02 public static void main(String[ ] args) {
Parent c=new Child( );
c.paint( );
c.draw();
}
}
class Parent {
public void paint() {
System.out.print("A");
draw( );
}
public void draw() {
System.out.print("B");
draw( );
}
}
class Child extends Parent {
public void paint() {
super.draw( );
System.out.print("C'');
this.draw( );
}
public void draw() {
System.out.print("D'');
}
}
Xu 서 1________________ .
r" 리 02 • main 메서드부터 실행
03
• Child 클래스 생성자가 호출됨(코드에 생성
자가 없으므로 따로 실행되는 것은 없음)
• Child 클래스의 인스턴스가 c 변수에 저장
04
• paint() 메서드는 오버라이딩 관계이므로
자식 클래스인 Child 클래스의 paint 메서
드를 호출
20
• super는 상위 클래스이므로 super.draw() [확인 필요]
메서드는 상위 클래스인 Parent 클래스의
draw 메서드
14 •B를 출력
15
• draw 메서드 호출하는데, draw 메서드는
오버라이딩 관계이므로 자식 클래스인 Child
클래스의 draw 메서드를 호출
25 •D를 출력
16
• Parent 클래스의 draw() 메서드가 끝났으
므로 Parent 클래스의 draw( ) 메서드를
호출했던 곳(20번째 줄)으로 이동
21 •C를 출력
22 • this.draw( )에서 this는 자기 자신이므로 [확인 필요]
Child 클래스의 draw 메서드를 호출
25 • 日를 줄력
23
• Child 클래스의 paint 메서드가 끝났으므
로 paint 메서드 호출했던 곳(04번째 줄)으
로이동
05
• draw 메서드는 오버라이딩 관계이므로 자
식 클래스인 Child 클래스의 draw 메서드
를호출
25 • □를 출력
F하
27. BDCDD
지피지기 기출문제 6-223
## Page 410

| > 23년 3홰
28 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int sum=fact(7);
04 System.out.println(sum);
05 }
06 public static int fact(int n) {
07 if(n=1) {
08 return 1;
09 }
10 else {
11 return n*fact(n-1);
12 }
13 }
14 }
07 • if(4==i)은 거짓이므로 else 문을 실행
08
•fact(4)를 호출한 부분에 n*fact(n-1);인
4*fact(3)을 전달
• fact(3) 메서드를 호출
06 • n=3을 전달
07 • if(3==i}은 거짓이므로 else 문을 실행
08
•fact(3)을 호출한 부분에 n*fact(n-1);인
3*fact(2)를 전달
• fact(2) 메서드를 호출
06 • n=2를 전달
07 • if(2==i)은 거짓이므로 else 문을 실행
08
• fact(2)를 호출한 부분에 n*fact(n—1);인
2*fact(l) 을 전달
• fact(l) 메서드를 호출
06 • n=1 을 전달
07 • if(i==i)은 참이므로 1을 fact⑴ 호출한 부분
에반환
04 • sum 값은 5040이므로 5040을 출력
:0H :.fact 함수는 재귀함수로, 입력값인 7부터 재귀호출을
시작한다.
• fact 함수의 n값이 점차적으로 1씩 줄어들고, 가장 마
지막에 호출되는 fact(1)에서 리턴되는 값 1부터 역으
로 값을 곱해가면 fact(7)의 최종 리턴값이 5040가 되
고, 5040을 sum에 저장하고 출력한다. [확인 필요]
02 • main 메서드 실행
03
• sum이라는 정수형 변수에 fact(7)의 결과값 [확인 필요]
을 저장
• fact(7) 메서드를 호출
06 • n=7 전달
07 • if(7==l)은 거짓이므로 else 문을 실행
08
•fact(7)을 호출한 부분에 n*fact(n—1);인
7*fact(6)을 전달
• fact(6) 메서드를 호출
06 • n=6을 전달
07 • if(6==i)은 거짓이므로 else 문을 실행
08
•fact(6)을 호출한 부분에 n*fact(n-1);인
6*fact(5)를 전달
• fact(5) 메서드를 호출
06 • n=5를 전달
07 • if(5==l)은 거짓이므로 else 문을 실행
08
•fact(5)를 호출한 부분에 n*fact(n —1);인
5*fact(4)를 전달
• fact(4) 메서드를 호출
06 • n=4를 전달
► 23 년 3 회
29 다음은 자바 코드이다. 오류가 발생하는 라인의
번호를 쓰시오.
01 class Person {
02 private String name;
03 public Person(String val) {
04 name=val;
05 }
06 public static String get() {
07 return name;
08 }
09 public void print() {
10 System.out.println(name);
11 }
12 }
13 class Soojebi {
14 public static void main(String[ ] args) {
15 Person p=new Person("soojebi");
16 p.print( );
17 }
18 }
호하『28. 5040 29. 7
6-224 VI 프로그래밍 언어 활용
## Page 411

7번째 라인에서 get 메서드는 String 타입을 반환 타입
으루 가지는 static 메서드인데, name은 static 변수가 [확인 필요]
아니므로 에러가 발생한다.
01 • Person 클래스 선언
02 • name이라는 String 타입의 멤버 변수 선언 [확인 필요]
03 • Person 생성자 선언
04 • 파라미터 val을 name 변수에 저장 [확인 필요]
06
• 반환 타입이 String 타입인 get 메서드를
static 메서드로 선언
07 • static 변수가 아닌 name을 반환할 때 에러 [확인 필요]
발생
09 • print 메서드
10 • name을 화면에 출력 [확인 필요]
15 • Person 클래스의 생성자에 "soojebi"를 매
개변수로 전달하여 객체 p를 생성
16 • p.print 메서드를 호출
| ► 24년 1회  |
30 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class Soojebi{
02 static private Soojebi instance=n내I; [확인 필요]
03 private int count=0;
04 static public Soojebi get(){
05 if(instance=null){
06 instance=new Soojebi( );
07 }
08 return instance;
09 }
10 public void count(){ count++ ;}
11 public int getCount(){return count;}
12 }
13 public class Soojebi2{
14 public static void main(String[ ] args){
15 Soojebi s1=Soojebi.get( );
16 s1.count();
17 Soojebi s2=Soojebi.get();
18 s2.count();
19 Soojebi s3=Soojebi.get();
20 s3.count( );
21 s1.count();
22 System.out.print(s1 .getCount( ));
23 }
24 p 丁 , . :
I해'get 함수에서 instance가 n네이 아니면 instance에 [확인 필요]
Soojebi 객체가 저장된 상태이므로 기존에 저장했던
Soojebi 객체를 반환해준다.
14 • main 메서드부터 실행
15 • Soojebi.get() 메서드를 호출
04〜 07
• instance는 null인 상태이므로 instance三 [확인 필요]
new Soojebi( );를 실행하여 instance 변수
에 Soojebi 클래스를 저장
08 • instance 변수를 반환
15 • get 메서드의 instance 반환 값을 s1 에 저장
16
• s1 의 count 메서드를 실행하면 Soojebi 클
래스의 count 값이 1 증가하여 count 값이
10| 됨
17 • Soojebi.get() 메서드를 호출
04〜 07
• instance에 Soojebi 객체가 저장된 상태이 [확인 필요]
므로 instance가 nulio| 아니게  되어 if 문 [확인 필요]
의 조건이 거짓
08 • instance 변수에는 기존에 저장했던 Soojebi
객체가 있으므로 Soojebi 객체를 반환
17
• instance는 Soojebi 클래스를 저장하고 있 [확인 필요]
기 때문에 만들어놨던 instance 변수를 s2
에 반환(S1 에 저장된 것과 동일함)
18
• s2의 count 메서드를 실행하면 Soojebi 클
래스의 count 값이 1 증가하여 count 값이
2가됨
19 • Soojebi.get() 메서드를 호출
04〜 07
• instanceoil Soojebi 객체가 저장된 상태이
므로 instance가 nulio| 아니게  되어 if 문 [확인 필요]
의 조건이 거짓
08 • instance 변수에는 기존에 저장했던 Soojebi
객체가 있으므로 Soojebi 객체를 반환
19
• instance는 Soojebi 클래스를 저장하고 있 [확인 필요]
기 때문에 만들어놨던 instance 변수를 S3
에 반환(S1 에 저장된 것과 동일함)
20
• s3의 count 메서드를 실행하면 Soojebi 클
래스의 count 값이 1 증가하여 count 값이
3이 됨
21
• s1 의 count 메서드를 실행하면 Soojebi 클
래스의 count 값이 1 증가하여 count 값이
4가됨
22 •s1 의 count 값은 4이므로 getCount 메서
드를 실행하면 4가 반환되어 4가 출력됨
• Soojebi.get( ) 메서드를 호출하면 반환되는 값이
instance이기 때문에 s1, s2, s3에 저장되는 변수는 모 [확인 필요]
두 instance에 저장된 값을 저장하게  되어 s1.count(), [확인 필요]
s2.count(), s3.count()를 하게  되면 instance에 저장 [확인 필요]
된 Soojebi 객체의 count 값을 1 증가시키게  된다.
지피지기 기출문제 6-225
## Page 412

► 24 년 1 회
31 다음은 자바 코드이다. 프로그램 동작 순서를
①~⑦의 번호로 쓰시오.(단, 번호는 중복되지
않아야 한다.)
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
class Parent {
int x, y;
Parent(int x, int y) { // ①
this.x=x;
this.y=y;
}
int getA() { // ②
return x*y;
}
class Child extends Parent {
int x;
Child(int x) { //(3)
super(x+1, x);
}
int getA(int n) { // ④
return x+x;
23 • main 메서드부터 실행
24
• new Child(3)에 의해 클래스 생성하고, 클
래스를 생성하면서 생성자를 호출
• Child(int x) 생성자에 3을 전달
14 • Child(int x) 생성자에서 x=3을 전달받음
15
•super(x + 1, 이를 통해 상위 클래스인
Parent 클래스의 생성자를 호출
•x=3이므로 super 메서드를 통해 4, 3을
전달
03 • Parent(int x, int y) 생성자에 x=4, y=3을
전달받음
04 • Parent의 x 변수에 4를 대입 [확인 필요]
05 • Parent의 y 변수에 3을 대입 [확인 필요]
24 • Child 클래스의 인스턴스를 parent 변수에
저장
25
• parent.getA( ) 메서드를 호출하면 매개변
수를 받지 않는 Parent 클래스의 getA( )
메서드를 호출
07 • getA() 메서드를 통해 Parent 클래스에 저
장된 x 값인 4와 y 값인 3을 곱한 12를 반환
25 • parent.getA( )의 반환값이 12이므로 12를
출력
public class Soojebi {
public static void main(String[ ] args) {// ⑤
Parent parent=new Child(3);// ⑥
System.out.println(parent.getA( ));// ⑦
6-226 VI 프로그래밍 언어 활용
## Page 413

► 24년 1회 ► 24년 2회
32 다음은 자바 코드이다. 출력 결과를 쓰시오. 33 다음은 자바 코드이다. 출력 결과를 쓰시오.
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
class A{
int a, b;
public A(int a, int b) {
this.a=a;
this.b=b;
class B extends A{
int c=3;
public B(int i) {
super(i, i+1);
}
public void print() {
System.out.println(c*c);
public class Soojebi{
public static void main(String[ ] args) {
B a=new B(1O);
a.print( );
}
r-1
「"린 20 • main 메서드부터 실행
21
• new B(10)에 의해 클래스 생성하고, 클래
스를 생성하면서 생성자를 호출
• B(int i) 생성자에 10을 전달
11 • B(int i) 생성자에서 =0을 전달받음
12
• super(i, i+1)를 통해 상위 클래스인 A 클래
스의 생성자를 호출
• i=10이므로 super 메서드를 통해 10, 11을
전달
03 • Parent(int a, int b) 생성자에 a=IO, b=l1 을
전달받음
04 • A의 a 변수에 10을 대입
05 • A의 b 변수에 11을 대입
21 • B 클래스의 인스턴스를 b 변수에 저장
22 • a.print() 메서드를 호출
14 • print 메서드 실행
15
•c는 B 클래스 초기값인 3이므로 3*3인 9
를 출력
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
리 08 • main 메서드부터 시작
09 〜 11 • a, b, c 배열을 선언
12 • check 메서드에, a, b 배열의 참조를 전달
02 • main 메서드로부터 a, b의 참조 값을 전달
받음
03 • a, 으는 다른 객체를 가리키므로 if 문은 거짓
06 •N을 출력
13 • check 메서드에, b, c 배열의 참조를 전달
02 • main 메서드로부터 b, c의 참조 값을 전달
받음
03 • b, c는 다른 객체를 가리키므로 if 문은 거짓
06 •N을 출력
14 • check 메서드에, a, c 배열의 참조를 전달
02 • main 메서드로부터 a, c의 참조 값을 전달
받음
03 • a, c는 다른 객체를 가리키므로 if 문은 거짓
06 • N 을 줄력
파
32. 9 33. NNN
지피지기 기출문제 6-227
## Page 414

► 24년 2회
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
34 다음은 자바 코드이다. 출력 결과를 쓰시오.
interface A {
int sum(int[ ] a, boolean odd);
}
class B implements A {
public int s니m(int[ ] a, boolean odd) { [확인 필요]
int result=O;
for(int i=O;i<a.length;i++) {
if((odd && a[i]%2!=0)|| (!odd && a[i]%2=0))
res 니 t+=a[i];
}
return result;
class Soojebi {
public static void main(String[ ] args) {
int a[ ]={1, 2, 3, 4, 5, 6, 7, 8, 9};
B x=new B();
System.out.print(x.sum(a, irue)+", "+x.sum(a, false));
}
I믜리 16
• main 메서드부터 시작
17 • a 배열 선언
18
• B 클래스를 x 변수에 생성하므로 B의 생성
자 B( )를 호출해야 하지만, 생성자가 없으므
로 클래스 생성 시 아무 일도 일어나지 않음
19
• x.sum(a, true) 메서드를 호출
• 오버라이딩 관계이므로 B 클래스의 sum
메서드를 호출
05
• a 변수에 main 메서드의 a 배열을 sum 메
서드의 a 배열 변수에, ture를 odd 변수에 [확인 필요]
전달
06 • result 변수를 0으로 초기화
07 • a 배열의 크기가 9이므로 alength는 9가 됨 [확인 필요]
• i=0부터 i<9일 때까지 반복
08〜 10
• odd는 true이므로 !odd는 f세se가 됨 [확인 필요]
(odd && a[i] % 2!=0)|| (k》dd && a[i] % 2==0)
(true && a[i] % 2!=0) || (false && a[i] % 2=三0)
• && 연산은 하나라도 false이면 false가 됨 [확인 필요]
(true && a[i] % 2(=0)|| false
• a[i] % 2!=0가 참이면 조건식이 참이 됨
(true && true) || false — true || false — true
• a[i] % 2 W가 거짓이면 조건식이 거짓이 됨
(true && false) || false — false || false — false
•a[i] % 2!=0가 참이면 조건식이 참이 되므
로 a[i]가 홀수일 때 조건식이 참이 되므로
result는 a[0], a[2], a[4], a[6], a[8] 값인 1, 3, [확인 필요]
5, 7, 9가 차례로 더해져 result는 25가 됨 [확인 필요]
11 • result 값인 25를 반환
19
• x.sum(a, false) 메서드를 호출
• 오버라이딩 관계이므로 B 클래스의 sum
메서드를 호출
05
♦ a 변수에 main 메서드의 a 배열을 sum 메
서드의 a 배열 변수에, ture를 false 변수에 [확인 필요]
전달
06 • result 변수를 0으로 초기화
07 • a 배열의 크기가 9이= ajength는 9가 됨 [확인 필요]
• i=0부터 i<9일 때까지 반복
08 〜 10
• odd는 false이므로 !odd는 true가 됨 [확인 필요]
(odd && a[i] % 2 !=0)|| (!odd && a[i] % 2==0)
(false && a[i] % 2 !=0)|| (true && a[i] % 2==0)
• && 연산은 하나라도 false이면 false가 됨 [확인 필요]
false || (true && a[i] % 2==0)
• a[i] % 2==0가 참이면 조건식이 참이 됨
f게 se 11 (true && true) ― false 11 false —* true
08 〜 10
• a[i] % 2=0가 거짓이면 조건식이 거짓이 됨
false || (true && false) —+ false || false — false
• a[i] % 2=0가 참이면 조건식이 참이 되므
로 a[i]가 짝수일 때 조건식이 참이 되므로
result는 a[1], a[3], a[5], a[7] 값인 2, 4, 6, [확인 필요]
801 차례로 더해져 result는 2001 됨 [확인 필요]
11 • result 값인 20을 반환
12
• x.sum(a, true)는 25이고, x.sum(a, false)는
20이므로 print(25+", "+20)이 되어 25, 20
이 출력됨
20
6-228 VI 프로그래밍 언어 활용
## Page 415

► 24년 2회
35 다음은 자바 코드이다. 출력 결과를 쓰시오.
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
class Soojebi {
public static String fn(String str, int index, bootean[ ] seen) {
if(index<0) return "";
char c=str.charAt(index);
String result=fn(str, index-1, seen);
if(!seen[c]) {
seen[c]=true;
return c+result;
}
return result;
}
public static void main(String[ ] args) {
String str="abacabcd";
int length=strJength();
booleanf ] seen=new boolean[256];
System.out.print(fn(str, length-1, seen));
1의르] 12
• main 메서드부터 시작
13 • str 변수에 "abacabcd" 대입
14
•str 문자열의 길이는 8이므로 str.length()
는 8
• length 변수에 8을 대입
15
• seen 배열을 선언
• 초기화가 안 되어 있으므로 256개 값 모두
false 로 초기화됨
16 • fn(str, length-1, seen) 호출
02
• str 배열 변수에 main 메서드의 str 배열을,
index에 7>, seen 배열 변수에 main 메 [확인 필요]
서드의 seen 배열을 전달
03 • index는 7이기 때문에 index<O은 거짓이 [확인 필요]
므로 if 문 안의 문장을 실행하지 않음
04 • c 변수에 str의 7번지 값인 'd'를 대입 [확인 필요]
05
• index가 7이므로 fn(str, 6, seen)을 호출하 [확인 필요]
고, fn(str, 6, seen)O| 완료된 후에 06〜10라
인 실행 … ①
03 • index는 6이기 때문에 index<O은 거짓이 [확인 필요]
므로 if 문 안의 문장을 실행하지 않음
04 • c 변수에 str의 6번지 값인 'c'를 대입 [확인 필요]
05
• index가 6이므로 fn(str, 5, seen)을 호출하 [확인 필요]
고, fn(str, 5, seen)O| 완료된 후에 06〜10라
인실행 … ②
04 • c 변수에 str의 1번지 값인 V를 대입 [확인 필요]
05
• index가 1이므로 fn(str, 0, seen)을 호출하 [확인 필요]
고, fn(str, 0, seen)이 완료된 후에 06~10
라인 실행 ... ⑦
03 • index는 00|7| 때문에 index<O은 거짓이 [확인 필요]
므로 it 문 안의 문장을 실행하지 않음
04 • c 변수에 str의 0번지 값인 'a'를 대입 [확인 필요]
05
• index가 0이므로 fn(str, -1, seen)을 호출하 [확인 필요]
고, fn(str, -1, seen)0| 완료된 후에 06〜10
라인 실행 … ⑧
03
• index는 -1이기 때문에 index<0은 참이므 [확인 필요]
로 if 문 안의 문장을 실행
• ""(빈 문자열)을 반환
05
• ⑧을 이어서 실행
• ""(빈 문자열)을 반환받았으므로 result는 [확인 필요]
""(빈 문자열)
06
• c 변수는 'a'이고, 'a'는 97
•seen[97]은 false이므로 !seen[9기은 true [확인 필요]
가 되어 if 문을 실행
07 • seen[97]=true가' 됨 [확인 필요]
08 • C의 값인 'a'에 ""(빈 문자열)를 더하여 반환
하므로 "a"를 반환
05
• ⑦을 이어서 실행
• "a"을 반환받았으므로 result는 "a" [확인 필요]
06
• c 변수는 'b'이고, 'b'는 98
•seen[98]은 false이므로 !seen[98]은 true [확인 필요]
가 되어 if 문을 실행
07 • seen[98]=true 가 됨
08 • C의 값인 'b'에 "a"를 더하여 반환하므로 "ba"
를 반환
05
• ②을 이어서 실행
• "cba"을 반환받았으므로 result는 "cba" [확인 필요]
06
• c 변수는 'c'이고, 'c'는 99
• seen[99]는 true이므로 !seen[98]은 false [확인 필요]
가 되어 if 문을 실행하지 않음
10 • result 값을 반환하므로 "cba"를 반환
05
• ①을 이어서 실행
• "cba"를 반환받았으므로 result는 "cba" [확인 필요]
06
•c 변수는 'd'이고, 'd'는 100
•seen[10이은 false이므로 !seen[10이은 [확인 필요]
true가 되어 if 문을 실행 [확인 필요]
07 • seen[10이三true가 됨 [확인 필요]
08 • c의 값인 'd'에 "abc"를 더하여 반환하므로
"dcba"를 반환
16 • fn(str, length-1, seen)의 반환값어 "dcba"
이므로 dcba를 출력 [확인 필요]
index는 1 이기 때문에 index<0은 거짓이 [확인 필요]
므로 if 문 안의 문장을 실행하지 않음
지피지기 기출문제 6-229
## Page 416

► 24 년 3 회
36 다음은 자바 코드이다. 출력 결과를 쓰시오.
1 class Soojebi {
2 static void func(String[ ] sM, int size) {
3 for (int i=l;i<size;i++) {
4 if (sM[i-1].equals(sM[i])) {
5 System.out.print("O");
6 }
7 else {
8 System.out.print("N");
9 }
10 }
11 for (String m:sM) {
12 System.out.print(m);
13 }
14 }
15 public static void main(string[ ] args) {
16 Stringf ] sM=new String[3];
17 sM[이="A";
18 sM[1]="A";
19 sM[2]=new String("A");
20 func(sM, 3);
21 }
22 }
03 •i++에 의해 i=3이 되고, i=3일 때, i<3는
거짓이 되어 for 문을 종료
11 •sM의 요소가 3개이므로 for each 문을 [확인 필요]
3번 반복
12 • sM[이의 "A"를 m에 대입하고 System.out.
print(m)에 의해 "A" 출력
11 〜13 • sM[1]의 "A"를 m에 대입하고 System.out.
print(m)에 의해 "A" 출력
11 〜13 • sM[2]의 "A"를 m에 대입하고 System.out.
print(m)에 의해 "A" 출력
► 24년 3회
다음은 자바 코드이다. 출력 결과를 쓰시오.
class Base{
int x=3;
int getX() {
return x*2;
I 해할 15 • main 메서드부터 프로그램 시작
16
• 배열의 크기가 3인 String 타입 변수 sM 선
언 및 생성
17 • sM[이에 문자열 "A" 대입
18 • sM[1]에 문자열 "A" 대입
19 • new 키워드를 사용하여 문자 "A"> 값으
로 가지는 새로운 String 객체를 생성
20 • func 메서드를 호출
•sM과3을 매개변수로 전달 [확인 필요]
02 • tunc 메서드를 실행
03 • i=|부터 시작하고, i<size은 1<3이므로 참 [확인 필요]
이 되어 for 문을 실행
04 • sM[이의 "A"와 sM[1]의 "A"는 같은 "A" 이
므로 참이 되어 if 문을 실행
05 • "0"를 출력
03 • i+十에 의해 i=2가 되고, i=2일 때, i<3는
참이 되어 for 문을 실행
04 • sM[1]의 "A"와 sM[2]의 "A"는 같은 "A"이
므로 참이 되어 "0"를 출력
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
class Derivate extends Base{
int x=7;
int getX() {
return x*3;
class Soojebi {
public static void main(String[ ] args) {
Base b=new Derivate();
Derivate d=new Derivate( );
System.out.print(b.getx( )+b.x+d.getX( )+d.x);
36. OOAAA 37. 52
6-230 VI 프로그래밍 언어 활용
## Page 417

► 24년 3회
38 다음은 자바 코드이다. 출력 결과를 쓰시오.
Lu 서 ! 스
16 • main 메서드부터 프로그램 시작
17
• 자식 클래스인 Derivate 클래스의 인스턴
스를 생성하고, 부모 클래스인 Base 타입
변수 b에 대입
• b의 타입은 Base지만, 실제 인스턴스는 [확인 필요]
Derivate
18
• 자식 클래스인 Derivate 클래스의 인스턴스
를 생성하여 Derivate 타입 변수 d에 대입
• 변수 거는 Derivate 타입이므로 직접적으로
Derivate의 필드와 메서드를 사용 [확인 필요]
19
• b.getX( ) 호출 시, getX 메서드는 오버라
이딩 관계에 있으므로 Derivate 클래스의
getX 메서드가 실행
10〜12 • Derivate 클래스의 x 값은 7이므로, 7*3=
21을 반환
19
• b.x에서 b의 타입은 Base이므로, 필드 x는 [확인 필요]
Base 클래스의 x 값인 3을 사용
• 메서드와 다르게 , 변수는 오버라이딩되지
않고 타입에 따라 결정
19 • d.getX() 호출 시, Derivate 클래스의 getX
메서드가 실행
10〜12 • Derivate 클래스의 x 값은 7이므로, 7*3=
21을 반환
19 • d.x는 Derivate 타입이므로 Derivate 클래
스의 x 값인 7을 사용
19
• b.getX()는 21, b.x는 3, d.getX()는 21, d.x
는 7이므로, 21+3+21+7=52가 되어 52
를 출력
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
public class Soojebi {
public static void main(String[ ] args) {
int sum=0;
try {
func( );
}
catch (NullPointerException e) {
sum三sum+1;
}
catch (Exception e) {
sum=sum+10;
}
finally {
sum=sum+100;
}
System.out.print(sum);
}
static void func() throws Exception {
throw new Nu 11 Poi nterException();
' 02 • main 메서드부터 프로그램 시작
03 • sum이라는 변수를 0으로 초기화 [확인 필요]
04 • try 문 시작
• 예외가 발생하면 그 즉시 catch 문으로 이동
05 • func 메서드 호출
18
• NullPointerException 예외를 throw하므 [확인 필요]
로 해당 예외를 처리할 수 있는 catch 문으
로이동
07 • NullPointerException 예외를 처리할 수
있는 catch 블록을 실행
08 • sum에 1을 더하여 sum은 1이 됨 [확인 필요]
13 • try~catch 문이 종료되었으므로 finally 문
을실행
14 • sum에 100을 더하여 sum은 100이 됨 [확인 필요]
16 • sum 값인 101이 출력됨
지피지기 기출문제 6-231
## Page 418

► 24년 3회 ► 25년 1회
39 다음은 자바 코드이다. 출력 결과를 쓰시오.
class Printer{
void print(lnteger x) {
System.o 니 t.print("A"+x);
}
void print(Object x) {
System.oulprint("B"+x);
}
void print(Number x) {
System.out.print("C"+x);
}
}
class Collection<T>{
T value;
public Collection(T t) {
value=t;
}
public void print() {
new Printed ).|아'int(value); [확인 필요]
}
}
class Soojebi {
public static void main(String[ ] args) {
new Collection<>(0).print();
}
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
" 다음은 자바 코드이다. 출력 결과를 쓰시오.
public class Soojebi {
public static void main(String[ ] args) {
int a=5,b=0;
try{
System.out.print(a/b);
}
catch(ArithmeticException e){
System.outprint("출력 1");
}
catch(ArraylndexOutOfBoundsException e) {
System.out.printf 출력 2");
}
catch(NumberFormatException e) {
System.out.printC 출력 3");
}
catch(Exception e){
System.out.pri nt(" 출력 4");
}
finally{
System.out.print("출력 5");
}
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
L"2J 22 • main 함수부터 프로그램 시작
23
• new Collection<>(0)으로 C 에 ection 클래스
의 인스턴스를 생성하기 때문에 Collection
생성자를 호출
14 • Collection 생성자 호출하고, t는 타입이
Integer가 되고, 느는 0을 전달 [확인 필요]
15 • t 값인 0을 Collection 내부 변수인 value
에 대입
23
• new Collection<lnteger>(0) 인스턴스의
print 메서드를 호출
17 • print 메서드 실행
18
• Printer 클래스의 print(O)을 호출
• print 메서드는 오버로딩 관계인데, 제네릭
은 Object 타입으로 Object# 매개변수로
받는 print(Object x) 메서드를 호출
05 〜 07 • X는 0이므로 "B"+0인 B0을 출력
I햇리 02
• main 메서드 시작
03 • 정수형 변수 a에 5, b에 0으로 초기화
04 〜 06
• try 문으로 a/b를 계산하여 출력
• 5/0으로 나누는 시도로 인해 Arithmetic-
Exception(산술연산 예외) 발생
07~09 • ArithmeticException 발생했으므로 "출력1"
을 출력
19〜21 • finally 문은 예외 발생 여부 상관 없이 무조
건 "출력5"를 출력
• 산술연산 예외가 실행되었으므로 배열 인덱스 예외,
문자열 숫자 변환 예외, 그 외 모든 예외 처리는 실행
하지 않는다.
ArraylndexOutOfBoundsException 배열 인덱스 예외
NumberFormatException
문자열 숫자
변환 예외
Exception
그 외모든
예외를 처리
40. 줄력 1 줄력 5
6-232 VI 프로그래밍 언어 활용
## Page 419

► 25년 1회
41 다음은 자바 코드이다. 출력 결과를 쓰시오.
class Parent{
static int total=0;
int v=1;
public Parent(){
total += (++v);
show();
}
public void show(){
total += total;
}
}
class Child extends Parent{
int v=10;
public Child(){
v •■+= 2;
total += v++;
show( );
}
©Override
public void show(){
total += total*2;
}
}
class Soojebi {
public static void main(String[ ] args) {
new Child( );
System.out.println(Parent.total);
}
}
H 실
三 • 프로그램 시작과 동시에 static 변수 total
선언 및 0으로 초기화
25 • main 메서드에서 프로그램 시작
26 • Child 클래스 생성
• 클래스를 생성하면서 Child() 생성자 호출
14
• Child 생성자 실행
• super( )가 명시되지 않았기 때문에, 자
식 클래스의 생성자에서는 부모 클래스인
Parent의 매개변수가 없는 생성자를 호출 [확인 필요]
04 • Parent 클래스의 생성자 실행
05
• Parent의 v는 1 증가하여 2가 됨 [확인 필요]
• Parent의 v 값인 2를 total 변수에 더하여 [확인 필요]
total 은 2가 됨
06
• 아10W 메서드는 오버라이딩 관계이므로 자
식 클래스의 아iow()를 호출 [확인 필요]
20 • show 함수 실행
21
• total 값은 2이므로 total*2=2*2=4가 되
고, 4를 total 값에 더하게  되면 기존 total
값인 2에서 4를 더하게  되어 601 됨
07 • Parent 생성자 종료하고 Child 클래스의
생성자로 돌아감
15 • Child 클래스의 v 값 10에 2를 더하여 12
가됨
16
• v 값 12를 total에 더하게  되어 total은 18 [확인 필요]
이 됨
• v 값을 1 증가시켸3이 됨
17 • show 메서드는 오버라이딩 관계이므로 자
식 클래스인 Child의 show()를 호출 [확인 필요]
20 • show 메서드 실행
21
• total 값은 18이므로 total*2=18*2=36이
되고, 36을 total 값에 더하게  되면 기존 total
값인 18에서 36을 더하게  되어 54가 됨
18 • Child 생성자 종료
27 • Parent.total 값은 54이므로 54를 화면에
출력
지피지기 기출문제 6-233
## Page 420

► 25년 1회| [확인 필요]
42 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 static int fn(int[ ] a, int st, int end) {
03 if(st>=end) return 0;
04 int mid=(st+end)/2;
05 return a[mid]+Math,max(fn(a, st, mid), fn(a, mid+1, end));
06 }
07 public static void main(String[ ] args) {
08 int[ ] values={3, 5, 8,12,17};
09 System.out.println(fn(values, 0, values.length-1));
10 }
11 }
| 해설 • 자바로 작성된 재귀 호출 코드이다.
07 • main 메서드에서 프로그램 시작
08
정수형 배열 values# 3, 5, 8, 12, 17로 초
기화
values[이 values[1] values[2] values[3] values[4]
3 5 8 12 17
09
• values는 57Hol므로 values.length는 5 [확인 필요]
가됨
• 매개변수에 values, 0 그리고 values,
length-1인 4를 전달하여 fn메서드를 호 [확인 필요]
출함
02
a는 values 배열, st는 0, end는 4가 전달 [확인 필요]
되어 fn 메서드 실행
a[이 a[1] 日 [2] a[3] a[4]
3 5 8 12 17
03 • if 문의 조건식인 st>=end는 0>=4이므로 [확인 필요]
거짓이 되어 if 문을 실행하지 않음
04 •(st+end)/2는 (0+4)/2이므로 mid에 2를 [확인 필요]
대입함
05
• a[2] + Math.max(fn(a, 0, 2), fn(a, 3, 4))를
반환
• fn(a, 0, 2)과 fn(a, 3. 4) 반환값을 계산해야
하므로 0 fn(a, 0, 2)과 © fn(a, 3, 4)을 호출
• 0의 반환값은 8이고, Q의 반환값은 12이
므로 a[2]+Math.max(fn(a, 0, 2), fn(a, 3,
4))=8+Math.max(8,12)=8+12=20이 됨
09 • fn(values, 0, values.length-1) 값인 20을
출력
• 0 fn(a, 0, 2)를 호출한 결과는 다음과 같다.
02 〜 05
• st는 0, end는 2가 전달되어 fn 메서드 실행 [확인 필요]
• if 문의 조건식인 st>=end는 0>=2이므로 [확인 필요]
거짓이 되어 if 문을 실행하지 않음
02 〜 05
•(st+end)/2는 (0+2)/2이므로 mid에 1을 [확인 필요]
대입함
• a[1]+Math.max(fn(a, 0, 1), fn(a, 2, 2》를 반
환해야 하므로 © fn(a, 0,1)과 0 fn(a, 2, 2)
를 호줄
• ©의 반환값은 3이고, ©의 반환값은 0이
므로 a[1] + Math.max(fn(a, 0, 1), fn(a, 2,
2))=5+Math.max(3, 0)=5+3=8이 됨
• 반환값은 801 됨(0)
• © fn(a, 0,1)을 호출한 결과는 다음과 같다.
02〜 05
• st는 0, end는 10| 전달되어 fn 메서드 실행 [확인 필요]
• if 문의 조건식인 st>=end는 0>=1이므로 [확인 필요]
거짓이 되어 if 문을 실행하지 않음
• (st+end)/2는 (0+1)/2이므로 mid에 0을 [확인 필요]
대입함
• a[1]+Math.max(fn(a, 0, 0), fn(a, 1,1))을 반
환해야 하므로 © fn(a, 0, 0)과 © fn(a, 1,1)
을호출
• ©의 반환값은 0이고, ©의 반환값은 0이
므로 a[0]+Math.max(fn(a, 0, 0), fn(a, 1,1))
=3+Math.max(0, 0)=3+0=3이 됨
• 반환값은 301 됨(0)
• © fn(a, 0, 0)을 호출한 결과는 다음과 같다.
02 〜 05
• st는 0, end는 0이 전달되어 fn 메서드 실행 [확인 필요]
• if 문의 조건식인 st>=end는 0>=0이므로 [확인 필요]
참이 되어 if 문을 실행하여 0을 반환
• 반환값은 0이 됨 (©)
• © fn(a, 1,1)을 호출한 결과는 다음과 같다.
02 〜 05
• st는 1, end는 10| 전달되어 fn 메서드 실행 [확인 필요]
• if 문의 조건식인 st>=end는 1>=1이므로 [확인 필요]
참이 되어 if 문을 실행하여 0을 반환
• 반환값은 001 됨(©)
• 0 fn(a, 2, 2)를 호출한 결과는 다음과 같다.
02 〜 05
• st는 2, end는 2가 전달되어 fn 메서드 실행 [확인 필요]
• if 문의 조건식인 st>=end는 2>=2이므로 [확인 필요]
참이 되어 if 문을 실행하여 0을 반환
• 반환값은 0이 됨(0)
• © fn(a, 3, 4}을 호출한 결과는 다음과 같다.
02 〜 05
• st는 3, end는 4가 전달되어 fn 메서드 실행 [확인 필요]
• if 문의 조건식인 st>=end는 3>=4이므로 [확인 필요]
거짓이 되어 if 문을 실행하지 않음
• (st+end)/2는 (3+4)/2이므로 mid에 3을 [확인 필요]
대입함
• a[3]+Math.max(fn(a, 3, 3), fn(a, 4, 4))을 반
환해야 하므로 0 fn(a, 3, 3)과 © fn(a, 4, 4)
을호출
• G의 반환값은 0이고, ©의 반환값은 0이
므로 a[3]+Math.max(fn(a, 3, 3), fn(a, 4, 4))
=12+Math.max(0, 0)=12+0=12가 됨
• 반환값은 30| 됨(@)
6-234 VI 프로그래밍 언어 활용
## Page 421

• O fn(a, 3, 3)을 호출한 결과는 다음과 같다.
02 〜 05
• st는 3, end는 301 전달되어 fn 메서드 실행 [확인 필요]
• if 문의 조건식인 st>=end는 3>=3이므로 [확인 필요]
참이 되어 if 문을 실행하여 0을 반환
• 반환값은 0이 됨(©)
• © fn(a, 4, 4)을 호출한 결과는 다음과 같다.
02 〜 05
• st는 4, end는 4가 전달되어 fn 메서드 실행 [확인 필요]
• if 문의 조건식인 st>=end는 4>=4이므로 [확인 필요]
참이 되어 if 문을 실행하여 0을 반환
• 반환값은 00| 됨(0)
• 재귀함수 관계는 다음과 같다.
fn(values, 0, 4) a[2]+Math.max(fn(a, 0, 2), fn(a, 3, 4))
=8+Math.max(8,12)=8+12=20
fn(a, 0, 2) a[1]+Math.max(fn(a, 0,1), fn(a, 2, 2))
=5+Math.max(3, 0)=5+3三8
fn(a, 3, 4) a[3]+Math.max(fn(a, 3, 3), fn(a, 4, 4))
=l2+Math.max(0, 0)=12+0=12
fn(a, 0,1) a[1]+Math.max(fn(a, 0, 0), fn(a, 1,1))
=3+Math.max(0, 0)=3+0=3
fn(a, 2, 2) 0
fn(a, 0, 0) 0
fn(a, 1,1) 0
fn(a, 3, 3) 0
fn(a, 4, 4) 0
► 25년 1회
43 다음은 자바 코드이다. 출력 결과를 쓰시오.
public class Soojebi {
public static void main(String[ ] args) {
System.out.println(calc("5"));
}
static int calc(int value) {
if(value<=l) return value;
return calc(value—1)+calc(value-2);
}
static int calc(String str) {
int value=Integer.valueOf(str);
if(value<=1) return value;
return calc(value-1)+calc(value—3);
01
02
03
04
05
06
07
08
09
10
11
12
13
14
J 02 • main 메서드에서 프로그램 시작
03 • calc("5") 를 실행
09 〜 13
• calc 메서드의 str에 문자열 "5"를 전달 [확인 필요]
• str은 "5"이므로 lnteger.valueOf("5")의 반 [확인 필요]
환값인 정수 5를 value 변수에 대입
• value는 5이므로 value<=l은 거짓이 되어 [확인 필요]
if 문을 실행하지 않음
• calc(4)+calc(2)을 반환해야 하므로 calc(4)
와 calc(2)의 반환값을 계산
• calc(4)는 3을 반환하고, calc(2)는 1을 반환
하므로 3+1=4가 되어 4를 반환
05 〜 07
calc(4)
• value는 4이로 value<=1은 [확인 필요]
거짓이 되어 if 문을 실행하지
않음
• calc(3)+calc(2)을 반환
• calc(3)은 2이고, calc(2)은 10|
므로 2+1=3을 반환
calc(3)
• value는 3이므로 value<=1 은 [확인 필요]
거짓이 되어 if 문을 실행하지
않음
• calc(2)+calc(l)을 반환
• calc(2)는 2이고, calc(1)은 0이
므로 1+1=2를 반환
c 게  c(2)
• value는 2이므로 value<=1은 [확인 필요]
거짓이 되어 if 문을 실행하지
않음
• calc(1)+c게 c(0)을 반환
• calc(1)은 1이고, calc(아은 00|
므로 1+0=1을 반환
calc(l) • value는 1이므로 value<=l 은 [확인 필요]
참이 되어 value 값인 1을 반환
calc(O) • value는 0이므로 value<=1은 [확인 필요]
참이 되어 value 값인 0을 반환
03 • calc("5")는 4를 반환하므로 4를 출력
지피지기 기출문제 6-235
## Page 422

► 25년 2회 ► 25년 2회
녀 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi{
02 public static void fn(String[ ] data, String s){
03 data[O]=s;
04 s="Z";
public static void main(String[ ] args) {
String data[ ]={"A"};
String s="B";
fn(data, s);
System.out.print(data[이+s);
애 己 07 • main 메서드부터 시작
08 • data 문자열 배열에 {"A"}로 초기화
09 •s 변수에 "B"로 초기화
10 •data 배열은 참조값(주소)이 전달되며, s는
문자열 참조 "B" 자체가 값으로 전달됨
02 • data 변수에 main의 data 배열, s 변수에 [확인 필요]
"B"를 전달받음
03 • data[()]에 "B"를 대입
04
• s 변수에 "Z"를 대입
• fn 메서드의 지역 변수는 main 메서드의 s
에는 영향이 없음
11 • data[이의 값인 "B"와 s 변수의 값인 "B"를
출력
45 다음은 자바 코드이다. 출력 결과를 쓰시오.
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
14 Ff=(x)->{
15 if(x>2){
16 throw new RuntimeException( );
17 }
18 return x*2;
19 };
20 System.out.print(run(f)+run((int n)->n+9));
6-236 VI 프로그래밍 언어 활용
## Page 423

► 25년 2회
13 • main 메서드부터 시작
14 〜 19
• F 타입의 변수 f0|| 익명 함수(X)->{...}을 대입
• 해당 익명 함수은 x>2이면 Runtime-
Exception 예외를 발생시키고, 그렇지 않
으면 x*2를 반환
20 • run(f) 메서드를 실행
05
• run 메서드를 실행
• f0|| main 함수의 14~19라인의 익명 함수를
대입
07 • f.apply(3)을 실행
14 〜 19
•f.apply(3)을 호출하면 익명 함수의 매개변
수에 301 전달되어 x=3이 되고 x>2 조건이
참이므로 RuntimeException 예외가 발생
09 • RuntimeException 예외가 발생하였으므로
catch 문을 실행
10 • 7을 반환
20 • run(f) 의 반환값은 701 됨
20 • run((int n)—>n+9))을 실행
• f는 익명함수(int n)—>n+9)
05 • run 메서드를 실행
• foil ((int n)->n+9)라는 익명 함수를 대입
07
• f.apply(3)을 실행
• ((int n)—>n+9)에서 n에 301 대입되어 3+9
인 12가됨
• return 12가 되어 12를 반환
20 • run((int n)—>n+9))의 반환값은 12가 됨
20 • run(f)는 7이고, run((int n)->n+9)는 12이므
로 7+12=19를 출력
46 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static class Parent {
03 public int x(int i) {return i+2;}
04 public static String id() {return "P";};
05 }
06 public static class Child extends Parent {
07 public int x(int i) {return i+3;}
08 public String x(String s) {return s+"R";}
09 public static String id() {return "C";}
10 }
11 public static void main(String[ ] args) {
12 Parent ref=new Child( );
13 System.out.println(ref.x(2)+ref.id( ));
1《희 11
• main 메서드부터 시작
12 • Parent의 변수 ref에 Child 클래스의 인스 [확인 필요]
턴스를 대입
13
•ref.x(2)는 x 메서드가 오버라이딩이므로
자식 클래스인 Child 클래스의 x 메서드를
실행
03 • x 메서드의 매개변수로 i에 3을 전달하므로
i+3 인 5를 반환
13
• ref.id()는 id 메서드들이 static이기 때문에 [확인 필요]
ref의 타입인 Parent 클래스의 id 메서드를 [확인 필요]
실행
09 • id 메서드에서 "P"를 반환
지피지기 기출문제 6-237
## Page 424

► 25 년 2회
47 다음은 자바 코드이다. 출력 결과를 쓰시오.
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9
0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
2
p니blic class Soojebi { [확인 필요]
public static class B0{
public int v;
public BO(int v) {
this.v=v;
}
}
public static void main(String[ ] args) {
BO a=new BO(1);
BO b=new BO(2);
BO c=new BO(3);
BO[ ] arr={a, b, c};
BO t=arr[이;
arr[이=arr[2];
arr[2]=t;
arr[1].v 三 arr[이.v;
System.out.printlrXa.v 十 "a" 十 b.v+"b"+ c.v);
11 • b 변수에 BO 클래스의 인스턴스를 대입
「"리 09 • main 함수부터 시작
10 • 생성자 B0(1)을 호출
04 〜 06 • V는 1이므로 해당 인스턴스의 V 변수에 1을
대입
10 • a 변수에 B0 클래스의 인스턴스를 대입
11 • 생성자 B0⑵를 호출
04 〜 06 • v는 2이므로 해당 인스턴스의 v 변수에 2를
대입
• t의 값인 a를 arr[2]에 대입
16 arr[이 arr[1] arr[2]
o b __a_
17
• arr[이은 c이므로 c.v 값인 3을 arr[1].v에
대입
arr[O]=c arr[1] 가) arr[2]=a
c.v=3 b.v=3 a.v=l
18
• a.v는 1, b.v는 3, c.v는 3이므로 a.v+"a"+
b.v+"b"+c.v는 1+"a"+3+"b"+3이 되어
1a3b3을 출력
► 25 년 3 회
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
48 다음은 자바 코드이다. 빈칸에 들어갈 키워드
를 작성하시오.
interface Person {
void introduce( );
}
class Student Person {
private String name;
public Student() {
this.name="Yuna";
}
public void introduce() {
System.out.printlnC'Hello, my name is "+name);
}
}
public class Soojebi{
public static void main(String[ ] args) {
Student st니dent=new Student( ); [확인 필요]
student. introduce( );
}
6
 7
 8
 9
1— 1- 1- 1—
12 • 생성자 B0(3)를 호줄
04〜 06 • v는 3이므로 해당 인스턴스의 v 변수에 3을
대입
12 • c 변수에 B0 클래스의 인스턴스를 대입
13
• arr 배열을 a, b, c로 초기화
arr[O] arr[1] arr[2]
a b c
14 • t 변수에 arr[이인 a를 대입
15
• arr[이에 arr[2]인 c를 대입
arr[이 arr[l] arr[2]
C b c
하헤
• interface를 상속받을 때는 일반 상속을 받을 때 사용하 [확인 필요]
는 extends가 아니라 implements 키워드를 사용한다. [확인 필요]
48. implements
6-238 VI 프로그래밍 언어 활용
## Page 425

► 25년 3회 ► 25년 3회
49 다음은 자바 코드이다. 빈칸에 들어갈 키워드
를 작성하시오.
class Rectangle {
int x, y;
Rectangle(int x, int y) {
this.x=x;
this.y=y;
}
int getArea() {
return x*y;
5
02
03
04
05
06
07
08
09
10커
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
class Square extends Rectangle {
Square(int s) {
_____________
}
int getSquareArea() {
return s* s;
}
}
public class Soojebi {
public static void main(String[ ] args) {
Square sq=new Square(lO);
sq.getArea( );
50 다음은 자바 코드이다. 출력 결과를 쓰시오.
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 int x=7, y=4, z;
04 z=y%3<3?2:1;
05 z三z&(z>>1);
06 z=(x>5&&z<=3) ? (z*x): (z/x);
07 System.out.printf("%d z);
08 }
09 }
느]
I 해설 I
02 • main 메서드 시작
03 • 정수형 변수 X, y, Z 선언
04
• y%3=4%3 = 1
• 삼항연산자를 통해 1<3은 참이므로 z=2
가됨
05
• z는 2진수로 10이고 z>>1 은 2진수로 01
10
& | 01
00
06
• (x>5&8z<=3)
• 삼항 연산자에 따라서 (7>5&&0<=3)는 참
이므로, z=z*x=0*7=0이 됨
07 • z의 값 0 출력
• 자바는 super 키워드를 이용하여 상위 클래스의 변수
나 메서드에 접근 할 수 있다.
부모 클래스 내부 변수 접근 super. 변수;
부모 클래스 내부 메서드 접근 super. 메서드(매개변수);
부모 클래스 내부 생성자 접근 super(매개변수);
49.super 50. 0
지피지기 기출문제 6-239
## Page 426

► 25년 3회
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
51 다음은 자바 코드이다. 출력 결과를 쓰시오.
enum Tri {
A("A"), B("AB"), C("ABC");
private String code;
Tri(String code) {
this.code=code;
}
public String code() {
return code;
public class Soojebi{
public static void main(String[ ] args) {
Tri t=Tri.values( )[TriAname( ).length( )];
System.out.print(t.code( ));
}
01 • Tri 열거형 선언 시작
02 • 열거형 상수 A("A"), B("AB"), C("ABC") 정의
03 • 문자열 필드 code 선언
04 〜 06
• 생성자 Tri(String code)로 상수 초기화 (this,
code=code)
07〜 09 • 메서드 code() 정의 및 code 값 반환
10 • 열거형 Tri 종료
11 • Soojebi 클래스 선언 시작
12 • main 메서드 시작
13
• Tri.A.name()은 "A"이고, 길이는 1이 됨
• Tri.values( )[1]0| 되어 Tri.B를 선택하고 변
수 t에 대입
14 • t.code() 호출 결과 "AB" 출력
6-240 VI 프로그래밍 언어 활용
## Page 427

코 천기누설 on 상문제
다음은 자바 코드이다. 출력 결과를 쓰시오. 02 다음 자바의 출력 결과를 쓰시오.
01
02
03
04
05
06
07
08
09
10
11
12
13
14
class Soojebi{
public static void main (String[ ] args){
int x=1;
int tX=O, t_X=O;
tX=(x>0)?x:-x;
if(x>0)
t_X=x;
else
t_X=-x;
System.out.println(tX+" "+t_X);
01
02
03
04
05
06
07
08
09
10
11
class Soojebi{
public static void main (String[ ] args){
int a=17;
a+=1;
a-=2;
a*=3;
a/=4;
a%=5;
System.out.print(a);
}
E
j 서 :i
「리 02 • main 메서드부터 실행
03 • x=l 로 초기화
04 • tx=o, t_x=o 으로 초기화
06
• 삼항 연산자는 조건이 참일 경우 물음표(?)
와 콜론(:) 사이의 값을 반환하고, 조건이
거짓일 경우 콜론(:)과 세미콜론(;) 사이의
값을 반환하는 연산자
• x>0은 참이므로 tx=x가 됨(tx=1)
07 • 乂는1이기 때문에 x>0가 참
08 • x는 1이므로 t_X=1 이 됨
12
• tx+" "는 숫자와 문자열을 더한 형태로 tx 의
1과 " "가 합쳐져 "1 " 형태의 문자열이 됨
• tX+" "과 t_X를 더하면 "1 "+t_X 형태인데,
문자열인 "1 "와 t_X의 101 합쳐져 "11"이 됨
• "1 1"이라는 문자열을 printin 함수를 이용
해 출력하면 11이 출력됨
I 02 • main 메서드부터 실행
03 • a=17 로 초기화
04 • a에 17에서 1을 더한 18을 저장
05 • a에 18에서 2를 뺀 16을 저장
06 • a에 16에서 3을 곱한 48을 저장
07 • a에 48에서 4를 나눈 12를 저장
08 • a에 12에서 5로 나눴을 때 나머지인 2를 저장
09 • a 값인 2를 출력
01. 1 1 02.2
천기누설 예상문제 6-241
## Page 428

03 다음 자바의 출력 결과를 쓰시오. 04 다음은 자바 코드이다. 출력 결과를 쓰시오.
n
2
3
4
5
6
7
8
9
o
1
2
3
4
5
6
7

0
0
0
0
0
 0
 0
0
0
1
1
1
1
1
1
1
1
class Soojebi{
public static void main(String[ ] arg){
int a=26;
int b=91;
int i=0, g=0;
int min=a<b ? a:b;
for(i=2;i<min;i++){
if(a % i=0 && b % i==0){
g=i;
System.out.println(g);
1
2
3
4
5
6
7
8
9
0
1
2
3
4
O
O
O
O
O
O
O
O
O
1
1
1
1
1
class Soojebi{
public static void main (Stringf ] args) {
int [ ]a=new int[8];
int i=0;
int n=11;
while(n>0){
a[i++]=n%2;
n/=2;
}
for(i=7;i>=0;i——){
System.out.print(a[i]);
°1리 02 • main 메서드부터 실행
03 • a는 26으로 초기화
04 • b를 91로 초기화
05 • i=0, g=0으로 초기화
07 •a<b는 26<91이므로 참이기 때문에 a값인
26을 min에 대입 [확인 필요]
09
• 느 2부터 26 미만까지 1씩 증가하면서 반
복문을 실행
10
•a%i가 0이면서 b%i가 0인 조건을 만족하
는 값을 g에 저장
• a%i==0은 i는 a의 약수이고, b%i==0은 i
는 b의 약수이므로 누가 a의 약수이면서 b
의 약수이면 if가 참이 됨 [확인 필요]
11 • i가 1일 때와 13일 때 if 문을 만족하므로 최
종적으로는 g에 13이 저장됨
15 • g 값인 13을 출력
02 • main 메서드부터 실행
03 • a 배열 선언, 자바는 정수형 배열에 초기화
가 없으면 모든 값은 0이 됨
04 니는 0으로 초기화
05 • n 은 11로 초기화
06 • n=11 이므로, n>00| 참이 되어 반복문 실행
07 •i=0이므로 a[이은 11%2인 1을 저장하고,
i++에 의해 느 1로 변경
08
• 으을 2로 나눈 값인 5가 n 에 저장(정수/정
수=정수)
06 • n=5이므로, n>00| 참이 되어 반복문 실행
07
• 더는 1이므로 a[1]은 5%2인 1을 저장하고,
i++에 의해 느 2로 변경
08 • n을 2로 나눈 값인 2가 n에 저장(정수/정
수=정수)
06 • n=2이므로, n>00| 참이 되어 반복문 실행
07 • i는 2이므로 a[2}은 2%2°] 0을 저장하고,
i++에 의해 '는 3으로 변경
08
• n을 2로 나눈 값인 10| n에 저장(정수/정
수=정수)
06 • n=1 이므로, n>00| 참이 되어 반복문 실행
07
• 누는 3이므로 a[3]은 1%2°1 1을 저장하고,
i++에 의해 는 3으로 변경
08 • n을 2로 나눈 값인 0이 n 에 저장(정수/정
수=정수)
06 • n=0이므로, n>00| 거짓이 되어 반복문 종료
10〜12 • a[7], a[6], a [이 값을 출력
04. 00001011
6-242 VI 프로그래밍 언어 활용
## Page 429

05 다음은 자바 코드이다. 출력 결과를 쓰시오.
class Soojebi{
public static void main (String[ ] args){
int [ ][ ]arr=new int[3][3];
init(arr);
hourGlass(arr);
arrayPrint(arr);
}
public static void init(int arr[ ][ ]){
for(int i=O;i<arr』ength;i++){
for(int j三0;j<arr[O].length;j++){
arr[i][j]=O;
}
}
}
public static void ho니rGlass(int arr[ ][ ]){ [확인 필요]
int v=0;
for(int i=O;i<arr.length;i+•+•){
for(int j 三 i; j<arr[이.length ; j++){
arr[i][j]=++v;
}
}
}
public static void arrayPrint(int arr[ ][ ]){
for(int i 三O;i<arr.length;i++){
for(int j:三0 ;j<arr[이.length ;j4-+){
if(arr[i][j]==O){
System.out.print(" ");
}
이 se{
System.out.print(arr[i][j]);
}
}
System.out.println("");
}
}
}
l햇리 02
• main 메서드부터 실행
03 • 3x3 크기의 arr 배열 생성
04 • init 메서드 호출
08 〜 14 • arr 배열 값을 모두 0을 대입
05 • hourGlass 메서드 호출
16 •V 변수 초기화
17 • 초기값은 i=0이므로 i=0일 때부터 실행
18
• 초기값은 j=0이고, arr[이Jength는 3이므 [확인 필요]
로 j<3을 만족할 때까지 반복
18 〜 19 • j=0일 때 v 값을 1 먼저 증가시키고 arr[이
[이에 1을 대입
18 〜 19 •j=1 일 때 v 값을 1 먼저 증가시키고 arr[이
[1]에 2를 대입
18〜19 • j=2일 때 v 값을 1 먼저 증가시키고 arr[이
[2]에 3을 대입
17 • i++에 의해 느 1이고, 는 arr.length인 3 [확인 필요]
미만이므로 반복문 수행
18
• 초기값은 j=1 이고, arr[이.length는 3이므 [확인 필요]
로 j<3을 만족할 때까지 반복
18〜19 • j=1 일 때 v 값을 1 먼저 증가시키고 arr[1]
[1]에 4를 대입
18〜19 •j=2일 때 v 값을 1 먼저 증가시키고 arr[1]
[2]에 5를 대입
17 • i++에 의해 i는 2이고, 는 arr.length인 3 [확인 필요]
미만이므로 반복문 수행
18
• 초기값은 j=2이고, arr[이.length는 3이므 [확인 필요]
로 j<3을 만족할 때까지 반복
18〜19 • j=2일 때 v 값을 1 먼저 증가시키고 arr[2]
[2]에 6을 대입
17 • i++에 의해 너는 3이므로 i<arr.length가 거 [확인 필요]
짓이므로 반복문 종료
06 • arrayPrint 메서드 호출
23 〜 35 •arr[i][j]가 0이면 띄어쓰기 1칸으로 표시하
고, 그렇지 않으면 값을 출력
05. 123
45
6
천기누설 예상문제 6-243
## Page 430

06 다음은 자바 코드이다. 출력 결과를 쓰시오.
class Berry{
protected String str;
public void meth() {
print();
}
public void print() {
System.out.print(str);
class Apple extends Berry{
private String str;
public void print(){
str="Apple";
super.str="Berry";
super.print();
System.out.print(str);
class Soojebi{
public static void main(String args[ ]){
Berry c=new Apple( );
c.meth();
rn 근 i 22 • main 메서드부터 실행
23
• Berry 타입의 인스턴스 c를 생성하기 위해
Apple 클래스 생성자를 호출
• Apple 클래스의 인스턴스가 c 변수에 저장
24 • c.meth 메서드는 상속 관계이므로 부모 클
래스인 Berry 클래스의 m아h 메서드를 호출 [확인 필요]
03 〜 05
• meth 메서드가 실행되어 print 메서드 호출
• print 메서드는 오버라이드 관계로 부모 클
래스와 자식 클래스에 동일한 이름으로 존
재함
• 객체를 자식 클래스인 Apple 클래스를 이용
하여 생성하였0므루 자식 클래스의 print가 [확인 필요]
호출되어 실행됨
13 • print 메서드 실행
14 • str에 "Apple"을 대입 [확인 필요]
15 • super.str에서 부모 클래스의 str에 "Berry" [확인 필요]
대입
16 • super.print에서 부모 클래스의 print 메서드 [확인 필요]
호출
05 〜 07 • str 값인 Berry를 화면에 출력 [확인 필요]
17 • 자식 클래스의 str인 "Apple"을 화면에 출력 [확인 필요]
25 • main 메서드를 모두 실행하고 프로그램을
종료함
다음은 자바 코드이다. 출력 결과를 쓰시오.
01 class Soojebi{
02 public static int a;
03 public static void main(String args[ ]){
04 for(int i=0;i<5;i++)
05 fn(i);
06 System.out.println(a);
07 }
08 public static int fn(int t) {
09 a=a+t;
10 return a;
11 }
12 }
06. BerryApple 07.10
6-244 vi 프로그래밍 언어 활용
## Page 431

08 다음은 자바 코드이다. 출력 결과를 쓰시오.
02 • static 정수형 변수 a 생성
03 • main 메서드부터 실행
04
• 느 0부터 5보다 작을 때까지 1씩 증가하면
서 for 반복문을 수행
• 느 0이므로 f n(0) 을 수행
08 • 매개변수 t에 0을 전달하여 fn 함수를 실행
09
• 오른쪽 a와 t를 더한 값을 왼쪽 a에 대입
• 오른쪽 a는 0이고 t도 0이므로 둘을 더한
0을 왼쪽 a에 대입
10 • a 값 0을 호출한 곳으로 리턴함
04 • i는 1이므로 fn(1) 을 수행
08 • 매개변수 에 1을 전달하여 fn 함수를 실행
09
• 오른쪽 a와 t를 더한 값을 왼쪽 a에 대입
• 오른쪽 a는 0이고 t도 1이므로 둘을 더한
1을 왼쪽 a에 대입
10 • a의 값 1을 호출한 곳으로 리턴함
04 • 느 2이므로 fn ⑵를 수행
08 • 매개변수 toil 2를 전달하여 fn 함수를 실행
09
• 오른쪽 a와 昌 더한 값을 왼쪽 a에 대입
• 오른쪽 a는 1이고 t도 2이므로 둘을 더한
3을 왼쪽 a에 대입
10 • a 의 값 3을 호출한 곳으로 리턴함
04 • 느 3이므로 fn(3)을 수행
08 • 매개변수 t에 3을 전달하여 fn 함수를 실행
09
• 오른쪽 a와 t를 더한 값을 왼쪽 a에 대입
• 오른쪽 a는 3이고 t도 3이므로 둘을 더한
6을 왼쪽 a에 대입
10 • a의 값 6을 호출한 곳으로 리턴함
04 • 느 4이므로 fn(4)를 수행
08 • 매개변수 toil 4를 전달하여 fn 함수 실행
09
• 오른쪽 a와 昌 더한 값을 왼쪽 a에 대입
• 오른쪽 a는 6이고 t도 4이므로 둘을 더한
10을 왼쪽 a에 대입
10 • a 의 값 10을 호출한 곳으로 리턴함
04 • i는 5가 되면 for 반복문을 종료함
06 • a의 값 10을 화면에 출력
07 • 프로그램을 종료함
01 public class Soojebi{
02 public static void main(String [ ]args){ //true, false
03 int x=1;
04 System.out.println(!(x==1));
05 System.out.println((x!=0) || (x>0));
06 System.out.printl n(x « 2); [확인 필요]
07 System.out.println(x&2);
08 System.out.println(x%=3);
09 }
10 }
|해실 | [확인 필요]
02 • main 메서드부터 실행
03 • X라는 이름의 변수를 1로 초기화
04 • X=1 은 참이지만,! 연산자에 의해 참이 거짓
05 • x!=0는 참이고, x>0도 참이므로 || 연산한
결과도 참
06
• x를 2비트 왼쪽으로 이동하면 22을 곱한 4
가 됨(x는 2진수로 인데, 2비트 왼쪽으로 이동
시키면 2진수로 100이 되므로 10진수로 4가 됨)
07
• x는 2진수로 1이고, 2는 2진수로 10이므로
둘을 비트 연산하면 0이 됨
and\ 10
00
08 • x=x%3과 같은데, x는 1이므로 1%3인 10|
X에 저장되어 X값인 1을 출력
08. false
true
4
0
1
천기누설 예상문제 6-245
## Page 432

01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
09 다음은 자바 코드이다. 출력 결과를 쓰시오.
public class Soojebi {
public static void main(String[ ] args) {
Parent a=new Parent( );
a.fn2( );
new Child(5).fn1( );
class Parent {
public Parent() {
this(3);
System.out.print("A");
}
public Parent(int x) {
System.out.print("B");
}
public void fn1() {
System.out.print("C");
}
public void fn2() {
System.out.print("D");
class Child extends Parent {
public Child() {
System.out.print("E");
}
public Child(int x) {
this( );
System.out.print("F");
}
public void fn1() {
System.out.print("G");
}
public void fn2() {
System.out.print("H");
|xu 서 I_____
Il리 02 • main 메서드부터 실행 [확인 필요]
03
• Parent 클래스 생성한 후 Parent 클래스
중 매개변수가 없는 생성자를 호출
• Parent 클래스의 인스턴스를 a 변수에 저장
09 • Parent 클래스 중 매개변수가 없는 생성자
를호출
10
•this(3)이므로 자기 자신 클래스의 생성자
중 int 형을 매개변수로 받는 생성자를 호출
• 3을 Parent(int x) 생성자에게  전달
13 • Parent(int x) 생성자에서 x=3을 전달받음
14 • B를 출력
11
• Parent(int x) 생성자가 끝나면 this(3) 명령
이 끝난 상태이므로 this(3)°| 다음 명령어
를 실행
• A를 출력
04 • a.fn2()를 통해 Parent 클래스의 fn2() 메
서드를 호줄
19 〜 21 • fn2 메서드에서 D를 출력
05 • Child(5) 클래스를 생성하고, 생성자를 호출
27
•생성자에 super( ) 메서드가 없으므로
super()가 생략되었기 때문에 상위 클래스
의 매개 변수가 없는 생성자를 호출
10
•this(3)이므로 자기 자신 클래스의 생성자
중 int 형을 매개변수로 받는 생성자를 호출
• 3을 Parent(int x) 생성자에게  전달
13 • Parent(int x) 생성자에서 x=3을 전달받음
14 • B를 출력
11
• Parent(int x) 생성자가 끝나면 this(3) 명령
이 끝난 상태이므로 this⑶의 다음 명령어
를 실행하여 A를 출력
28
• Child(int x) 생성자를 이어서 진행
• this()이므로 자기 자신 클래스의 생성자
중 매개변수가 없는 생성자를 호출
24 〜 25 • E를 출력
29 • this() 다음 명령어를 실행하여 두를 출력
05 • Child(5)에 의해 생성된 인스턴스에서 fn1()
메서드를 호출
31 •fn1()은 오버라이딩 관계이므로 Child 클래
스의 fn1 메서드를 실행
32 •G를 출력
09. BADBAEFG
6-246 vi 프로그래밍 언어 활용
## Page 433

다음은 자바 코드이다. 출력 결과를 쓰시오.
public class Soojebi {
public static void selection(int arr[ ], int n) {
int i, j, minjdx, temp;
for(i=0;i<n—1 ;i++) {
min_idx=i;
for (j=i+1;j<n;j++) {
if (arr[j]<arr[min_idx])
minjdx=j;
}
temp=arr[〔J;
arr[i]=arr[min_idx];
arr[min_idx]=temp;
}
}
public static void main(String[ ] args) {
int arr[ ]={2, 4, 7,1};
int i;
int n=4;
s이ection(arr, n); [확인 필요]
for (i三0;i<n;i++){
System.out.print(arr[i]);
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
I
15 • main 메서드부터 시작
16 〜 18
• 배열 arr, 변수 i, n을 선언
• n은 4로 초기화
20 • selection 메서드에 arr 배열과 n값인 4를
인자로 전달하고 호출
02 • selection 메서드 수행
03 • 정수형 변수 i, j, minjdx, temp 선언
04 • 초기식에 의해 i=0이고, i<n-1이면 0<3
이기 때문에 참이 되어 반복문 수행
05 • i 값인 0을 minjdx 변수에 저장
06 〜 08
• 초기식이 j:디+1이므로 j=l이 되고, j<n를
만족할 때까지 반복
• j=l일 때 arr[1]<arr•[이은 거짓, j=2일 때
arr[2]<arr[0]은 거짓
• j三3일 때 arr[3]<arr[이은 참이므로 min_
idx는 301 됨 [확인 필요]
• arr[i] 와' arr[min_idx] 값을 교환
10〜12 arr[이 arr[1] arr[2] arr[3]
1 4 7
흐_
04 • 증감식에 의해 i=l이고, i<n-1이면 1<3이
기 때문에 참이 되어 반복문 수행
05 • i 값인 1을 minjdx 변수에 저장
06 〜 08
• 초기식이 j느+1이므로 j=2가 되고, j<n를
만족할 때까지 반복
• j=2일 때 arr[2]<arr[1]은 거짓
• j=3일 때 arr[3]<arr[1]은 참이므로 min_
idx는 3이 됨 [확인 필요]
04 • 증감식에 의해 i=2이고, i<n-1이면 2<3이
기 때문에 참이 되어 반복문 수행
05 • i 값인 2를 minjdx 변수에 저장
06 〜 08
• 초기식이 j 늬+1이므로 j=3이 되고, j<n를
만족할 때까지 반복
•j=3일 때 arr[3]<arr[2]은 참이므로 min_
idx는 3이 됨 [확인 필요]
• arr[i] 와 arr[minjdx: 값을 교환
10〜12 arr[O] arr[1] arr[2] arr[3]
1 2 7 4_
04
• 증감식에 의해 i=2이고, i<n-1 이면 2<3이
기 때문에 참이 되어 반복문 수행
05 • i 값인 2를 minjdx 변수에 저장
06〜 08
• 초기식이 j=i+l 이므로 j=3이 되고, j<n를
만족할 때까지 반복
•j=3일 때 arr[3]<arr[2]은 참이므로 min_
idx는 301 됨 [확인 필요]
• arr[i] 와 arr[minjdx 값을 교환
10〜12 arr[O] arr[1] arr[2] arr[3]
1 2 4 7
04 • 증감식에 의해 i=3이고, i<n-1이면 3<3이
기 때문에 거짓이 되어 반복문 종료
22 〜 24 • arr[이 ~ arr[3] 값을 출력
천기누설 예상문제 6-247
## Page 434

D4| 파이썬
| Level |
0 파이썬기본구조 ★
• 파이썬은 사용자 정의 함수, 클래스가 먼저 정의되고, 그다음에 실행
코드가 나온다.
• 파이썬은 가독성을 위해 들여쓰기를 한다.
데 개념 박살내기 파이썬 기본 구조
會% Point
파이썬은 들여쓰기가 강
제되어 있습니다. 파이
썬 기본 구조 코드에서
def fn(num): 안에 들여
쓰기 되어 있는 명령어
(if num % 2=0과 return
Y)는 def fn(num)에 속
하는 명령어들입니다.
마찬가지로 def fn(self):
와 print('A')는 class
A:속하는 명령어입니다.
• def 키워드로 시작되는 명령어는 사용자 정의 함수이고 class 키워드로
시작되는 명령어는 클래스이다.
• 사용자 정의 함수, 클래스를 제거했을 때 남아있는 명령어들을 순차적으
로 실행한다.
[소스코드]
01 def fn(num):
02 if num % 2==0:
03 return Y
04
05 class A:
06 def fn(self):
07 print('A')
08
09 print('Hello')
출력 Hello
[코드 해설]
09 • Hello를 출력 [확인 필요]
6-248 VI 프=그래밍 언어 활용
## Page 435

자료형 ★★★
(1) 자료형(Data Type)의 개념
• 자료형은 프로그래밍 언어에서 실숫값, 정숫값과 같은 여러 종류의 데
이터를 식별하는 형태이다.
⑵ 자료형 유형
VIS
H11
IJ2=
O°
C2오 W
OIO
▼ 자료형 유형
유형 설명 세부 유형
기본 자료형
(Primitive Data Type)
• 직접 자료를 표현하는 자료형
숫자형 (Number),
논리 형 (Logical)
컬렉션 자료형
(Collection Data Type)
• 다수의 데이터를 효과적으로
처리할 수 있는 자료형
문자열형 (String),
리스트형(List), 튜플형(Tuple),
딕셔 너 리형 (Dictionary),
세트형 (Set),
(3) 기본 자료형(Primitive Data Type)
• 기본 자료형은 직접 자료를 표현하는 자료형이다.
• 기본 자료형에는 숫자형, 논리형이 있다.
▼기본자료형 _______________________________________________________________ 齡f으in 쪼 [확인 필요]
유형 설명 자바는 참과 거짓을 나
타낼 때 전부 소문자
(tiw/false)이지만, 파이
썬은 앞 글자가 대문자
(True/False)라는 것을
눈여겨 보세요.
숫자형
(Number)
• 숫자를 저장하고자 할 때 사용하는 자료형
• 정수형(int), 실수형(float)이 있음
논리형
(Logical; Boolean)
• 변수의 참, 거짓을 나타낼 때 사용하는 자료형
• True(참), False(거짓)를 저장
Chapter 04 파이썬 6-249
## Page 436

개념 박살내기 파이썬기본자료형
[소스코드
01
02
print(31+2.7)
print(True)
출력 33.7
True
[코드 해설]
01 • 정수값인 31과 실수값인 2J을 더한 33.7을 출력
02 • 참값인 True를 출력 [확인 필요]
(4) 컬렉션 자료형(C이ection Data Type) [확인 필요]
• 컬렉션 자료형은 시퀀스 자료형과 비시퀀스 자료형이 있다.
• 시퀀스 자료형은 문자열형, 리스트형, 튜플형이 있고, 비시퀀스 자료
형은세트형, 딕셔너리형이 있다.
요%f의nil서느 [확인 필요]
시퀀스 자료형은 순서가
있는 자료형이고 비시퀀
스 자료형은 순서가 없
는 자료형입니다.
齡LE으 M [확인 필요]
파이썬의 세트형은 자바
의 Set 클래스(HashSet)
와 비슷하고, 파이썬의
리스트형은 자바의 List
클스(ArrayList, Linked-
List)와 비슷하고, 파이
썬의 딕셔너리형은 자바
의 Map 클래스(Hash)와
비슷합니다.
▼ 컬렉션 자료형
구분 유형 설명
문자열형
• 문자를 한 개 또는 여러 개 저장하고자 할 때 사용하는 자료형
(String) ED s="Soojebi"
시퀀스
리스트형
(List)
• 크기가 가변적으로 변하는 선형리스트의 성질을 가지고 있는
자료형
• 읽기, 쓰기가 모두 가능
자료형 GDI=[1,2, 이
튜플형
(Tuple)
• 초기에 선언된 값에서 값을 생성, 삭제, 수정할 수 없는 형태
의 자료형
• 읽기 전용이며 속도가 빠름
EDt=(1,2, 3)
세트형
(Set)
• 중복된 원소를 허용하지 않는 집합의 성질을 가지고 있는 자
료형
비시퀀스 EDs니1,2, 3} [확인 필요]
자료형
딕셔너리형
• 키와 값으로 구성된 객체를 저장하는 구조로 되어 있는 자료형
(Dictionary) EDd={'s':1,'j':2, 'b':3}
6-250 VI 프로그래밍 언어 활용
## Page 437

n 시퀀스 자료형 구조
• 시퀀스 자료형은 순서가 존재하는 자료형으로 순서가 중요하다.
• 시퀀스 자료형에는문자열형, 리스트형, 튜플형이 있다.
① 시퀀스자료형 종류
O 문자열형 (String) MB 幽% 24년 1회 . 2회
• 문자열형은 문자를 한 개 또는 여러 개 저장하고자 할 때 사용하는 자
V
I
E
IJa=
o£ [확인 필요]
R2오 W
OIO료형이다. [확인 필요]
• 파이썬 문자열은 포맷 스트링을 이용하여 문자열을 출력할 수 있다.
개 념 박살내기 파이썬 문자열 포맷 스트링 출력
[소스코드]
01 a="soojebi"
02 print("%s" % a)
03 b="%s" % " world"
04 print(a+b)
05 c=123
06 print("%s %d" % (a, c))
Chapter 04 파이썬 6-251
## Page 438

수제비 카페(cafe.naver.
com/soojebi) 질문 중에
파이썬의 출력 결과에
괄호가 들어가는지 안
들어가는지에 대해서
많은 수험생들이 헷갈
려합니다.
파이썬에서 컬렉션 자
료형 변수를 그냥 출력
했을 때는 괄호가 표시
되지만, 문자열 변수를
출력했을 때 괄호가 표
시되지 않습니다. 기억
해두세요.
soojebi
출력 soojebi world
soojebi 123
[코드 해설
01 • "soojebi" 문자열을 a에 대입
02 • 포맷 스트링 %s에 a 문자열 "soojebi"* 전달하여 출력
03 • %s와 문자열 " world"를 으에 대입
04 • a와 b를 연결한 "soojebi world"를 화면에 출력
05 • c에 정수 123을 대입
06 • %s에는 a, %d에는 c가 매핑되어 soojebi 1230| 화면에 출력됨
• 파이썬 문자열에서는 in 연산자를 이용하여 찾고자 하는 문자열이 존
재하면 True, 없으면 False를 리턴한다. [확인 필요]
베 데 박살내기 파이썬 문자열 in
[소스코드]
01
02
print("h이Io" in "h이Io world") [확인 필요]
print("soojebi" in "hello world")
출력 True
False
[코드 해설]
01 • "hello world" 내에 "hello"가 존재하므로 True를 출력 [확인 필요]
02 • "hello world" 내에 "soojebi"가 존재하지 않으므로 Ealse를 출력 [확인 필요]
-
• 문자열 대소문자 변경 등 문자열 관련 메서드는 다음과 같다.
▼ 문자열 관련 메서드
함수 설명
upper() • 문자열을 대문자로 변환하는 메서드
lower() • 문자열을 소문자로 변환하는 메서드
isalnum()
• 문자열이 알파벳 또는 숫자로만 구성되어 있으면I山e, 아니며^
를 리턴하는 메서드 、
isalpha()
• 문자열이=t벳으로만 구성되어 있으면 Trig 아니면 €alse를 리 [확인 필요]
턴하는 메서드
6-252 VI 프로그래밍 언어 활용
## Page 439

함수 설명
isdecimaK) • 문자열이 정수이면 True, 아니면 False를 리턴하는 메서드 [확인 필요]
isdigit() • 문자열이 숫자이면 True, 아니면 False를 리턴하는 메서드 [확인 필요]
isspace()
• 문자열이 공백으로만 구성되어 있으면 True, 아니면 False를 리턴 [확인 필요]
하는 메서드
split()
• 문자열을 매개변수로 전달된 문자(구분자)로 나누어 리스트로 변환
하는 메서드
sep •구분자(기본값'') ri오 [확인 필요]
( 쥬? 박살내기 파이썬 문자열(str) 메서드
[소스코드
01 a="Soojebi 123"
02 print(a.upper())
03 print(a.lower())
04 print(a.isalnum())
05 print(a.isalpha())
06 print(a.isdecimal())
07 print(a.isdigit())
08 print(a.isspace())
09 print(a.split())
10 print(a.split(sep 三 T))
11 str="1,2,3".split(",")
12 print(str)
출력
SOOJEB1123
soojebi 123
False
False
False
False
False
['Soojebi', '123']
['Soojebi '23']
[T, '2', '3']
[코드 해설]
01 • a라는 이름의 변수에 문자열 "Soojebi 123"을 대입
02 • a를 대문자로 변환한 값을 출력
03 • a를 소문자로 변환한 값을 출력
04 • a는 알파벳, 숫자, 공백으로 구성되어 있으므로 False를 출력 [확인 필요]
05 • a는 알파벳, 숫자, 공백으로 구성되어 있으므로 False를 출력 [확인 필요]
06 • a는 정수가 아니므로 False를 출력 [확인 필요]
Chapter 04 파이썬 6-253
## Page 440

07 • a는 숫자가 아니므로 False를 출력 [확인 필요]
08 • a는 공백으로만 구성되어 있지 않으므로 False를 출력 [확인 필요]
09 • a를 구분자로 분리(구분자가 지정되어 있지 않으므로 띄어쓰기를 기준으로 분리)
10 • a를 구분자인 '1'을 기준으로 분리
11 • 문자열 "1,2,3"에서 콤마를 기준으로 나눠서 리스트로 생성
12 • str을 화면에 출력 [확인 필요]
• split 함수를 이용하여 구분자를 기준으로 부분 문자열을 추출할 수 있다.
호 개념 박살내기 파이썬 split 함수
[소스코드]
01 str="1,2,3"
02 print(str.split(", "))
출력 [T, '2', '3']
[코드 해설]
01 • 문자열 "1,2,3"에서 콤마를 기준으로 나눠서 리스트로 만듦
02 • str을 화면에 출력함 [확인 필요]
⑪ 리스트형 FSSWI BEU WW1EEEW1
• 리스트는 크기가 가변적으로 변하는 선형리스트의 성질을 가지고 있는
자료형이다.
• [, ]를 이용하여 리스트형을 선언한다.
리스트명=[요소1, 요소2, …]
• 리스트형 메서드에는 append, insert, remove 등이 있다.
▼ 리스트형 메서드
메서드 설명
append(x) • 리스트 마지막 요소 뒤에 값 X를 추가하는 메서드
clear() • 리스트의 모든 항목을 삭제하는 메서드
copy() • 리스트를 복사하는 메서드
count(x) • 리스트에서 X 항목의 갯수를 알려주는 메서드
6-254 VI 프로그래밍 언어 활용
## Page 441

메서드 설명
extend(i) • 리스트 마지막에 컬렉션 자료형 i를 추가하는 메서드
index(x) • 값 x와 같은 값을 가지고 있는 인덱스 번호를 알려주는 메서드
insert(i, x) • 리스트의 i 번지 위치에 값 X를 삽입하는 메서드
pop(i)
• i 번째 항목을 삭제하고 값을 꺼내오는 메서드
• 昌 생략할 경우 마지막 항목을 삭제하고 값을 꺼냄
remove(x)
• 리스트에서 해당하는 값 X를 제거하는 메서드
• 해당하는 값이 여러 개 있을 경우 가장 앞에 있는 값을 제거
reverse() • 리스트의 위치를 전부 역순으로 바꿔주는 메서드
sort() • 리스트의 항목들을 정렬하는 메서드
VIS
HU:lm=
Q°
r2오
e
oto
1H 념 박살내기 파이썬 리스트형 메서드
[소스코드
01 a=[20,10, 30]
02 print(a)
03 a.extend(a)
04 print(a)
05 a.pop()
06 print(a)
07 a.reverse()
08 print(a)
출력
[20,10, 3이
[20,10, 30, 20,10, 30]
[20,10, 30, 20,10]
[10, 20, 30, 10, 2이
[코드 해설]
01 • 리스트 a 선언 및 20,10, 30으로 초기화
02 • 리스트 a에 저장된 [20,10, 3이을 출력
03 • 리스트 확장, 20,10, 30을 한 번에 추가함
04 • 리스트 a에 저장된 [20,10, 30, 20,10, 3이을 출력
05 • 리스트 마지막 또는 지정 요소를 삭제하고 그 값을 반환함
06 • [20,10, 30, 20,1이 리스트 a 출력
07 • 리스트를 역순으로 뒤집음
08 • [10, 20, 30,10, 20] 리스트 a 출력
• 리스트에서 append, index 메서드를 이용하여 리스트에 값을 주가하
고 remove 메서드를 이용하여 삭제한다.
a公 '談
파이썬에서 문자열형을
뺀 컬렉션 자료형들은
변수를 그냥 출력할 경
우 괄호가 포함됩니다.
예시에서도 a 변수는 리
스트형인데, print(a)하면
괄호도 같이 출력된다
는 것을 기억해두세요.
Chapter 04 파이썬 6-255
## Page 442

춰호 거; 뎌 박살내기 파이썬 리스트형 메서드
[소스코드]
01 I늬3, 5, 7]
02 l.append(3)
03 print(l)
04 ljnsert(2, 4)
05 print(l)
06 l.remove(3)
07 print(l)
[3, 5, 7, 3]
출력 [3, 5, 4, 7, 3]
[5, 4, 7, 3]
[코드 해설
01 • I이라는 변수에 3, 5, 7 값을 리스트형으로 초기화
02 • I의 맨 뒤에 3을 추가
03 • 3, 5, 7 뒤에 301 추가되어 [3, 5, 7, 3]을 화면에 출력
04 • |의 2번지에 4라는 값을 추가<2번지는 세 번째 값이므로 세 번째에 4 추가) [확인 필요]
05 • I을 화면에 출력
06 • I에서 3을 제거하는데 3은 두 개이므로 앞의 301 지워짐
07 • I을 화면에 출력
• 리스트를 2차원으로 만들 수 있고, 2차원 리스트는 [와 ]사이에 [와 ]를
중첩하여 사용한다.
[소스코드]
파이썬 2차원 리스트
01 a=[[1, 2], [3, 4], [5, 6]]
02 print(a)
03 print(a[0])
04 print(a[1][0])
05 b=[[1, 2, 3], [4, 5], [6, 7, 8, 9]]
06 print(b[0])
[[1, 2], [3, 4], [5, 6]]
출력 [1,2]
3
[1, 2. 3]
6-256 VI 프로그래밍 언어 활용
## Page 443

[코드 해셀
01 • 2차원 리스트 a를 선언 및 초기화
02 • 2차원 리스트 a를 출력
03
• a[아는 [1, 2], a[1]는 [3, 4], a[2]는 [5, 6]을 가리킴
• a[이인 [1, 2]를 출력
04 •a[1][이 값인 3을 출력
05 • 2차원 리스트 b를 선언 및 초기화
06 • b[이인 [1, 2, 3] 를 줄력
r2오
• 리스트형 내포는 리스트를 간결하게 생성하는 방법이다.
▼ 리스트형 내포 종류
종류 설명
조건을 포함하지 않는 리스트 내포
• 반복문을 한 줄에 표현하여 새로운 리스트를 만듦
[표현식 for 항목 in 자료형]
조건을 포함한 리스트 내포
• 반복문과 조건문을 한 줄에 표현하여 새로운 리스
트를 만듦
[표현식 for 항목 in 자료형 if 조건]
(단) 튜플형 (Tuple)
• 튜플형은 초기에 선언된 값에서 값을 생성, 삭제, 수정이 불가능한 형
태의 자료형이다.
• (, )를 이용하여 튜플형을 선언한다.
튜플명듸요소1, 요소2, •••)
禪 퓨펼 박살내기 파이썬 리스트형 내포
[소스코드]
01 a 늬1, 2, 3, 4, 5]
02 b三[num**2 for num in a]
03 print(b)
04 c=[num**2 for num in a if num%2 == 1]
05 print(c)
출력 [1, 4, 9,16, 25]
[1. 9, 25]
Chapter 04 파이썬 6 - 2 5 7
## Page 444

[코드 해설
01 • a 변수에 리스트 [1, 2, 3, 4, 5]를 대입
02 • b 변수는 리스트 내포를 사용하여 리스트 a의 각 요소를 제곱
• 리스트 a의 요소 중 num%2==1 를 만족하는 요소만 제곱하여 새로운 리스
03 트 0를 만듦
• if num%2=1 조건은 num이 홀수인 경우에만 제곱(num**2)을 수행하므로 [확인 필요]
최종적으로 홀수 요소의 제곱값들이 리스트 b에 저장
② 시퀀스 자료형 요소 접근 방법 -인덱싱(Indexing)
• 인덱싱은 시퀀스 자료형에서 특정 요소에 접근하는 방법이다.
• 시퀀스 자료형이 n개의 값을 가질 때 인덱스는 다음과 같다.
첫 번째요소 두 번째요소 ... 뒤에서
두 번째 요소
뒤에서
첫 번째 요소
0 1 (n-2) (n-1)
-n -2 -1
EO a=[4, 2, 7, 3, 5]
4 2 7 3 5
a[이 a[1] a[2] a[3] a[4]
a[-5] a[-4] a[-3] a[-2] a[-1]
• 인덱싱은 문자열, 리스트 같은 자료구조에서 사용한다.
• 문자열 인덱싱은 문자열에 부여된 번호로 원하는 문자를 가리킬 때 사
용한다.
6-258 VI 프로그래밍 언어 활용
## Page 445

• 문자열 앞에서부터 시작하면 인덱스는 0부터 시작하고, 뒤에서부터 시
작하면 -1부터 시작한다.
패 가？념 박살내기 파이썬문자열 인덱싱
[소스코드]
01
02
03
04
print("soojebi"[3])
print("soojebi"[—7])
str="soojebi"
print(str[1])
출력
j
s
0
[코드 해설]
01
문자열 soojebi에서 3번째 문자인 j를 화면에 출력 [확인 필요]
문자열 S 0 0 j e b i
인덱스
[이 [1] [2] [3] [4] [5] [6]
[-7] [-6] [-5] [—4] [-3] [-2] [-1]
02 문자열 soojebi에서 -7번째 문자인 s를 화면에 출력 [확인 필요]
03 문자열 soojebi를 str이라는 변수에 대입 [확인 필요]
04 문자열 str은 문자열 soojebi이므로 1번째 문자인 o를 화면에 출력 [확인 필요]
• 튜플의 요소 접근을 위해 인덱싱을 사용한다.
_재우# 비서員戶내리세사세冒冒己山네네昌가세서세다네昌■체세■서차세체
뽀g 개 념 박살내기 파이썬튜플인덱싱
[소스코드]
01 t=('s', 'f, 'b')
02 print(t[O])
출력 s
[코드 해설]
01 • 튜플 변수 toll 's', 'f, 'b'로 초기화
02 • t°| 0번째 값인 s를 화면에 출력
Chapter 04 파이썬 6-259
## Page 446

③ 시퀀스 자료형 요소 접근 방법 -슬라이싱(Slicing) 1^1
• 슬라이싱은 시퀀스 자료형에서 여러 개의 데이터에 동시에 접근하는
기법이다.
시퀀스변수명 [시작: 종료: 스텝]
형태 설명
시작
• 슬라이싱을 시작할 인덱스
• 생략할 경우 '시퀀스변수명[:종료]' 또는 '시퀀스변수명[:종료:스텝]' 형태가 됨
• 생략할 경우 처음부터 슬라이싱
종료
• 슬라이싱을 종료할 인덱스
• 종료 인덱스에 있는 인덱스 전까지만 슬라이싱
• 생략할 경우 '시퀀스변수명[시작:]' 또는 '시퀀스변수명[시작::스텝]' 형태가 됨
• 생략할 경우 마지막까지 슬라이싱
스텝
• 몇 개씩 끊어서 슬라이싱을 할지 결정하는 값
• 생략할 경우 '시퀀스변수명[시작:종료]' 또는 '시퀀스변수명[시작:종료:]' 형
태가 됨
• 생략할 경우 1이 기본값
⑩ 문자열 슬라이싱 5^國
• 문자열 슬라이싱은 문자열에서 부분 문자열을 추출할 수 있다.
• 문자열 슬라이싱된 결과를 비교할 때는= = 연산자를 이용한다.
예%上의 혀
슬라이싱을 통해 출력할
때는 괄호가 표시됩니다.
다만, 문자열 슬라이싱은
다른 시퀀스 자료형과 다
르게 출력 결과에 괄호가
표시되지 않습니다.
齡上=1혀
문자열끼리 비교할 때는
자바처럼==연산을 이
용하면 됩니다.
체느 개 념 박살내기 파이썬문자열슬라이싱
[소스코드]
01 print("soojebi"[1:])
02 print("soojebi"[2:4])
03 print("soojebi"[:3])
04 print( "soojebisoojebi "[1 :3]=三 "soojebisoojebi " [8:1 이)
oojebi
출력 oj
SOO
True
[코드 해셀
01 • 시작 위치만 지정하면 oojebi가 출력 [확인 필요]
02
• 2번째부터 시작해서 3번째(4-1 번째)까지 출력하며, step은 생략되어 10| 되 [확인 필요]
어 oj 가 출력
03 • 시작 인덱스는 생략되어 있고, 종료 인덱스만 명시된 형태로 2번째까지 출력
04
• "soojebisoojebi"[1:3]는 'oo'이고, "soojebisoojebi"[8:1 이도 'oo'이므로
'oo'='oo'는 참이기 때문에 True를 출력 [확인 필요]
6-260 VI 프=그래밍 언어 활용
## Page 447

⑪ 리스트 슬라이싱
• 리스트 슬라이싱은 리스트의 원하는 부분을 추출할 수 있다.
[ 념 박살내기 파이썬 리스트슬라이싱
[소스 코듸
이 a=[4, 2, 7, 3, 5]
02 print(a[0:4:2])
출력 [4,7] _______________________
[코드 해설]
01 • 리스트 a에 4, 2, 7, 3, 5로 초기화
• 0번지부터 4번지 바로 전 인덱스인 3번지 인덱스까지 2개씩 끊어서 슬라
02 이싱
VIH
KU
IJm=
0°
r2오
le
oto
® 튜플 슬라이 싱
• 튜플 슬라이싱은 튜플의 원하는 부분을 추출할 수 있다.
패丄저? 박살내기 파이썬튜플슬라이싱 [확인 필요]
소스코드]
01
02
t=('s', 'f, 'b')
print(t[1:])
출력 (j. 'b')
[코드 해설]
01 • 튜플 변수 toll 's','f, 'b'로 초기화
02 • 튜플 변수(를 슬라이싱하여 화면에 출력
④ 시퀀스 자료형 연산자
⑪ 연결, 반복 연산자
▼ 연결, 반복 연산자
연산자 설명
+ • 두 시퀀스 자료형을 연결하는 연산자
* • 시퀀스 자료형을 반복하는 연산자
Chapter 04 파이썬 6-261
## Page 448

개념 박살내기 파이썬 연결, 반복연산자
[소스코드]
01 a=[1, 2, 3]
02 b=[4, 5, 6]
03 print(a+b)
04 print(a*3)
출력 [1, 2, 3, 4, 5, 6]
[1, 2, 3,1, 2, 3,1, 2, 3]
[코드 해설
01 • a 변수에 리스트 [1, 2, 3]을 대입
02 • b 변수에 리스트 [4, 5, 6]을 대입
03
• 연산자+를 사용하여 a 리스트와 b 리스트를 연결한 값인 [1, 2, 3, 4, 5, 6]
을 출력
04 • 연산자 *를 사용하여 a 리스트를 3번 반복하여 출력
⑪ in, not in 연산자
• 특정 값이 시퀀스 자료형 내부에 있는지 확인하기 위해서 in 연산자를
활용한다.
▼ in, not in 연산자
연산자 설명
in • 시퀀스 자료형 내부의 특정 값이 존재하는지 확인하는 연산자
not in • 시퀀스 자료형 내부의 특정 값이 존재하는지 않는지 확인하는 연산자
바g 개 념 박살내기 파이썬 in, not in 연산자
[소스코드]
01
02
03
04
a=[1, 2, 3, 4, 5]
print(1 in a)
print(7 in a)
print(8 not in a)
출력
True
False
True
6-262 vi 프로그래밍 언어 활용
## Page 449

[코드 해설]
01 • a 변수에 리스트 [1, 2, 3, 4, 5]를 대입
02 • a 리스트 내부에 10| 있으므로 True를 반환 [확인 필요]
03 • a 리스트 내부에 701 없으므로 False를 반환 [확인 필요]
04 • a 리스트 내부에 801 없으므로 True를 반환 [확인 필요]
S 비시퀀스 자료형 구조
• 비시퀀스 자료형은 순서가 존재하지 않는 자료형으로 순서가 중요하지
않다.
① 세트형 bb n뗘]
⑪ 세트(Set)형 개념
• 세트형은 중복된 원소를 허용하지 않는 집합의 성질을 가지고 있는 자
료형이다.
• set라는 키워드로 세트형을 초기화하거나 {, }를 이용하여 세트형을 선 [확인 필요]
언한다.
세트명=set([요소1, 요소2, …])
세트명={요소1, 요스오,
VIH
H1J
IJ모 [확인 필요]
0E
R2오 W
OIO
⑪세트형 연산자
• 세트형 연산자는 수학의 집합과 유사하게 동작하는 연산자이다.
▼ 세트형 연산자
= 아&冷햬
리스트형을 set 함수의
매개변수로 넣으면 반환
값이 세트형이 됩니다.
예를 들어, a=[1, 2] 일 때
set(a) 라고 하면 set(a)는
{1, 2}와 같습니다.
연산자 설명
I • 두 세트의 모든 요소를 포함하는 세트를 만드는 연산자(합집합)
&
• 두 세트에 공통으로 포함된 요소들로 이루어진 세트를 만드는 연산자(
교집합)
-
• 첫 번째 세트에는 있지만 두 번째 세트에는 없는 요소들로 이루어진 세트
를 만드는 연산자(차집합)
A • 두 세트 중 하나에만 속하는 요소들로 이루어진 세트를 만드는 연산자(
대칭 차집합)
Chapter 04파이썬 6-263
## Page 450

념 박살내기 파이썬세트형연산자
[소스코드]
01 x = {1, 2, 3}
02 y = {3, 4, 5}
03 print(x | y)
04 print(x & y)
05 print(x — y)
06 print(x A y)
{1, 2, 3, 4, 5}
출력 {3}
{1. 2}
{1, 2, 4, 5}
[코드 해설
01 • x 변수에 1, 2, 3 값을 세트형으로 초기화
02 • y 변수에 3, 4, 5 값을 세트형으로 초기화
03 • X, y 변수에 있는 모든 요소를 출력
04 • X, y 변수에 있는 공통된 요소를 출력
05 • x 변수에는 있지만 y 변수에 없는 요소들을 출력
06 • x, y 변수 중 하나에만 속하는 요소를 출력
⑪ 세트형 메서드
• 세트형 메서드는 add, update, remove 등이 있다.
▼ 세트형 메서드
메서드 설명
add(값) • 값을 1개 추가하는 메서드
update([값, 값2, •••]) • 여러 개의 값을 한꺼번에 추가하는 메서드
remove(값) • 특정 값을 제거하는 메서드
6-264 VI 프로그래밍 언어 활용
## Page 451

파이썬 세트형 메서드
[소스코드]
01 s={1, 5, 7}
02 s.add(3)
03 print(s)
04 s.add(5)
05 print(s)
06 s.update([1, 2, 3, 4])
07 print(s)
08 s.remove(1)
09 print(s)
{1. 3, 5, 7}
춤려 저,3. 5, 7}
{1. 2, 3, 4, 5, 7}
{2, 3, 4, 5, 7}
VI
IH
HlJ:l
nJ=
o°
C2오
[코드 해설]
01 • s라는 변수에 1, 5, 7 값을 세트형으로 초기화
02 • s에 3이 없3이 추가
03 • s를 화면에 출력함
04 • s에 5를 추가하지만 이미 5가 있으므로 변화 없음
05 • s를 화면에 출력함
06 • S에 1, 2, 3, 4를 한 번에 추가하지만 1과 3은 이미 있으므로 2, 4만 추가
07 • s를 화면에 출력함
08 • s에서 1을 제거
09 • s를 화면에 출력함
②딕셔너리
⑪ 딕셔 너리 형 (Dictionary) 개 념
• 딕셔너리형은 키와 값으로 구성된 객체를 저장하는 구조로 되어 있는
자료형이다.
⑪딕셔너리형요소생성/변경/삭제
▼ 딕셔너리형 = 생성/변경/삭제
구분 문법 설명
생성 딕셔너리명={키1:값1, 키2:값2, •■•}
• {,}안에 콜론(:)을 이용하여 키와 값을
구분하여 선언
Chapter 04 파이썬 6-265
## Page 452

구분 문법 설명
변경 딕셔너리명[키]=값
. 기존 변수에 키와 값을 추가
• 기존 변수에 해당 키에 해당하는 값
이 있었으면 값을 변경
삭제 del 딕셔너리명[키]
• 기존 변수에서 해당 키와 키에 해당
하는 값을 삭제
# 1;뎜 박살내기 파이썬 딕셔너리형
[소스코드
01 d={'A':5, 'C':4}
02 print(d)
03 d['K']=7
04 print(d)
05 del d['C']
06 print(d)
07 d['K']=6
08 print(d)
출력
{'A':5, 'C':4}
{'A':5, 'C':4, 'K':7}
{'A':5, 'K':7}
{'A':5, 'K':6}
[코드 해설]
01 • d라는 변수에 키가 'A'일 때 값을 5로, 'C'일 때 값을 4로 초기화
02 • d 출력
03 • d라는 변수에 키가 'K'일 때 값을 7로 저장
04 • d 출력
05 • d라는 변수에 키가 'C'에 해당하는 값을 삭제
06 • d출력
07
• d라는 변수에 키가 'K'일 때 값을 6으로 저장(기존에 키가 'K'일 때 값이 7에서 6
으로 변경)
08 • d 출력
© 딕셔너리형 메서드
▼ 딕셔너리형 메서드
메서드 설명
keys() • 딕셔너리형에 저장된 모든 키를 반환하는 메서드
values() • 딕셔너리형에 저장된 모든 값을 반환하는 메서드
6-266 VI 프로그래밍 언어 활용
## Page 453

큐 개 념 박살내기 파이썬 딕셔너리형 메서드
[소스코드]
01 d={'A':5, 'C':4}
02 print(d.keys())
03 print(d.values())
출력 dict_keys(['A', 'C'])
dict_values([5, 4])
[코드 해설
01 • d 변수에 키가 'A'일 때 값을 5로, 'C'일 때 값을 4로 초기화
02 • d 변수의 키를 출력
03 • d 변수의 값을 출력
오
e
olo
붜흐 개 념 박살내기 파이썬세트형/딕셔너리형 내포
[소스코드
01 a=[1, 2, 3, 4, 5]
02 b={i**2 for i in a}
03 print(b)
04 c={i** 2 for i in a if i%2=1}
05 print(c)
06 d={i:i**2 for i in a}
07 print(d)
08 e={i:i** 2 for i in a if i%2==1}
09 print(e)
출력
{1, 4, 9,16, 25}
{1, 9, 25}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
{1: 1, 3: 9, 5: 25}
[코드 해설
01 • a 변수에 리스트 [1, 2, 3, 4, 5]를 대입
02 • 내포를 사용하여 리스트 a의 각 요소를 제곱하여 세트형으로 b 변수에 대입
03 • b 변수의 값을 출력
04
• 리스트 a의 요소 중 num%2==1 를 만족하는 요소만 제곱하여 새로운 세
트 c를만듦
• if num%2==1 조건은 num0| 홀수인 경우에만 제곱(num**2)을 수행하므로
최종적으로 홀수 요소의 제곱값들이 세트 c에 저장
05 • c 변수의 값을 출력
Chapter 04 파이썬 6-267
## Page 454

06
• 내포를 사용하여 리스트 a의 요소의 값은 key로 요소를 제곱한 값은 value [확인 필요]
로 하여 딕셔너리로 d 변수에 대입
07 • d 변수의 값을 출력
08
• 리스트 a의 요소 중 num%2==l를 만족하는 요소 중 요소의 값은 key로, [확인 필요]
요소를 제곱한 값은 value로 하여 딕셔너리 e를 만듦 [확인 필요]
• if num%2==1 조건은 num이 홀수인 경우에만 제곱(num**2)을 수행하므 [확인 필요]
로 최종적으로 홀수 요소 key와 홀수 요소의 제곱값 value가 딕셔너리 e [확인 필요]
에 저장됨
09 • e 변수의 값을 출력
(5) 자료형 함수
Q type 함수 wk텯1 [확인 필요]
• type 함수를 사용하면 자료형을 확인할 수 있다.
숫자형(Number)에 정수
형과 실수형이 있습니다.
잘기억해두세요.
▼ type 함수
유형 세부 유형 출력
기본 자료형
(Primitive Data Type)
정수형 (Integer) (class 'int'>
실수형(Floating Point) (class 'float')
논리 형 (Logical) (class 'bool'>
컬렉션 자료형
(Collection Data Type)
문자열형 (String) (class 'str'>
리스트형 (List) (class list'>
튜플형 (Tuple) (class 'tuple'>
딕 셔 너리 형 (Dictionary) (class 'diet')
세트형 (Set) (class 'set'>
I췌 ,H 념 박살내기 파이썬 type 함수 자료형 확인
[소스코드]
01 print(type(31))
02 print(type(2.7))
03 print(type(True))
04 print(type('Soojebi'))
05 print(type([1, 2, 3]))
06 print(type((1, 2, 3)))
07 print(type({1, 2, 3}))
08 print(type({'s':1, 'j':2, 'b':3}))
6-268 VI 프로그래밍 언어 활용
## Page 455

출력
(class 'inf>
(class 'float')
(class 'bool'>
(class 'str'>
(class 'list'>
(class 'tuple'>
(class 'set'>
(class 'diet'>
[코드 해설]
01 • 31은 정수형이므로 <class 'int'>를 출력
02 • 2J은 실수형이므로 (class 'float'>를 출력
03 • True는 논리형이므로 (class 'bool'>를 출력 [확인 필요]
04 • 'Soojebi'는 문자열형이므로<class 'str'>을 출력
05 • [1, 2, 3]은 리스트형이므로 (class 'list'>을 출력
06 • (1, 2, 3)은 튜플형이므로 (class 'tuple'>을 출력
07 • {1, 2, 3}은 세트형이므로 <class 'set'>을 출력
08 • {'s':1, 'j':2, 'b':3}은 딕셔너리형이므로 (class 'diet'>을 출력
r5오 e
oto
0 len 함수
• len 함수는 컬렉션 자료형의 크기를 계산하는 함수이다.
파이썬 len 함수
[소스코드]
01 print(len('Soojebi'))
02 print(len([1, 2, 3]))
03 print(len((1, 2, 3)))
04 print(len({1, 2, 3}))
05 print(len({'s':1, 'j':2, 'b':3}))
7
3
출력 3
3
3
Chapter 04 파이썬 6-269
## Page 456

[코드 해설]
01 • 'Soojebi' 문자열의 길이가 7이므로 lenfSoojebi')은 701 됨
02 • [1, 2, 3]은 요소의 개수가 3개이므로 len([1, 2, 3])은 301 됨
03 • (1, 2, 3)은 요소의 개수가 3개이므로 len((1, 2,3))은 30| 됨
04 • {1, 2, 3}은 요소의 개수가 3개이므로 len({1, 2, 3})은 301 됨
05
•{'s':1, 'j':2, 'b':3}은 요소의 개수가 3개이므로 len({'s':1, 'f:2, 'b':3})은
301 됨
同 sum 함수
• sum 함수는 컬렉션 자료형의 요소 값을 모두 더해주는 함수이다.
• sum 함수에 사용되는 자료형은 요소가 숫자로만 이루어져 있어야 한다.
베브, 가!急 박살내기 파이썬 sum 함수
[소스코드]
01 print(sum([l, 2, 3]))
02 print(sum((1, 2, 3 )))
03 print(sum({l, 2, 3}))
04 print(sum({l :'A', 2:'B', 3:'C'}))
6
출려 6
골거 6
6
[코드 해설]
01 • [1, 2, 3]은 요소의 합이 6이므로 sum([l, 2, 3])은 601 됨
02 •(1, 2, 3)은 요소의 합이 6이므로 sum((1, 2, 3))은 601 됨
03 • {1, 2, 3}은 요소의 합이 6이므로 sum({l, 2, 3})은 601 됨
_ . • sum({l:'A', 2:'B', 3:'C'})의 키의 합이 6이므로 sum({l:'A', 2:'B', 3:'C'})은
6-270 VI 프로그래밍 언어 활용
## Page 457

0 입출력 함수 ★★
(1) 표준 줄력 함수(print)
• 파이썬은 화면에 출력하기 위해 표준 출력 함수인 print 함수를 사용한다.
n 단순 출력 및 개행
print(문자열, end)
파라미터 설명
end • print 함수가 완료될 때 추가할 문자(기본값 '\n')
VI
IBB
2
=
0°
r2오 W
OIO
• print 함수를 쓰면 함수가 종료된 후에 기본으로 개행(줄바꿈) 된다.
print('ABC')일 경우 end
값을 따로 지정해주지
않았으므로 end='\n'이
생략된 형태입니다. 그
래서 ABC를 출력한 후 [확인 필요]
에 개행을 하게 됩니다.
폐 개 념 박살내기 파이썬 단순출력
[소스코드]
01 print('Hello', end=")
02 printfSoojebi')
03 print('Hello', end:브!,)
04 print('Soojebi')
축려 HelloSoojebi
= —1
Hello!Soojebi
[코드 해설]
01 • end에 아무 값도 없으므로 Hello 출력하고 개행하지 않음 [확인 필요]
02 • Soojebi 출력 후 개행
03 • end에 !가 있0므루 Hello 출력하고 개행 대신에 !를 출력 [확인 필요]
04 • Soojebi 출력 후 개행
0 변수 출력
• print 함수로 변수를 출력하고자 할 때 매개변수에 출력하고자 하는 변
수명만 넣어주면 된다.
print(인자, …)
Chapter 04 파이썬 6-271
## Page 458

0 % 포맷팅을 이용한 변수 출력
• % 포맷팅은 일반적으로 print를 통해 결과를 출력하기 위하여 사용하 [확인 필요]
는 형식이다.
• 인자에는 변수명, 값, 수식이 올 수 있다.
print(포맷_코드가_포함된-문자열 % (인자, …))
▼ % 포맷팅 종류
유형 설명 의미 설명
문자
(Character) %c Character • 문자 1 글자에 대한 형식
문자열
(String) %s String •문자열
정수
(Integer)
%d Decimal • 10진수 정수
%o Octal • 8진수 정수
%x
%X Hexa Decimal
• 16진수 정수
• %x일 경우 영어로 표기되는 부분이 소
문자로, %X일 경우 영어로 표기되는
부분이 대문자로 표시됨
부동소수점
(Floating Point) %f Floating Point • 부동 소수점 표기
6-272 VI 프로그래밍 언어 활용
## Page 459

파이썬 % 포맷팅을 이용한 변수 출력
[소스코드
01
02
03
04
05
출력
[코드 해설]
a=4
b='A'
c=5
print("a는 %d, b는 %c입니다." % (a, b))
print("%d" % (a+c))
a는 4, b는 A입니다.
9
이〜03 • a=4, b='A', c=5로 초기화
04
• 첫 번째 포맷 스트링(%d) 자리에 첫 번째 인자에 해당하는 a의 값 4가 들
어가고, 두 번째 포맷 스트링(%c) 자리에 두 번째 인자에 해당하는 b의 값
A 가들어감
05
• 첫 번째 포맷 스트링(%d) 자리에 첫 번째 인자에 해당하는 a+c의 값 9
(=4+5)가 들어감
VI
IH
HU
IJm=
0£ [확인 필요]
r2오
e
olo
□ f 문자열을 이용한 변수 출력 幽^]
• 문자열 앞에 f를 붙이면, 중괄호와 변수 이름만으로 문자열에 원하는
변수를 삽입할 수 있다.
print(f" 문자열 {인자}")
파이썬 f 문자열을 이용한 변수 출력
[소스코드]
01 a=4
02 b='A'
03 c 三5
04 print(f"a는 {a}, b는 {b}입니다.")
05 print(f"{a+c}")
출력 a는 4, b는 A입니다.
9
[코드 해설]
01 〜 03 • a=4, b='A', c=5로 초기화
04 • {a}에서 a의 값 4가 들어가고, {b}에서 b의 값 A가 들어감
05 • {a+c}에서 a+c의 값 9(=4+5)가 들어감
Chapter 04 파이썬 6-273
## Page 460

同 format 메서드를 이용한 변수 출력
• 내장함수인 format 메서드를 사용하여 변수의 값을 출력한다.
print("문자열{인자 번하".format(인자, ■••))
I처g 개 념 박살내기 파이썬 format 메서드를 이용한 변수 출력 [확인 필요]
[소스코드]
01 a=4
02 b='A'
03 c=5
04 print("a는 {0}, b는 {1}입니다.".format(a, b))
05 print("{0}".format(a+c))
출력 a는 4, b는 A입니다.
9
[코드 해설]
이〜03 • a=4, b='A', c=5로 초기화
04 • {a}에서 a의 값 4가 들어가고, {b}에서 b의 값 A가 들어감
05 • {a+c}에서 a+c의 값 9(=4+5)가 들어감
(2) 표준 입력 함수(input)
• 파이썬 표준 입력 함수인 input은 문자열 또는 숫자를 입력받을수 있다. [확인 필요]
• 파이썬에서는 정수형과 실수형과 같은 숫자를 입력받을 때는 문자열로
저장한 후에 eval 함수를 써서 숫자로 변환해 주어야 한다.
▼ 표준 입력 함수
구분 코드
문자열 입력 변수명늰nput() [확인 필요]
숫자 입력 변수명=input()
변수명=eval(변수명)
• 敗호배개변수를 숫자로 변환할 수 없는 형태의 문자열일 경우 에러가
발생한다.
6-274 VI 프=그래밍 언어 활용
## Page 461

개념 파이썬 입력 함수
[소스코드]
01 s=input()
02 s=eval(s)
03 print(s)
입력 1
출력 1
[코드 해설]
01 • s 변수에 값 입력(문자로 저장)
02 • s 변수를 숫자로 변환(만약 입력값을 숫자로 변환할 수 없을 경우 에러가 발생)
03 • s 화면에 출력
얻給 Point
옆의 코드는 입력값이
1인 경우의 동작을 설명
한 것입니다.
VIH
HIJzl 따
0£ [확인 필요]
R2오 e
oto
베 연산자 ★★
(1) 연산자(Operator) 개념
• 연산자는 프로그램 실행을 위해 연산을 표현하는 기호이다.
⑵ 연산자 종류
D Swap 연산자
• Swap 연산자는 두 변수의 값을 교환하는 연산자이다.
• 콤마를 기준으로 두 값을 교환한다.
• 파이썬 연산자는 대부
분 c언어 연산자가 동
일합니다. 연산자 종류
가 많기 때문에 C언어
에 없는 연산자만 다루
도록 하겠습니다.
• 파이썬은 증감 연산자
인 ++, -—를 지원하
지 않습니다. 참고해두
세요.
Chapter 04 파이썬 6-275
## Page 462

출력
10
20
20
10
[코드 해설
01 • a에 10을 대입, b에 20을 대입
02 • a에 있는 값인 10을 출력
03 • b에 있는 값인 20을 출력
04 • a 에 있는 값과 b에 있는 값을 교환
05 • a에 있는 값인 20을 출력
06 • b에 있는 값인 10을 출력
@ 산술 연산자
• 산술 연산자는 두 수의 수치 계산을 위한 연산자이다.
• 산술 연산자에는 사칙 연산(+, *, /, //), 지수 연산(**), 나머지 연산
(%)이 있다.
두: 박살내기 파이썬산술연산자
[소스코드]
01 print(3/2)
02 print(3//2)
03 print(3**2)
04 print(3%2)
1.5
출력 1
9
1
[코드 해설
01 • 3/2 결과인 1.5를 출력
02 • 3/2 결과에서 몫인 1을 출력
03 • 3의 2승인 9를 출력
04 • 3을 2로 나머지 연산한 1을 출력
6-276 VI 프로그래밍 언어 활용
## Page 463

H 비교 연산자
• 비교 연산자는 두 피 연산자가 같은지 다른지를 비교하는 연산자이다.
私 박살내기 파이썬비교연산자
[소스 코디
01
02
print(3==3)
print(5==3)
출력 True
False
[코드 해설]
01 • 관계 연산 결과가 참일 때 True를 출력 [확인 필요]
02 • 관계 연산 결과가 거짓일 때 False를 출력 [확인 필요]
-. 싸
예_Po |뗘| [확인 필요]
C는 참일 때 1, 거짓일
때 0, 자바와 파이썬은
참/거짓을 출력하는데,
2021년 3회  시험 때 파
이썬에서 결과를 출력하
는 문제가 시험에 나왔습
니다. 자바는 true/false
가 소문자로만 이루어
져 있고, 파이썬은 True
/False에서 앞 글자가 대 [확인 필요]
문자라는 것을 꼭 기억해
두세 a
0 대입 연산자
• 대입 연산자는 변수에 값을 할당하는 연산자이다.
• '+=', '/='은 C나 Java와 동일하며, 파이썬에는 추가적으 [확인 필요]
로 '**='와 '//=' 연산자를 제공한다.
▼ 대입 연산자
연산자 내용
**= • 왼쪽의 변수 값을 오른쪽 수의 제곱한 후 왼쪽 변수에 재할당
//= 으—『왼쪽의 변수 값을 오른쪽 수로 나눈 후 내림한 값을 왼쪽 변수에 재할당
개념 박살내기
[소스코드]
파이썬 대입 연산자
01 a, b=3, 2
02 a*三b
03 print(a)
04 a**=b
05 print(a)
06 a/=b
07 print(a)
08 a//=b
09 print(a)
10 a% 三 b
11 print(a)
Chapter 04 파이썬 6-277
## Page 464

파이썬은 C, 자바와 달리
switch 문이 없습니다.
출력
6
36
18.0
9.0
1.0
[코드 해설]
01 • a에는 3, b에는 2를 대입
02 • a 값 3과 b 값 2를 곱하고 그 결과인 6을 a에 대입
03 • a 값 6을 화면에 출력
04 • a 값 6과 b 값 2를 거듭제곱하고 그 결과인 36을 a에 대입
05 • a 값 36을 화면에 출력
06 • a 값 36을 b 값 2로 나누고 그 결과인 18을 a에 대입
07 • a 값 18.0을 화면에 출력
08 • a 값 18.0을 b 값 2로 나누고 그 몫인 9.0을 a에 대입
09 • a 값 9.0을 화면에 출력
10 • a 값 9.0과 b 값 2를 나머지 연산하고 그 결과인 1.0을 a에 대입
11 • a 값 1.0을 화면에 출력
0 조건문 ★★
(1) if 문
(Dif 문개념
• if 문 조건이 참인지 거짓인지에 따라 경로를 선택하는 명령문이다.
② if 문문법
• if의 조건문이 참일 경우 if 안에 있는 명령문을 실행한다. [확인 필요]
• if 문의 조건이 거짓이면서 elif 문의 조건이 참일 경우 elif 안에 있는
명령문이 실행한다.
• else는 if 문의 조건문이 거짓이고 여러 개의 elif 문이 모두 거짓일 때 [확인 필요]
else 안에 있는 명령문이 실행한다.(else는 사용하지 않거나 한 번만 사용) [확인 필요]
• elif는 여러 개 사용이 가능하다. [확인 필요]
6-278 VI 프로그래밍 언어 활용
## Page 465

▼ if 문 문법
if 조건문 :
명령문
이if 조건문 : [확인 필요]
명령문
else :
명령문
춰K 개 뎔 박살내기 파이썬 if 문
[소스코드
score 三 60
if score >=90:
print("A")
elif score)=80:
print("B")
elif score>=70:
print("C")
else:
print("F")
출력 F
[코드 해설]
01 • score 변수를 60으로 초기화
02
• score가 60보다 작으므로 거짓이 되어 if 문 안의 명령어를 실행하지 않고, [확인 필요]
다음 #를 실행
04
• score가 60보다 작으므로 거짓이 되어 elif 문 안의 명령어를 실행하지 않으 [확인 필요]
므로, 다음에 있는 elif를 실행 [확인 필요]
06
• score가 60보다 작으므로 거짓이 되어 elif 문 안의 명령어를 실행하지 않으 [확인 필요]
므로, 다음에 있는 else를 실행 [확인 필요]
08 • if, elif 조건이 모두 만족하지 않았으므로 else 안의 명령어를 실행
09 • F를 화면에 출력
⑵ 조건부 표현식
① 조건부 표현식 (Conditional Expression) 개념
• 조건부 표현식은 간단한 조건문을 한 줄로 표현하는 방법이다.
Chapter 04 파이썬 6-279
## Page 466

② 조건부 표현식 문법
• if의 조건문이 참일 경우 if 앞에 있는 명 령문을 실행하고, 거짓일 경우 [확인 필요]
else 뒤에 있는 명령문을 실행한다.
참 if 조건식 이se 거짓 [확인 필요]
효 반복문 ★★★
(1) while 문
• while 문은 조건문이 참일 경우 명령문을 반복하여 수행한다.
• 조건문 뒤에는 반드시 콜론(':')을 붙인다.
while 조건문 :
명령문
개 념 박살내기 파이썬 while 문
[소스코드
01 i=0
02 sum=0
03 while i<4:
04 i긔+1
05 sum=:sum+i
06
07 print(sum)
6-280 vi 프로그래밍 언어 활용
## Page 467

출력 10
[코드 해설]
01 니선언및0으로초기화
02 • sum 선언 및 0으로 초기화
03 •느0이므로乂4는참
04 • i를 1 증가
05 .sum은 0이고, i는 1이므로 0+1 값을 sum에 저장 [확인 필요]
03 •1는1이므로匕4는참 [확인 필요]
04 • i를 1 증가
05 •sum은 1이고, i는 2이므로 1+2 값을 sum 에 저장 [확인 필요]
03 •느2이므로더<4는참
04 • i를 1 증가
05 • sum은 3이고, i는 3이므로 3+3 값을 sum에 저장 [확인 필요]
03 니는3이므로1<4는참
04 • i를 1 증가
05 • sum은 6이고, 느 4이므로 6+4 값을 sum에 저장 [확인 필요]
03 • 누는 4이므로 i<4는 거짓(반복문 종료)
07 • sum을 화면에 출력 [확인 필요]
a公 談
파이썬은 do-while 문
을 지원하지 않습니다.
VIH
HlJ
IJm=
OE
r2오
ne
olo
(2) for 문
• for 문은 in 연산자 뒤에 range 함수를 사용하여 반복의 범위를 지정하
거나 리스트 개수만큼 반복을 수행한다.
D for 문 W隨]
• 시퀀스 자료형의 각각의 요소가 변수에 대입되어 명령문을 실행하며
반복한다.
for 변수 n 시퀀스자료형:
명령문
Chapter 04 파이썬 6-281
## Page 468

&3 박살내기 파이썬 for 문
소스코드]
01
02
03
li늬1, 2, 3, 4, 5] [확인 필요]
for a in li:
print(a)
출력
1
2
3
4
5
[코드 해설]
01 • 리스트 li에 1, 2, 3, 4, 5로 초기화 [확인 필요]
02 • 리스트 li에서 하나씩 a에 대입함 [확인 필요]
03 • a를 화면에 출력함
재 개 념 박살내기 파이썬 이중 for 문
[소스코드]
01 li늬[1, 2], [3, 4, 5]] [확인 필요]
02 for a in li:
03 for b in a:
04 print(b, end=*')
출력 12345
[코드 해설]
01 • 2차원 리스트 I에 [1. 2], [3, 4, 5]로 초기화함
02 • 리스트 li에서 하나씩 a에 대입함 [확인 필요]
• a를 b에 하나씩 대입함
a b
[1, 2] 1
03 [1, 2] 2
[3, 4, 5] 3
[3, 4, 5] 4
[3, 4, 5] 5
04 • b 값을 화면에 출력함
6-282 vi 프로그래밍 언어 활용
## Page 469

0 range 함수
• range 함수는 범위를 지정하는 함수이다.
• range 함수에서 시작을 생략하면 0, 스텝 값을 생략하면 1이 자동으로
들어간다.
for 변수 in range(시작, 종료, 스텝):
명령문
(시작) 값부터 for 문을 반복할 때마다 (스텝) 수
만큼 값을 증가시키고 변숫값이 (종료) 값 이상
이면 반복문을 종료
• range 함수에 값이 하나일 경우 시작=0, 스텝=1이 자동으로 들어가고,
range 함수에 값이 두 개일 경우 스텝=1이 자동으로 들어간다.
range 함수에 들어가는
매개변수의 순서랑 슬라
이싱에 들어가는 값들의
순서랑 비슷합니다. 슬라
이싱이랑 같이 비교해가
면서 보세요.
VIm
Hllzlmll
os
ES오 [확인 필요]
le
olo
눠느 개 념 박살내기 파이썬 range 함수
[소스코드]
01 i=0
02 sum=0
03 for i in range (1, 4):
04 sum=sum+i
05 print(sum)
출력 6
[코드 해설
01 •i를 0으로 초기화
02 • sum을 0으로 초기화 [확인 필요]
03
• range에 매개변수가 2개이므로 스텝=1이 자동으로 들어감 [확인 필요]
• i는 1부터 3까지 반복
04 • i 값을 sum에 더함(for 문이 돌고난 후에 sum은 601 됨) [확인 필요]
05 • sum을 출력 [확인 필요]
0 enumerate 함수
• enumerate 함수는 리스트나 튜플 같은 반복 가능한(iterable) 객체를
순회하면서  인덱스(index)와 값을 동시에 가져올 수 있게 해주는 함수
이다.
enumerate(자료형, 시작=0)
Chapter 04파이썬 6-283
## Page 470

4
브 1;허념 박살내기 파이썬 enumerate 함수
[소스코드]
01
02
03
04
05
06
07
08
09
10
a늬[1, 2, 3], [4, 5]]
for x, y in enumerate(a):
print(x, y)
b={'A':5, 'C':4}
for x, y in enumerate(b, 10):
print(x, y)
for x, y in enumerate(b.values(), 10):
print(x, y)
출력
0 [1, 2, 3]
1 [4, 5]
10 A
11 C
10 5
11 4
[코드 해설
01 • a 변수에 [[1, 2, 3], [4, 5]]를 대입
02~03
• enumerate에 자료형은 [[1, 2, 3], [4, 5]]이고, 시작 값을 지정하지 않았으므 [확인 필요]
로 인덱스는 0부터 시작
• 첫 번째 요소는 [1, 2, 3]이고, 이때 인덱스는 0이므로 x=0, y=[1, 2, 3]이 되
어, 0과 [1,2, 3]이 출력됨
• 두 번째 요소는 [4, 5]이고, 이때 인덱스는 1이므로 x=1, y=[4, 5]가 되어, 1
과 [4, 5]가 출력됨
05 •b 변수에 {'A':5, 'C':4}를 대입
06~07
• enumerate에 자료형은 ['A', 'C']이고, 시작 값을 10으로 지정하였으므로 인 [확인 필요]
덱스는 10부터 시작
• 첫 번째 키는 'A'이고, 이때 인덱스는 10이므로 x=IO, y='A'이 되어, 10과
'A'이 출력됨
. 두 번째 키는 'C'이고, 이때 인덱스는 11이므로 x=11, y='C'가 되어, 11과
'C'가 출력됨
09~10
• enumerate에 자료형은 [5, 4]이고 시작 값을 10으로 지정하였으므로 인덱 [확인 필요]
스는 10부터 시작
• 첫 번째 키는 5이고, 이때 인덱스는 10이므로 x=10, y=5가 되어, 10과 5
가 줄력됨
• 두 번째 키는 4이고, 이때 인덱스는 11이므로 x=11, y=4가 되어, 11과 4가
출력됨
6-284 vi 프로그래밍 언어 활용
## Page 471

흐 함수 ★★★
(1) 사용자 정의 함수
11 사용자 정의 함수(User-Defined Function) 개념
• 사용자 정의 함수는 사용자가 직접 새로운 함수를 정의하여 사용하는
방법이다.
• 사용자 정의 함수에서 매개변수나 생성된 변수는 사용자 정의 함수가
종료되면 없어진다.
B 사용자 정의 함수 선언 SB
def 함수명(변수명, ■••):
명령어
return 반환값
VIH
KlJ
IJ2=
0°
r2오 e
oto
cj 개념 박살내기 파이썬사용자정의 함수
[소스코드
01
02
03
04
05
06
07
08
def fn(num):
if num % 2==0:
return 'Y'
else:
return 'N'
a=fn(5)
print(a)
출력 N
[코드 해설
07 • fn(5) 함수를 호출하고 반환 값을 a라는 변수에 저장
01
• 함수명은 fn이고, 입력값은 num이라는 정수형 변수에 저장되어 num에 5 [확인 필요]
가저장
02
• num은 5이므로 2로 나눈 나머지가 001 아니라 if 문 내의 명령어는 실행하 [확인 필요]
지 않음
04 • if 문이 거짓이므로 else 안의 명령어를 실행
05 • N 값을 반환함
07 • fn(5) 함수를 호출한 반환 값이 'N'이므로 a에 'N'을 저장
08 • a 값인 'N'을 출력___________________________________________________________
파이썬도 자바나 C처럼
재귀 함수를 사용할 수
있습니다.
Chapter 04 파이썬 6-285
## Page 472

@ 디폴트 매개변수
• 디폴트 매개변수는 기본값이 정의된 매개변수이다.
• 함수를 호출할 때, 매개변수가 명시되어 있지 않으면 디폴트 매개변수
값이 전달된다.
def 함수이름(매개변수=디폴트값):
명령문
춰후 뎜 박살내기 파이썬 디폴트매개변수
[소스코드]
01 def soojebi(num1, num2三2):
02 print('a=', num1, 'b三num2)
03
04 soojebi(20)
05 soojebi(20, 3)
06 soojebi(nurrj2=20, num1=3)
a= 20 b= 2
출력 a= 20 b= 3
a= 3 b= 20
[코드 해설
04 • 매개변수로 20을 전달하여 soojebi 함수 호출
01
• soojebi 함수에 2개의 매개변수 사용
• num1 에 20을 전달, num2는 전달한 값이 없0므루 2를 디폴트 매개변수
로지정
02 • print함수에서 num1 은 20, num2는 2로 'a= 20 b= 2'를 출력 [확인 필요]
05 • 매개변수로 20, 3을 전달하여 soojebi 함수 호출
04 • 매개변수로 20, 3을 전달하여 soojebi 함수 호출
01
• soojebi 함수에 2개의 매개변수 人요
• num1 에 20을 전달, num2에 3을 전달
02 • print함수에서 num1 은 20, num2는 3으로 'a=20 b=3'을 출력 [확인 필요]
□ 가변 매개변수
• 가변 매개변수는 함수에 전달되는 인자의 수가 가변적일 때 이를 처리
하기 위해 사용되는 매개변수이다.
• 가변 매개변수는 일반 변수와 다르게 변수명 앞에 아'를 붙인다.
6-286 VI 프로그래밍 언어 활용
## Page 473

• 가변 매개변수는 하나만 사용 가능하며, 가변 매개변수 뒤에는 일반
매개변수가 올 수 없다.
념 박살내기 파이썬가변매개변수
[소스코드]
01 def sum_many(*a):
02 s 니n=0
03 for i in a:
04 sum+:듸
05 return sum
06
07 b 三 sum_many(1, 2, 4)
08 print(b)
출력 7
[코드 해셀
07 • sum many라는 함수에 1, 2, 4를 전달 [확인 필요]
— .....1 ■ 1 1....... ...  .................... . ■ --- -----------------------------------------------------
01 • sum_many 함수는 a 변수에 1, 2, 4를 저장
02 • sum은 0으로 초기화 [확인 필요]
• a는 1, 2, 4라는 3개의 값이 있으므로 i 값은 첫 번째 반복문에서는 1, 두 번
03 〜 04 째 반복문에서는 2, 세 번째 반복문에서는 4가 되어 s니m은 1, 2, 4를 더한 [확인 필요]
7이 됨
05 • return sum에 의해 siim_many를 호출한 부분에 sum 값인 7을 넘겨줌 [확인 필요]
07 • sum_many(1, 2, 4)의 반환값이 7이므로 b=70| 되어 b에 701 저장됨
08 • b의 값인 7을 출력
VI
IH
HU:12=
O°
R2오 W
OIO
(2) 람다 함수
D 람다 함수(Lambda Function) 개념
• 람다 함수는 함수 이름 없이 동작하는 함수이다.
• 매개변수에 값을 전달하면 표현식에서 연산을 수행한다.
S 람다 함수 문법
① 일반 람다 함수
lambda 매개변수:표현식
Chapter 04 파이썬 6-287
## Page 474

• 람다 함수는 콜론(:) 앞에서 매개변수를 입력받고, 콜론 뒤에서 표현식
을 처리한다.
츄句뎔 박살내기 파이썬람다함수
[소스 코듸
01 print((lambda n, m:n+m)(2, 3))
출력 5____________________________________________________________
[코드 해설]
• 숫자 2와 3을 람다 함수의 매개변수 n과 m이 전달 받아 n과 m을 더한 결
01 과 5를 화면에 출력
② 변수를 이용한 람다 함수
• 람다 함수를 변수에 할당하여 재사용할 수 있다.
브 개 념 박살내기 파이썬 변수를 이용한 람다 함수
[소스코드]
01 sum=lambda n, m:n+m
02 print(sum(2,3))
줄력 5
[코드 해설]
01 • 매개변수 n과 m을 전달받아 n과 m을 더한 결과를 sum에 대입 [확인 필요]
02 • sum에 2와 3 값을 전달하여 더한 결과인 5를 화면에 출력 [확인 필요]
6-288 VI 프로그래밍 언어 활용
## Page 475

③ 사용자 정의 함수를 이용한 람다 함수
• 람다 함수는 사용자 정의 함수로 구현할 수 있다.
채 ;; 념 박살내기 파이썬 사용자 정의 함수를 이용한 람다 함수
[소스 코듸
01 def f(n):
02 return lambda a:a*n
03 k늬(3)
04 print(k(10))
출력 30
[코드 해설
03
• f(3)을 호출하면 f 함수를 호출하고 호출한 결과를 k에 저장
• f(3)0| lambda a:a*3이므로 스는 람다 함수인 lambda a:a*3을 저장
04
• k(10)이므로 k가 저장하고 있는 람다 함수에 10을 넣게 되면 a가 100| 되어
10 *3인 30을 반환하여 30을 출력
01 • f(3)에 의해서 호출되었기 때문에 n은 3이 됨
02 • n0| 3이므로 return 값인 lambda a:a*3을 반환
R2오
④ 내장 함수를 이용한 람다 함수
• 람다 함수는 파이썬 map 함수, filter 함수와 같이 사용할 수 있다.
▼ 내장 함수를 이용한 람다 함수
함수 형태 설명
map
map
(함수, 리스트)
• 첫 번째 매개변수에는 함수, 두 번째 매개변수에는 리스트
를 전달
• 리스트 요소를 함수에 전달하여 반복을 수행하는 함수
filter
filter
(함수, 리스트)
• 첫 번째 매개변수에는 함수, 두 번째 매개변수에는 리스트
를 전달
• 리스트 요소를 함수에 전달하여 조건이 참인 값을 반환하
는 함수
Chapter 04 파이썬 6-289
## Page 476

채、개녀 박살내기 파이썬 map을 이용한 람다 함수 [확인 필요]
[소스코드]
01 a=[1, 2, 3, 4, 5]
02 m=list(map(lambda num:num+100, a))
03 print(m)
출력 [101, 102, 103,104, 105]
[코드 해설
01 • 리스트 a을 선언하고 1, 2, 3, 4, 5로 초기화
02
• num:num+100에서 매개변수인 왼쪽 num 값으로 리스트 a의 값이 순차적
으로 전달되며, 이 값은 오른쪽의 num+100에 전달되어 연산
• 1+100, 2+100, 3+100, 4+100, 5+100이 실행되어 101, 102, 103, 104,
105가 계산됨
• list 함수 매개변수에 101, 102, 103, 104, 105가 전달되며, 리스트로 변환한
결과를 m에 대입
03 • print 함수에서 리스트 m을 출력
뛔( 워념 박살내기 파이썬 filter를 이용한 람다 함수 [확인 필요]
[소스코드]
01 a=[1, 2, 3, 4, 5]
02 m=list(filter(lambda num:num>2, a))
03 print(m)
출력 [3, 4, 5]
[코드 해설
01 • 리스트 a를 선언하고 1, 2, 3, 4, 5로 초기화
• num:num>2에서 매개변수인 왼쪽 num 값으로 리스트 a의 값이 순차적으
로 전달되며, 이 값은 오른쪽의 n니m>2에 전달됨 [확인 필요]
02 • 1, 2, 3, 4, 5가 순차적으로 전달 되어 2보다 큰 값을 list 함수 매개변수로
전달
• 리스트로 변환한 결과를 m에 대입
03 • print 함수에서 리스트 m을 출력
6-290 VI 프로그래밍 언어 활용
## Page 477

0 클래스 ★★
(1) 클래스(Class) 개념
• 클래스는 객체 지향 프로그래밍(OOP;Object-Oriented Programming)에
서 특정 객체를 생성하기 위해 변수와 메서드를 정의하는 틀이다.
⑵ 클래스 정의
• 클래스에서 변수는 변수 선언과 동일하고, 메서드는 사용자 정의 함수
와 문법이 동일하다.
오오
class 클래스명:
def 메서드명(self, 변수명,
명령어
return 반환값
• 파이썬에서는 함수명에 입력받을 값(매개변수) 앞에 self라는 키워드를 [확인 필요]
적어야 한다.
class Soojebi:
def fn(self):#입력받는 값이 없을 경우 self만 사용 [확인 필요]
print(5)
(3) self
• self는 현재 객체를 가리키는 키워드이다. [확인 필요]
• 클래스 내부의 변수와 함수를 가리킬 수 있다.
self. 변수명
self. 함수명 (매개변수)
소스 코드 중간에 보시
면 #이 있는데, #은 주석
이라고 부르고, # 뒤에
있는 문장은 프로그램
동작에 영향을 주지 않
습니다.
Chapter 04 파이썬 6-291
## Page 478

박살내기 파이썬 self
[소스코드]
01 class Soojebi:
02 def setS(s이f, a): [확인 필요]
03 s 이 f.a 三 a
04 def getS(self):
05 return self.a
06
07 a=Soojebi()
08 a.setS(5)
09 print(a.getS())
출력 5
[코드 해설]
01 • sets 함수에서 a라는 매개변수 받음
02 • self.a는 class 내의 a 변수, 그냥 a는 매개변수로 받은 변수
03 • gets 함수는 클래스 내의 변수에 저장된 a라는 값을 반환
07 • a 라는 변수에 A클래스 생성
08 • sets라는 함수를 통해 5를 저장 [확인 필요]
09 • 저장된 값을 gets를 통해 출력 [확인 필요]
(4) 생성入KConstructor) 幽
• 생성자는 해당 클래스의 객체가 생성될 때 자동으로 호출되는 특수한
종류의 메서드이다.
• 생성자는 _init_이라는 메서드 명을 사용하고, 첫 번째 매개변수로
self를 작성하며, 반환 값이 없다. [확인 필요]
▼ 생성자
구분 코드
생성자 정의
class 클래스명:
def __ _______ 매개변수):
명령어
생성자 호출 클래스변수=클래스(매개변수)
6-292 VI 프로그래밍 언어 활용
## Page 479

(5) 소멸자(Destiwtor)
• 소멸자는 객체의 수명이 끝났을 때 객체를 제거하기 위한 목적으로 사
용되는 메서드이다.
• 소멸자는 __del__이라는 메서드명을 사용하고, 첫 번째 매개변수에
self를작성하며, 반환값이 없다. [확인 필요]
▼ 소멸자
구분 코드
소멸자 정의
class 클래스명:
def __del_(self):
명령어
소멸자 호출 del 클래스변수
r2오
클래스변수=클래스(매개변수) t 생성시
클래스변수 # 소멸시
제 박살내기 파이썬생성자/소멸자
[소스코드]
01
02
03
04
05
06
07
08
09
10
11
class Soojebi:
def____ _(self):
print(" 생성자")
def __del______
print("소멸자")
def fn(s이f): [확인 필요]
print(" 일반함수")
s 三 SoojebK)
s.fn()
del s
출력
생성자
일반함수
소멸자
[코드 해설]
09 • Soojebi 클래스를 생성하고, 생성한 클래스를 변수 s에 저장
02 •생성자가 호출됨
03 • "생성자"를 화면에 출력
10 • S의 fn 메서드 호출
--------------------------------------------------- - ——..................
Chapter 04 파이썬 6-293
## Page 480

06 • 일반 메서드 fn가 호출됨 [확인 필요]
07 • "일반함수"를 화면에 출력
11 • del 키워드를 이용해서 소멸자 호출
04 • 소멸자 호출
05 • "소멸자"를 화면에 출력
(6) 클래스 접근 제어자
• 파이썬은 private, public 등의 접근제어자 키워드가 존재하지 않고 작
명 법 (Naming) 으로 접근제어를 한다.
• public, private, protected에 대한 규칙은 다음과 같다. [확인 필요]
▼ 클래스 접근 제어자
종류 규칙 설명
public
• 아무 밑줄이 접두
사에 없어야 함
• 외부의 모든 클래스에서 접근이 가능한 접근 제
어자
protected
• 한 개의 밑줄 _이
접두사여야 함
• 같은 패키지 내부에 있는 클래스, 하위 클래스
(상속받은 경우)에서 접근이 가능한 접근 제어자
• 자기 자신과 상속받은 하위 클래스 둘 다 접근이
가능한 접근 제어자
private
• 두 개의 밑줄 _이
접두사여야 함
• 같은 클래스 내에서만 접근이 가능한 접근 제
어자
흐 J 개 념 박살내기 파이썬접근 제어자
[소스 코듸
01 class Soojebi:
02 def __init__(self):
03 self.public="PUBLIC"
04 self ._protected="PROTECTED"
05 self.__private="PRIVATE"
06 def fn(self):
07 print(self.public)
08 pri nt(self ._protected)
09 ______________
10
11 s 三 SoojebK)
12 s.fn()
6-294 VI 프로그래밍 언어 활용
## Page 481

13
14
15
출력
print(s.public)
print(s._protected)
# _____________
PUBLIC
PROTECTED
PRIVATE
PUBLIC
PROTECTED
VIH
HUzl
nJ=
OE
r2오 w
oto
[코드 해설]
11 • Soojebi() 클래스 객체인 s를 생성
02 • Soojebi 클래스의 _Jnit__() 메서드 호출
03 • self.public에 "PUBLIC" 값을 대입 [확인 필요]
04 • self._protected에 "PROTECTED" 값을 대입 [확인 필요]
05 • self.__private에 "PRIVATE" 값을 대입 [확인 필요]
12 • s의 메서드 fn()을 호출
06 • fn 메서드 실행
07 • self.public 값인 "PUBLIC"을 출력
08 • self._protected 값인 "PROTECTED"# 출력
09 • self.__private 값인 "PRIVATE"를 출력
13 • s의 public 변수 접근 시 public 값인 "PUBLIC"을 출력
14 • s의 _protected 변수 접근 시 _protected 값인 "PROTECTED" 출력
15
• s의 __private 변수는 접근할 수 없음
• #은 주석으로 주석 뒤에 문장은 실행하지 않음
Q 클래스 상속 ★
(1) 클래스 상속(Inheritance) 개념
• 상속은 어떤 객체가 있을 때 그 객체의 변수와 메서드를 다른 객체가
물려받는 기능이다.
class 부모_클래스명:
class 자식_클래스명(부모_클래스명):
Chapter 04 파이썬 6-295
## Page 482

( 개 념 박살내기 파이썬클래스상속
덜{冷 Point |圓
파이썬은 오버로딩이 정
식으로 지원하지 않습니
다. 오버로딩은 메서드
명은 동일하지만 매개변
수의 타입이 달라지는
형태인데, 파이썬은 변
수의 타입을 실행시간
(Run Time)에 검사하기
때문에 오버로딩이 지원
되지 않습니다.
[소스코드
01
02
03
04
05
06
07
08
09
10
class A:
def fnA(self):
print('A')
class B(A):
def fnB(self):
print('B')
b=B()
b.fnA()
b.fnB()
출력 A
B
[코드 해설]
08
• b라는 이름의 클래스 B에 대한 변수 설정
• B 클래스와 부모 클래스인 A 클래스에 생성자인 __jnit__이 없으므로 건
너뜀
09
• b라는 변수로 fnA 메서드에 접근
• b의 fnA() 함수를 호출하면 B 클래스에 fnA() 메서드가 없으므로 부모 클래
스인 A 클래스의 fnA() 메서드를 실행
02 • fnA() 메서드를 실행
03 • A를 출력
10 • b°| fnB() 함수를 호출하면 B 클래스의 fnB( )> 호출
05 • fnB() 메서드를 실행
06 • 日를 줄력
(2) 메서드 오버라이딩(Overriding)
• 오버라이딩은 하위 클래스에서 상위 클래스 메서드를 재정의할 수 있
는 기능이다.
• 오버라이딩 특징은 다음과 같다.
• 오버라이드하고자 하는 메서드가 상위 클래스에 존재하여야 한다.
• 메서드 이름은 같아야 한다.
• 메서드 매개변수 개수, 데이터 타입이 같아야 한다.
6-296 VI 프로그래밍 언어 활용
## Page 483

▼ 오버라이딩 구문
class 부모_클래스명
def 메서드명(self, 변수명)
명령어
class 자식_클래스명(부모_클래스명)
def 메서드명(self, 변수명) #부모 클래스와 메서드명, 매개변수가 같아야 함
명령어
蘇 개념 박살내기 파이썬생성자/오버라이딩
[소스코드]
01 class A:
02 def____ ______
03 print('A')
04 def fn(self):
05 printCB')
06 class B(A):
07 def __init______
08 print('C)
09 def fn(self):
10 print('D')
12 a=A()
13 b=B()
14 b.fn()
A
출력 c
D
r2오 W
OIO
[코드 해설]
12 • A 클래스를 생성
02 • A 클래스의 생성자가 호출됨
03 • A를 출력
13 •B클래스를 생성
07 • B 클래스의 생성자가 호출됨
08 • C 를 줄력
14 • b 변수는 B 클래스이므로 B 클래스의 fn 메서드를 호출
09 • fn 메서드 실행
10 • D 를 줄력
파이썬은 상속을 받는 경
우 자바와 다르게  부모
클래스 생성자를 호출
하지 않습니다. 호줄을
해야 하는 경우 super
()와 같이 직
접 호출해야 합니다.
Chapter 04 파이썬 6-297
## Page 484

⑶ 부모 클래스 접근
• 파이썬은 super 키워드를 이용하여 상위 클래스의 변수나 메서드에 접
근할 수 있다.
super().메서드명()
파이썬 부모 클래스 접근
[소스코드
01 class A:
02 def fn(self)'
03 print('A')
04 class B(A):
05 def fn(self):
06 super( ).fn()
07 print('B')
08 a=B()
09 a.fn()
A출력
B
[코드 해설]
01 • 클래스 명을 A로 지정
02 • 메서드 명은 fn
03 •'A'를 출력
04 • 클래스 B는 클래스 A를 상속받음
05 • 메서드 명은 fn
06 • super()를 이용해 A 클래스에 접근
07 • 'B'를 출력
08 • a라는 이름의 클래스 B에 대한 변수 설정
09 • a라는 변수로 fn 메서드에 접근
6-298 VI 프로그래밍 언어 활용
## Page 485

Chapter
지리지기 기출문제
[► 20년 2회 , 23년 1홰
01 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 a={'한국', '중국', '일본'}
02 a.add('베트남')
03 a.addC 중국')
04 a.removeC 일본')
05 a.update({'홍콩', '한국', '태국'})
06 print(a)
세트는 순서가 상관없은 컬렉션 자료형이므로 출력
순서는 상관없다.
01
• a라는 세트형 변수에 '일본', '중국', '한국'을
초기화
02 • '베트남'이라는 값을 추가
03
. '중국'이라는 값을 추가하는데 이미 '중국'
이 존재하므로 무시
04 • '일본'이라는 값을 제거
05
• update를 통해 '홍콩', '한국', '태국'을 추가 [확인 필요]
하는데, '한국'은 이미 있으므로 '홍콩', '태
국'이 추가
06 • 세트 값을 출력
► 20년 4회
02 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 lol=[[1, 2, 3], [4, 5], [6, 7, 8, 9]]
02 print(lol[이)
03 print(lol[2][1])
04 for sub in lol:
05 for item in sub:
06 print(item, end 三")
07 print()
I Adi
M 이 • 2차원 리스트를 lol 변수에 저장
1 | lol[이이
2 lol[0][1] lol[0]
3 lol[0][2]
01
4 lol[1][이 r q
—厂 —ssr lol[1]
6 lol[2][이
7 t 同⑵⑴ r n
"T" —szKir lol[2]
g lol[2][3] __________________
02
• lol[이은 1 차원 리스트이므로 출력하면
lol[이에 해당하는 [1 2, 3]이 출력됨
03
• lol[2][1]은 2차원 리스트 안의 값이므로 출
력하면 701 출력됨
04
• lol 변수는 [1, 2, 3]과 [4, 5], [6, 7, 8, 9]로
구성되어 있으므로 0번지 값인 [1, 2, 3]을
sub 변수에 저장
05 〜 06
• sub 변수는 1, 2, 3이므로 차례로 item 변
수에 저장
• 첫 번째 반복일 때 item이 1이므로 1을 출 [확인 필요]
력하고, end="에 의해 개행하지 않음
• 두 번째 반복일 때 item이 2이므로 2를 출 [확인 필요]
력하고, end="에 의해 개행하지 않음
• 세 번째 반복일 때 item 이 3이므로 3을 출
력하고, end="에 의해 개행하지 않음
07 • 개행(다음에 print로 출력하면 개행이 됨) [확인 필요]
04
• lol 변수는 [1, 2, 3]과 [4, 5], [6, 7, 8, 9]
로 구성되어 있으므로 1번지 값인 [4, 5]를
sub 변수에 저장
05 〜 06
•sub 변수는 4, 5이므로 차례로 item 변수
에 저장
• 첫 번째 반복일 때 item이 4이므로 4를 출 [확인 필요]
력하고, end="에 의해 개행하지 않음
• 두 번째 반복일 때 item이 5이므로 5를 출 [확인 필요]
력하고, end="에 의해 개행하지 않음
07 • 개행(다음에 print로 출력하면 개행이 됨) [확인 필요]
{'한국', '중국', '베트남', '홍콩', '태국'}
7
123
45
6789
지피지기 기출문제 6-299
## Page 486

04
• lol 변수는 [1, 2, 3]과 [4, 5], [6, 7, 8, 9]로
구성되어 있으므로 2번지 값인 [6, 7, 8, 9]
를 sub 변수에 저장
05 〜 06
• sub 변수는 6, 7, 8, 9이므로 차례로 item
변수에 저장
• 첫 번째 반복일 때 item이 6이므로 6을 출 [확인 필요]
력하고, end="에 의해 개행하지 않음
• 두 번째 반복일 때 item이 7이므로 7을 출 [확인 필요]
력하고, end="에 의해 개행하지 않음
• 세 번째 반복일 때 item0| 8이므로 8을 출
력하고, end="에 의해 개행하지 않음
• 네 번째 반복일 때 item이 9이므로 9를 출 [확인 필요]
력하고, end="에 으I해 개행하지 않음
07 • 개행(다음에 print로 출력하면 개행이 됨) [확인 필요]
07
• strO1 은 'SKI'이고, i[이은 i°| 0번지 문자인
D이므로 'SKI'+'D'는 'SKID'가 되어 strO1
에 저장됨
06 • 에 s.li의 4번지 값인 "Daegu"을 대입 [확인 필요]
07
•str()1 은 'SKID'이고, i[이은 i의 0번지 문자
인 D이므로 'SKID'+'D'는 'SKIDD'가 되어
strO1 에 저장됨
06 • 에 s.li의 5번지 값인 "Pusan"을 대입 [확인 필요]
07
• str이은 'SKIDD'이고,{이은 i의 0번지 문 [확인 필요]
자인 D이므로 'SKIDD'十'P'는 'SKIDDP'가
되어 str이에 저장됨 [확인 필요]
08 • strO1 값인 문자열 'SKIDDP'를 출력
► 21 년 2 회
► 21년 1회
다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 class Soojebi:
02 li늬"Seoul", "Kyeonggi", "Inchon", [확인 필요]
03 "Daejeon", "Daegu", "Pusan"]
04 s 三 Soojebi()
05 strO1="
06 for i in s.li:
07 strO1=strO1+i[이
08 print(strOI)
04 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 a=100
02 i=0
03 result=0
04 for i in range(1, 3):
05 res내t=a>>i [확인 필요]
06 result+=1
07 print(result)
广■기
10nBi 04 • s 변수에 Soojebi 클래스의 인스턴스를 저장
05 • strO1 은 비어 있는 문자열을 대입
06
• for 문에서 s.li에 있는 값을 하나씩 i 변수 [확인 필요]
에 저장하면서 반복
• 에 s.li의 0번지 값인 "Seoul"을 대입 [확인 필요]
07
• str이은 비어있는 문자열이고, i[이은 i의 [확인 필요]
0번지 문자인 S이므로 "+'S'는 'S'가 되어
st。에 저장됨
06 • 에 s.li의 1번지 값인 "Kyeonggi"을 대입 [확인 필요]
07 • str이은 'S'이고, i[아은 i의 0번지 문자인 K0| [확인 필요]
므로 'S'+'K'는 'SK'가 되어 5而1에 저장됨
06 • i에 s.li의 2번지 값인 "Inchon"을 대입 [확인 필요]
07 • str(거은 'SK이고, {아은 i의 0번지 문자인 10| [확인 필요]
므로 'SK'+T는 'SKI'가 되어 아이에 저장됨
06 • KHI s.li의 3번지 값인 "Daejeon"을 대입 [확인 필요]
I 01 • a 변수에 100을 대입
02 • i 변수에 0을 대입
03 • result 변수에 0을 대입
04 • for 문에서 •는 1 이상 3 미만일 때 반복
• i=|일 때부터 반복문 시작 [확인 필요]
05
• 두가 1일 때 a>>i는 100>>1이므로 result에는 [확인 필요]
5001 저장됨
06 • resultoil 1을 더하면 51이 됨
04 •i=2 가됨
05
• 누가 2일 때 a>>i는 100>>2이므로 result에는 [확인 필요]
25가 저장됨
06 • resultoil 1을 더하면 2601 됨
07 • result 값인 2601 출력됨
오후
OXSKIDDP 04. 26
6-300 VI 프=그래밍 언어 활용
## Page 487

► 21년 3회
05 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 a, b=100, 200
02 print(a:=三 b)
[보기]
remove(), reverse(), sort(), index(), insert(),
select(), pop(), extend()
①________________________________________
②________________________________________
③____________________ ____________________
• a는 100, b는 20001 대입
• a와 b는 값이 다르므로 거짓
| 卜 22년 1회
06 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 def func(num1, num2=2):
02 print('a=', num1, 'b=', num2)
03 func(20)
• 리스트와 관련된 파이썬 함수는 다음과 같다.
extend()
• 리스트 확장, 여러 값을 한 번에 추가
하는 함수
pop()
• 마지막 또는 지정 요소를 삭제하고 그
값을 반환하는 함수
reverse() • 역순으로 뒤집는 함수
append()
• 리스트 마지막 요소 뒤에 값을 추가하
는 함수
insert()
• 리스트의 인덱스 위치에 값을 삽입하
는 함수
remove()
• 리스트에서 해당하는 값을 제거하는
함수
E씩
_______
03
• func(20)을 통해 func 함수에 20이라는 파
라미터를 전달
01
•func(20)을 통해서 num1 에 20이라는 값
넘겨주고, num2는 넘겨주지 않았으므로
2가됨
02
• 파이썬은, 단위로 띄어쓰기가 되기 때문에
a=20 b=2 가 출력됨
► 22 년 2회
08 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 a="REMEMBER NOVEMBER"
02 b=a[:3]+a[12:16]
03 c="R AND %s"%"STR"
04 print(b+c)
► 22 년 1 회
07 다음은 리스트와 관련된 파이썬 함수이다. 각
항목에 해당하는 함수를 [보기]에서 골라서 쓰
시오.
① 리스트 확장, 여러 값을 한 번에 추가할 수 있는
함수
② 마지막 또는 지정 요소를 삭제하고 그 값을 반환
하는 함수
③ 역순으로 뒤집는 함수
r—1
1히설 1
01
• a 변수에 "REMEMBER NOVEMBER" 문자
열저장
02
• a[:3]은 REM, a[12:16]는 EMBE가 되고 [확인 필요]
"REMEMBER b에 대입
03
• %s에는 "STR"0| 전달되어 "RAND STR"을
c에 대입
04
• b + c를 출력하여 REMEMBE와 R AND [확인 필요]
STR 를 합친 REMEMBER AND STR 출력
05. False 06. a= 20 b= 2 07. Q) extend(), ② pop(),
③ reverse() 08. REMEMBER AND STR
지피지기 기출문제 6-301
## Page 488

► 22년 3회
09 다음은 파이썬 코드이다. 실행 결과를 쓰시오.
01 1=[1,2,3,4,5]
02 l=list(map(lambda num:num+100,1))
03 print(!)
• 리스트 I은 1, 2, 3, 4, 5로 초기화
• 파이썬 map 함수에서 첫 번째 매개변수에
는 함수, 두 번째 매개변수에는 리스트를
지정하여 반복을 수행(첫 번째 매개변수에는
lambda 함수를 전달할 수도 있음)
• lambda 함수는 함수 이름 없이 동작하는
함수로다르과 같이작흐__ __
lambda 매개변수:표현식
02 • num:num+100에서 매개변수인 왼쪽 num
값으로 리스트 1°| 값이 순차적으로 전달되
며, 이 값은 오른쪽의 num+100에 전달되
어연산
• 1+100, 2+100, 3+100, 4+100, 5+100이
실행되어 101,102,103,104,105가 계산
• list 함수 매개변수에 101,102, 103, 104, 105
가 전달되며, 리스트로 변환한 결과를 I에
대입
03 • 리스트 I을 출력
I애리 01
• 문자열을 a에 대입
02 • a의 시작부터 2번째(3 미만 번째)까지인
"eng"를 b에 대입
03 • a의 4번째부터 5번째(6 미만 번째)까지인
"ne"를 c에 대입
04 • a의 29번째부터 마지막까지 "ng"를 d에 대입
05 • b의 "eng"와 c의 "ne"와 d의 "ng"를 연결
하고 e에 대입
06 • e를 화면에 출력
► 23년 3회
11 다음은 파이썬 언어이다. 밑줄 친 빈칸에 들어
갈 메서드를 쓰시오.
01 num1, num2=input().()
02 print(numl)
03 print(num2)
[입력값]
hello soojebi
[출력값]
hello
soojebi
► 23 년 2 회
10 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 a="engineer information processing"
02 b=a[:3]
03 c=a[4:6]
04 d=a[29:]
05 e=b+c+d
06 print(e)
|xu서 ■oH a [확인 필요]
01
• hello soojebi 라는 문자열을 입력하면 공
백(' ')를 구분자로 하여 num1 에는 hello,
n니m2에는 soojebi 라는 문자열로 분할함 [확인 필요]
02 • num1 을 줄력하므로 h이Io가 줄력됨 [확인 필요]
03 • num2를 출력하므로 soojebi가 출력됨 [확인 필요]
, 102, 103,104, 105] 10. engneng 11. split
6-302 vi 프로그래밍 언어 활용
## Page 489

► 24년 1회 ► 24년 2회
12 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
a=["Seoul", "Kyeonggi", "Incheon", "Daejun", "Daegu",
빠 "Pusan"]
03 strO1 = "S"
for i in a:
04 r .的 strO1=strO1+i[1]
print(strOI)
1햇히
01
• a 변수에 리스트 ["Seoul", "Kyeonggi",
fit 1 i M 丄 W 44 f■丄 JI J, "1Incheon , Daejun , Daegu , Pusan」 [확인 필요]
를 저장
02 • strO1 에 문자열 "S"를 대입
03
• for 문에서 a에 있는 값을 하나씩 i 변수에
저장하면서 반복
• 에 a의 0번지 값인 "Seoul"을 대입
04
• str이은 'S'이고, i[1]은 i°| 1번지 문자인 [확인 필요]
e이므로 'S'+'e'는 'Se'가 되어 str이에 저 [확인 필요]
장됨
03 • i에 a의 1번지 값인 "Kyeonggi"을 대입
04
•strO1 은 'Se'이고, i[1]은 i°| 1번지 문자인
y이므로 'Se'+'y'는 'Sey'가 되어 str이에 저 [확인 필요]
장됨
03 • 에 a의 2번지 값인 "Inchon"을 대입
04
•strO1 은 'Sey'이고, i[1]은 i의 1번지 문자인
n이므로 'Sey'+'n'는 'Seyn'이 되어 strO1
에 저장됨
03 • 에 a의 3번지 값인 "Daejeon"을 대입
04
• str이은 'Seyn'이고, i[1]은 i의 1번지 문자 [확인 필요]
인 a이므로 'Seyn'+'a'는 'Seyna'가 되어
str이에 저장됨 [확인 필요]
03 • i에 a의 4번지 값인 "Daegu"을 대입
04
•strO1 은 'Seyna'이고, i[1]은 i의 1번지 문자
인 a이므로 'Seyna'+'a'는 'Seynaa'가 되
어 str이에 저장됨 [확인 필요]
03 • 에 a의 5번지 값인 "Pusan"을 대입
04
• str이은 'Seynaa'이고, i[1]은 i의 1번지 문자 [확인 필요]
인 1』이므로 'Seynaa'+'u'는 'Seynaau'가
되어 str이에 저장됨 [확인 필요]
05 • strO1 값인 문자열 'Seynaau'를 출력
13 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 def fn(x, y):
02 result=0
03 for i in range(len(x)):
04 s=x[i:i+len(y)]
05 if s=y:
06 result+=1;
07 return result
08
09 str="abdcabcabca"
10 p1 = "ca"
11 p2="ab"
12 print(f'ab{fn(str, p1)}' f'ca{fn(str, p2)}')
!xu 서____________________________________________________ _______________________
r" 리 09 • str에 문자열 "abdcabcabca"를 대입 [확인 필요]
10 • 이에 문자열 "ca"> 대입
11 • p2에 문자열 "ab"를 대입
12 • f 스트링이므로 중괄호 안의 변수를 출력
• fn(str, p1)를 호출
01 • fn 메서드의 x 변수는 "abdcabcabca"을
전달받고, y 변수는 "ca"를 전달받음
02 • result# 0으로 초기화
03
•X 변수에서 문자열의 길이가 11이므로
len(x)는 11이 되어 i=0부터 11 미만일 때까
지반복
04
•y 변수에서 문자열의 길이가 2이므로
x[i:i+2]와 같음
•x[i:i+2]는 x의 i번지부터 i+2번지 미만일
때까지 슬라이싱
i 0 1 2 3 4 5 6 7 8 9 10
s ab bd de ca ab be ca ab be ca a
05 〜 06
• S 변수와 y 변수의 문자열인 "ca"를 비교하
여 같으면 result 값을 1 증가
• i=3일 때 s가 "ca"이고, i=6일 때 s가 "ca"
이고, i=9일 때 s가 "ca"이므로 result는 3이 [확인 필요]
되어 3을 반환
12 • f 스트링이므로 중괄호 안의 변수를 출력
• fn(str, p2)를 호출
01 • fn 메서드의 x 변수는 "abdcabcabca"을
전달받고, y 변수는 "ab"를 전달받음
02 • result 를 0으로 초기화
짜
12. Seynaau 13. ab3ca3
지피지기 기출문제 6-303
## Page 490

► 24년 3회
15 다음은 파이썬 코드이다. 출력 결과를 쓰시오.03
•X 변수에서 문자열의 길이가 11이므로
len(x)는 11이 되어 i=0부터 11 미만일 때까
지반복
04
•y 변수에서 문자열의 길이가 2이므로
x[i:i+2] 와 같음
•x[i:i+2]는 x의 i번지부터 i十2번지 미만일
때까지 슬라이싱
i 0 1 2 3 4 5 6 7 8 9 10
s ab bd de ca ab be ca ab be ca a
05 〜 06
• s 변수와 y 변수의 문자열인 "ab"를 비교하
여 같으면 result 값을 1 증가
• i=0일 때 s가 "ab"이고, i=4일 때 s가 "ab"
이고, i=7일 때 s가 "ab"이므로 result는 301 [확인 필요]
되어 3을 반환
12
• f 스트링이므로 {fn(str, p1)}은 3으로 {fn(str,
p2)}는 3으로 변환되어 print('ab3' 'ca3')이
되기 때문에 ab3ca3을 출력
01 def func(value):
02 if type(value)==typed 00):
03 return 100
04 elif type(value)==type(""):
05 return len(value)
06 else:
07 return 20
08
09 a="100.0"
10 b=100.0
11 C=(100, 200)
12
13 print(func(a)+f u nc(b)+f u nc(c))
► 24년 2회
14 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 def fn(str, k):
02 s=str.split('T')
03 return s[k]
04
05 Str="ITISTESTSTRING"
06 k=3
07 result=fn(str, k)
08 print(result)
I효 05 • str 변수에 "mSTESTSTRING" 문자열을 대입
06 •k변수에 3을 대입
07 • fn 메서드 호출
01
• str 변수에 "ITISTESTSTRING" 문자열, k 변
수에 3을 전달
02
• 'T' 문자열을 기준으로 분리
s[이 T
s[1] ' IS'
s[2] 'ES'
s[3] 'S'
s[4] ' RING'
03 • s[3]을 반환하므로 'S'를 반환
07 • resultoil fn(str, k)의 반환 값인 'S'를 대입
08 • result 값인 S를 출력
Ll.i 서 시 _______
「"리 09 • a 변수에 문자열 "100.0"을 대입
10 • b 변수에 실수형 100.0을 대입
11 • c 변수에 튜플형 (100, 200)을 대입
13
•func(a)를 호출하고, 매개변수로 문자열
"100.0"을 전달
01 • func 메서드에서 value는 "100.0"이 됨 [확인 필요]
02
• value는 문자열이므로 type(value)는 (class [확인 필요]
'str'>, type(100)은 (class 'inf>이므로 if 문
이 거짓이 되어 if 블록을 실행하지 않음
04
• type(value)는 (class 'str'>, type("")도<class
'str'>이므로 elif 조건이 참이 되어, elif 블록
의 명령어를 실행
05 • 문자열 "100.0"의 길이는 5이므로 5를 반환
13
•func(b)를 호출하고, 매개변수로 실수형
100.0을 전달
01 • func 메서드에서 value는 100.0이 됨 [확인 필요]
02
• value는 실수형이므로 type(value)는 (class [확인 필요]
'float'>, type(100)은 (class 'inf>이므로 if
문이 거짓이 되어 if 블록을 실행하지 않음
04
• type(value)는 (class 'float'>, type("")은
(class 'str'>이므로 elif 문도 거짓이 되어
elif 블록을 실행하지 않음
06
• if, elif 문 전부 거짓이므로 else 블록의 명
령어를 실행
14/S 15.45
6-304 vi 프로그래밍 언어 활용
## Page 491

07 • 20을 반환
13
• func(c)를 호출하고, 매개변수로 튜플형(100,
200)을 전달
01 • func 메서드에서 value는 (100, 200)01 됨 [확인 필요]
02
• val니e는 튜플형이므로 type(value)는 (class [확인 필요]
'tuple'>, type(100)은 (class 'inf>이므로 if
문이 거짓이 되어 if 블록을 실행하지 않음
04
• type(value)는 (class 'tuple'>, type("")은
<class 'str'>이므로 elif 문도 거짓이 되어 elif
블록을 실행하지 않음
06
• if, elif 조건이 모두 거짓이므로 else 블록의
명령어를 실행
07 • 20을 반환
13
• func(a)는 5, func(b)는 20, func(c)는 20이
므로, 5+20+20=45가 되어 45를 출력
► 24년 3회
16 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 def func(x):
02 for i in range(len(x) // 2):
03 x[i], x[—i—1]=x[—i—1],><[i]
04
05 x=[1, 2, 3, 4, 5, 6]
06 func(x)
07 print(sum(x[::2])-sum(x[1 ::2]))
[해설 1
1 05 • x 변수에 리스트 [1, 2, 3, 4, 5, 6]를 대입
06 • func(x) 메서드를 호출
01 • func 메서드 실행
02
•x의 크기가 6이므로 len(x)는 6이 되고,
len(x)//2는 6//2이므로 6을 2로 나눴을
때의 몫인 3이 됨
• i=0부터 3 미만일 때까지 반복
03
X[이/
x[-6]
><[1]/
x[—5]
x[2]/
x[-4]
x[3]/
x[-3]
x[4]/
x[-2]
x[5]/
x[—1]
1 2 3 4 5 6
• i=0일 때 x[0], x[-1]=x[—1], x[이이므로
x[이에 x[-1] 값인 6을, x[-1]에 x[0] 값인
1을 대입
X[이/
x[-6]
><[1]/
><[-5]
x[2]/
x[-4]
x[3]/
x[-3]
x[4]/
x[-2]
x[5]/
><[-1]
6 2 3 4 5 1
03
• i=1 일 때 x[1], x[-2]=x[—2], x[1]이므로
x[1]에 x[-2] 값인 5를, x[-2]에 x[1] 값인
2를대입
X[이/
x[-6]
><[1]/
x[-5]
x[2]/
x[-4]
x[3]/
x[-3]
x[4]/
x[-2]
x[5]/
x[-1]
6 5 3 4 2 1
03
• i=2일 때 x[2], x[—3]=x[—3], x[2]이므로
x[2]에 x[-3] 값인 4를, x[-3]에 x[2] 값인
3을대입
X[이/
x[-6]
X[1]/
x[-5]
x[2]/
x[-4]
x[3]/
x[-3]
x[4]/
x[-2]
x[5]/
x[-1]
6 5 4 3 2 1
07
• x[::2]는 리스트 0번지부터 끝까지 스텝을
2로 하여 값을 슬라이싱하므로 [6, 4, 2] 가
되고, sum([6, 4, 2])를 하면 12가 됨
• sum(x[1::2])는 리스트 1번지부터 끝까지 스
텝을 2로 하여 값을 슬라이싱하므로 [5, 3,
1]이 되고, sum([5, 3,1])을 하면 9가 됨
• 12-9는 3이므로 3을 출력
16. 3
천기누설 예상문제 6-305
## Page 492

► 25년 1회
1? 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 class Node:
02 def______ ___(self, v):
03 self.v=v
04 self.c=[ ]
05
06 def tree(li):
07 n=[Node(i) for i in li]
08 for i in range(1, len(li)):
09 n[(i-1)//2].c.append(n[i])
10 return n[이
11
12 def calc(n, level=0)'
13 return n.v if level % 2 else 0+\
sum(calc(n, lewl+1) for n in n.c) if n else 0
14
15 li니3, 5, 8, 12,15,17, 21] [확인 필요]
16 root=tree(li)
17 print(c 기 c(root))
10
17
5
n[(5-1)//2].c.append(n[5]
三 n[2].c.append(n[5])
n[2]에 n[5]를
자식으로 추가
6
n[(6-1)//2].c.append(n[6]
=n[2].c.append(n[6])
n[2]에 n[6]를
자식으로 추가
n[이 n[1] n[2] n[3] n[4] n[5] n[6]
V 3 5 8 12 15 17 21
C
[n[1],
n[2]]
[n[3],
n[4]]
[n[5],
n[6]]
[] [] [] []
三다음과 르이 트리가 구성됨
3
/ \
5 8
12 15 17 21
• n[이을 반환
• calc(root)를 호출
• calc 함수에 n에 n[이 전달하고, level은 디 [확인 필요]
폴트 매개변수로 0이 됨
• level은 0이므로 0%2 값은 0이므로 거짓이 [확인 필요]
되어 n.v if level % 2 else 0의 결과는 001 됨
I핸리 15
• 리스트 li를 [3, 5, 8,12,15,17, 21]로 초기화 [확인 필요]
16
• 리스트 li를 매개변수로 전달하여 tree 함수 [확인 필요]
를호출
17 • tree 함수 실행
07
• 리스트 li에서 하나씩 Node(i)로 전달하여 [확인 필요]
객체 생성하고 리스트형 노드들 생성함
01 〜 04
• Node 클래스에서 _init_으로 전달받은 v
값을 self.v에 대입하고 c는 빈 리스트([ ])를
생성함
li 값은 [3, 5, 8, 12, 15, 17, 21]이므로「은
[Node(3), Node(5), Node(8), Node(12),
Node(15), Node(17), Node(2l)]가 됨
n[이 n[1] n[2] n[3] n[4] n[5] n[6]
V 3 5 8 12 15 17 21
C [] [] [] [] [] [] []
• for 문을 이용하여 트리를 구성
i n[(H)//2].c.append(n[i]) 내용
08 〜 09
1
n[(1-1)//2].c.append(n[l])
三 n[이.c.append(n[l])
n[이에 n[1]를
자식으로 추가
2
n[(2-l)//2].c.append(n[2])
=n[이.c.append(n[2])
n[이에 n[2]를
자식으로 추가
3
n[(3너)//2].c.append(n[3])
=n[1].c.append(n[3])
n[1]에 n[3]를
자식으로 추가
4
n[(4-1)//2].c.append(n[4])
三 n[1].c.append(n[4])
n[1]에 n[4]를
자식으로 추가
• n.v if level % 2 else 0에서 level % 2
의 값이 1 이면 참이므로 n.v를 반환하고,
level % 2 한 값이 0이면 거짓이므로 0을
더함(level이 홀수이면 n.v 값을 더하고 level [확인 필요]
이 짝수이면 0을 더함)
12…14------------------------------ ------------
• n은 n[이이므로 객체가 존재하기 때문에 if
n에서 n은 참이 되어 sum(calc(n, level+1)
for n in n.c)을 실행
• n[0].c에 n[1]과 n[2]가 있으므로 sum
(calc(n[1], 1), calc(n[2], 1))가 되기 때문에 0
calc(n[1], 1)과 @ calc(n[2], 1)을 재귀 호출
• O의 반환 값은 5이고, ②의 반환 값은 801
므로 0+sum(5, 8)=0+13=13이 됨
• calc(root)의 반환값은 13
• O calc(n[1], 1)를 실행하여 n에 n[1]을, level
에 1을 전달
• level은 1이므로 1%2는 1인 참이 되어 n.v [확인 필요]
if level % 2 else 0의 결과는 n.v인 5가 됨
• n은 n[1]이므로 객체가 존재하기 때문에 if
n에서 n은 참이 되어 sum(calc(n, level+1)
12~14 for n in n.c)을 실행
• n[1].c는 n[3]과 n[4]가 있으므로 sum
(calc(n[3], 2), calc(n[4], 2))가 되기 때문에
© calc(n[3], 2)과 0 calc(n[4], 2)를 재귀
호출함
• ©의 반환 값은 0이고, 0의 반환 값은 0이
므로 5+sum(0, 0)=5+0=5가 됨
6-306 VI 프=그래밍 언어 활용
## Page 493

► 25년 2회
12 〜 14
• © calc(n[3], 2)를 실행하여 n에 n[3], level
에 2를 전달
• lev이은 2이므로 2%2는 0인 거짓이 되어 [확인 필요]
n.v if level % 2 이se 0의 결과는 0이 됨 [확인 필요]
• n은 n[3]이므로 객체가 존재하기 때문에 if
n에서 n은 참이 되어 sum(calc(n, lewH너) [확인 필요]
for n in n.c)을 실행
• n[3].c는 비어 있으므로 s니i)(c기c(n, level [확인 필요]
+1)for n in n.c)은 sum(0)=0이 됨
• 반환 값은 0+0=0 이 됨
12 〜 14
• 0 c게 c(n[4], 2)를 실행하여 n에 n[4], level
에 2를 전달
• lev이은 2이므로 2%2는 0인 거짓이 되어 [확인 필요]
n.v if level % 2 else 0의 결과는 0이 됨
• n은 n[4]이므로 객체가 존재하기 때문에 if
n에서 n은 참이 되어 sum(calc(n, level+1)
for n in n.c)을 실행
• n[4].c는 비어 있으므로 sum(calc(n, level+
1) for n in n.c)은 sum(0)=0이 됨
• 반환 값은 0+0=0 이 됨
12〜14
• @ calc(n[2], 1)를 실행하여 n에 n[2], level
에 1을 전달
• level은 1이므로 1%2는 1인 참이 되어 n.v if [확인 필요]
level % 2 else 0의 결과는 n.v인 801 됨
• n은 n[2]이므로 객체가 존재하기 때문에 if
n에서 n은 참이 되어 sum(calc(n, level+1)
for n in n.c)을 실행
• n[2].c는 n[5]과 n[6]가 있으므로 sum (calc
(n[5], 2), calc(n[6], 2))가 되기 때문에 ©
calc(n[5], 2)과 © calc(n[6], 2)를 재귀 호출함
• ©의 반환 값은 0이고, ©의 반환 값은 0이
므로 8+sum(0, 0)=8+0=8이 됨
12〜14
• © calc(n[5], 2)를 실행하여 n에 n[5], lev이 [확인 필요]
에 2를 전달
• level은 2이므로 2%2는 0인 거짓이 되어 [확인 필요]
n.v if level % 2 else 0의 결과는 0이 됨
• n은 n[5]이므로 객체가 존재하기 때문에 if
n에서 n은 참이 되어 s니m(calc(n, level+1) [확인 필요]
for n in n.c)을 실행
• n[5].c는 비어 있으므로 sum(calc(n, level4-
1) for n in n.c)은 wm(0)=0이 됨
• 반환 값은 0+0=0 이 됨
12〜14
• © calc(n[6], 2)를 실행하여 n에 n[6], level
에 2를 전달
• lev이은 2이므로 2%2는 0인 거짓이 되어 [확인 필요]
n.v if level % 2 else 0의 결과는 0이 됨
• n은 n[6]이므로 객체가 존재하기 때문에 if
n에서 n은 참이 되어 sum(calc(n, level+1)
for n in n.c)을 실행
• n[6].c는 비어 있으므로 sum(calc(n, levd+
1) for n in n.c)은 s니m(0)=0이 됨 [확인 필요]
• 반환 값은 0+0=0 이 됨
17 • calc(root)의 반환값은 13이므로 13을 출력
18 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 1st늬1,2,3] [확인 필요]
02 dst={i:i*2 for i in 1st}
03 s=set(dst.values())
04 1st[이=99
05 dst[2]=7
06 s.add(99)
07 print(len(s & set(dst.values())))
01
• 1st 변수에 리스트 [1, 2, 3] 대입
1st[이 lst[1] lst[2]
1 2 3
02 〜 04
•dst 변수에 딕셔너리형 {i:i*2}를 대입
• 1st에 있는 1, 2, 3을 key로 하고, 그 값에 2 [확인 필요]
를 곱한 결과인 2, 4, 6을 value로 하는 딕 [확인 필요]
셔너리 생성
key value
1 2
2 4
3 6
03 • dst°| 값인 2, 4, 6을 세트형으로 s에 저장
04
• 1st[이의 값을 99로 변경
1st[이 lst[1] lst[2]
99 2
_3___
• dst[2]의 값을 7로 변경
key value
04 1 2
2 7
3 6
6
• s 세트형 변수에 99를 추가하면 s={2, 4, 6,
99} 가됨
7
•s 변수의 값은 {2. 4, 6, 99}이고, set(dst.
values)는 dst의 값을 세트형으로 변환하는 [확인 필요]
것이므로 {2, 6, 가이 됨
• s 변수와 set(dst.values)의 교집합(&) 값은
2이므로2를 출력
지피지기 기출문제 6-307
## Page 494

19 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 〜 06
• data 변수에 2차원 리스트 대입
data[이 [3, 5, 2, 4,1]
01 data=[
02 [3, 5, 2, 4,1],
03 [4, 5,1],
04 [4, 4,1, 5, 4],
05 [4,5]
06 ]
08 result={}
10 for index, lis in enumerate(data):
11 list_sum=sum(lis)
12 listjen 긔 en(lis)
13 result[index]=(list_s니m, listjen) [확인 필요]
15 print(result)
data[1] [4, 5,1]
data[2] [4, 4,1, 5, 4]
data[3] [4,5]
08 • result 변수에 빈 딕셔너리형 대입
10
• 첫 번째 반복일 때 인덱스는 0, data의 0번 [확인 필요]
지 요소를 lis 변수에 대입(index=0, lis=[3,
5, 2, 4,1]가 됨)
11
• sum은 요소들의 합을 계산 [확인 필요]
• list_sum三sum([3, 5, 2, 4,1])너5
12
• sum은 요소들의 개수를 계산 [확인 필요]
• listjen:긔en([3, 5, 2, 4,1])=5 [확인 필요]
13
• result[이=(15, 5)
• result 딕셔너리형의 키는 0, 값은 (15,5)가 됨
10
• 두 번째 반복일 때 인덱스는 1, data°| 1번
지 요소를 lis 변수에 대입(index너, lis=[4, [확인 필요]
5,1]가됨)
11 • list_sum=sum([4, 5,1])三10
12 • listjen긔en([4, 5,1])=3 [확인 필요]
13
• result[1]=(10, 3)
• result 딕셔너리형의 키는 1, 값은 (10,3)이 됨
10
• 세 번째 반복일 때 인덱스는 2, data의 2번 [확인 필요]
지 요소를 lis 변수에 대입(index=2, lis늬4, [확인 필요]
4,1, 5, 4] 가 됨)
11 • list_s니m=sum([4,4,1, 5, 4])=18 [확인 필요]
12 • listjen 긔en([4,4,1, 5,4])=5 [확인 필요]
13
• res니lt[2] = (18, 5) [확인 필요]
• res니It 딕셔너리형의 키는 2, 값은 (18,5)가 됨 [확인 필요]
10
• 네 번째 반복일 때 인덱스는 3, data의 3번 [확인 필요]
지 요소를 lis 변수에 대입(index=3, lis=[4,
5]가됨)
11 • list_sum=sum([4, 5])=9
12 • listjen긔en([4, 5])=2 [확인 필요]
13
• result[3]三(9, 2)
• result 딕셔너리형의 키는 3, 값은 (9, 2)가 됨
혀뎌우
『19. 石: (15, 5), 1: (10, 3), 2: (18, 5), 3: (9, 2)}
6-308 VI 프로그래밍 언어 활용
## Page 495

효 천기누설 볘상문제
01 다음은 파이썬 코드이다. 빈칸에 들어갈 출력
결과를 쓰시오.
[소스코드] [출력 결과]
a=10
b='text'
print(type(a))
print(type(b))
<class ' Q '>
(class © '>
• a는 10이라는 정수값이므로 int 형, b는 text라는 문 [확인 필요]
자/문자열을 저장하고 있으므로 str 형이다.
• 파이썬 타입은 다음과 같다.
int 정수값
float 실수값
str 문자 또는 문자열
02 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 temp=0
02 minjndex=0
03 a=[4, 2, 3, 5,1]
04 for i in range(0,4):
05 min_index=i
06
07 for j in range(i+1, 5):
08 if a[j]<a[min_index]:
09 minjndex 듸
10
11 temp=a[min_index]
12 a[min_index]=a[i]
13 a[i]=temp
14
15 print(a)
1 01 • temp=0으로 초기화
02 • min_index=0 으로 초기화
03 • a 변수에 리스트 [4, 2, 3, 5,1]을 대입
04 • i=0부터 4 미만일 때까지 반복
• i=0부터 시작
05 • minjndex에 i 값 0을 대입 [확인 필요]
• j느부터 5 미만일 때까지 반복
j a[j]<a[min_index] 조건 minjndex
07 〜 09
1 a[1]<a[이 참 1
2 a[2]<a[1] 거짓 1
3 a[3]<a[2] 거짓 1
4 a[4]<a[2] 참 4
11 〜13
• minjndex는 4이고., 는 0이므로 a[4]와 [확인 필요]
a[이 값을 교환
a[이 a[1] a[2] a[3] a[4]
1 2 3 5 4
04 •i너이 됨
05 • minjndex에 i 값 1을 대입 [확인 필요]
•j=2부터 5 미만일 때까지 반복
j a[j]<a[min_index] 조건 minjndex
07 〜 09 2 a[2]<a[1] 거짓 1
3 a[3]<a[1] 거짓 1
4 a[4]<a[1] 거짓 1
11 〜13
• minjndex는 1이고, 느 1이므로 a[1]와 a[1] [확인 필요]
값을 교환
a[이 a[1] a[2] a[3] a[4]
1 2 3 5 4
04 •i=2 가됨
05 • minjndex에 i 값 2를 대입 [확인 필요]
07〜 09
• j=3부터 5 미만일 때까지 반복
j a[j]<a[min_index] 조건 minjndex
3 a[3]<a[2] 거짓 2
4 a[4]<a[2] 거짓 2
11~13
• minjndex는 2이고, i는 2이므로 a[2]와 [확인 필요]
a[2] 값을 교환
a[이 a[1] a[2] a[3] a[4]
1 2 3 5 4
01. @:int, ©:str 02. [1, 2, 3, 4, 5]
천기누설 예상문제 6-309
## Page 496

04 •i=3 이 됨
05 • minjndex에 i 값 3을 대입 [확인 필요]
• j=4부터 5 미만일 때까지 반복
07〜 09 j a[j]<a[minjndex] 조건 minjndex
4 a[4]<a[3] | 참 4
11 〜13
• minjndex는 4이고, 누는 3이므로 a[4]와 [확인 필요]
a[3] 값을 교환
a[이 a[1] a[2] a[3] a[4]
1 2 3 4 5
15 • a를 출력
03 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 a=['Hello', 'Python', "World"]
02 print(a[이[3:], a[2][:—3])
03 print(f"{a[0][::-1]} {a[1][—1:-5:-2]}")
04 print("{} {}".format(a[1][::], a[2][::2]))
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
04 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
class A:
a=2
def____ _(self):
self.a 十=3
def fn(self):
self.a+=5
class B(A):
a 三7
def____ _(self):
self.a+=11
def fn(self):
self.a+=13
a=B()
print(a.a, end=")
a.fn()
print(a.a)
r—h
01
• a는 리스트 변수로 다음과 같이 저장
a[이 Hello
a[1] Python
a[2] World
02
• a[이는 'Hello'이고, [3:]은 3번지부터 끝까
지 슬라이싱하므로 Io를 출력 [확인 필요]
•a[2]는 'World'이고, [:-3}은 처음부터 뒤
에서 3번지 문자 전까지 슬라이싱하므로
Wo를 출력 [확인 필요]
03
• a[이는 'Hello'이고, [::-1]은 -1씩 건너뛰
므로 결과적으로 역순인 olleH를 출력 [확인 필요]
•a[1]는 'Python'이고, [-1:-5:-2]는 마지
막부터 -5번지 직전인 -4번지까지 한 번
에 두 글자씩 건너뛰며 역방향으로 슬라이
싱하므로 nh를 출력 [확인 필요]
04
•a[1]는 'Python'이고, [::]는 처음부터 끝
까지 1글자씩 건너뛰며 슬라이싱하므로
Python을 출력 [확인 필요]
•a[2]는 'World'이고, [::2]는 처음부터 끝까
지 2글자씩 건너뛰며 슬라이싱하므로 Wrd
를 출력
I--1
15
• B 클래스의 생성자를 실행하고 a 변수에 B
클래스의 인스턴스를 대입
• B 클래스 생성할 때 매개변수가 없으므로
매개변수가 없는 생성자 호출
10 • B 클래스 생성자를 실행
11 • 클래스 변수 a=7를 참조한 후, 거기에 11
을 더한 18을 self.a에 저장
16 • a.a는 인스턴스 변수인 18을 출력
17 • B 클래스를 저장하고 있는 a 변수의 fn 호출
12 • B 클래스의 fn 메서드 호출
13
• 인스턴스 변수 self.a에 13을 더하므로
18+13인 31을 대입
16 • a.a는 인스턴스 변수인 31을 출력
03. Io Wo
olleH nh
Python Wrd
04.1831
6-310 VI 프로그래밍 언어 활용
## Page 497

05 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01 x={1 : 'Apple', 2: 'Banana', 3: 'Cherry', 4: 'Durian'}
02 print(x[1])
03 print(len(x))
04 print(x.pop(2))
05 print(x)
l해실 •x 변수에 딕셔너리형 초기화
키 값
01
1 Apple
2 Banana
3 Cherry
4 Durian
02 • 키가 1인 요소의 값은 Apple이므로 Apple [확인 필요]
을 출력
03 • 딕셔너 리 요소의 개수는 4이므로 4를 출력
04
• 키가 2인 요소의 값인 Banana를 출력하 [확인 필요]
고, x 변수에서 키가 2인 요소를 제거
키 값
1 Apple
3 Cherry
4 Durian
05 • X 변수 출력
06 다음은 파이썬 코드이다. 출력 결과를 쓰시오.
01
02
03
04
05
06
07
08
09
10
11
12
13
14
def fn(x):
n=len(x)
for i in ranged, n):
now=x[i]
j=i-1
while j>=0 and x[j]>now:
x[j+1]=x[j]
j-너
x[j+1]=now
r—-!
r: 리 12 • x 변수에 [5, 8, 2. 3}을 저장
13 • fn 메서드에 x 변수 전달
01 • fn 메서드 안의 x 변수에 fn 메서드 밖에서
전달받은 X를 대입
02 • x의 개수는 4이므로 len(x)는 4가 되어 n은 4
가됨
04 • i너부터 n 미만일 때까지 반복
• i너부터 반복문 실행
05 • =이므로 x[1]은 801 되어 now는 801 됨 [확인 필요]
06 • i-1 은 1-1=0이므로 j는 001 됨
07
• j=0이므로 j>=0은 참이고,><[j]인 x[이은 5,
now는 8이므로 x[j]>now는 거짓이 되어 [확인 필요]
반복문을 실행하지 않음
10
• j=0이므로 x[1]에 now 값인 8을 대입
이이 X[1] S x[2] x[3]
5 8 2 3
04 •i=2 가됨
05 • now는 x[2]의 값인 2를 대입 [확인 필요]
06 •i-1은 2-1=1이므로 j는 1이 됨
07
• j=1 이므로 j>=0은 참이고, x[j]인 x[1]은 8,
now는 2이므로 x[j]>now는 참이 되어 반 [확인 필요]
복문을 실행
08
• x[2]=x[1 이므로 x[1]인 8을 x[2] 에 대입
X[이 x[1] x[2] x[3]
5 8 8 3
09 • j를 1 감소시켜 j는 0이 됨
07
• j=0이므로 j>=0은 참이고, x[j]인 x[이은 5,
now는 2이므로 x[j]>now는 참이 되어 반 [확인 필요]
복문을 실행
08
• x[1]=x[0 이므로 x[이인 5를 x[1] 에 대입
X[이 ><[1] x[2] x[3]
5 5 8 3
09 • j 를 1 감소시켜 j 는-1이 됨
07 •j=-1이므로 j>=0은 거짓이므로 거짓이 되
어 반복문을 실행하지 않음
10
• j=너이므로 X[이에 now 값인 2를 대입
x[이 X[1] x[2] x[3]
2 5 8 3
x=[5, 8, 2, 3]
fn(x)
print(x) 05. Apple
4
Banana
06. [2, 3, 5, 8]
{1:'Apple', 3:'Cherry', 4:'Durian'}
천기누설 예상문제 6-311
## Page 498

04 •i=3 이 됨
05 • now는 x[3]의 값인 3을 대입 [확인 필요]
06 • i-1 은 3-1=2이므로 느 2가 됨
07
• j=2이므로 j>=0은 참이고, x[j]인 x[2]은 8,
now는 3이므로 x[j]>now는 참이 되어 반 [확인 필요]
복문을 실행
08
• x[3]=x[2]이므로 x[2]인 8을 x[3]에 대입
x[이 X[1] x[2] x[3]
2 5 8 8
09 • j를 1 감소시켜 j는 101 됨
07
• j=1 이므로 j>=0은 참이고, x[j]인 x[1]은 5,
now는 3이므로 x[j]>now는 참이 되어 반 [확인 필요]
복문을 실행
08
•x[2]=x[1] 이므로><[1 인 5를 x[2]에 대입
X[이 x[1] x[2] x[3]
2 5 5 8
09 • j를 1 감소시켜 j는 00| 됨
07
• j=0이므로 j>=0은 참이고, x[j]인 x[이은 2,
now는 3이므로 x[j]>ncw는 거짓이 되어 [확인 필요]
반복문을 실행하지 않음
10
• j=0이= x[1]에 now 값인 3을 대입
X[이 x[1] x[2] x[3]
2 3 5 8
14 • X 값을 출력
6-312 vi 프로그래밍 언어 활용
## Page 499

베스트 합괵 후기
비전공, 임금피크, 동차 합격 후기(감사의 마음을 담아서)(아이디: 워**님)
퇴직을 앞두고 시간 여유가 조금 생겨서 무엇을 할까 고민이 많았습니다. 직장인들은 매일 연
속되는 업무로 공부할 시간이 별로 없고, 특별한 동기부여가 없으면 새로운 분야로의 도전은 현
실적으로 어려움이 많습니다.
저 또한 비슷한 상황에서 약간의 시간 여유가 생기면서 기사 자격증에 관심을 가지기 시작했습
니다. 처음 도전한 자격은 사회적으로  핫한 산업안전기사로 23년 도전하여 무난하게 획득할 수
있었습니다. 물론 새로운 지식을 머리에 심는 과정이 싶지는 않았지만, 도전하며 꾸준히 열심히
하니 좋은 결과가 나왔습니다. 아마 이것이 원동력이 되어 정보처리기사자격증도 도전하는 계기
가 되었는지도 모릅니다. 또 한가지는 제 업무 중 스마트공장 사업이 있는데, 많은 소프트웨어 공
급기업의 전문인력 중 정처기 자격증이 많지 않은 것도 한몫했습니다. 저는 소위 말하는 임금피
크제 인력으로 50대 후반, 비전공자, 프로그램 능력 전무한상태에서 도전하게 되었습니다.
수제비 책은 7월 말에 이미 구입하여 언어 부분은 그냥 눈으로만 조금씩 보다가 빅데이터 분석
기사 필기시험 끝나고 9월 9일부터 본격적으로 시작했습니다. 수제비에서 제안하는 6주 프로그
램에 따라 매일 매일 제가 할 수 있는 부분까지 공부하고, 공부한 내용은 가능한한 자세하게 수제
비 카페에 스터디 후기를 등록했습니다. 지금 생각해보니 스터디 후기 등록하면서 복습이 자연스
럽게 되었고, 나중에 내가등록한 글을 찾아서 읽어보면서 기억을 유지하는데 도움이 되었습니다.
6주 스터디는 도중에 추석도 있고, 개인 사정으로 몇 번 누락은 했지만, 29일차까지 계속되었
고, 수제비에서 출제한 마지막 모의고사도 보았습니다. 모의고사 성적이 60점 부근이라서 좀 애
매한 상황이었지만, 지금까지 공부방법을 유지하며 암기과목을 마지막으로 복습하는 것으로 공
부를 마무리했습니다. 물론 이번 시험은 자바 등 프로그래밍이 많았고 생소한 것이 나왔지만, 수
제비에서 보고 듣고 공부한 내용을 기억하며 차분히 접근하여 70점의 성적으로 합격할 수 있었습
니다. 비전공자에게 가장 어려운 프로그래밍은 연습장에 직접 기록해가며 루프문을 돌리고 답이
어떻게 나오는지 머리로 이해하려고 노력했습니다.
저의 합격 비결은 1) 6주 동안 꾸준히 1일 3시간 정도 공부, 2) 공부한 내용을 스터디 후기에 자
세히 등록 및 복습, 3) 모르는 내용은 질문 코너 활용하여 묻고 답하기, 4) 수제비 책 3회독 , 5) 프
로그래밍 이해
첫 번째 1회독은  시간도 많이 걸리고 무슨 내용인지 전혀 모르고 넘어간 것도 있지만, 회독을  더
하면서 시간도 단축하고 모르는 부분도 줄어들었습니다. 시중에 수많은 정보처리기사 책이 있고,
분명 장단점이 있지만, 수제비 카페처럼 10만명 이상의 회원을  보유하고 데일리 문제, 질의응답
대응, 4, 6, 8주 스터디 운영, 인강까지 갖추고 체계적으로 접근하는 곳은 없다고 생각합니다.
혹시 이 글을 읽는 분들도 수제비 카페에서 꾸준히 공부하면 분명 좋은 소식이 있을 것으로 생
각합니다. 수제비 카페의 운영진 모두에게 감사드립니다.
## Page 500

베스트 합격 후기
정보처리기사 실기 합격 후기(아이디: 푸른**님)
이론 파트의 경우는 수제비 실기 교재를 3회독만  하면 탄탄하게 잡힙니다.
이론 파트에서는 새로운 경향의 문제가 회차마다  1〜2개씩은 나오기도 하지만, 그걸 감안하더
라도 수제비에 실린 내용은 나머지 8〜9문제를 꽉 잡을 수 있을 정도로 정리가 잘 되어 있는 편입
니다.
처음에는 대략적인 흐름을 판단하기 위해서 가볍게 읽어 넘어가고 2회차부터  정독을 하면서
각 파트의 기출 문제와 예상 문제를 노트에 풀이를 하는 것과 동시에 카페에 거의 매일 올라오는
데일리 문제를 체크해가며 본인이 어느 부분에서 부족했는지 점검하면 2〜3개월에 충분히 합격
선까지 완성된다고 생각합니다.
사실 프로그래밍과 많이 엮이는 SQL 파트도 현재까지는 수제비 실기 참고서에 실린 내용만 반
복해서 학습해도 전 문제를 맞히는 데에는 문제가 없을 정도로 평이하게 출제되고 있기에, SQL
파= 위의 방법대로 학습하면 되지 않을까 싶습니다.
문제는 프로그래밍 파트인데, 2회차의  경우는 특히 전공자들이 유리할 만한 프로그래밍 문제
가 중심이 되었습니다.
작년까지 빈번하게 출제되었던 노가다에 가까운 단순 계산 방식의 프로그래밍보다는 정말 원
리에 기초해서 프로그램의 구조를 이해할 수 있는가에 초점이 맞춰진 지극히 전공자 입장에 가까
운 문제로 변하고 있는 듯합니다.
그렇다고 막 엄청나게 어려운 프로그래밍 문제는 아니었고, 학부생 기준으로 1〜2학년의 학기
초에 접할 만한 수준이었지만 비전공자 입장에서는 그럼에도 워낙 프로그래밍의 양이 방대하다
보니 대비함에 어려움이 있을 거라 생각이 듭니다.
물론 수제비에 실린 프로그래밍 파트를 정말 100% 이해하고 응용할 수 있을 정도로 공부하면
이 역시 충분히 대비할 수 있다고는 생각합니다.
프로그래밍은 본인이 학습한 이론을 토대로 응용해서 풀어야 하는 파트인데, 기출이나 예상 문
제를 풀다 보면 원리를 이해하기보다는 약간 좀 문제 풀이를 외우게 되는 방식으로 접근하기가 쉬
워지는지라 '해당문제만' 이해하고 넘어가게 될 수도 있습니다.
개인적으로는 비전공자의 경우에는 인강 등의 방법을 병행하는 것이 더욱 더 합격률을 높일 수
있는 방법이라 생각합니다.
