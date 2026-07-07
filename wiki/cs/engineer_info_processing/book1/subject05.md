---
type: Study Note
title: "[5과목] 인터페이스 구현"
description: "정보처리기사 실기 기본서 1권 5과목 인터페이스 구현 본문 텍스트 추출본"
tags: [engineer-info-processing, 기본서1권, 과목5]
timestamp: 2026-06-19
status: active
---

# 5과목 인터페이스 구현

## Page 317

1_J 15
• main 메서드부터 시작
16 • n1 이라는 Node 구조체 변수를 선언하고,
v 값을 1로, next 값을 NULL로 초기화 [확인 필요]
17 • n2라는 Node 구조체 변수를 선언하고,
v 값을 2로, next 값을 NULL로 초기화 [확인 필요]
18
• n3이라는 Node 구조체 변수를 선언하고,
v 값을 3=, next 값을 NULM 초기화
n1 n2 n3
'[디 next
[Xj V
|NULL) next
kudnext
19 • Node 포인터 c를 선언하고, n1 의 주소값을
c에 대입
21
• nlnext에 n3의 주소값을 대입 [확인 필요]
n1 n2 n3
m v
|~&n3 j next
m v
next
pq v
|NULL[ next
22 • func(&n1) 을 호출
06 • func 함수 내에서 포인터 n0| n1 의 주소가 됨
07
•n은 &n1 이므로 n! = NULL은 참이고, [확인 필요]
n—>next는 (&n1)->next이므로 &n3이기 때 [확인 필요]
문에 n->next !=NULL은 참이 되어 while [확인 필요]
문을 수행
08 • n은 &n1 이므로 n->v는 (&n1)_>v가 되고,
n1 의 v는 1이므로 toll 1을 대입
09
•n—>next—>v는 (&n1)->next—>v이고,
(&n1)—>next는 &n3이므로 (&n3)->v ^21 [확인 필요]
3이 됨
• n->v인 n1.v에 n3.v 값을 대입하여 n1.v는
301 됨
n1 n2 n3
p—j V
| &n3 | next
느山 next 릐 next
10
•n—>next—>v는 (&n3)—>v이므로 n3.v에
t 값을 대입하여 n3.v는 10| 됨
n1 n2 n3
의 n:xt Knit CO v
| &n2 | next
11 • n->next->next는 (&n3)—>next이므로 n3 [확인 필요]
의 next 값인 &n2를 n 에 대입
07
•□은 &n2이므로 n ! = NULL은 참이고, [확인 필요]
n—>next는 (&n2)—>next이므로 NULL0|7| [확인 필요]
때문에 n->next !=NULL은 거짓이 되어 [확인 필요]
while 문을 종료
13 • func 함수를 호출한 부분으로 복귀
24 •c는 &n1 이므로 NULL이 아니기 때문에 [확인 필요]
c!=NULL는 참이 되어 while 문 실행 [확인 필요]
25 • c->v는 (&n1)->v이므로 n1.v 값인 3을 출력
26 •c—>next는 (&n1)—>next이므로 &n3가 되 [확인 필요]
어 c=&n3가 됨
24 •c는 &n3이므로 NULL이 아니기 때문에 [확인 필요]
c!=NULL는 참이 되어 while 문 실행 [확인 필요]
25 • C->v는 (&n3)->v이므로 n3.v 값인 1을 출력
26 •c~>next는 (&n3)—>next이므로 &n2가 되 [확인 필요]
어 c:=&n2가 됨
24 •c는 &n2이므로 NULL이 아니기 때문에 [확인 필요]
c!=NULL는 참이 되어 while 문 실행 [확인 필요]
25 • c->v는 (&n2)->v이므로 n2.v 값인 2를 출력
26 •c—>next는 (&n2)—>next이므로 NULL0| [확인 필요]
되어 c=NULL이 됨 [확인 필요]
24 • c는 NULL이므로 c!=NULL는 거짓이 되어 [확인 필요]
while 문 종료
► 24년 3회
43 다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 void func(int **arr, int size){
03 int i;
04 for(i=0;i<size;i++){
05 *(*arr+i)=(*(*arr+i)+i) % size;
06 }
07 }
08 int main(){
09 int arr[ ]={3,1, 4,1, 5};
10 int *p=arr;
11 int **pp=&p;
13 func(pp, 5);
14 printf("%d", arr[2]);
15 return 0;
지피지기 기출문제 6-131
## Page 318

► 25 년 1 회
44 다음은 C언어 코드이다. 출력 결과를 쓰시오.
I—h
I빠리 08
• main 함수부터 시작
09 •arr 배열을 {3,1, 4,1, 5}로 초기화
10 • 포인터 변수 p에 배열 arr을 대입 [확인 필요]
11 • pp 포인터 변수에 p의 주소값을 대입
13 • func 함수에 pp와 5를 전달하여 호출 [확인 필요]
02
• func 함수에서 arr는 main 함수의 &p이고, [확인 필요]
size는 5 [확인 필요]
03 • i 변수 선언
04 • for 루프는 i=0부터 i=4까지 반복 실행
05
• arr은 &p이므로 (*(*arr+i))는 (*(*&p+i))= [확인 필요]
(*(p+i))==arr[i]이고, (*(*arr+i)+i))==(*(*&
p+i)+i)==(*(p+i)+i)==(*(arr+i)+i)==(arr
[i]+i)가 됨
• size는 5이므로 arr[i]=(arr[i]+i) % 5와 같음 [확인 필요]
• i=0일 때 arr[이= (arr[이+0) % 5이므로,
arr[이=3 % 5가 되어 arr[이에 3을 대입
04
•i=1 일 때, Ksize인 1<5가 참이므로 for 문 [확인 필요]
실행
05
• i=|일 때 arr[i]=(arr[i]+i) % 5는 arr[1]= [확인 필요]
(arr[1]+1)%5와 같음
• arr[1]=(1+1)%5이므로, arr[1]=2 % 5가 되
어 arr[1]에 2를 대입
04
• i三2일 때, i<size인 2<5가 참이므로 for 문 [확인 필요]
실행
05
•i=2일 때 arr[i]=(arr[i]+i) % 5는 arr[2]=
(arr[2]+2)%5와 같음
•arr[2]=(4+2)%5이므로, arr[2]=6 % 5가
되어 arr[2]에 1을 대입
04
• i=3일 때, i<size인 3<5가 참이므로 for 문 [확인 필요]
실행
05
• i=3일 때 arr[i]=(arr[i]+i) % 5는 arr[3]=
(arr[3]+3)%5와 같음
•arr[3]=(1+3)%5이므로, arr[3]=4 % 5가
되어 arr[3]에 4를 대입
04
• i=4일 때, i<size인 4<5가 참이므로 for 문 [확인 필요]
실행
05
• i=4일 때 arr[i]=(arr[i]+i) % 5는 arr[4]=
(arr[4]+4)%5와 같음
•arr[4]=(5+4)%5이므로, arr[4]=9 % 5가
되어 arr[4]에 4를 대입
04
• i=5일 때, i<size인 5<5가 거짓이므로 for [확인 필요]
문종료
14 • arr[2] 는 1이므로 1을 출력
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
include <stdio.h>
char Data[5]={'B', 'A', 'D', 'E'};
char c;
int main(){
int i, temp, temp2;
c='C';
printf("%d\n", Data[3]-Data[1]);
for(i=0;i<5;++i){
if(Data[i]>c)
break;
}
temp=Data[i];
Data[i]=c;
i++;
for(;i<5; ++i){
temp2=Data[i];
Data[i]=temp;
temp 三 temp2;
}
for(i=0; i<5; i++){
printf("%c", Data[i]);
}
return 0;
BACDE
6-132 VI프로그래밍 언어 활용 [확인 필요]
## Page 319

► 25년 1회
45 다음은 C언어 코드이다. 출력 결과를 쓰시오.
02
Data 배열 선언 및 문자 초기화(마지막 요소
는 \0으로 자동 초기화)
• 전역 변수 c를 선언
Data[이 Data[1] Data[2] Data[3] Data[4]
'B' 'A' 'D' 'E' '\0'
03
04
05
• main 함수 시작
• 정수형 변수 i, temp, temp2를 선언
06 • c 변수에 문자 'C' 대입
Data[3]인 'E'와 Data[1]인 'A'를 뺀 값을 10
진수로 출력
E의 아스키 코드는 69이고, A의 아스키 코
드는 65이므로 E-A=69—65=4
08〜11
12
13
• 누는 0으로 초기화하고, i 값이 5보다 작을 때
까지 1씩 증가하면서 for 문을 수행
• Data[i]>'C' 조건을 만족할 때 break을 만 [확인 필요]
나 for 문을 종료
• i=2일 때 'D'>'C'가 성립되어 for 문이 종료
• temp에 Data[2]의 값인 'D'를 저장 [확인 필요]
• Data[2]에 'C'를 대입
• i 값이 1 증가
15〜19
• 느 0으로 초기화하고 i 값이 5보다 작을 때
i temp2=
Data[i]
Data[i]=
temp
temp 三
temp2
3 'E' 'D' 'E'
4 '\0' 'E' '\0'
20 〜 22
까지 1씩 증가하면서 for 문을 수행
• Data[〔 의 값을 순서대로 출력
Data[이 Data[1] Data[2] Data[3] Data[4]
'B' 'A' 'C' 'D' 'E'
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
#include <stdio.h>
#include <stdlib.h>
void set(int**arr, int*data,  int rows, int cols) {
• 느 3부터 시작하고 i 값이 5보다 작을 때까
지 1씩 증가하면서 for 문을 수행
int i;
for(i=0; i<rows*cols ; ++i) {
arr[((i+1) /rows) % rows][(i+1) % cols]=data[i];
int main() {
int rows=3, cols=3, sum=0;
int i;
int **arr;
int data[ ]={5, 2, 7, 4,1, 8, 3, 6, 9};
arr= (int**)malloc(sizeof(int*)  * rows);
for(i=0; i<cols; i++) {
arr[i]=(int *)  malloc(sizeof(int) * cols);
}
set(arr, data, rows, cols);
for(i=0; i<rows*cols ; i++) {
sum+=arr[i / rows][i %cols]*  (i % 2=0 ? 1: 너);
}
for(i=0; i<rows; i++) {
free(arr[i]);
}
free(arr);
printf("%d", sum);
return 0;
지피지기 기출문제 6-133
## Page 320

L2a? 09 • main 함수에서 프로그램 시작
10 • rows는 3, cols는 3, sum은 0으로 초기화 [확인 필요]
11 • i 변수 선언
12 • 2차원 포인터 변수 arr을 선언 [확인 필요]
13 • 정수형 배열 data를 선언 및 초기화 [확인 필요]
• sizeof(int*)는 int 형 포인터 변수의 크기를
반환하는 연산자로 4
• sizeof(int*)의 값인 4와 rows 값인 3을 곱한
12를 malloc 함수의 매개변수로 전달하여
14 12바이트의메모리를할당
• 12바이트의 메모리를 int**로 형 변환
12 바이트
arr ― ■'으' ■、
--------j----------------너 arr[이 | arr[1] | arr[2] j
• 는 0으로 초기화하고 i 값이 cols인 3보다 [확인 필요]
작을 때까지 1씩 증가하면서 for 문을 실행
• malloc 함수에 sizeof(int)와 cols를 곱한 값 [확인 필요]
12를 매개변수로 전달하여 메모리를 할당
15M7 하고 卽仙에 대입
12 바이트
rr 느------- --------- 、
I —I-----------' arr|01 --------- 후 .1
arr[1}------- 서
I I ]
• 정수형 2차원 포인터 변수 arr, 정수형 배열
data, 정수형 변수 rows에 3, 정수형 변수 [확인 필요]
cols에 3을 매개변수로 하여 set() 함수를 [확인 필요]
호출
• arr, data, rows은 3, cols은 3을 전달받음 [확인 필요]
• 너는 0으로 초기화하고 i 값이 rows*cols인 [확인 필요]
9보다 작을 때까지 1씩 증가하면서 for 문
을수행
i arr[((i+1)/rows)%rows][(i+1)% cols] data[i]
0 arr[((O+1)/3)%3][(O+1)%3]=arr[이 [1] 5
1 arr[((1+1)/3)%3][(l+1)%3]=arr[0][2] 2
2 arr[((2+1)/3)%3][(2+1)%3]=arr[1][이 7
Varr[((3+1)/3)%3][(3+1)%3]=arr[1][1] 4
4 arr[((4+1)/3)%3][(4+1)%3]=arr[1][2] 1
5 arr[((5+1)/3)%3][(5+1)%3]=arr[2][이 8
6 arr[((6+1)/3)%3][(6+1)%3]=arr[2][1] 3
7 arr[((7+1)/3)%3][(7+1)%3]=arr[2][2] 6
8 arr[((8+1)/3)%3][(8+1)%3]=arr[이이 9
• arr은 다음과 같음 [확인 필요]
[이 [1] [2]
arr[이 9 5 2
arr[1] 7 4 1
arr[2] 8 3 6
• 너는 0으로 초기화하고 i 값이 rows*cols인 [확인 필요]
9보다 작을 때까지 1씩 증가하면서 for 문을
수행
• arr[i/rows][i%cols]와 (i%2==0?1:-1)를 곱
한 값을 sum 변수에 누적해서 더함
i arr[i/rows][i%c 이 s] (i%2==0?1:-1) sum
19 〜 21
0 arr[0/3][0%3]=arr[이[이=9 1 9
1 arr[1 /3][1 %3]=arr[이 [1 ] 三 5 -1 4
2 arr[2/3][2%3]=arr[0][2]=2 1 6
3 arr[3/3][3%3]=arr[1][이=7 -1 -1
4 arr[4/3][4%3]=arr[1][1]=4 1 3
5 arr[5/3][5%3]=arr[1][2]=1 -1 2
6 arr[6/3][6%3] 三 arr[2][이=8 1 10
7 arr[7/3][7%3]=arr[2][1]=3 -1 7
8 arr[8/3][8%3]=arr[2][2]=6 1 13
22 〜 24 • arr[이부터 a리까지 할당된 메모리를 free
함수를 이용하여 해제함
25 • arr에 할당된 메모리를 free 함수를 이용하 [확인 필요]
여 해제함
26 • sum 값인 13을 출력
6-134 vi 프로그래밍 언어 활용
## Page 321

► 25년 1회
46 다음은 C언어 코드이다. 출력 결과를 쓰시오.
include <stdio.h>
ffinclude<stdlib.h>
typedef struct Data {
int value;
struct Data *next;
} Data;
Data *insert(Data *head, int value) {
Data *new_node=(Data *)malloc(sizeof(Data));
new_node -> value=value;
new_node -> next=NULL;
if(head=NUI_L)
return new_node;
new_node-> next=head;
head=new_node;
return head;
}
Data *reconnect(Data *head, int disconnect_count) {
Data *prev三head, *curr=head—>next;
while(curr && curr —>v게 ue!=disconnect_count) {
prev=curr;
curr=curr—>next;
}
if(ciirr==NULL) return head;
prev—>next=curr—>next;
curr—>next三head;
return curr;
}
int main(){
Data *head:三NULL, *curr三NULL, *tmp=NULL;
int i;
for (i三 1; i<三5; i++)
head=insert(head, i);
head=reconnect(head, 3);
for(curr=head; curr!:三NULL; curr=curr->next)
printf("%d", curr—>value);
while(head){
tmp 三 head;
head=head-) next;
free(tmp);
}
return 0;
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
38
39
40
41
42
43
44
45
46
47
48
02 • malloc, free 함수 사용을 위해 stdlib.h 헤
더파일 include 함
03 〜 06 • Data라는 구조체에 정수형 변수 value, 구 [확인 필요]
조체 포인터(struct Data *) 변수 next를 선언 [확인 필요]
06 • typedeS 사용하여 struct Data를 Data로 [확인 필요]
사용함
31 • main 함수부터 프로그램 시작
32 • Data *head=NULL, *curr=NUI_L, *tmp=
NULL;
33 • 정수형 변수 i 선언
34 〜 35 • =일 때 i<=5는 참이= for 문을 실행
07〜 10
• i=1 일 때 head는 NULL이므로 insert(NULL, [확인 필요]
1)을 실행
• insert 함수에 head는 NULL, value에 1을 [확인 필요]
전달
• sizeof 연산자를 이용하여 Data 구조체의
크기를 malloc 함수에 매개변수로 전달하여
메모리 할당받은 후 (Data *) 타입으로 new_
nodeojl 대입함
• new_node->value에 매개변수로 전달받 [확인 필요]
은 1을 대입
• new_node—>next에 NULL 값 대입 [확인 필요]
vahje next
new_node 1 NULL
12〜13 • head7|- NULL이므로 new_node를 반환 [확인 필요]
35
• insert 함수에서 반환한 new_node 값을
headoil 대입
head | new_node ------------------► new_node [ 1 | NULL ]
34 • i는 1 증가하여 2가 되며, 2는 5보다 작으므
로 for 문을 실행
35 • head 값 그리고 I는 2를 매개 변수로 전달
하여 insert 함수 호출
07 〜 10
• sizeof 연산자를 이용하여 Data 구조체의
크기를 malloc 함수에 매개변수로 전달하
여 메모리 할당 받은 후 (Data *) 타입으로
new_node에 대입함 [확인 필요]
• new_node->value에 매개변수로 전달받 [확인 필요]
은 2를 대입
• new_node—>next에 NULL을 대입 [확인 필요]
12 • head는 NULLOI 아니므로 if 문을 실행하 [확인 필요]
지 않음
46. 35421
지피지기 기출문제 6-135
## Page 322

15〜16
• head를 new_node->next에 대입 [확인 필요]
• new_node를 head에 대입 [확인 필요]
head | ------------------스에세de | 1 | Null j [확인 필요]
스 new_node | 2 | new_node j 乂>
17 • head를 반환 [확인 필요]
35 • insert 함수에서 반환한 head 값을 head에 [확인 필요]
대입
34
• 느 1 증가하여 301 되며, 3은 5보다 작으므
로 for 문을 수행함
35 • head 값 그리고 I는 3을 매개 변수로 전달
하여 insert 함수 호출
07 〜 10
• sizeof 연산자를 이용하여 Data 구조체의
크기를 malloc 함수에 매개변수로 전달하
여 메모리 할당 받은 후 (Data *) 타입으로
new_node에 대입함 [확인 필요]
• new_node->value에 매개변수로 전달받 [확인 필요]
은 3을 대입
• new_node—>next에 NULL을 대입 [확인 필요]
12 • head는 NULL0| 아니므로 if 문을 실행하지 [확인 필요]
않음
15〜16 • head를 new_node—>next에 대입 [확인 필요]
• new_node를 head에 대입 [확인 필요]
17 • head 를 반환
35 • insert 함수에서 반환한 head 값을 head에 [확인 필요]
대입
34
• 더는 1 증가하여 4가 되며, 4는 5보다 작으므
로 for 문을 수행함
35 • insert 함수에 head 값과 i 값인 4를 매개
변수로 전달
07〜 10
• sizeof 연산자를 이용하여 Data 구조체의
크기를 malloc 함수에 매개변수로 전달하
여 메모리 할당 받은 후 (Data *) 타입으로
new_node에 대입함 [확인 필요]
• new_node->value에 매개변수로 전달받 [확인 필요]
은 4를 대입
• new_node—>next에 NULL을 대입 [확인 필요]
12 • head는 NULL0I 아니므로 if 문을 실행하지 [확인 필요]
않음
15〜16 • head를 new_node->next에 대입 [확인 필요]
• new_node를 head 에 대입 [확인 필요]
17 • head를 반환 [확인 필요]
35 • insert 함수에서 반환한 head 값을 head에 [확인 필요]
대입
34 〜 35
• 더는 1 증가하여 5가 되며, 5는 5와 같으므로
for 문을 수행함
35 • head 값 그리고 느 5를 매개 변수로 전달
하여 insert 함수 호출
7 • insert 함수 실행
8 〜 10
• sizeof 연산자를 이용하여 Data 구조체의
크기를 malloc 함수에 매개변수로 전달하
여 메모리 할당 받은 후 (Data *) 타입으로
new_node에 대입함 [확인 필요]
• new_node->value에 매개변수로 전달받 [확인 필요]
은 5를 대입
• new_node->next에 NULL을 대입 [확인 필요]
12 • head는 NULL0I 아니므로 if 문을 실행하지 [확인 필요]
않음
15〜16 • heac® new_node—>next에 대입 [확인 필요]
• new_node를 head에 대입 [확인 필요]
17 • head를 반환 [확인 필요]
35 • insert 함수에서 반환한 head 값을 head에 [확인 필요]
대입
34
• 느 1 증가하여 601 되며 6은 5보다 크므로
거짓이 되어 for 문을 종료함
37 • head와 3을 매개변수로 전달하여 recon- [확인 필요]
nect 함수를 호출함
19 • head, disconnect_count는 3을 전달받아 [확인 필요]
reconnect 함수를 실행함
20
• Data * 구조체 포인터 타입 변수 prev를 선 [확인 필요]
언하고 head를 대입함 [확인 필요]
• Data * 구조체 포인터 타입 변수 curr를 선 [확인 필요]
언하고 head->next를 대입함 [확인 필요]
• prev—>value는 5, curr—>value는 4기' 됨 [확인 필요]
21
• while 문에서 curr—>value는 4이고 에s— [확인 필요]
connect_count는 3이므로 같지 않음으로 [확인 필요]
참이되瓦 반복을수행함
22 〜 23 • curr값을 prev에 대입 [확인 필요]
• curr을 다음 노드로 이동함 [확인 필요]
21
• while 문에서 curr->wlue는 3이고 세s— [확인 필요]
connect_count는 30기짓0| 되어 반 [확인 필요]
복을 멈춤
25 • if 문에서 curr=NULL은 거짓이 되어 실행 [확인 필요]
하지 않음
27 • curr—>next를 prev-> next 에 대입 [확인 필요]
28 • head를 curr—>next에 대입 [확인 필요]
29 • curr을 반환 [확인 필요]
37 • head에 reconnect 함수의 반환 값을 대입함 [확인 필요]
39 〜40
• tor 문에서 초기화를 위해 head 값을 curr
에 대입
• curr0| NULL0| 아니므로 curr—>value의 [확인 필요]
값 3을 출력
• curr=curr->next 다음으루 이동
39 〜40
• currO| NULL0| 아니므로 curr—>value의 [확인 필요]
값 5를 줄력
• curr=curr—>next 다음으로 이동
6-136 vi 프로그래밍 언어 활용
## Page 323

39 〜40
• currO| NULLO| 아니므로 curr—>value의 [확인 필요]
값 4를 줄력
• curr=curr—>next 다음으로 이동
39 〜40
• curr이 NULLO| 아니므로 curr->vah」e의 [확인 필요]
값 2를 출력
• curr=curr->next 仁|■음으로 이동
39~40
• currO| NULLO| 아니므로 curr—>value의 [확인 필요]
값 1을 출력
• curr=curr—>next 仁|•음으^ 이동
42 〜45 • 링크드 리스트에 할당된 메모리를 해제
► 25년 1 회
다음은 C언어 코드이다. 출력 결과를 쓰시오.
#include<stdio.h>
typedef struct student{
char *name;
int score[3];
}Student;
int dec(int enc){
return enc & 0xA5;
}
int sum(Student *p){
return dec(p—>score[이)+dec(p->score[1])+dec(p-)score[2]);
}
int main(){
Student $[2]={"師", (GxAO, 0xA5, OxDB), "Lee", {0xA0,0xED, 0x81}};
Student *p=s;
int result=0, i;
for(i=0; i<2; i++){
result +=sum(&s[i]);
}
printf("%d", result);
return 0;
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
21
22
Lu 서
12 • main 함수에서 프로그램 시작
13
• 크기가 2인 Student 구조체 배열 변수 s를
선언하고 초기화
s name score[3]
s「01 "Kim" [이 『 ⑴ ⑵
° K OxAO 0xA5 _OxDB_
s「1l "Lee" [이 p] [2]
⑴ L OxAO i OxED 0x81
14 • Student * 구조체 포인터 변수 p를 선언하
고 구조체 배열 변수 s를 대입
15
• 정수형 변수 result 선언 및 0으로 초기화함
• for 문에서 사용할 정수형 변수 i* 선언함
17 • i=0일 때 i<2는 참이므로 for 문을 수행함
18 • sum(&s[이)을 호출
10 • dec에 p->score[0] 값인 OxAO을 매개변 [확인 필요]
수로 전달
06 〜 08 • enc로 전달받은 OxAO 값과 0xA5를 AND [확인 필요]
연산한 160을 반환
10 • dec에 p—>score[1] 값인 0xA5를 매개변 [확인 필요]
수로 전달
06 〜 08 • enc로 전달받은 0xA5 값과 0xA5를 AND [확인 필요]
연산한 165를 반환
10 • dec에 p—>score[2] 값인 OxDB를 매개변 [확인 필요]
수로 전달
06 〜 08 • enc로 전달받은 OxDB 값과 0xA5를 AND [확인 필요]
연산한 129를 반환
10 • 160과 165와 129를 더한 값 454를 반환
18 • 454를 resultoil 더하여 result는 454가 됨 [확인 필요]
17 • i++에서 i 값을 1 증가시켜 느 10| 된 상태
에서 i<2가 되며 참이므로 for 문을 수행함
18 • sum(&s[l]) 을 호출
10 • dec에 p->score[이 값인 OxAO을 매개변 [확인 필요]
수로 전달
6 〜8 • enc로 전달받은 OxAO 값과 0xA5를 AND [확인 필요]
연산한 160을 반환
10 • dec 에 p->score[1] 값인 Ox EDS 매개변
수로 전달
06 〜 08 • enc로 전달받은 OxED 값과 OxA5를 AND [확인 필요]
연산한 165를 반환
지피지기 기출문제 6-137
## Page 324

10
• dec에 p->score[2] 값인 0x81 을 매개변 [확인 필요]
수로 전달
06 〜 08 • enc로 전달받은 0x81 값과 0xA5를 AND [확인 필요]
연산한 129를 반환
10 • 160과 165와 129를 더한 값 454를 반환
18 • result 값이 454인 상태에서 반환값인 454
를 res니It에 더하면 result는 90801 됨 [확인 필요]
17
• i++에 의해 느 2개 되고, i<2가 거짓이 되
어 for 문을 탈출함
21 • result 값인 908을 줄력
► 25년 2회
48 다음은 C언어 코드이다. 출력 결과를 쓰시오.
include <stdio.h>
#define SIZE 3
typedef struct {
int data[SIZE];
int front;
int rear;
}Queue;
void enq(Queue* q, int va!) {
q->data[q —>rear] 三 val;
q -) rear=(q -> rear+1) % SIZE;
}
int deq(Queue* q) {
int val=q_>data[q-> front];
q—>front=(q—>front+1) % SIZE;
return val;
}
int main(){
Queue q={{0}, 0, 0};
int a, b;
enq(&q, 1);
enq(&q, 2);
deq(&q);
en이(&q, 3); [확인 필요]
a=deq(&q);
b 三 deq(&q);
printf("%d 그리고 %d", b, a);
return 0;
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
r—1
L::....르」02 • SIZE를 3으로 정의 [확인 필요]
03 〜 07
• 구조체에 data 배열, front, rear 변수를 선
언하고, 구조체의 이름을 Queue로 정의 [확인 필요]
17 • main 함수부터 시작
18
• q 구조체에 {0}, 0, 0으로 초기화
data
data[이=0
data[1]=0
data[2]=0
이 front 0
rear 0
19 • a, b 변수 선언
20 • enq 함수에 &q, 1을 전달
08 • enq 함수에서 q 포인터 변수에 main 함수
의 q 주소값을 대입, va에 1을 대입 [확인 필요]
09 • q—>rear는 0, val은 1이므로 q—>data[이=! [확인 필요]
10
•q->rear는 0이므로 (0+1)%3인 1을 q-> [확인 필요]
rear에 대입 [확인 필요]
data
data[이=1
data[1]=0
data[2]=0
이 front 0
rear 1
21 • enq 함수에 &q, 2를 전달
08 • enq 함수에서 q 포인터 변수에 main 함수
의 이 주소값을 대입, Va에 2를 대입 [확인 필요]
09 • q—>rear는 1, val은 2이므로 q->data[1]=2 [확인 필요]
10
•q->rear는 1이므로 (1十1)%3인 2를 q-> [확인 필요]
rear에 대입 [확인 필요]
data
data[이 =l
data[1]=2
data[2]=0
이 front 0
rear 2
22 • deq 함수에 &q를 전달
12 • deq 함수에서 q 포인터 변수에 main 함수
의 이 주소값을 대입
13 • q->front는 0이므로 q->data[이인 1을 val 에 [확인 필요]
대입
14
•q->front는 0이므로 (0+1)%3인 1을 q-> [확인 필요]
front에 대입 [확인 필요]
data
data[이=1
data[1] 三2
data[2]=0
이 front 1
rear 2
6-138 VI 프로그래밍 언어 활용
## Page 325

► 25년 2회15 • val 값인 1 을 반환
23 • enq 함수에 &q, 3을 전달
08 • enq 함수에서 q 포인터 변수에 main 함수
의 q 주소값을 대입, val에 3을 대입 [확인 필요]
09 • q—>rear는 2, val은 3이므로 q—>data[2]=3 [확인 필요]
•q->rear는 2이므로(2+1)%3인 0을 q-> [확인 필요]
rear에 대입 [확인 필요]
10 data
data[이=1
data[1]=2
data[2]=3
front 1
rear 0
24 • deq(&q) 를 실행
12 • deq 함수에서 q 포인터 변수에 main 함수
의 q 주소값을 대입
13 • q—>front는 1이므로 q—>data[1]인 2를 val [확인 필요]
에 대입
•q->front는 1이므로(1+1)%3인 2를 q-> [확인 필요]
front에 대입 [확인 필요]
14 data
data[이=1
data[1]=2
data[2]=3
이 front 2
rear 0
15 • val 값인 2를 반환
24 • a 변수에 deq(&q)의 반환값인 2를 대입
25 • deq(&q)를 실행
12 • deq 함수에서 q 포인터 변수에 main 함수
의 q 주소값을 대입
13 •q_)front는 2이므로 q->data[2]인 3을 [확인 필요]
valOil 대입
.q_>front는 2이므로(2+1)%3인 0을 q-> [확인 필요]
front에 대입 [확인 필요]
14 data
data[이 =l
data[1]=2
data[2]=3
이 front 0
rear 0
15 • val 값인 3을 반환
25 • b 변수에 deq(&q)의 반환값인 3을 대입
23 • b=3, a=2이므로 3 그리고 2를 출력
49 다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 struct dat {
03 int x;
04 int y;
05 };
06 int main() {
07 struct dat a[ ]={{1, 2}, {3, 4}, {5, 6}};
08 struct dat* ptr=a;
09 struct dat** pptr=&ptr;
10 (*pptr)[1]=(*pptr)[2];
11 printf("%d 그리고 %d", a[1].x, a[1].y);
12 return 0;
13 }
1
n리 02〜05 • dat 구조체에 x, y 변수 선언
06 • main 함수부터 시작
07
dat 구조체 타입의 a 배열 초기화
a[이 x=1, y=2
a[1] x=3, y=4
a[2] x=5, y=6
08 • ptr 포인터 변수에 a를 대입
09 • pptr 포인터 변수에 ptr°| 주소를 대입
10
pptr=&ptr이므로 (*pptr)=(*&ptr)=ptr이 됨 [확인 필요]
•ptr=a이므로 a[1]=a[2]이기 때문에 a[2]의
값을 a[1]에 대입
a[이 x=1, y=2
a[1] x=5, y 三6
a[2] x=5, y=6
11 • a[1].x=5이고, a[1].y=6이므로 5 그리고 6
을 출력
지피지기 기출문제 6-139
## Page 326

다음은 C언어 코드이다. 출력 결과를 쓰시오.
► 25 년 2 회
12
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
include <stdio.h>
include<stdlib.h>
struct node {
int p;
struct node* n;
};
int main() {
struct node a={1, NULL};
struct node b={2, NULL};
struct node c={3, NULL};
struct node* head=:&c;
a.n=&b;
b.n=&c;
c.n=NULL;
c.n=&a;
a.n=&b;
b.n=NULL;
printf("%d%j%d", head->p, head-)n->p, head->n-)n->p);
return 0;
a
• a 변수의 n에 b 변수의 주소를 대입
p 1
n &b
b 변수의 n에 c 변수의 주소를 대입
13
14
15
16
17
18
n &c
• c 변수의 n에 NULL을 대입 [확인 필요]
—p 으—5—
c ---------------------------------
n NULL
• c 변수의 n에 a 변수의 주소를 대입
P 3
• a 변수의 n에 b 변수의 주소를 대입
P 1 a ---------—--------------------
n &b
• b 변수의 n에 NULL을 대입 [확인 필요]
P 2
n NULL
h 실
I
03 〜 06
• node라는 이름의 구조체는 p라는 정수형, [확인 필요]
n이라는 node 구조체를 가리킬 수 있는 포
인터 변수로 정의
07 • main 함수부터 실행
08
• node 구조체 타입의 a 변수에 1, NULL을 [확인 필요]
대입 __
P 1 a-----------------------------------------
n_NULL___________
09
• node 구조체 타입의 b 변수에 2, NULL을 [확인 필요]
대입_______________________________
b —으一一스
n NULL
10
• node 구조체 타입의 c 변수에 3, NULL을 [확인 필요]
대입 _______________________________
P 3C -----------------------------------------
n NULL________
11 • node라는 구조체 포인터 변수 head를 선 [확인 필요]
언하고, head의 값을 &c로 대입 [확인 필요]
head는 &c이므로 head->p는 &c—>p이 [확인 필요]
기 때문에 c 변수의 p인 3이 됨
head—>n—>p에서 head—>n은 &a이므로
(head—>n)->p는 (&a)->p이므로 a 변수의
p 값인 10| 됨
head—>n—>n—>p에서 head->n은 &a0|
므루 (head->n)->n->p는 (&a)—>n—>p가
되고, (&a->n)->p는 &b->p이므로 b 변
수의 p 값인 2가 됨
50. 3 1 2
6-140 VI 프로그래밍 언어 활용
## Page 327

► 25년 2회
51 다음은 C언어 코드이다. 출력 결과를 쓰시오.
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
#include<stdio.h>
#include (stdlib.h)
struct node {
char c;
struct node*  p;
• main 함수의 n은 h의 값인 400번지
};
stiuct node*  func(char*  s) {
struct node*  h=NULL, *n ;
while(*s)  {
n=(struct node*)malloc(sizeof(struct  node));
n—>c=*s  十+;
n->p=h;
h=n;
}
return h;
}
int main() {
struct node*  n=func("BEST");
19 while(n) {
20 struct node*  t=n;
21 putchar(n—>c);
22 n=n->p;
23 free(t);
24 }
25 return 0;
26 }
09
10
유 설 |
03 〜 06 • node라는 이름의 구조체에 문자형 변수 c, [확인 필요]
node 구조체의 포인터 변수 Q를 선언
17 • m기n 함수부터 시작 [확인 필요]
18 • tunc 함수에 문자열 "BEST" 전달
07 • func 함수는 node*  타입을 반환
• s는 문자열 "BEST"의 시작 주소를 가리킴
08
• 포인터 변수 h에 null로 초기화, 포인터 [확인 필요]
변수 n을 선언
09
• while 문의 조건이 0이면 while 문을 종료
• s가 가리키는 값이 'B'이므로 while 문 조건
은참
10 • n 변수에 node 구조체 크기의 공간을 할당
• 새로 생성된 주소를 100번지라고 가정
11
• *s인 'B'를 n—>c에 저장하고, s++로 포인
터를 다음 문자CE')로 이동 [확인 필요]
11
12
13
09
15
18
51. TSEB
12
• n->p에 h를 대입
n(100 번지) —-
C 'B'
NULLP
13
09
10
09
10
11
12
13
• h에 n을 대입하여 h는 100번지가 됨
• s가 가리키는 값이 'E'이므로 while 문 조건
은참___________________________________
• n 변수에 node 구조체 크기의 공간을 할당
• 새로 생성된 주소를 200번지라고 가정
11
12
• *s인 'E'를 n->c에 저장하고, s++로 포인
터를 다음 문자CS')로 이동 [확인 필요]
• n->p에 h를 대입(n->p가 이전 노드인 h를
가리키게  하여 연결)
C 'E'
n(200번지) 一
P 100
• h에 n을 대입하여 h는 200번지가 됨13
' s가 가리키는 값이 'S'이므로 while 문 조건
은참
• n변수에 구조체 크기의 공간을 할당
' 새로 생성된 주소를 300번지라고 가정
• s 인 'S'를 n->c에 저장하고, S++로 포인
터를 다음 문자fT')로 이동 [확인 필요]
*
三三品arS"허입(n—>p가 이전 노드인 h를
가리키게  하여 연결)
n(300번지) --------- ------
p 200
• h에 rT을 대입하여 h는 300번지가 됨 [확인 필요]
• s가 가리키는 값이 T이므로 while 문 조
건은 참
• n 변수에 node 구조체 크기의 공간을 할당
• 새로 생성된 주소를 400번지라고 가정
• s인 T를 n->c에 저장하고, s++로 포인
터를 다음 문자(null)로 이동
*
• n->p에 h를 대입(n->p가 이전 노드인 h를
가리키게  하여 연결)
n(400번지)--------- - -----------
p 300
• 브엣 n을 대입하여 h는 400번지가 됨
• s가 가리키는 값이 NULL이므로 while 문 [확인 필요]
조건은 거짓이 되어 while 문 종료
• h 값인 400번지를 반환
지피지기 기출문제 6-141
## Page 328

► 25년 3회
19 •n은 400번지이므로 0이 아니기 때문에
while 문 조건은 참
20
• t 변수에 n인 400번지를 대입
c 'T'
400번지----------------------
p 300
21 •n->c 값인 T를 출력
22 • n->p 값인 300번지를 n에 대입
23 • 400번지에 할당된 메모리를 해제시킴
19 •n은 300번지이므로 0이 아니기 때문에
while 문 조건은 참
20
• t 변수에 n인 300번지를 대입
c 'S'
300번지----------------------
p 200
21 •n->c 값인 S를 출력
22 • n->p 값인 200번지를 n에 대입
23 • 300번지에 할당된 메모리를 해제시킴
19 •n은 200번지이므로 0이 아니기 때문에
while 문 조건은 참
20
• t 변수에 n인 200번지를 대입
c ' E'
p 100
21 • n->c 값인 E를 출력
22 •n->p 값인 100번지를 n에 대입
23 • 200번지에 할당된 메모리를 해제시킴
19 •n은 100번지이므로 0이 아니기 때문에
while 문 조건은 참
20
• t 변수에 n인 100번지를 대입
c 'B'
100번지 ——-…一
p NULL
21 • n->c 값인 B를 출력
22 • n->p 값인 NULL(0번지)를 n에 대입
23 • 100번지에 할당된 메모리를 해제시킴
19 • n0| 가리키는 값이 NULL이므로 while 문 [확인 필요]
조건은 거짓이 되어 while 문 종료
52 다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 #include <stdio.h>
02 struct Soo {
03 int x;
04 const char *y;
05 };
06 int main() {
07 struct Soo t[ ]={{1, "AB"}, {2, "DC"}, {3, "EB"}};
08 struct Soo *p=&t[1];
09 printf("%s", p->y+(p->x—1));
10 return 0;
11 }
•t 구조체 배열 값 초기화
02 〜 05
• 구조체 Soo를 정의 [확인 필요]
• int 형 변수 x, char 포인터 변수
06 • main 함수부터 시작
07
• 포인터 변수 P에 &t[1]을 대입
X y
t[이 1 "AB"의 시작 주소값
t[1] 2 "DC"의 시작 주소값
t[2] 3 "EB"의 시작 주소값
09
P는 &t[l]이므로 p—>y==&t[1]—>y=네1].
y인 "DC"의 시작 주소
P는 &t[1]이므로 p—>x—1은 &t[1]—>><—1이
기 때문에 t[1].x-1인 2-1=1
("DC"의 시작 주소)를 %s로 출력하면 시작
주소의 값인 D부터 NULL 전까지 출력되므
로 DC가 출력되지만, ("DC"의 시작 주소 [확인 필요]
+1)를 %s로 출력하면 시작 주소의 다음 값
인 C부터 NULL 전까지 출력되므로 C가 출
력됨
6-142 VI 프로그래밍 언어 활용
## Page 329

► 25년 3회 ► 25년 3회
53 다음은 C언어 코드이다. 출력 결과를 쓰시오. 54 다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 int main(){
03 char str[ ]="REPUBLICOR<OREA":
04 int a=0;
05 while (str[a] !='\0') ++a;
06 putchar(str[a—2]);
07 return 0;
08 }
L.ii 서 1―
LL르J 02 • main 함수부터 시작 [확인 필요]
• str 문자형 배열을 초기화
03 [이 [1] [2] [13] [14] [15]
R E P E A \0
04 • a 변수를 0으로 초기화
05
• a=0일 때, str[이은 'R'이므로 while 조건이
참이기 때문에 a를 1 증가시킴
• a=1 일 때, str[1]은 'E'이므로 while 조건이
참이기 때문에 a를 1 증가시킴
• a=2일 때, str[2]은 'P'이므로 while 조건이
참이기 때문에 a를 1 증가시킴
• a=14일 때, str[14]은 'A'이므로 while 조건
이 참이기 때문에 a를 1 증가시킴
• a=15일 때, str[15]은 '\0'이므로 while 조건
이 거짓이기 때문에 while 문 종료
06
•a=l5이므로 str[15—2]=str[13]이므로 E를
출력
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
#inchjde<stdio.h>
struct Node{
struct Node* next;
unsigned int x;
};
int main(){
struct Node t1={ 0, 5u };
struct Node t2={ 0, 7u };
struct Node t3={ 0,11u };
struct Node* curr;
int sum=0;
t3.next=&t2;
t2.next=&t1;
curr=&t3;
while (curr){
sum=sum * 3+curr—>x;
cun=curr—>next;
}
sum=(sumA42u)+100u;
printf("%u", sum);
return 0;
54.187
지피지기 기출문제 6-143
## Page 330

1 허지_____普하-
02 〜 05
• 구조체 Node를 정의 [확인 필요]
• 구조체 포인터 변수 next, unsigned int 형
변수 X를 선언
07 • main 함수부터 시작
• t1 구조체를 초기화
08 next 0
t1 x 5
• t2 구조체를 초기화
09 next 0
t2 x  7
• t3 구조체를 초기화
10 next 0
t3 x  11
11 • curr 포인터 변수 선언
12 • sum을 0으로 초기화 [확인 필요]
14 • t3의 next를 t2의 주솟값으로 대입 [확인 필요]
15 • t2의 next를 t1 의 주솟값으로 대입 [확인 필요]
• curr을 t3의 주솟값으로 대입 [확인 필요]
curr &t3
next 0
16
t1 x  5
next &t1
t2 x  7
next &t2
t3 x  11
18 •curr=81t3이므로 조건식이 참
19 • sum三0, curr—>x는 (&t3)—>x==l1 이기 때
문에 sum=0*3+11=11
20 • curr=&t3이므로 curr—>next는 &t2가 되어 [확인 필요]
cun=&t2가 됨
18 • curr=&t2이므로 조건식이 참
19 •sum=11, curr—>x는 (&t2)—>x==7이기 때
문에 sum=11*3+7=40
20 • curr=&t2이므로 curr—>next는 8dl가 되어 [확인 필요]
curr=&t1 이 됨
18 • curr=&t1 이므로 조건식이 참
19 • sum=40, curr—>x는 (&t1)—>x=5이기 때
문에 sum=40*3+5=125
20 • curr=&t1 이므로 c니rr—>next는 O(NULL) 되 [확인 필요]
어 c니rr=NULL이 됨 [확인 필요]
18 • curr=NULL이므로 조건식이 거짓 [확인 필요]
23
• 125(2진수로 0111 1101)와 42(2진수로 0010
1010)를 2진수로 변환하여 XOR 연산하면
8701 됨
0111 1101
XOR) 0010 1010
0101 이11
• sum=(sm1A42u)+100u=87+100=187
이 됨
25 • sum 값인 187을 출력
6-144 vi 프로그래밍 언어 활용
## Page 331

천기누설 Wl 상문제
01 다음은 C언어 코드이다. 출력 결과를 쓰시오.
#include<stdio.h>
int Soojebi(int num) {
int i;
for(i=2;i<num;i++){
if(num % i=0)
return 0;
}
return 1;
}
int main() {
int num=IO, cnt=0, i;
for(i 三 2;i<num;i++)
cnt+=Soojebi(i);
printf("%d\n", ent);
return 0;
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
r—
LL리 io • main 함수부터 실행 [확인 필요]
11
• 정수형 변수 num을 10으로 초기화, ent는 [확인 필요]
0으로 초기화
12 • i=2일 때 i<10은 참이므로 반복문 실행
13 • Soojebi(2) 를 호출
02 〜 09 •num = 2이므로 for 문을 실행하지 않아
return 1을 반환
13 • Soojebi(2)는 1이므로 ent에 1을 더해 ent는 [확인 필요]
1이 됨
12 • i++에 의해 i=3이 되면 i<10이 참이 되어
반복문 실행
13 • Soojebi(3) 을 호출
02 〜 09
• num=3이므로 if(3 % 2==0)이 거짓이 되어
if 문 안의 return 0을 실행하지 않아 return
1을 반환
13 • Soojebi(3)은 1이므로 ent에 1을 더해 ent는 [확인 필요]
2가됨
12 • i++에 의해 i=4가 되면 i<10이 참이 되어
반복문 실행
13 • Soojebi(4)를 호출
02 〜 09
• num=4이므로 if(4 % 2==0)이 참이 되어 if
문 안의 return 0을 반환
• 사용자 정의 함수는 return을 만나면 그 순 [확인 필요]
간 사용자 정의 함수를 종료하고 반환값을
함수 호출했던 곳으로 전달
13 • Soojebi(4)는 0이므로 ent에 0을 더해 ent [확인 필요]
는 2가됨
12 • i+十에 의해 i=5가 되면 i<10이 참이 되어
반복문 실행
13 • Soojebi(5) 를 호출
02〜 09
• num=5이므로 if(5 % 2==0), if(5 % 3==0),
if(5 % 4==0)모두 거짓이 되어 if 문 안의
return 0을 실행하지 않아 return 1을 반환
13 • Soojebi(5)는 1이므로 ent에 1을 더해 ent는 [확인 필요]
3이 됨
12 • i+十에 의해 i=6이 되면 i<10이 참이 되어
반복문 실행
13 • Soojebi(6) 을 호출
02 〜 09 • num=6이므로 if(6 % 2==0)이 참이 되어 if
문 안의 return 0을 반환
13 •Soojebi(6)은 0이므로 ent에 0을 더해 ent [확인 필요]
는 3이 됨
12
• i+十에 의해 i=70| 되면 i<10이 참이 되어
반복문 실행
13 • Soojebi(7)을 호줄
02 〜 09
• num=7이= if(7 % 2==0), if(7 % 3==0),
if(7 % 4==0), if(7 % 5=0), if(7 % 6==0)
모두 거짓이 되어 if 문 안의 return 0을 실
행하지 않아 return 1을 반환
13 • Soojebi(7)은 1이므로 ent에 1을 더해 ent는 [확인 필요]
4가됨
12
• i++에 의해 i=80| 되면 i<10이 참이 되어
반복문 실행
13 • Soojebi(8) 을 호출
02〜 09 • num=8이므로 if(8 % 2=0)이 참이 되어 if
문 안의 return 0을 반환
13 • Soojebi(8)은 0이므로 ent에 0을 더해 ent [확인 필요]
는 4가됨
12 • i++에 의해 i=9가 되면 i<10이 참이 되어
반복문 실행
13 • Soojebi(9) 를 호출
천기누설 예상문제 6-145
## Page 332

02 〜 09
• n니m三9이므로 if(9 % 2==0)는 거짓이지만, [확인 필요]
if(9 % 3==0)0| 참이 되어 if 문 안의 return
0을 반환
13 • Soojebi(9)는 0이므로 ent에 0을 더해 ent [확인 필요]
는 4가됨
12
• i++에 의해 i=|()이 되면 i<io이 거짓이 [확인 필요]
되어 반복문 종료
14 • ent 값인 4> 출력
02 다음은 C언어 코드이다. 1에서 6 사이에 숫자
를 10번 임의로 생성한 값을 hist라는 배열에 [확인 필요]
저장하고, 1에서 6까지 몇 번 발생했는지 출력
하는 코드를 ①, ② 밑줄친 부분을 채워 완성하
시오.
#include<stdio.h>
#include<stdlib.h>
ffinclude <time.h>
int main(){
int hist[6]={0,};
int n, i=0;
srand(time(NULL));
do{
i++;
n=rand( )%6+1;
hist[ ① ]+=1;
} while(i<10);
for(i=:0;i<6;i++)
printf("[%d] 발생 횟수=%d\n", i+1, ② );
return 0;
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
①___________________________________________________________________________________
②___________________________________________________________________________________
너 Xu 서 서 ______
L1리 05 • m기n 함수부터 실행 [확인 필요]
06
• 크기가 6인 1차원 정수 배열 hist를 선언하 [확인 필요]
고 0으로 초기화
07 • 정수형 변수 n를 선언
• 정수형 변수 녀를 선언하고 0으로 초기화
08 • time 함수에서 구해온 시간 값을 srand 함수
의 파라미터로 전달하여 랜덤한 값을 생성
11 • i 값을 1 증가시킴
12
• 랜덤 함수에서 생성한 값을 6으로 나눈 나
머지와 1을 합한 값을 n에 대입
• 랜덤 값을 6으로 나누면 0~5 중 1개의 숫자
가 나= 해당 숫자에 1을 더하면 1~6 중
1개의 숫자가 됨
13
• hist는 int 형 6개의 배열이고, 랜덤 숫자는 [확인 필요]
1〜6이므로 n에서 1을 뺀 값의 번지를 1 증
가시킴
• hist 배열은 n너이라는 랜덤 숫자가 몇 번 나
왔는지를 표시
• i가 10미만일 때까지 반복하= do 〜 while
문은 총 10번 반복
• n 값이 5, 2, 4,1, 5, 4, 4, 5, 6, 2이라고 가정
하면 다음과 같이 수행
i n hist[n—1]
10〜14
1 5 hist[4]=1
2 2 hist[1]=1
3 4 hist[3]=1
4 1 hist[이=1
5 5 hist[4]=2
6 4 hist[3]=2
7 4 hist[3]=3
8 5 hist[4]=3
9 6 hist[5]=1
10 2 hist[1]=2
hist[O] hist[1] hist[2] hist[3]hist[4] hist[5]
1 2 0 3 3 1
16〜17 • 느 0부터 6보다 작을 때까지 1씩 증가하며
hist 배열의 값을 화면에 출력
F하
02. ① n-1, ② hist[i]
6-146 VI 프로그래밍 언어 활용
## Page 333

03 다음은 C언어 코드이다. 출력 결과를 보고 밑
줄친 곳에 들어갈 가장 적합한 답을 쓰시오.
(단, 밑줄에 ch 변수를 사용해야 한다.)
01 ffinclude<stdio.h>
02 int main() {
03 char ch, str[ ]="12345000";
04 int i, j;
05
06 for(i=0;i<8;i++) {
07 ch=str[i];
08 if(__)
09 break;
10 }
11
12 for(j=0;j<i;j 十+){
13 i--;
14 ch=str[j];
15 str[j]=str[i];
16 str[i]=:ch;
17 }
18
19 printf("%s", str);
20 return 0;
21 }
[출력 결과]
54321000
r:리 02 • main 함수부터 실행
03
• ch 변수 선언
• 문자열 타입 배열 변수 str을 선언하고 [확인 필요]
"12345000"로 초기화
04 • i, j 변수를 선언
06 〜 10
• for 문에서 너는 0부터 8보다 작을 때까지
i 값을 1씩 증가시키며 str[i] 값을 ch에 대입 [확인 필요]
i 0 1 2 3 4 5 6 7
str 1 2 3 4 5 0 0 0
• 다음 for 문(12~16라인)에서 str[i]와 str[j]를
교환하고, strO| "12345000"에서 "54321
000"으로 바뀌어야 하기 때문에 0이 시작
할 때의 번지에 해당하는 i 값을 반환해주어
야 함(값은 5가 될 때 if문을 만족해서 break를 [확인 필요]
만나 반복문을 종료해야 함)
12〜16
for문은 j값이 0부터 보다 작을 때까지 반 [확인 필요]
복을수행
str[j] 값을 ch에 대입하고 str[i] 값을 str[j] [확인 필요]
에 대입하고 ch값을 str[i]에 대입하여 두 [확인 필요]
값을 교환
j 0 1 2
i 4 3 2
str[j] str[이너 str[1]=2 str[3]=3
str[i] str[4]=5 str[3]=4 str[2]=3
str 52341000 54321000 54321000
j가 301 될 때 j<i 조건이 거짓이 되어 반복
문을 종료
19 • 화면에 str 배열의 값인 "54321000"을 출력
04 다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 include<stdio.h>
02 include<string.h>
03 int main(){
04 charstr1[2 이:="K0REA";
05 char str2[20]="LOVE";
06 char* p1=NULL;
07 char* p2=NULL;
08 p1:=str1;
09 p2=str2;
10 Str1[1]=p2[2];
11 str2[3]=p1[4];
12 strcat(str1, str2);
13 printf("%c",*(pl+2));
14 return 0;
15 }
표수
03. ch='O' 04. R
천기누설 예상문제 6-147
## Page 334

LL리 04 • 크기가 20인 배열 str1 을 선언 [확인 필요]
05 • 크기가 20인 배열 str2를 선언
06 • 포인터 변수 p1 을 선언
07 • 포인터 변수 p2를 선언
08
• p1 에 str1 의 시작 주소값(&str1[이)을 저장(str1
배열을 포인터 山에 대입하면 山은 str1 배열처럼
사용할 수 있음)
09
• p2에 str2의 시작 주소값(&str2[이)을 저장
(str2 배열을 포인터 p2에 대입하면 p2는 str2
배열처럼 사용할 수 있음)
10 • Str1[1]에 p2[2]의 값 "V"를 저장
11 • str2[3]에 p1[4]의 값 "A"를 저장
12
• strcat으로 문자열 strl 에 str2를 붙임 [확인 필요]
("KVREALOVA")
13
• p1 은 &str1[이이고, p1+2는 &str1[2]
• P1+2 가진 값인 "R"을 출력
Of 다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 #include<stdio.h>
02 int main(){
03 int arr[2][3]={1, 2, 3, 4, 5, 6};
04 int (*p)[3]=NULL;
05 p=arr;
06 printf("%d", *(p[이+1)+*(p[1]+2));
07 printf("%d", *(*(p+1)+0)+*(*(p+1)+1));
08 return 0;
09 }
03 • 2x3 크기의 2차원 배열 생성
04
• P라는 배열 포인터 선언, p라는 포인터는
p[x][3] 크기의 배열을 가리킬 수 있음
05
• arr 배열을 포인터 p에 대입함
•P는 arr 배열처럼 사용할 수 있음
06
• *(p[0]+1)은 *(arr[이+1)과 같은데, *(arr[0]+1)
은 arr[이[이에서 1번째 뒤에 있는 arr[0][1]
의 값 2를의미
• *(p[1]+2)는 *(arr[1]+2)와 같은데, *(arr[1]+2)
는 arr[1][이에서 2번째 뒤에 있는 arr[1][2]
의 값 6을의미
• *(p[0]+1)+*(p[1]+2) 인 8을 출력
07
• *(arr+1)은 arr[l]과 같으므로 *(*(p+1)+0)
은 *(arr[1]+0)과 같음
• *(arr[1]+0)은 arr[1][0]의 값인 4를 의미
• *(arr+1)은 arr[1]과 같으므로 *(*(p+1)+1)은
*(arr[1]+1)과 같음
• *(arr[1]+1)은 arr[1][1]의 값인 5를 의미
• *(*(p+1)+0)+*(*(p+1)+1)인 9를 출력
06 다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 #include<stdio.h>
02 int main(){
03 int n1=1, n2=2, n3=3;
04 int r1, r2, r3;
05 r1=(n2<=2) || (n3>3);
06 r2=!n3;
07 r3=(n1>1)&&(n2<3);
08 printf("%d", r3—r2+r1);
09 return 0;
10 }
|하규|•C언어에서 00| 아니면 참, 0이면 거짓으로 인식하고, [확인 필요]
계산한 결과는 참이면 1로, 거짓이면 0이 된다.
03
• 정수형 변수 n1 은 1, n2은 2, n3은 3으로 초
기화함
04 • 정수형 변수 r1, r2, r3 선언함
05
• n2<=2는 참이고, n3>3은 거짓이므로 (참
II 거짓) 이기 때문에 참이 되어 r1은 1이 됨
06
• n3는 3이므로 참이기 때문에!(NOT) 연산을
하면 거짓이 되므로 r2는 0이 됨
07
•n1>1은 거짓이고, n2<3은 참이므로 (거짓
&& 참)이기 때문에 거짓이 되어 r3는 0이 됨
08 • r3는 0, r2는 0, ri은 1이므로 1이 출력됨 [확인 필요]
6-148 VI 프로그래밍 언어 활용
## Page 335

■ 다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 include<stdio.h>
02
03 int fn(char* a){
04 int i=0;
05 for(i=0;a[i] !:='\0';i++);
06 return i;
07 }
08
09 int main() {
10 char a[10]="Hello";
11 printf("%d", fn(a));
12 return 0;
13 }
Ei ।
I 09 • main 함수부터 시작
10 • "Hello'1 라는 문자열을 a라는 변수에 저장
11 • fn(a)를 호출하고, "Hello" 문자열의 시작 주
소인 a를 전달
03 • fn 함수에서 a는 "Hello" 문자열의 시작 주소
04 • i 변수를 선언
05
• for 문 끝에 세미콜론이 있으므로 for 문 조
건을 만족했을 때의 실행할 명령어가 없는
반복문 형태로 다음과 같음
for(i=0;a[i] !='\0';i++){ }
•i=0 이 되고수[i] !='\0'을만족할때까지 반복
i a[i] a[i]!='\0'
0 a[이='H' 참
1 a[1]='e' 참
2 a[2]:니' 참
3 a[3]=T 참
4 a[4]='o' 참
5 a[5]='\0' 거짓
• i가 5일 때 조건식이 거짓이 되므로 반복문
을종료
6 • return 드에 의해 5를 반환
11 • 반환 값인 5를 출력
08 다음은 C언어 코드이다. 출력 결과를 쓰시오.
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
include <stdio.h>
struct st{
int a;
int c[10];
};
int main(){
int i=0;
struct st ob1;
struct st ob2;
ob1.a=0;
ob2.a=0;
for(i=0;i<10;i++){
ob1.c[i]=i;
ob2.c[i]=ob1.c[i]+i;
}
for(i=0;i<10;i늬+2){
ob1.a=ob1.a+ob1.c[i];
ob2.a=ob2.a+ob2.c[i];
printf("%d", ob1.a+ob2.a);
return 0;
07. 5 08. 60
천기누설예상문제 6-149
## Page 336

벼설 I
i 02〜05 • 구조체 st를 정의함 [확인 필요]
06 • main 함수의 시작 부분(프로그램이 제일 처
음 실행되는 부분)
07 • 정수형 변수 에 0을 초기화
08 • ob1 이라는 st 구조체 생성
09 • ob2라는 st 구조체 생성
10 • ob1 구조체 안에 a 변수를 초기화
11 • ob2 구조체 안에 a 변수를 초기화
13〜16
< = 0부터 i = 9까지 반복문을 수행하면서
ob1.c[i]라는 값에 i를 넣고, ob2.c[i]에 ob1.
c[i]와 昌 더한 값을 저장
• for(i=0;i<l0;i++)를 실행한 후의 ob1, ob2
의 c 값은 다음과 같다.
cP] c[1] C[2] c[3] C[4] c[5] c[6] C[7] c[8] cP]
ob1 0 1 2 3 4 5 6 7 8 9
ob2 0 2 4 6 8 10 12 14 16 18
i=0부터 i=9까지 반복문을 수행하는데, 증
감식이 i늬+2이므로 i가 0, 2, 4, 6, 8일 때
반복
i obta ob1.c[i] otrl.a ob2.a ob2.c[i] ob2.a
18〜21
0 0 0bl.c[이=0 0 0 ob2.c[이=0 0
2 0 ob1.c[2]=2 2 0 ob2.c[2]=4 4
4 2 ob1.c[4]=4 6 4 ob2.c[4]=8 12
6 6 ob1.c[6]=6 12 12 ob2.c[6]=12 24
8 12 0bl.c[8] 三 8 20 24 ob2.c[8] 더6 40
09 다음은 C언어 코드이다. 출력 결과를 쓰시오.
(답안의 점선은 답을 쓸 수 있도록 하기 위한 가
상의 선으로 실제 출력되지 않음, 정답란에 1칸
은 공백 3칸)
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
#include <stdio.h>
void Show(int a[ ][6]) {
int i, j;
for(i=0;i<=4;i++) {
for(j=5;j>=0;j—) {
if(i=0 || i==4 || j==O || j==5)
printf("%3d", a[i][j]);
else
printf(" ");//공백 3칸
}
printf("\n");
}
}
int main() {
int a[5][6]={{24, 25, 26, 27, 28, 29},
{18, 19, 20, 21, 22, 23},
{12, 13, 14,15,16,17},
{6, 7, 8, 9,10, 11},
{0, 1, 2, 3, 4, 5}};
Show(a);
return 0;
• obl.a값 20과 ob2.a값 40을 더한 60을 화
면에 출력함
29 28 27 26 25 24
23 18
17 12
11 6
5 4 3 2 1 0
6-150 VI 프로그래밍 언어 활용
## Page 337

I
I 14 • main 함수부터 시작
15〜19 • 5행 6열의 2차원 배열 a를 선언하고 초기화
20 • Show 함수 호출
02 • Show 함수는 2차원 배열을 입력받아 행렬
을 출력하는 함수
04 〜 12
• 5행 6열의 배열을 받기 위한 형태로 2개의
for문을 사용하여 처리 [확인 필요]
• 조건문을 통해 i의 값이 0, 4이거나, j의 값
이 0, 5인 경우에는 a[i][j]의 값을 출력하고,
그렇지 않을 경우 공백 3칸을 출력한 뒤 두
번째 for문의 마지막에 개행을 출력 [확인 필요]
10 다음은 C언어에서 피보나치 수를 구하는 함수
를 구현하려고 한다. 밑줄 친 곳에 알맞은 코드
를 작성하시오.
피보나치 수는 처음 두 항을 1과 1로 한 후, 그 다음
항부터는 바로 앞의 2개의 항을 더해 만드는 수이다.
fn(0)=0, fn(1)=1, fn(2)=1, fn(3)=2,
01 #include <stdio.h>
02 int fn(int n){
03 if(n==0)
04 return 0;
05 else if(n=1)
06 return ① ;
07 else
08 return ② ;
09 }
10 int main(){
11 printf("%d", fn(8));
12 return 0;
13 }
區|.fn이라는 함수는 피보나치 수열을 계산하는 함수로 [확인 필요]
n0| 1일 때, 첫 번째 수열 값인 10| 반환되어야 한다.
• n이 1일 때 else if(n=l)에 있는 return0| 실행되고,
1을 반환해야 하므로 return 10| 되어야 한다.
• n0| 2 이상일 때 else에 있는 return이 실행되고, 피보 [확인 필요]
나치 수열은 앞의 2개 항을 더한 수이므로 바로 앞의
값인 fn(n너)과 앞의 앞 값인 fn(n-2)를 더한 값을 반
환해야 한다.
11 다음은 c언어 코드이다. 출력 결과를 쓰시오.
01 include <stdio.h>
02 union Number {
03 int i;
04 float f;
05 };
06 struct Data {
07 union Number x;
08 union Number y;
09 char z;
10 };
11 void func(struct Data *a) {
12 if (a->z) {
13 a—>x.i+=a—>y.f;
14 }
15 else {
16 a—>x.f+=a—>y.f;
17 }
18 }
19 int main() {
20 struct Data a={{.i=5}, {.f=3.5}, 1};
21 func(&a);
22 printf("%d\n", a.xj);
23 return 0;
[출력 결과]
21
① 三 스
②________________________ _
10. ① 1, ② fn(n—2)+fn(n—1) 11. 8
천기누설 예상문제 6-151
## Page 338

E'흐
। 느
19 • main 함수부터 시작
20
• Data 구조체 타입의 a 변수에서 a.x.i는 5,
a.y.f는 3.5, a.z는 1로 초기화
x 으으구!으으—5으으
.......... ,- ,.______ , .-…-.-그- ■그,__ _______________________
y 「―厂 3.5 I
a Z 1
21 • a 변수의 주소값을 tunc 함수에 전달
11 • func 함수에서 a 포인터 변수에 main 함수
의 a 변수 주소값을 대입
12
• a->z는 main 함수의 a 변수 안의 z 값이므
로 1
• if(a->z)는 if(1)이므로 if 문이 참이 되어 if 문
안의 명령어를 실행
13
• a->x는 main 함수의 a 변수 안의 x 값이므로
5이고, a->x.i도 int 형이므로 그대로 5가 됨
• a->y.f는 3.5이므로 a->x.인 5에 3.5를 더
하면 정수끼리 연산이므로 a->x.i는 801 됨
22 • a.x.i 는 8이므로 8을 출력
12 다음은 C언어 코드이다. 출력 결과를 쓰시오.
01 #include <stdio.h>
02 int main(){
03 int x[4]={2, 3}, i;
04 if (x[2]=x[이>x[1] ?
(x[1]>x[2]?x[1]:x[2]):(xM>x[2]?)《)]:x[2])){ [확인 필요]
05 4이 «=2; [확인 필요]
06 }
07 else {
08 x[1] «=2; [확인 필요]
09 }
10 for(i=0;i<4;i++)
11 printf("%d", x[i]);
12 return 0;
13 }
iu,,a 02 • main 함수부터 시작
03 • X 배열 초기화,i 변수 초기화
04
• 연산자 우선순위에 따라 삼항 연산자를 먼
저실행
• x[이은 2이고 x[1]은 3이므로, X[이>x[1]은
거짓이기 때문에 (x[0]>x[2] ? x[0]:x[2])가 됨
•><[이은 2이고><[2]은 0이므로, x[0]>x[2]는
참이기 때문에 X[이이 됨
• x[2]=x[이이므로 x[이 값인 2를 x[2]에 대입
• if(x[2])는 if(2)이므로 if 문이 참이 되어 if 문
을실행
05
• x[이은 2이므로 2진수로 10
• 2진수 10을 왼쪽으로 2비트 시프트하면
10000| 되고, 2진수 1000을 10진수로 변
환하면 801 됨
• x[이=8이 됨
10 • i=0부터 i<4를 만족할 때까지 반복하므로
i=0,1, 2, 3일 때 for 문을 반복
11
• i=0일 때 x[이 값인 8을 출력하고, i=1 일
때 x[1] 값인 3을 출력, i=2일 때 x[2] 값인
2를 출력, i=3일 때 x[3] 값인 0을 출력
6-152 VI 프로그래밍 언어 활용
## Page 339

1뼌J 자바 | Level | [확인 필요]
o 자바기본구조 ★
|쯔) . >外잠1간! 알고가기 [확인 필요]
• Java에서 모든 소스 코드는 클래스 단위로 구성된다. [확인 필요]
• 프로그램은 public static void main부터 시작한다. [확인 필요]
개 념 박살내기 자바기본 코드
클래스 Class
• 객체 지향 관점에서 객
체(Object)를 정의하는
틀로서 많은 객체 지
향 프로그래밍 언어의
기본구조이다.
•클래스는 변수(Vari-
able)와 메서드(Method)
로 구성된다.
?!
오 $
[소스코드]
01 public class Soojebi {
02 public static void main(String[ ] args){
03 System.out.println("Hello");
04 }
05 }
출력 Hello
[코드 해설]
01
• Soojebi 클래스 생성
• 클래스 이름이 Soojebi이면 소스 코드에 대한 파일 이름은 SoojebLjava가 [확인 필요]
되어야 함
02 • main 함수의 시작 부분(프로그램이 제일 처음 실행되는 부분)
03 • Hello라는 문자열을 printin이라는 함수를 이용해 출력 [확인 필요]
Q 자료형 ★★
(1) 자료형(Data Type)의 개념
• 자료형은 프로그래밍 언어에서 @(저주 자료형과 같은 여러 종류의
데이터를 식별하는 형태이다.
• 메모리 공간을 효율적으로 사용하고 A진수 데이터를 다양한 형태로 사
용하기 위해 존재한다.
Chapter 03 자바 6-153
## Page 340

⑵ 자료형의 유형
• 자료형은 기본 자료형, 참조 자료형 이 있다.
D 기본 자료형(Primitive Type)
• 기본 자료형은 정수,' •실수, 문자, 논리값과 깉은 기본 데이터를 저장하
는 간단한 데이터 타입이다.
• 크기가 고정되고 nulT값을 가질 수 없다. - [확인 필요]
• 별도의 초기화가 없으면 논리형으 false를 정수형은 0, 실수형은 0.0으 [확인 필요]
.   .....-   " ' - '…•-- 1—- ■
로, 문자형은'\u0000'로 초기화한다.
▼ 기본 자료형 종류
구분 설명 타입 크기
논리형 • 참(true)과 거짓(false)을 저장하는 자료형 boolean 1 바이트
정수형 • 정숫값을 저장하고자 할 때 人요하는 자료형
byte 1 바이트
short 2 바이트
Jnt 4 바이트
long 8 바이트
실수형
• 소수점을 포함하는 실숫값을 저장하고자 할 때 사
용하는 자료형
float 4 바이트
double 8 바이트
문자형 • 문자 하나를 저장하고자 할 때 사용하는 자료형 char 2 바이트
▽,유 '漆
酸!
참조형은 C언어에서 포
인터와 비슷한 개념이
라고 보시면 됩니다. 예
를 들어 C언어에서 int
a[5];와 같이 배열을 선
언하면 a 자체는 주소값
인 것처럼, 자바에서도
int a[ ]=new int[5];와
같이 배열을 선언하면 a
자체는 주소값입니다.
0 참조 자료형(Reference Type) 盤£創 [확인 필요]
• 참조 자료형은 객체를 참조하는 변수이다.
• 값이 저장되어 있는 곳의 주소값을 저장하는 공간이다.
• 기본 자료형을 제외한 모든 타입이 참조 자료형 이다.
▼ 참조 자료형 종류
타입 설명
배열 (Array) • 같은 타입의 변수들로 이루어진 집합
클래스 (Class)
• 객체 지향 프로그래밍에서 특정 객체를 생성하기 위해 변수와 메
서드를 정의하는 틀
인터페이스 (Interface) • 클래스가 구현해야 하는 메서드의 선언만을 포함하는 형태
/
열거 (Enumeration) • 서로 관련 있는 상수들의 집합을 정의할 때 사용하는 형태
6-154 VI 프로그래밍 언어 활용
## Page 341

|禍0개 념 박살내기 자바 참조자료형
[소스코드]
01 public class Soojebi {
02 public static void main(String[ ] args){
03 int a[ ]=new int[ ] {1, 2, 3, 4};
04 int b[ ]=new int[ ] {1, 2, 3, 4};
05 int c[ ]=new int[ ] {1, 2, 3};
06 System.out.println(a==b);
07 System.out.println(a==c);
08 System.out.println(b=c);
09 }
10 }
false
출력 false
false
[코드 해설]
02 • main 메서드부터 실행
03 • a 배열은 1, 2, 3, 4를 초기화
04 • b 배열은 1,2, 3, 4를 초기화
05 •c 배열은 1, 2, 3을 초기화
06 • a와 b는 주소가 다르므로 false
07 • a와 c는 주소가 다르므로 false
08 • b와 c는 주소가 다르므로 false
(所 변수 ★★★
(1) 변수(Variable)의 개념
• 변수는 저장하고자 하는 어떠한 값이 있을 때, 그 값을 주기억장치에
기억하기 위한공간이다.
(2) 변수 유효범위(Variable Scope)
Q 클래스 변수(Class Variable)
• 클래스 변수는 클래스 블록에 선언하는 변수이다.
F 잠간! 알고가기
블록 Block
자바에서 중괄호로 묶은
부분이다.
Chapter 03 자바 6-155
## Page 342

• 클래스 변수는 클래스가 시작되면 변수가 생성되고, 클래스가 종료되
면 변수가 소멸된다.
• 클래스 변수는 클래스 내에서 사용할 수 있다.
두J 박살내기 자바클래스변수
[소스코드]
01 public class Soojebi {
02 int a=5;
03 void fn(){
04 a=a+3;
05 }
06 public static void main(String[ ] args){
07 Soojebi s=new Soojebi( );
08 s.a=s.a+5;
09 s.fn( );
10 System.out.println(s.a);
11 }
12 }
출력 13
[코드 해설]
02
• a라는 변수에 5를 대입
• a는 클래스 변수
06 • main 함수부터 시작
07 • Soojebi 클래스를 s라는 변수에 생성
08
• s의 a는 5가 저장되어 있0므루 5+5는 10이 되고, 10을 s의 a라는 변수
에 저장
09 • s의 fn 사용자 정의 함수를 호출
03 • fn 함수 호출
04 • a는 10이 저장되어 있으므로 10+3은 13이 되고, 13을 a라는 변수에 저장
10 • s의 a는 13이므로 13을 출력
0 지역 변수(Local Variable)
• 지역 변수는 블록 내에서 선언하는 변수이다.
• 지역 변수는 블록이 시작되는 부분에 바로 선언해주어야 하고, 중괄호
가 닫히는 시점에 소멸된다.
6-156 vi 프로그래밍 언어 활용
## Page 343

• 지 역 변수는 해당 블록 안에서만 사용할 수 있다.
[소스코드]
박살내기 자바 지역 변수
01
02
03
04
05
06
public class Soojebi {
public static void main(String[ ] args){
int a=3;
System.out.println(a);
}
}
R2오
#
Oto
출력
[코드 해설]
02 • main 함수부터 시작
03
• a라는 변수에 3을 저장
• a는 지역 변수
04 • a에 저장된 3을 출력
H static 변수(Static Variable) 21 년 2회 , 3 회
•서}수는 변수설언할때 static 이라는..키워드를부여준다.
• st狂丁벼^ 프로그램이 시작되면 변수각생성되고, 프로그램이 종료
▼우 - f — ll». I,———»^^^—^*********^***^"*^** —— , , ■■■스—■■■으_ . _ [확인 필요]
되며 변수가 소멸된다.
• 平*변추는 프로그램 전체에서 사용할 수 있다.
뛔 그뎜 박살내기 자바 static 변수
[소스코드]
01 class Soojebi {
02 static int count=0;
03 }
04 public class SoojebiMain {
05 public static void main(String[ ] args){
06 Soojebi s=new Soojebi( );
07 s.count++;
08 System.out.println(s.count);
09 s.count++;
10 System.out.println(s.count);
11 }
12 }
3
히薦@1
Chapter 03 자바 6-157
## Page 344

&스*1酸!
• 초기화는 int a=3; 과 같
이 변수가 어떤 자료형
을 사용하는지 선언할
때 넣어주는 값을 말
하는데, 초기화는 처음
한 번만 수행합니다.
• static 변수는 프로그램
이 종료될 때까지 소멸
되지 않기 때문에「C언
어 static 변수」예시처
럼 여러 번 지나는 경
우가 있습니다. 이런 경
우에도 초기화는 처음
한 번만 수행합니다.
[코드 해설]
05 • main 함수부터 시작
06 • Soojebi 클래스 객체 s 생성
02 • s의 count 변수는 0으로 초기화
07 • s의 count 값을 1 증가시켜 s.count는 10| 됨 [확인 필요]
08 • 화면에 s의 count 값을 출력함
09 • s의 count 값을 1 증가시켜 s.count는 2가 됨 [확인 필요]
10 • 화면에 s의 count 값을 출력함
0 배열 ★★★
(1) 배열(Array) 개념
• 배열은 같은 타입의 변수들로 이루어진 집합이다.
⑵ 배열 선언
0 1차원 배열 선언
▼ 1차원 배열 선언
구분 선언
자료형 [ ]배열명=new 자료형[배열_요소_개수];
초깃값이 없는 경우 _ ____ ___ __________________ _ .
자료형 배열명[ ]=new 자료형[배열_요소_개순];
초깃값이 있는 경우 자료형 [ ]배열명={초깃값};
• 배열 요소 개수에 정의된 숫자만큼 같은 타입의 데이터 공간이 선언된다.
• 배열 요소 개수를 명시하지 않고 초깃값이 정의되어 있을 경우 초깃값
개수만큼 공간이 선언된다.
• 초깃값을 선언하지 않을 경우 정수일 때는 0, 실수일 때는 0.0, 문자열
일 때는 NULL이 저장된다. [확인 필요]
• 불린, 문자, 정수, 실수 등을 배열로 선언할 때 사용한다.
6-158 VI 프로그래밍 언어 활용
## Page 345

• 자바에서 배열의 크기를 구할 때는 length 속성을 사용한다.
■내기 자바 1차원 배열 length 속성
[소스코드]
01 public class Soojebi {
02 public static void main(String[ ] args){
03 int [ ]a=new int[3];
04 System.out.println(a.length);
05 }
06 }
출력 3
[코드 해설]
03 • int 형 변수 3개 선언
04 • a 배열의 개수를 출력
VIH
H1J
IJ2=
O°2!
오 w
oto
0 2차원 배열 선언 圓
▼ 2차원 배열 선언
구분 선언
초깃값이 없는 경우
자료형 [ ][ ]배열명=new 자료형[행의 개수][열의 개수];
자료형 배열명[ ][ ]=new 자료형[행의 개수][열의 개수];
초깃값이 있는 경우 자료형 [ ][ ]배열명={{초깃값}, {초깃값}, "■};
개 념 박살내기 자바 2차원 배열 length 속성 EW
[소스코드
01 public class Soojebi {
02 public static void main(String[ ] args){
03 int[ ][ ] a=new int[3][2];
04 System.out.println(a.length);
05 System.out.println(aK)].length);
06 }
07 }
출력 3
2
Chapter 03 자바 6-159
## Page 346

[코드 해설
03 •int 형 변수 3x2개 선언
04 • a 배열의 행의 개수를 출력
05 • a[이 배열의 개수를 출력
뎔 박살내기 자바 2차원 배열 length 속성사용
[소스코드]
01 public class Soojebi {
02 public static void main(String[ ]args){
03 int [ ][ ]a={{1, 2}, {3}, {4, 5, 6}};
04 System.out.println(a.length);
05 System.out.println(a[이.length);
06 System.out.println(a[1].length);
07 System.out.println(a[2].length);
08 }
09 }
3
출력 2
1
3
[코드 해설
03 • int 형 2차원 배열 선언
04 • a 배열의 행의 개수를 출력
05 • a[이 배열의 개수를 출력
06 • a[1] 배열의 개수를 출력
07 •a[2] 배열의 개수를 출력
6-160 VI 프로그래밍 언어 활용
## Page 347

0 표준 입출력 함수 ★★★
(1) 표준 줄력 함수 smi
• 표준 출력 함수는 print, printin, printf 함수가 있다.
▼ 표준 출력 함수
함수 설명
System.out.print() • 개행을 하지 않는 출력함수
System.out.println() • 개행을 하는 출력함수
System.out.printf() • C 언어처럼 변수를 출력할 수 있는 출력 함수
VIH
HUZ12_-
O°
E2오
*
010
M 5포 박살내기 자바표준출력 함수
[소스코드]
01 public class Soojebi {
02 public static void main(String[ ]args){
03 int a=100;
04 System.out.print("Hello\n");
05 System.out.println("Hello");
06 System.out.printf("%d", a);
07 }
08 }
Hello
출력 Hello
100
[코드 해설
03 • 변수 a에 100을 대입
04 • H에o 값을 출력한 후에 이스케이프 문자인 \n을 만나고 개행 [확인 필요]
05 • Hello 값을 출력하고 개행
06 • a 값을 %d(l0진수)로 출력
⑵ 표준 입력 함수
• 표준 입 력 함수는 readline 함수가 있다.
System.in.readLine()
Chapter 03 자바 6-161
## Page 348

• readLine은 입력장치(키보드)로부터 한 줄 전체를 읽는 함수이다. [확인 필요]
BufferedReader를 사' [확인 필요]
용하기 위해서는 java,
io.BufferedReader 를
import하|(야 흐고•, Input [확인 필요]
Stream Reader를 人요 [확인 필요]
하기 위해서는 java.io.
InputStreamReader 를
import해야 합니다. 또 [확인 필요]
한 코드에 추가하지 않
았지만 입력할 때는 예
외 처리를 해줘야 해서
main 메서드 선언한 후,
main 메서드 시작하기
바로 직전에 throws를 [확인 필요]
이용해 예외 처리를 해
주어야 합니다__ _
public static void
main(String[ ] args)
throws lOException {
( 1;'념 박살내기 자바표준출력함수
예외처리를 위한 10
Exception을 사용하 [확인 필요]
기 위해서는 java.io. 10
Exception을 import하| [확인 필요]
야 합니다. 자바 표준 입
력 함수 예제를 실제 돌
려보실 분들은 [소스 코
드]의 이줄 위에 다음 코
드를 입력해줘야 동작
하고, 04줄에 throws 10
Exception을 추가해주 [확인 필요]
셔야 합니다
['import java.
Ho.BufferedReader;
j import java.
po.InputStreamReader; j
limport java.
|i 이 OException;
[소스코드]
01 public class Soojebi {
02 public static void main(String[ ] args) {
03 String a 三 null;
04 BufferedReader r三
new BufferedReader(new InpiitStreamReader(System.in));
05 a=r.readLine( );
06
07 System.out.println(a);
08 }
09 }
입력 Hello
출력 Hello
[코드 해설]
03 • 문자열을 저장하는 변수 a를 선언 및 아니로 초기화
04
• system.in을 통해 한 글자씩 받은 후, InputStreamReader로 문자열로 변형 [확인 필요]
• BufferedReader의 객체인 르 결과를 받음 [확인 필요]
05 • Enter 키 입력 전까지 입력값을 a에 저장
07 • a에 저장된 값을 출력
쪼잠깐! [알고가기'
0 문자열 ★★★
(1) 문자열 생성
n 리터럴을 이용한 방식
• 리터럴을 이용한 방식은 String 변수에 문자열 리터럴을 저장한 주소
를 대입하는 방식이다.
String 변수명 = "문자열";
리터럴Literal [확인 필요]
소스 코드에서 고정된
값이나 데이터를 나타내
는 방식이다.
정수
리터럴 1, 2, 3 등
문자열
리터럴 "ABC" 등
6-162 VI 프로그래밍 언어 활용
## Page 349

• 리터럴 문자열은 문자열 풀에 저장되고, 같은 리터럴을 사용하는 변수
는 같은 문자열 풀을 가리키게 된다.
ED String a="abc";
— 리터럴 문자열 abc가 String Pool에 저장되고, a라는 변수는 String Pool에 저장 [확인 필요]
된 abc를 가리킴 [확인 필요]
ff『짐간!I
알고가기
S new를 이용한 방식 [확인 필요]
• new를 이용한 방식은 문자열 인스턴스를 생성하여 String 변수에 주 [확인 필요]
소값을 대입하는 방식이다.
String 변수명 = new String("문자열");
• String 인스턴스는 힙(Heap)에 저장되고, 변수는 힙에 저장된 인스턴스
의 주소를 대입하게 된다.
문자열 풀String Pool [확인 필요]
• 자바에서 문자열 리터
럴을 관리하기 위한 메
모리 영역이다.
•문자열 풀은 문자열
리터럴을 저장하고 중
복을 피하기 위해 사용
한다.
VI
IH
HIJI12=
O°
r2오
즈]( 개 념 박살내기 자바문자열생성
[소스코드]
01 public class Soojebi {
02 public static void main(String[ ] args){
03 String a="abc";
04 String b="abc";
05 String c:기new String("abc"); [확인 필요]
06 String d=new String("abc");
07
08 System.out.println(a);
09 System.out.println(b);
10 System.out.println(c);
11 System.out.println(d);
12 }
13 }
abc
춤려 abc
거 abc
abc
인스턴스라는 말이 어렵
게  다가올 수 있는데, 간
단하게  얘기하면 new로 [확인 필요]
생성된 객체가 인스턴스
입니다. new String("문
자열")을 이용하면 객체
가 만들어지는데, 그것
을 인스턴스라고 보시면
되겠습니다.
Chapter 03 자바 6" 1 63
## Page 350

[메모리 구조]
02 • main 메서드부터 실행
03~04 • a, 느라는 이름의 문자열 변수에 "abc" 문자열을 저장
05~06 • c, d라는 이름의 문자열 변수에 "abc"가 저장된 문자열 객체를 생성
08~11 • a, b, c, d 변수에 저장된 문자열 출력
⑵ 문자열 연산자
n + 연산자
• + 연산자는 문자열을 연결하는 연산자이다.
• 문자열과 문자열, 문자열과 정수, 문자열과 실수를 더하게 되면 문자열
이 된다.
s == 연산자
• == 연산자는 문자열의 주소값을 비교하는 연산자이다.
6-164 VI 프로그래밍 언어 활용
