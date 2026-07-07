---
type: Study Note
title: "Chapter 02: Linear Algebra (선형대수) - Complete Study Note"
description: "MML(Mathematics for Machine Learning)의 Chapter 2 'Linear Algebra' 전체 장에 대한 완벽한 국문 강의록입니다. 벡터 공간, 연립선형방정식의 해법, 기약 사다리꼴 행렬(RREF), 마이너스 1 트릭, 기저와 차원, 선형 사상과 기저 변환, 상(Image)과 핵(Kernel), 그리고 아핀 공간까지의 모든 개념과 엄밀한 수식 유도, 시각 자료 묘사를 수록합니다."
tags: [mml, math, linear-algebra, study-note, gaussian-elimination, vector-space, linear-mapping, basis-change]
timestamp: 2026-06-18
status: active
---

# 2. 선형대수 (Linear Algebra)

직관적인 개념을 공식화할 때 흔히 사용하는 접근법은 **대상(Symbols)의 집합**과 이 대상들을 **조작하는 규칙(Rules)의 집합**을 구축하는 것입니다. 이를 **대수(Algebra)**라고 부릅니다. **선형대수(Linear Algebra)**는 벡터(vectors)와 벡터를 조작하는 특정 대수적 규칙을 연구하는 학문입니다. 

고등학교 수학이나 물리학에서 흔히 마주하는 벡터는 화살표 기호가 올려진 문자($\vec{x}$, $\vec{y}$)로 표기되는 **"기하학적 벡터(geometric vectors)"**입니다. 본서에서는 보다 일반적인 벡터 개념을 다루며, 이를 표현하기 위해 볼드체 소문자($\mathbf{x}$, $\mathbf{y}$)를 사용합니다.

추상적인 수학 관점에서 벡터는 **서로 더해질 수 있고(addition)**, **스칼라와 곱해져(scalar multiplication)** 동일한 종류의 또 다른 객체를 만들어낼 수 있는 특별한 대상을 뜻합니다. 이 두 가지 성질(덧셈과 스칼라 곱에 대한 닫힘성)을 만족하는 대상이라면 무엇이든 벡터로 간주될 수 있습니다.

---

### 벡터의 네 가지 예시

1. **기하학적 벡터 (Geometric vectors)**:
   * 기하학적 벡터는 방향과 크기를 가진 유향 선분(directed segments)으로, 최소 2차원 공간 상에 그려서 시각화할 수 있습니다. 
   * 두 기하 벡터 $\vec{x}$와 $\vec{y}$를 더해 생성된 $\vec{x} + \vec{y} = \vec{z}$ 역시 또 다른 기하 벡터입니다. 또한 스칼라 $\lambda \in \mathbb{R}$와의 곱인 $\lambda \vec{x}$ 역시 원래 벡터의 길이를 $\lambda$배만큼 조정한 기하 벡터입니다. 
   * 이 벡터 해석은 우리가 방향과 크기에 대한 직관을 발휘하여 수학적 연산을 추론할 수 있게 돕습니다.
2. **다항식 (Polynomials)**:
   * 다항식 역시 훌륭한 벡터입니다. 임의의 두 다항식을 더하면 또 다른 다항식이 되며, 다항식에 실수 $\lambda \in \mathbb{R}$를 곱한 결과 역시 다항식입니다.
   * 다항식은 구체적인 선 형태의 기하학적 그림이 아니라 고도로 추상적인 대수 구조이지만, 덧셈과 스칼라 곱 규칙을 보존하므로 수학적으로 완벽한 벡터입니다.
3. **오디오 신호 (Audio signals)**:
   * 오디오 신호는 연속된 숫자의 나열(시계열 데이터)로 표현됩니다. 두 오디오 신호를 합치면(소리의 중첩) 새로운 오디오 신호가 생성되며, 오디오 신호의 볼륨을 조절하는 것(스칼라 곱) 역시 여전히 오디오 신호입니다. 따라서 오디오 신호 또한 벡터의 일종입니다.
4. **$\mathbb{R}^n$의 원소 (실수 $n$-튜플)**:
   * $\mathbb{R}^n$은 다항식보다 더 추상적이며, 본서에서 가장 집중적으로 다루는 개념입니다. 예를 들어, 3차원 공간의 원소인 다음과 같은 3개의 실수 묶음(triplet)을 들 수 있습니다:
     $$\mathbf{a} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \in \mathbb{R}^3$$
   * 두 벡터 $\mathbf{a}, \mathbf{b} \in \mathbb{R}^n$을 성분별로(component-wise) 더한 결과 $\mathbf{a} + \mathbf{b} = \mathbf{c} \in \mathbb{R}^n$ 역시 벡터이며, 실수 $\lambda \in \mathbb{R}$를 곱한 $\lambda \mathbf{a} \in \mathbb{R}^n$ 또한 스케일링된 벡터입니다.
   * 데이터를 $\mathbb{R}^n$의 원소로 간주하는 방식은 컴퓨터 상의 **실수 배열(array)** 개념과 거의 일대일로 매핑되므로, 대다수 프로그래밍 언어에서 다차원 배열 연산을 활용하여 매우 편리하게 알고리즘으로 구현할 수 있다는 커다란 장점이 있습니다.

선형대수는 이러한 서로 다른 벡터 개념들 사이의 **공통 대수 구조**를 규명하는 데 주안점을 둡니다. 본서에서는 무한 차원이 아닌 **유한 차원 벡터 공간(finite-dimensional vector spaces)**에 초점을 맞추며, 이 경우 임의의 벡터 객체와 $\mathbb{R}^n$ 사이에는 항상 일대일 대응(Isomorphism)이 성립하므로 모든 이론을 $\mathbb{R}^n$ 상에서 서술할 수 있습니다.

수학에서 핵심이 되는 아이디어 중 하나는 **"닫힘성(closure)"**입니다. 이는 "내가 제안한 대수적 연산들을 반복해서 가했을 때 만들어지는 결과물 전체의 집합은 무엇인가?"라는 질문과 직결됩니다. 벡터의 경우, 소수의 초기 벡터 집합에서 시작하여 이들을 서로 더하고 실수배하여 얻을 수 있는 모든 벡터들의 집합을 가리키며, 이 닫힌 대수 구조를 **벡터 공간(vector space)**이라 부릅니다. 이 벡터 공간의 개념과 성질들이 오늘날 머신러닝 모델들의 수학적 뼈대를 구성합니다.

---

# 2.1 연립선형방정식 (Systems of Linear Equations)

연립선형방정식은 선형대수의 핵심 주제입니다. 현실 세계의 수많은 최적화 및 모델링 문제가 연립선형방정식으로 공식화될 수 있으며, 선형대수는 이를 풀기 위한 가장 체계적인 도구들을 제공합니다.

### [예제 2.1] 생산 계획과 자원 제한
어떤 공장에서 $n$개의 제품 $N_1, \dots, N_n$을 생산하려고 하며, 여기에 $m$개의 자원 $R_1, \dots, R_m$이 요구된다고 가정합시다.
* 제품 $N_j$ 하나를 생산하는 데 자원 $R_i$가 $a_{ij}$ 단위만큼 소비됩니다 ($i=1,\dots,m$, $j=1,\dots,n$).
* 가용한 총 자원 $R_i$의 양이 $b_i$ 단위로 한정되어 있을 때, 자원을 남김없이 딱 맞춰 소비하면서 각 제품을 몇 개($x_j$) 생산해야 할지 최적의 생산 계획을 수립하고자 합니다.
* 각 제품을 $x_1, \dots, x_n$ 단위 생산할 때 소비되는 자원 $R_i$의 총합은 다음과 같습니다.
  $$a_{i1}x_1 + \dots + a_{in}x_n \tag{2.2}$$
* 따라서 이상적인 생산 계획 $\mathbf{x} = (x_1, \dots, x_n) \in \mathbb{R}^n$은 다음 식을 만족해야 합니다.
  $$\begin{matrix}
  a_{11}x_1 + \dots + a_{1n}x_n = b_1 \\
  \vdots \\
  a_{m1}x_1 + \dots + a_{mn}x_n = b_m
  \end{matrix} \tag{2.3}$$
  여기서 $a_{ij} \in \mathbb{R}$와 $b_i \in \mathbb{R}$는 기지수(knowns)이고, $x_j$는 우리가 구하려는 미지수(unknowns)입니다. 식 (2.3)이 일반적인 **연립선형방정식(system of linear equations)**의 형태입니다. 이 식을 동시에 만족하는 모든 실수 묶음 $(x_1, \dots, x_n) \in \mathbb{R}^n$을 방정식의 **해(solution)**라고 부릅니다.

### [예제 2.2] 해의 세 가지 양태
일반적인 연립선형방정식의 해는 **'해가 존재하지 않음', '오직 하나의 유일한 해만 존재', '무한히 많은 해가 존재'**의 세 가지 상태 중 하나를 갖습니다.

1. **해가 없는 경우 (No solution)**:
   $$\begin{matrix}
   x_1 + x_2 + x_3 = 3 & (1) \\
   x_1 - x_2 + 2x_3 = 2 & (2) \\
   2x_1 + 3x_3 = 1 & (3)
   \end{matrix} \tag{2.4}$$
   식 (1)과 (2)를 더하면 $2x_1 + 3x_3 = 5$가 되는데, 이는 식 (3)의 $2x_1 + 3x_3 = 1$이라는 조건과 완전히 모순됩니다. 따라서 이 연립방정식을 만족하는 해는 존재하지 않습니다.
2. **유일한 해가 존재하는 경우 (Unique solution)**:
   $$\begin{matrix}
   x_1 + x_2 + x_3 = 3 & (1) \\
   x_1 - x_2 + 2x_3 = 2 & (2) \\
   x_2 + x_3 = 2 & (3)
   \end{matrix} \tag{2.5}$$
   식 (1)과 (3)으로부터 $x_1 = 1$임을 즉시 알 수 있습니다. 식 (1)과 (2)를 더해 $2x_1 + 3x_3 = 5$를 얻고, 여기에 $x_1 = 1$을 대입하면 $x_3 = 1$이 나옵니다. 마지막으로 식 (3)에 대입하면 $x_2 = 1$이 됩니다. 따라서 유일한 해는 $\mathbf{x} = (1, 1, 1)$뿐입니다.
3. **무한히 많은 해가 존재하는 경우 (Infinitely many solutions)**:
   $$\begin{matrix}
   x_1 + x_2 + x_3 = 3 & (1) \\
   x_1 - x_2 + 2x_3 = 2 & (2) \\
   2x_1 + 3x_3 = 5 & (3)
   \end{matrix} \tag{2.6}$$
   식 (1)과 (2)를 더하면 정확히 식 (3)이 유도되므로, 식 (3)은 아무런 새로운 정보를 주지 못하는 중복(redundancy) 식입니다. 따라서 식 (3)을 소거하고 식 (1), (2)만 연립하면, 변수 관계식 $2x_1 = 5 - 3x_3$ 및 $2x_2 = 1 + x_3$를 얻습니다. 여기서 $x_3 = a \in \mathbb{R}$를 자유롭게 움직일 수 있는 임의의 실수인 **자유 변수(free variable)**로 지정하면, 해집합은 다음과 같은 선(Line) 형태의 무한 집합이 됩니다.
   $$\left\{ \begin{bmatrix} \frac{5}{2} - \frac{3}{2}a \\ \frac{1}{2} + \frac{1}{2}a \\ a \end{bmatrix}, a \in \mathbb{R} \right\} \tag{2.7}$$

### 연립선형방정식의 기하학적 해석
2개의 변수 $x_1, x_2$를 가진 연립방정식에서 각각의 선형방정식은 2차원 평면 위의 **직선(Line)**을 나타냅니다. 연립방정식의 해는 모든 식을 동시에 충족해야 하므로, 기하학적으로는 **두 직선의 교점(intersection)**에 해당합니다. 
* 두 직선이 평행하면 교점이 없으므로 **해가 없습니다**.
* 두 직선이 한 점에서 만나면 교점이 하나이므로 **유일한 해**를 가집니다.
* 두 직선이 완벽히 겹치면 교점이 무한하므로 **무한한 해**를 가집니다.

유사하게 3개의 미지수가 주어지면 각 방정식은 3차원 공간 상의 **평면(Plane)**을 나타내며, 이 평면들이 겹쳐서 만드는 교집합 영역(평면, 선, 점, 혹은 공집합)이 방정식의 해공간이 됩니다.

---

### 행렬 표기법으로의 압축

연립방정식을 체계적으로 다루기 위해 미지수의 계수(coefficients)들을 벡터와 행렬로 묶는 콤팩트한 표기법을 도입합니다.
식 (2.3)은 열벡터들의 가중합 형태로 다음과 같이 나타낼 수 있습니다:
$$x_1 \begin{bmatrix} a_{11} \\ \vdots \\ a_{m1} \end{bmatrix} + x_2 \begin{bmatrix} a_{12} \\ \vdots \\ a_{m2} \end{bmatrix} + \dots + x_n \begin{bmatrix} a_{1n} \\ \vdots \\ a_{mn} \end{bmatrix} = \begin{bmatrix} b_1 \\ \vdots \\ b_m \end{bmatrix} \tag{2.9}$$

이 식은 행렬과 벡터의 곱셈을 사용하여 더욱 조밀하게 표현할 수 있습니다:
$$\begin{bmatrix} a_{11} & \dots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \dots & a_{mn} \end{bmatrix} \begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} = \begin{bmatrix} b_1 \\ \vdots \\ b_m \end{bmatrix} \quad \Longleftrightarrow \quad \mathbf{A}\mathbf{x} = \mathbf{b} \tag{2.10}$$

여기서 계수행렬 $\mathbf{A} \in \mathbb{R}^{m \times n}$과 입력 벡터 $\mathbf{x} \in \mathbb{R}^n$의 곱 $\mathbf{A}\mathbf{x}$는 행렬 $\mathbf{A}$의 **열벡터들의 선형 결합(linear combination)**을 의미합니다.

---

# 2.2 행렬 (Matrices)

행렬(Matrix)은 연립선형방정식을 간결하게 표현할 뿐 아니라, 공간 상의 선형 변환(linear mapping)을 대수적으로 구현하는 핵심 도구입니다.

### [정의 2.1] 행렬
자연수 $m, n \in \mathbb{N}$에 대하여 실수 성분을 가지는 $(m, n)$ 행렬 $\mathbf{A}$는 $m$개의 행(rows)과 $n$개의 열(columns)로 구성된 직사각형 구조의 수치 배열입니다.
$$\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{bmatrix}, \quad a_{ij} \in \mathbb{R} \tag{2.11}$$

* $(1, n)$ 행렬은 **행벡터(row vector)**, $(m, 1)$ 행렬은 **열벡터(column vector)**라고 부릅니다.
* $\mathbb{R}^{m \times n}$은 실수 성분을 가진 모든 $(m, n)$ 행렬의 집합입니다.
* 행렬 $\mathbf{A} \in \mathbb{R}^{m \times n}$은 행렬의 $n$개 열을 아래로 길게 이어 붙임으로써 $mn$차원 벡터 $\mathbf{a} \in \mathbb{R}^{mn}$로 동등하게 재구성(reshape)할 수 있습니다 (Figure 2.4 참조).

---

### 2.2.1 행렬의 합과 곱

* **행렬의 덧셈**: 크기가 동일한 두 행렬 $\mathbf{A}, \mathbf{B} \in \mathbb{R}^{m \times n}$의 합은 각 성분을 일대일로 더한 것입니다.
  $$\mathbf{A} + \mathbf{B} := \begin{bmatrix} a_{11} + b_{11} & \dots & a_{1n} + b_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} + b_{m1} & \dots & a_{mn} + b_{mn} \end{bmatrix} \in \mathbb{R}^{m \times n} \tag{2.12}$$
* **행렬의 곱셈**: 행렬 $\mathbf{A} \in \mathbb{R}^{m \times n}$과 $\mathbf{B} \in \mathbb{R}^{n \times k}$가 주어졌을 때, 두 행렬의 곱 $\mathbf{C} = \mathbf{A}\mathbf{B} \in \mathbb{R}^{m \times k}$의 각 성분 $c_{ij}$는 다음과 같이 정의됩니다.
  $$c_{ij} = \sum_{l=1}^{n} a_{il}b_{lj}, \quad i=1,\dots,m, \quad j=1,\dots,k \tag{2.13}$$
  즉, $\mathbf{C}$의 $i$행 $j$열 원소 $c_{ij}$는 행렬 $\mathbf{A}$의 $i$번째 행벡터와 행렬 $\mathbf{B}$의 $j$번째 열벡터의 내적(dot product) 값입니다. 
* **곱셈 조건**: 두 행렬을 곱하기 위해서는 좌측 행렬의 **열의 수**가 우측 행렬의 **행의 수**와 반드시 일치해야 합니다. 즉, 인접 차원이 맞아야 합니다:
  $$\underline{\mathbf{A}}_{n \times k} \underline{\mathbf{B}}_{k \times m} = \underline{\mathbf{C}}_{n \times m} \tag{2.14}$$
  만약 $m \neq n$이라면 우측에서 좌측으로의 곱인 $\mathbf{B}\mathbf{A}$는 차원이 맞지 않아 정의되지 않습니다.

> [!WARNING]
> 행렬의 대수적 곱셈은 단순 성분별 곱셈($c_{ij} = a_{ij}b_{ij}$)이 아닙니다. 컴퓨터 프로그래밍에서 가끔 다차원 배열 간에 일어나는 단순 성분별 곱은 **아다마르 곱(Hadamard Product)**이라 부르며, 선형대수의 표준 행렬 곱셈과는 완전히 다른 연산입니다.

### [예제 2.3] 곱셈의 비가환성 (Non-commutativity)
행렬 곱셈은 교환법칙이 성립하지 않습니다 ($\mathbf{A}\mathbf{B} \neq \mathbf{B}\mathbf{A}$).
$\mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 3 & 2 & 1 \end{bmatrix} \in \mathbb{R}^{2 \times 3}$, $\mathbf{B} = \begin{bmatrix} 0 & 2 \\ 1 & -1 \\ 0 & 1 \end{bmatrix} \in \mathbb{R}^{3 \times 2}$ 일 때:
$$\mathbf{A}\mathbf{B} = \begin{bmatrix} 2 & 3 \\ 2 & 5 \end{bmatrix} \in \mathbb{R}^{2 \times 2} \tag{2.15}$$
$$\mathbf{B}\mathbf{A} = \begin{bmatrix} 6 & 4 & 2 \\ -2 & 0 & 2 \\ 3 & 2 & 1 \end{bmatrix} \in \mathbb{R}^{3 \times 3} \tag{2.16}$$
이처럼 $\mathbf{A}\mathbf{B}$와 $\mathbf{B}\mathbf{A}$는 결과 행렬의 물리적인 크기조차 다르게 정의됩니다 (Figure 2.5 참조).

### [정의 2.2] 항등행렬 (Identity Matrix)
정사각 행렬 공간 $\mathbb{R}^{n \times n}$ 상에서, 주대각선 성분(diagonal elements)은 모두 1이고 그 외의 모든 성분은 0인 특수한 행렬을 항등행렬 $\mathbf{I}_n$이라 정의합니다.
$$\mathbf{I}_n := \begin{bmatrix} 1 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{bmatrix} \in \mathbb{R}^{n \times n} \tag{2.17}$$

---

### 행렬 곱의 성질

* **결합법칙 (Associativity)**:
  $$(\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C}) \tag{2.18}$$
* **분배법칙 (Distributivity)**:
  $$(\mathbf{A} + \mathbf{B})\mathbf{C} = \mathbf{A}\mathbf{C} + \mathbf{B}\mathbf{C} \tag{2.19a}$$
  $$\mathbf{A}(\mathbf{C} + \mathbf{D}) = \mathbf{A}\mathbf{C} + \mathbf{A}\mathbf{D} \tag{2.19b}$$
* **항등행렬 곱셈**:
  $$\mathbf{I}_m\mathbf{A} = \mathbf{A}\mathbf{I}_n = \mathbf{A} \tag{2.20}$$
  ($m \neq n$일 때 $\mathbf{I}_m \neq \mathbf{I}_n$ 임에 주의해야 합니다.)

---

### 2.2.2 역행렬과 전치행렬

### [정의 2.3] 역행렬 (Inverse)
정사각 행렬 $\mathbf{A} \in \mathbb{R}^{n \times n}$에 대하여, $\mathbf{A}\mathbf{B} = \mathbf{I}_n = \mathbf{B}\mathbf{A}$를 만족하는 정사각 행렬 $\mathbf{B} \in \mathbb{R}^{n \times n}$이 존재할 때, 이 $\mathbf{B}$를 $\mathbf{A}$의 **역행렬**이라 부르고 $\mathbf{A}^{-1}$로 표기합니다.
* 역행렬이 존재하는 행렬을 **정칙/가역/비특이 행렬(regular/invertible/nonsingular matrix)**이라 부르고, 역행렬이 없는 행렬을 **특이/비가역 행렬(singular/noninvertible matrix)**이라 합니다.
* 가역 행렬의 역행렬은 유일하게 존재합니다.

### $2 \times 2$ 행렬의 역행렬 존재 조건
임의의 행렬 $\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} \in \mathbb{R}^{2 \times 2}$에 대하여 $\mathbf{A}' = \begin{bmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{bmatrix}$을 곱하면 다음과 같이 스칼라배 형태가 유도됩니다:
$$\mathbf{A}\mathbf{A}' = (a_{11}a_{22} - a_{12}a_{21})\mathbf{I} \tag{2.23}$$
따라서 다음의 분모 조건($a_{11}a_{22} - a_{12}a_{21} \neq 0$)을 만족할 때만 역행렬이 정의됩니다:
$$\mathbf{A}^{-1} = \frac{1}{a_{11}a_{22} - a_{12}a_{21}} \begin{bmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{bmatrix} \tag{2.24}$$
이때 스칼라 항 $a_{11}a_{22} - a_{12}a_{21}$을 $2 \times 2$ 행렬의 **행렬식(determinant)**이라 부르며, 고차원 행렬에서도 행렬식이 0이 아닌지의 여부가 가역성의 척도가 됩니다.

### [정의 2.4] 전치행렬 (Transpose)
임의의 행렬 $\mathbf{A} \in \mathbb{R}^{m \times n}$에 대하여 $b_{ij} = a_{ji}$를 성분으로 갖는 행렬 $\mathbf{B} \in \mathbb{R}^{n \times m}$을 $\mathbf{A}$의 **전치행렬**이라 부르고 $\mathbf{A}^{\top}$로 표기합니다.
* 전치행렬은 원래 행렬의 행을 열로, 열을 행으로 바꾼 것입니다.

### 역행렬과 전치행렬의 주요 대수적 성질
* $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I} = \mathbf{A}^{-1}\mathbf{A} \tag{2.26}$
* $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1} \tag{2.27}$ 
* $(\mathbf{A} + \mathbf{B})^{-1} \neq \mathbf{A}^{-1} + \mathbf{B}^{-1} \tag{2.28}$ 
* $(\mathbf{A}^{\top})^{\top} = \mathbf{A} \tag{2.29}$
* $(\mathbf{A}\mathbf{B})^{\top} = \mathbf{B}^{\top}\mathbf{A}^{\top} \tag{2.30}$ 
* $(\mathbf{A} + \mathbf{B})^{\top} = \mathbf{A}^{\top} + \mathbf{B}^{\top} \tag{2.31}$
* 정사각 행렬 $\mathbf{A}$가 가역이면 그 전치행렬도 가역이며, 다음이 성립합니다: $(\mathbf{A}^{-1})^{\top} = (\mathbf{A}^{\top})^{-1} =: \mathbf{A}^{-\top}$

### [정의 2.5] 대칭행렬 (Symmetric Matrix)
어떤 정사각 행렬 $\mathbf{A} \in \mathbb{R}^{n \times n}$이 $\mathbf{A} = \mathbf{A}^{\top}$를 만족할 때, 이 행렬을 **대칭행렬**이라 부릅니다.
* **대칭행렬의 성질**: 두 대칭행렬의 합은 언제나 대칭행렬입니다. 그러나 대칭행렬끼리의 곱은 일반적으로 교환법칙이 지켜지지 않기 때문에 대칭성을 유지하지 못합니다 (식 (2.32) 예시 참조).

---

# 2.3 연립선형방정식의 풀이 (Solving Linear Equations)

행렬과 벡터의 연산 성질을 응용하여 일반적인 형태의 연립선형방정식 $\mathbf{A}\mathbf{x} = \mathbf{b}$의 해를 체계적이고 구체적으로 구하는 절차를 살펴봅니다.

### 2.3.1 특수해와 일반해 (Particular and General Solution)

다음 예제 연립방정식을 관찰해 봅시다:
$$\begin{bmatrix} 1 & 0 & 8 & -4 \\ 0 & 1 & 2 & 12 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 42 \\ 8 \end{bmatrix} \tag{2.38}$$

이 연립방정식은 미지수가 4개이고 방정식이 2개이므로 무한한 해공간을 가질 것으로 예측됩니다. 특히 앞쪽의 2개 열이 기본 단위 벡터의 모양($[1, 0]^{\top}$, $[0, 1]^{\top}$)으로 구성되어 있어 편리합니다.

* **특수해 (Particular Solution)**:
  우변의 상수벡터 $\mathbf{b} = [42, 8]^{\top}$를 만들기 위해 앞쪽 2개의 기본 열벡터를 활용하여 다음과 같이 조합할 수 있습니다.
  $$\begin{bmatrix} 42 \\ 8 \end{bmatrix} = 42\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 8\begin{bmatrix} 0 \\ 1 \end{bmatrix} + 0\mathbf{c}_3 + 0\mathbf{c}_4$$
  따라서 특정 해 $\mathbf{x}_p = [42, 8, 0, 0]^{\top}$를 얻을 수 있으며, 이를 이 방정식의 **특수해(particular solution)**라고 부릅니다.
* **일반해 (General Solution)**:
  전체 해집합을 구성하기 위해서는 동차 연립방정식 $\mathbf{A}\mathbf{x} = \mathbf{0}$을 만족하여 결과값에 아무런 영향을 주지 않는 영벡터 조합 성분(커널 공간)을 규명해야 합니다.
  * 3번째 열벡터 $\mathbf{c}_3 = [8, 2]^{\top}$은 앞의 두 단위 열벡터의 선형결합인 $8\mathbf{c}_1 + 2\mathbf{c}_2$로 표현되므로 다음과 같은 영 조합을 유도할 수 있습니다:
    $$8\mathbf{c}_1 + 2\mathbf{c}_2 - \mathbf{c}_3 + 0\mathbf{c}_4 = \mathbf{0}$$
    여기에 임의의 실수배 $\lambda_1$을 한 결과 역시 영벡터를 출력합니다.
  * 4번째 열벡터 $\mathbf{c}_4 = [-4, 12]^{\top}$ 또한 $-4\mathbf{c}_1 + 12\mathbf{c}_2$이므로 다음 영 조합을 생성합니다:
    $$-4\mathbf{c}_1 + 12\mathbf{c}_2 + 0\mathbf{c}_3 - \mathbf{c}_4 = \mathbf{0}$$
    여기에 실수배 $\lambda_2$를 취할 수 있습니다.
  
  따라서 이 방정식의 전체 해집합인 **일반해(general solution)**는 특수해와 동차해의 선형 결합으로 다음과 같이 기술됩니다.
  $$\mathbf{x} = \begin{bmatrix} 42 \\ 8 \\ 0 \\ 0 \end{bmatrix} + \lambda_1 \begin{bmatrix} 8 \\ 2 \\ -1 \\ 0 \end{bmatrix} + \lambda_2 \begin{bmatrix} -4 \\ 12 \\ 0 \\ -1 \end{bmatrix}, \quad \lambda_1, \lambda_2 \in \mathbb{R} \tag{2.43}$$

---

### [핵심] 연립선형방정식 해법의 3단계 가이드라인
1. 비동차 연립방정식 $\mathbf{A}\mathbf{x} = \mathbf{b}$의 임의의 **특수해(Particular Solution)** $\mathbf{x}_p$를 찾는다.
2. 동차 연립방정식 $\mathbf{A}\mathbf{x} = \mathbf{0}$을 충족하는 모든 해를 구한다.
3. 이 두 해를 결합하여 최종 **일반해(General Solution)**를 구성한다.

---

### 2.3.2 기본 행 연산과 사다리꼴 행렬

임의의 무작위 방정식 시스템을 위와 같이 풀기 쉬운 정형적인 모양으로 바꾸기 위해, 해집합을 보존하면서 식을 변형하는 세 가지 **기본 행 연산(elementary transformations)**을 적용합니다.

1. **행 교환 (Row Swap)**: 두 방정식(행)의 위치를 서로 맞바꾼다.
2. **실수배 (Scalar Multiplication)**: 임의의 방정식(행)에 0이 아닌 상수 $\lambda \in \mathbb{R} \setminus \{0\}$을 곱한다.
3. **행 가산 (Row Addition)**: 한 방정식(행)에 다른 방정식(행)의 상수배를 더한다.

### [예제 2.6] 첨가행렬과 가우스 소거법을 통한 풀이
다음 방정식 시스템의 해를 구하고자 합니다:
$$\begin{matrix}
-2x_1 + 4x_2 - 2x_3 - x_4 + 4x_5 = -3 \\
4x_1 - 8x_2 + 3x_3 - 3x_4 + x_5 = 2 \\
x_1 - 2x_2 + x_3 - x_4 + x_5 = 0 \\
x_1 - 2x_2 - 3x_4 + 4x_5 = a
\end{matrix} \tag{2.44}$$

변수 $x_j$를 매번 적는 번거로움을 피하기 위해 계수와 우변 상수를 모은 **첨가 행렬(augmented matrix)** $[\mathbf{A} \mid \mathbf{b}]$ 구조를 구성합니다:
$$\left[ \begin{array}{ccccc|c}
-2 & 4 & -2 & -1 & 4 & -3 \\
4 & -8 & 3 & -3 & 1 & 2 \\
1 & -2 & 1 & -1 & 1 & 0 \\
1 & -2 & 0 & -3 & 4 & a
\end{array} \right]$$

1. 소거 속도를 올리기 위해 1행과 3행을 맞바꿉니다 ($R_1 \leftrightarrow R_3$):
   $$\left[ \begin{array}{ccccc|c}
   1 & -2 & 1 & -1 & 1 & 0 \\
   4 & -8 & 3 & -3 & 1 & 2 \\
   -2 & 4 & -2 & -1 & 4 & -3 \\
   1 & -2 & 0 & -3 & 4 & a
   \end{array} \right]$$
2. 1행의 계수 $1$을 피벗으로 삼아 하단 행들의 1열 성분을 제거합니다 (2행 $- 4R_1$, 3행 $+ 2R_1$, 4행 $- R_1$):
   $$\left[ \begin{array}{ccccc|c}
   1 & -2 & 1 & -1 & 1 & 0 \\
   0 & 0 & -1 & 1 & -3 & 2 \\
   0 & 0 & 0 & -3 & 6 & -3 \\
   0 & 0 & -1 & -2 & 3 & a
   \end{array} \right]$$
3. 2행의 피벗인 $-1$을 기준으로 4행의 3열 성분을 지웁니다 ($R_4 - R_2$):
   $$\left[ \begin{array}{ccccc|c}
   1 & -2 & 1 & -1 & 1 & 0 \\
   0 & 0 & -1 & 1 & -3 & 2 \\
   0 & 0 & 0 & -3 & 6 & -3 \\
   0 & 0 & 0 & -3 & 6 & a
   \end{array} \right]$$
4. 3행을 기준으로 4행의 4열 및 5열 성분을 지웁니다 ($R_4 - R_3$):
   $$\left[ \begin{array}{ccccc|c}
   1 & -2 & 1 & -1 & 1 & 0 \\
   0 & 0 & -1 & 1 & -3 & 2 \\
   0 & 0 & 0 & -3 & 6 & -3 \\
   0 & 0 & 0 & 0 & 0 & a+1
   \end{array} \right]$$
5. 피벗 값들을 단순화하기 위해 각 행에 상수를 곱합니다 ($R_2 \times (-1)$, $R_3 \times (-\frac{1}{3})$):
   $$\left[ \begin{array}{ccccc|c}
   1 & -2 & 1 & -1 & 1 & 0 \\
   0 & 0 & 1 & -1 & 3 & -2 \\
   0 & 0 & 0 & 1 & -2 & 1 \\
   0 & 0 & 0 & 0 & 0 & a+1
   \end{array} \right]$$

이 변환이 완료된 상태를 **사다리꼴 행렬(Row-Echelon Form, REF)**이라고 합니다. 
이를 다시 변수 형태의 방정식으로 복원하면 다음과 같습니다:
$$\begin{matrix}
x_1 - 2x_2 + x_3 - x_4 + x_5 = 0 \\
x_3 - x_4 + 3x_5 = -2 \\
x_4 - 2x_5 = 1 \\
0 = a + 1
\end{matrix} \tag{2.45}$$

마지막 행인 $0 = a + 1$ 조건에 의해, 이 방정식 시스템은 오직 **$a = -1$일 때만 해가 존재**합니다. 만약 $a \neq -1$이라면 해가 존재하지 않는 모순이 발생합니다.
$a = -1$일 때의 특수해 중 하나는 피벗이 있는 열들의 계수를 역대입 연산(오른쪽 피벗부터 왼쪽 피벗으로 역추적)하여 다음과 같이 지정할 수 있습니다:
$$\mathbf{x}_p = \begin{bmatrix} 2 & 0 & -1 & 1 & 0 \end{bmatrix}^{\top} \tag{2.46}$$
또한 두 개의 자유 변수 $x_2 = \lambda_1$, $x_5 = \lambda_2$를 설정하여 최종 일반해를 구성할 수 있습니다:
$$\mathbf{x} = \begin{bmatrix} 2 \\ 0 \\ -1 \\ 1 \\ 0 \end{bmatrix} + \lambda_1 \begin{bmatrix} 2 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix} + \lambda_2 \begin{bmatrix} 2 \\ 0 \\ -1 \\ 2 \\ 1 \end{bmatrix}, \quad \lambda_1, \lambda_2 \in \mathbb{R} \tag{2.47}$$

### [정의 2.6] 사다리꼴 행렬 (Row-Echelon Form, REF)
행렬이 다음 두 조건을 모두 만족할 때 사다리꼴 행렬(REF) 형태를 지녔다고 정의합니다.
1. 모든 성분이 0인 행(영행)들은 항상 행렬의 가장 아래쪽에 위치한다.
2. 영행이 아닌 임의의 행에서 가장 왼쪽에 처음 나타나는 0이 아닌 성분(이를 **피벗, pivot** 또는 **선도 계수, leading coefficient**라고 부름)은 항상 그 바로 윗행의 피벗보다 엄격히 오른쪽에 위치한다. (따라서 계단식 staircase 구조가 형성됩니다.)

* **기본 변수와 자유 변수**: 사다리꼴 행렬 상태에서 피벗(Pivot) 성분에 대응되는 열 변수들을 **기본 변수(basic variables)**라고 부르며, 피벗이 없는 열에 대응되는 변수들을 **자유 변수(free variables)**라고 부릅니다. 예제 (2.45)에서 $x_1, x_3, x_4$는 기본 변수이고 $x_2, x_5$는 자유 변수입니다.

### 기약 사다리꼴 행렬 (Reduced Row-Echelon Form, RREF)
연립선형방정식을 기계적으로 해결하기 위해, REF에서 더 나아간 **기약 사다리꼴 행렬(RREF)** 형태를 정의합니다. 다음 세 조건을 충족해야 합니다:
1. 행렬이 사다리꼴 행렬(REF) 형태를 갖춘다.
2. 모든 nonzero 행의 피벗(Pivot) 값은 정확히 **1**이다.
3. 피벗이 위치한 열에서, 피벗을 제외한 나머지 모든 행 성분은 **0**이다.

RREF를 만드는 컴퓨터 알고리즘 과정을 **가우스 소거법(Gaussian elimination)**이라고 부릅니다.
예를 들어, 다음 행렬은 RREF 상태입니다 (피벗은 1열 1행의 $1$, 3열 2행의 $1$, 4열 3행의 $1$):
$$\mathbf{A} = \begin{bmatrix} \mathbf{1} & 3 & 0 & 0 & 3 \\ 0 & 0 & \mathbf{1} & 0 & 9 \\ 0 & 0 & 0 & \mathbf{1} & -4 \end{bmatrix} \tag{2.49}$$

---

### 2.3.3 마이너스 1 트릭 (The Minus-1 Trick)

RREF로 변환된 행렬로부터 동차 방정식 $\mathbf{A}\mathbf{x} = \mathbf{0}$의 모든 해집합(즉, 선형 결합의 기초가 되는 커널 기저 벡터들)을 매우 직관적이고 빠르게 읽어내는 실용적인 수학 비법이 있습니다. 이를 **마이너스 1 트릭**이라고 합니다.

1. 계수행렬 $\mathbf{A} \in \mathbb{R}^{k \times n}$이 RREF 형태이고 영행이 소거된 상태라고 가정합시다 (식 (2.51) 구조).
2. 피벗 성분이 대각선 상에 존재하지 않고 비어 있는 행들의 인덱스 위치에 다음과 같은 형태의 행을 삽입하여 $n \times n$ 정사각 행렬 $\tilde{\mathbf{A}}$를 구성합니다.
   $$\begin{bmatrix} 0 & \dots & 0 & -1 & 0 & \dots & 0 \end{bmatrix} \tag{2.52}$$
3. 이렇게 대각 성분을 $1$ 또는 $-1$로 채워 구성한 확장 행렬 $\tilde{\mathbf{A}}$에서, **대각선 상에 $-1$이 들어간 열벡터들**을 그대로 꺼내면 이 벡터들이 동차 연립방정식 $\mathbf{A}\mathbf{x} = \mathbf{0}$의 해공간(Null Space)을 스팬하는 기저 벡터가 됩니다.

### [예제 2.8] 마이너스 1 트릭의 적용
RREF 행렬인 식 (2.49)를 가져와서 missing diagonal(피벗이 없는 2열과 5열 위치)에 $-1$ 행을 끼워 넣습니다:
$$\tilde{\mathbf{A}} = \begin{bmatrix} 1 & 3 & 0 & 0 & 3 \\ 0 & -1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 9 \\ 0 & 0 & 0 & 1 & -4 \\ 0 & 0 & 0 & 0 & -1 \end{bmatrix} \tag{2.54}$$
여기서 대각선 성분이 $-1$인 열은 **2번째 열**과 **5번째 열**입니다. 이 두 열벡터를 꺼내면 다음과 같습니다:
$$\mathbf{x}_1 = \begin{bmatrix} 3 \\ -1 \\ 0 & 0 & 0 \end{bmatrix}^{\top}, \quad \mathbf{x}_2 = \begin{bmatrix} 3 \\ 0 \\ 9 \\ -4 \\ -1 \end{bmatrix}^{\top}$$
이 벡터들이 $\mathbf{A}\mathbf{x} = \mathbf{0}$의 해집합을 구성하는 기저가 되므로, 일반해는 다음과 같이 즉시 도출됩니다:
$$\mathbf{x} = \lambda_1 \begin{bmatrix} 3 \\ -1 \\ 0 \\ 0 \\ 0 \end{bmatrix} + \lambda_2 \begin{bmatrix} 3 \\ 0 \\ 9 \\ -4 \\ -1 \end{bmatrix}, \quad \lambda_1, \lambda_2 \in \mathbb{R} \tag{2.55}$$

---

### 가우스 소거법을 통한 역행렬 계산

정사각 행렬 $\mathbf{A} \in \mathbb{R}^{n \times n}$의 역행렬 $\mathbf{A}^{-1}$을 계산하는 것은 대수적으로 $\mathbf{A}\mathbf{X} = \mathbf{I}_n$을 푸는 공동 연립방정식 문제와 같습니다.
이를 위해 첨가 행렬 $[\mathbf{A} \mid \mathbf{I}_n]$을 세우고, 가우스 소거법을 적용하여 좌변의 $\mathbf{A}$가 $\mathbf{I}_n$이 되도록 RREF 변환을 수행하면 우변에 자동으로 역행렬이 유도됩니다.
$$[\mathbf{A} \mid \mathbf{I}_n] \quad \rightsquigarrow \quad [\mathbf{I}_n \mid \mathbf{A}^{-1}] \tag{2.56}$$
(구체적인 $4 \times 4$ 역행렬 도출 연산은 식 (2.57~2.58) 예제 참조)

---

### 2.3.4 연립선형방정식 해결 알고리즘 및 계산 복잡도

* **직접 역행렬 계산**: $\mathbf{A}$가 정사각 가역행렬이면 $\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$로 풀 수 있습니다.
* **유사역행렬 (Pseudo-inverse)**: 행렬의 열들이 선형 독립적일 때 양변의 왼쪽에 전치행렬 $\mathbf{A}^{\top}$를 곱하는 **규칙 방정식(normal equation)** 형태로 변환하여 해를 도출할 수 있습니다.
  $$\mathbf{A}\mathbf{x} = \mathbf{b} \quad \Longleftrightarrow \quad \mathbf{A}^{\top}\mathbf{A}\mathbf{x} = \mathbf{A}^{\top}\mathbf{b} \quad \Longleftrightarrow \quad \mathbf{x} = (\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{b} \tag{2.59}$$
  여기서 $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$를 **무어-펜로즈 유사역행렬(Moore-Penrose pseudo-inverse)**이라 부르며, 해가 존재하지 않는 시스템에서 오차의 제곱합을 최소화하는 **최소제곱해(least-squares solution)**를 줍니다 (Ch.9 선형 회귀의 근간).
* **수치적 한계와 대안**:
  가우스 소거 직접법은 변수 개수가 수천 개 수준일 때는 유용하지만, 미지수가 수백만 개를 넘어서는 실제 대규모 머신러닝 시스템에서는 연산 횟수가 세제곱 복잡도($O(n^3)$)로 스케일링되어 물리적으로 작동이 불가능합니다.
  따라서 컴퓨터 과학 및 수치해석 실무에서는 다음과 같은 **간접 반복법(iterative methods)**을 사용하여 근사해를 구합니다.
  * **정적 반복법**: 리처드슨(Richardson), 야코비(Jacobi), 가우스-자이델(Gauss-Seidel), SOR(Successive Over-Relaxation) 방법.
  * **크릴로프 부공간(Krylov subspace) 반복법**: 켤레구배법(Conjugate Gradients, CG), GMRES(Generalized Minimal Residual), BiCG(Biconjugate Gradients).
  이들은 임의의 행렬 $\mathbf{C}$와 벡터 $\mathbf{d}$를 잡아 오차(잔차)를 매 스텝마다 감소시키며 해로 수렴시키는 수치적 루프를 돕습니다:
  $$\mathbf{x}^{(k+1)} = \mathbf{C}\mathbf{x}^{(k)} + \mathbf{d} \tag{2.60}$$

---

# 2.4 벡터 공간 (Vector Spaces)

선형 연립방정식을 해결하는 시스템적 토대를 다진 후, 이제 벡터가 살아 숨 쉬는 수학적 대수 구조인 **벡터 공간**의 엄밀한 정의를 정립합니다.

### 2.4.1 군 (Groups)

벡터 공간을 정의하기에 앞서, 현대 대수학의 기본 구조인 **군(Group)**을 정의합니다. 군은 임의의 집합과 연산자가 만나 대수적 구조를 보존하는 기본 뼈대입니다.

### [정의 2.7] 군 (Group)
집합 $G$와 이 집합 위에서 정의된 연산 $\otimes : G \times G \to G$에 대하여, 대수 구조 $G = (G, \otimes)$가 다음 네 가지 공리를 만족하면 **군**이라고 부릅니다.
1. **닫힘성 (Closure)**: 집합 내 두 원소를 연산한 결과는 항상 집합 내에 존재한다. ($\forall x, y \in G: x \otimes y \in G$)
2. **결합법칙 (Associativity)**: 연산의 우선순위는 결과에 영향을 주지 않는다. ($\forall x, y, z \in G: (x \otimes y) \otimes z = x \otimes (y \otimes z)$)
3. **항등원 존재 (Neutral element)**: 연산해도 원래 원소를 보존하는 유일한 원소 $e$가 존재한다. ($\exists e \in G \; \forall x \in G: x \otimes e = x = e \otimes x$)
4. **역원 존재 (Inverse element)**: 모든 원소에 대해 연산하여 항등원을 만드는 유일한 짝이 존재한다. ($\forall x \in G \; \exists y \in G: x \otimes y = e = y \otimes x$) 이 $y$를 보통 $x^{-1}$로 씁니다.

* **아벨 군 (Abelian Group)**: 추가적으로 교환법칙($\forall x, y \in G: x \otimes y = y \otimes x$)까지 만족하면 이를 **아벨 군(또는 가환군)**이라고 부릅니다.
* **일반선형군 (General Linear Group, $GL(n, \mathbb{R})$)**: 실수 가역 정사각 행렬들의 집합 $\mathbb{R}^{n \times n}$은 행렬 곱셈 연산에 대해 닫혀 있고 결합법칙이 성립하며, 항등원으로 $\mathbf{I}_n$, 역원으로 역행렬 $\mathbf{A}^{-1}$을 가집니다. 단, 교환법칙은 성립하지 않으므로 이는 **비가환군(Non-Abelian group)**에 속하며, 이 군을 **일반선형군**이라 정의합니다.

---

### 2.4.2 벡터 공간 (Vector Space)

군은 단 하나의 연산자만 다루는 반면, 벡터 공간은 내부의 덧셈 연산(inner operation)과 외부의 스칼라배 연산(outer operation)이라는 두 종류의 연산 체계를 가집니다.

### [정의 2.9] 벡터 공간 (Vector Space)
실수체 $\mathbb{R}$ 위에서 정의된 대수 구조 $V = (V, +, \cdot)$가 다음 조건들을 충족하면 이를 **벡터 공간**이라 정의하고, 그 집합의 원소들을 **벡터**라고 부릅니다.
1. $(V, +)$가 **덧셈 연산에 대해 아벨 군**을 이룬다. (항등원은 영벡터 $\mathbf{0}$)
2. 스칼라배에 대해 다음의 **분배법칙**이 성립한다:
   * $\forall \lambda \in \mathbb{R}, \; \mathbf{x}, \mathbf{y} \in V: \lambda \cdot (\mathbf{x} + \mathbf{y}) = \lambda \cdot \mathbf{x} + \lambda \cdot \mathbf{y}$
   * $\forall \lambda, \psi \in \mathbb{R}, \; \mathbf{x} \in V: (\lambda + \psi) \cdot \mathbf{x} = \lambda \cdot \mathbf{x} + \psi \cdot \mathbf{x}$
3. 스칼라배 간의 **결합법칙**이 성립한다:
   * $\forall \lambda, \psi \in \mathbb{R}, \; \mathbf{x} \in V: \lambda \cdot (\psi \cdot \mathbf{x}) = (\lambda \psi) \cdot \mathbf{x}$
4. 스칼라 항등원 $1$에 대하여 다음이 보존된다:
   * $\forall \mathbf{x} \in V: 1 \cdot \mathbf{x} = \mathbf{x}$

> [!NOTE]
> 일반적인 벡터 연산에서 "벡터끼리의 표준 곱셈($\mathbf{a}\mathbf{b}$)"은 수학적으로 정의되지 않습니다. 컴퓨터 배열 곱셈과 다르게 행렬 대수 규칙에 따라 열벡터(형식 $n \times 1$)끼리는 곱할 수 없으며, 오직 외적($\mathbf{a}\mathbf{b}^{\top} \in \mathbb{R}^{n \times n}$)과 내적($\mathbf{a}^{\top}\mathbf{b} \in \mathbb{R}$)만 정의됩니다.

---

### 2.4.3 부분공간 (Vector Subspaces)

### [정의 2.10] 부분공간 (Vector Subspace)
벡터 공간 $V = (V, +, \cdot)$의 비비어있는 부분집합 $U \subseteq V$ ($U \neq \emptyset$)가 원래 $V$에서 사용하는 연산자들을 그대로 적용했을 때 스스로도 완벽한 벡터 공간을 형성할 경우, 이를 $V$의 **부분공간(또는 선형 부분공간)**이라 부르고 $U \subseteq V$로 표기합니다.

### 부분공간 판정을 위한 3가지 간소화 조건
대부분의 성질(분배법칙, 결합법칙 등)은 원래 공간 $V$로부터 자연스럽게 유전되므로, 어떤 집합 $U$가 부분공간인지 검증하기 위해서는 다음 3가지만 체크하면 됩니다:
1. $U$가 공집합이 아니어야 한다 (특히 **영벡터 $\mathbf{0}$을 반드시 포함**해야 함: $\mathbf{0} \in U$).
2. 스칼라배 연산에 대해 닫혀 있어야 한다 ($\forall \lambda \in \mathbb{R}, \; \mathbf{x} \in U \implies \lambda \mathbf{x} \in U$).
3. 덧셈 연산에 대해 닫혀 있어야 한다 ($\forall \mathbf{x}, \mathbf{y} \in U \implies \mathbf{x} + \mathbf{y} \in U$).

* **중요 특징**: 
  * 동차 선형연립방정식 $\mathbf{A}\mathbf{x} = \mathbf{0}$의 해집합은 언제나 $\mathbb{R}^n$의 부분공간을 이룹니다. 반면, 우변이 0이 아닌 비동차 연립방정식 $\mathbf{A}\mathbf{x} = \mathbf{b}$의 해집합은 영벡터를 포함할 수 없으므로(즉, $\mathbf{A}\mathbf{0} = \mathbf{0} \neq \mathbf{b}$), **부분공간이 될 수 없습니다** (Figure 2.6 참조).
  * 모든 실수 부분공간 $U \subseteq \mathbb{R}^n$은 항상 적절한 동차 선형방정식 시스템 $\mathbf{A}\mathbf{x} = \mathbf{0}$의 해공간으로 표현될 수 있습니다.

---

# 2.5 선형 독립 (Linear Independence)

벡터 공간 내에서 중복되는 정보 없이 최소한의 필수적인 벡터 집합만을 가려내기 위한 선형 독립성과 종속성의 대수적 성질을 탐구합니다.

### [정의 2.11] 선형 결합 (Linear Combination)
벡터 공간 $V$ 내의 유한한 벡터 집합 $\{\mathbf{x}_1, \dots, \mathbf{x}_k\} \subseteq V$와 실수 계수 $\lambda_1, \dots, \lambda_k \in \mathbb{R}$에 대하여, 다음과 같이 가중합으로 나타낸 임의의 벡터 $\mathbf{v}$를 이 벡터들의 **선형 결합**이라 부릅니다.
$$\mathbf{v} = \lambda_1\mathbf{x}_1 + \dots + \lambda_k\mathbf{x}_k = \sum_{i=1}^{k} \lambda_i\mathbf{x}_i \in V \tag{2.65}$$

### [정의 2.12] 선형 독립과 선형 종속
벡터 집합 $\{\mathbf{x}_1, \dots, \mathbf{x}_k\} \subseteq V$에 대하여, 영벡터를 만드는 선형 결합 수식
$$\lambda_1\mathbf{x}_1 + \dots + \lambda_k\mathbf{x}_k = \mathbf{0}$$
을 충족하는 해가 **오직 $\lambda_1 = \dots = \lambda_k = 0$인 트리비얼한 해(trivial solution)만 존재**할 때 이 벡터들을 **선형 독립(linearly independent)**이라고 정의합니다.
만약 계수 중 적어도 하나라도 0이 아닌 성분이 존재하면서 영벡터를 만들어낼 수 있다면(non-trivial solution), 이 벡터들은 **선형 종속(linearly dependent)**이라고 정의합니다.

* **지리적 직관 비유**: 
  나이로비에서 출발하여 키갈리로 갈 때 "북서쪽으로 506km 이동 후 남서쪽으로 374km 이동하라"는 지시는 독립적입니다. 북서 방향 화살표와 남서 방향 화살표는 서로의 배수로 표현될 수 없습니다. 그러나 여기에 "서쪽으로 751km 이동하라"는 정보를 추가하는 순간, 이 세 번째 화살표는 앞의 두 화살표의 조합으로 완전 대체가 가능하므로 전체 지시 집합은 **중복(선형 종속)**이 됩니다 (Figure 2.7 참조).

### 가우스 소거법을 통한 선형 독립 판정
주어진 벡터 $\mathbf{x}_1, \dots, \mathbf{x}_k \in \mathbb{R}^n$들의 선형 독립 여부를 판정하기 위한 가장 명확한 알고리즘 절차는 다음과 같습니다:
1. 해당 벡터들을 행렬의 **열(Columns)**로 가지는 계수행렬 $\mathbf{A} = [\mathbf{x}_1 \mid \dots \mid \mathbf{x}_k]$를 빌드합니다.
2. 가우스 소거법을 가하여 사다리꼴 행렬(REF) 형태로 변환합니다.
3. 이 때 **행렬의 모든 열이 피벗(Pivot) 열이 된다면 선형 독립**입니다. 만약 피벗이 존재하지 않는 비피벗 열이 하나라도 발생하면, 그 열벡터는 좌측에 있는 독립 벡터들의 선형 결합으로 표현 가능하다는 뜻이므로 **선형 종속**입니다 (식 (2.66) 예시 및 Example 2.14 참조).

---

# 2.6 기저와 랭크 (Basis and Rank)

벡터 공간을 스팬하는 뼈대가 되는 기저 벡터의 집합과 행렬이 지니는 고유 차원 정보인 랭크에 대해 서술합니다.

### 2.6.1 생성 집합과 기저 (Generating Set and Basis)

### [정의 2.13] 생성 집합과 스팬 (Span)
벡터 공간 $V$ 내의 부분집합 $A = \{\mathbf{x}_1, \dots, \mathbf{x}_k\} \subseteq V$에 대하여, 이 벡터들의 가능한 모든 선형 결합 결과를 모아놓은 집합을 $A$의 **스팬(span)**이라 부르고 $\text{span}[A]$ 혹은 $\text{span}[\mathbf{x}_1, \dots, \mathbf{x}_k]$ 로 표기합니다. 만약 이 스팬 결과가 공간 $V$ 전체와 일치한다면($V = \text{span}[A]$), 집합 $A$를 $V$의 **생성 집합(generating set)**이라고 부릅니다.

### [정의 2.14] 기저 (Basis)
어떤 벡터 공간 $V$의 생성 집합 $A \subseteq V$ 중에서, 그보다 더 작은 진부분집합이 $V$를 스팬할 수 없도록 설계된 **최소한의 생성 집합**을 **기저**라고 부릅니다.
기저는 다음 3가지 수학적 명제와 완전히 동치입니다:
1. $B$는 $V$의 **최소 생성 집합**이다.
2. $B$는 $V$에서 취할 수 있는 **극대 선형 독립 집합**이다. (기저 외에 다른 어떤 벡터라도 기저 집합에 추가하면 즉시 선형 종속이 됨)
3. $V$ 내의 모든 벡터 $\mathbf{x}$는 기저 벡터들의 선형 결합으로 **단 한 가지만 존재하도록 유일하게 표현**된다. (식 (2.77) 참조)

* **차원 (Dimension)**:
  임의의 벡터 공간 $V$를 형성하는 기저 벡터들의 총 개수를 그 공간의 **차원**이라 부르고 $\dim(V)$로 씁니다. 차원은 공간 내에서 움직일 수 있는 독립적인 방향의 수입니다. 

---

### [알고리즘] 부분공간의 기저를 찾아내는 방법
어떤 부분공간 $U = \text{span}[\mathbf{x}_1, \dots, \mathbf{x}_m] \subseteq \mathbb{R}^n$이 임의의 생성 벡터들로 주어졌을 때, 참 기저(True Basis)를 추출하는 공식 절차입니다:
1. 생성 벡터들을 행렬의 **열**로 배치하여 $\mathbf{A} = [\mathbf{x}_1 \mid \dots \mid \mathbf{x}_m]$을 만듭니다.
2. 가우스 소거법을 가하여 사다리꼴 행렬(REF)을 유도합니다.
3. **피벗(Pivot)이 존재하는 열에 대응되는 원본 벡터들**만을 수집하면, 이들이 $U$의 가장 깔끔한 최소 기저가 됩니다. (Example 2.17 상세 유도 참조)

---

### 2.6.2 랭크 (Rank, 계수)

임의의 행렬 $\mathbf{A} \in \mathbb{R}^{m \times n}$에서 선형 독립을 유지하는 최대 열(column)의 개수는 놀랍게도 선형 독립을 유지하는 최대 행(row)의 개수와 완벽히 일치하며, 이를 행렬의 **랭크**라 정의하고 $\text{rk}(\mathbf{A})$로 표기합니다.

### 랭크의 대수적 성질
* $\text{rk}(\mathbf{A}) = \text{rk}(\mathbf{A}^{\top})$
* $\mathbf{A} \in \mathbb{R}^{m \times n}$의 열들이 그리는 스팬 공간(열 공간, Column Space)의 차원은 $\text{rk}(\mathbf{A})$와 같습니다.
* $n \times n$ 정사각 행렬 $\mathbf{A}$가 역행렬을 가질(regular) 필요충분조건은 $\text{rk}(\mathbf{A}) = n$인 것입니다.
* 연립선형방정식 $\mathbf{A}\mathbf{x} = \mathbf{b}$가 해를 가질(solvable) 필요충분조건은 원래 계수행렬의 랭크와 우변을 포함한 첨가행렬의 랭크가 일치하는 것입니다:
  $$\text{rk}(\mathbf{A}) = \text{rk}([\mathbf{A} \mid \mathbf{b}])$$
* 동차 연립방정식 $\mathbf{A}\mathbf{x} = \mathbf{0}$의 해공간(Kernel)의 차원은 다음과 같이 결정됩니다:
  $$\dim(\ker(\mathbf{A})) = n - \text{rk}(\mathbf{A})$$
* **풀 랭크 (Full Rank)**: 행렬의 랭크가 가질 수 있는 최댓값에 도달했을 때(즉, $\text{rk}(\mathbf{A}) = \min(m, n)$) 이를 풀 랭크 행렬이라 부르고, 그보다 작으면 **랭크 결손(rank deficient)** 행렬이라 합니다.

---

# 2.7 선형 사상 (Linear Mappings)

선형 사상은 벡터 공간 고유의 대수적 성질(덧셈과 스칼라배)을 왜곡하지 않고 그대로 유지하면서, 하나의 벡터 공간을 다른 벡터 공간으로 대응시키는 함수입니다.

### [정의 2.15] 선형 사상 (Linear Mapping)
두 실수 벡터 공간 $V, W$에 대하여, 다음 덧셈 보존성과 스칼라배 보존성을 충족하는 함수 $\Phi : V \to W$를 **선형 사상(또는 벡터 공간 동형사상/선형 변환)**이라 정의합니다.
$$\forall \mathbf{x}, \mathbf{y} \in V, \; \forall \lambda, \psi \in \mathbb{R} : \Phi(\lambda\mathbf{x} + \psi\mathbf{y}) = \lambda\Phi(\mathbf{x}) + \psi\Phi(\mathbf{y}) \tag{2.87}$$

* **단사/전사/전단사 (Definition 2.16)**:
  * **단사 (Injective)**: 다른 원소는 다른 상으로 간다. ($\Phi(\mathbf{x}) = \Phi(\mathbf{y}) \implies \mathbf{x} = \mathbf{y}$)
  * **전사 (Surjective)**: 공역의 모든 원소가 화살표를 받는다. ($\Phi(V) = W$)
  * **전단사 (Bijective)**: 단사면서 동시에 전사다. 이 때 역함수 $\Phi^{-1}$가 정의됩니다.
* **선형 사상의 특수 분류**:
  * **Isomorphism (동형 사상)**: 전단사인 선형 사상.
  * **Endomorphism (단일 공간 사상)**: 정의역과 공역이 같은 선형 사상 ($\Phi : V \to V$).
  * **Automorphism (자기 동형 사상)**: 전단사이면서 동시에 정의역과 공역이 같은 선형 사상.

### [정리 2.17] 차원과 동형 관계
> 유한 차원 벡터 공간 $V$와 $W$가 대수적으로 동형(isomorphic)일 필요충분조건은 두 공간의 차원이 같은 것이다: $\dim(V) = \dim(W)$.

이 정리는 매우 중대한 직관을 부여합니다. 차원이 같다면 기하학적인 모양이 다소 달라 보일지라도 수학적으로는 완벽히 동치인 공간임을 뜻합니다. 예컨대, 실수 행렬 공간 $\mathbb{R}^{m \times n}$과 $mn$차원 열벡터 공간 $\mathbb{R}^{mn}$은 차원이 $mn$으로 같으므로, 아무런 정보 손실 없이 일대일로 완벽하게 변환해 가며 다룰 수 있습니다.

---

### 2.7.1 선형 사상의 행렬 표현

유한 차원 벡터 공간 사이의 임의의 선형 사상은 특정한 **행렬과의 곱셈**으로 완벽히 치환되어 계산될 수 있습니다.

### [정의 2.19] 표현/변환 행렬 (Transformation Matrix)
벡터 공간 $V$의 순서 기저 $B = (\mathbf{b}_1, \dots, \mathbf{b}_n)$과 $W$의 순서 기저 $C = (\mathbf{c}_1, \dots, \mathbf{c}_m)$이 주어지고, 선형 사상 $\Phi : V \to W$가 존재할 때, 각 기저 벡터의 상 $\Phi(\mathbf{b}_j)$를 $W$의 기저 $C$의 선형결합으로 고유하게 나타냅니다:
$$\Phi(\mathbf{b}_j) = \sum_{i=1}^{m} \alpha_{ij}\mathbf{c}_i \tag{2.92}$$
이 때의 계수 $\alpha_{ij}$를 성분으로 갖는 $m \times n$ 행렬 $\mathbf{A}_{\Phi}$를 이 선형 사상의 **변환 행렬**이라 부릅니다.
* $\mathbf{A}_{\Phi}$의 $j$번째 열벡터는 $\mathbf{b}_j$의 상인 $\Phi(\mathbf{b}_j)$를 기저 $C$ 기준으로 바라본 좌표 벡터에 대응합니다.
* 어떤 벡터 $\mathbf{x} \in V$의 기저 $B$ 하에서의 좌표가 $\hat{\mathbf{x}}$이고, 그 상인 $\mathbf{y} = \Phi(\mathbf{x}) \in W$의 기저 $C$ 하에서의 좌표가 $\hat{\mathbf{y}}$라면, 다음 행렬 곱 연산이 성립합니다:
  $$\hat{\mathbf{y}} = \mathbf{A}_{\Phi}\hat{\mathbf{x}} \tag{2.94}$$
  (구체적인 사상 매핑 및 대칭/회전/밀림의 기하 변환 행렬 예시는 Example 2.21, 2.22 및 Figure 2.10 참조)

---

### 2.7.2 기저 변환 (Basis Change)

정의역과 공역의 기저가 다른 새로운 기저로 바뀔 때, 선형 사상을 대수적으로 표현하는 변환 행렬이 어떻게 전환되는지 분석합니다.

### [정리 2.20] 기저 변환 (Basis Change)
선형 사상 $\Phi : V \to W$가 있고, $V$의 구기저 $B$와 신기저 $\tilde{B}$, $W$의 구기저 $C$와 신기저 $\tilde{C}$가 주어졌다고 합시다. 구기저 기준의 변환 행렬이 $\mathbf{A}_{\Phi}$일 때, 신기저 기준의 변환 행렬 $\tilde{\mathbf{A}}_{\Phi}$는 다음과 같이 계산됩니다:
$$\tilde{\mathbf{A}}_{\Phi} = \mathbf{T}^{-1}\mathbf{A}_{\Phi}\mathbf{S} \tag{2.105}$$
* $\mathbf{S} \in \mathbb{R}^{n \times n}$는 신기저 $\tilde{B}$의 좌표를 구기저 $B$의 좌표로 변환해주는 항등 사상의 좌표 변환 행렬입니다 (각 열은 신기저 벡터를 구기저로 표현한 좌표).
* $\mathbf{T} \in \mathbb{R}^{m \times m}$는 신기저 $\tilde{C}$의 좌표를 구기저 $C$의 좌표로 변환해주는 좌표 변환 행렬입니다.

### [유도 과정] 기저 변환 공식의 증명
신기저 벡터의 상 $\Phi(\tilde{\mathbf{b}}_j)$를 두 가지 관점으로 쪼개어 분석합니다.
1. **첫 번째 관점**: 신기저 공간 $W(\tilde{C})$ 상에서 다이렉트 변환 행렬 $\tilde{\mathbf{A}}_{\Phi}$를 적용한 뒤 이를 다시 구기저 $C$의 결합으로 번역합니다.
   $$\Phi(\tilde{\mathbf{b}}_j) = \sum_{k=1}^{m} \tilde{a}_{kj}\tilde{\mathbf{c}}_k = \sum_{k=1}^{m} \tilde{a}_{kj}\left( \sum_{l=1}^{m} t_{lk}\mathbf{c}_l \right) = \sum_{l=1}^{m} \left( \sum_{k=1}^{m} t_{lk}\tilde{a}_{kj} \right)\mathbf{c}_l \tag{2.108}$$
2. **두 번째 관점**: 정의역 측에서 신기저 벡터 $\tilde{\mathbf{b}}_j$를 구기저 $B$의 결합으로 먼저 번역한 다음, 구기저 사상 $\mathbf{A}_{\Phi}$를 통과시킵니다.
   $$\Phi(\tilde{\mathbf{b}}_j) = \Phi\left( \sum_{i=1}^{n} s_{ij}\mathbf{b}_i \right) = \sum_{i=1}^{n} s_{ij}\Phi(\mathbf{b}_i) = \sum_{i=1}^{n} s_{ij}\left( \sum_{l=1}^{m} a_{li}\mathbf{c}_l \right) = \sum_{l=1}^{m} \left( \sum_{i=1}^{n} a_{li}s_{ij} \right)\mathbf{c}_l \tag{2.109}$$

두 관점의 최종 기저 $\mathbf{c}_l$ 앞의 계수가 완벽히 같아야 하므로 모든 $l, j$에 대해 다음이 만족합니다:
$$\sum_{k=1}^{m} t_{lk}\tilde{a}_{kj} = \sum_{i=1}^{n} a_{li}s_{ij} \quad \Longrightarrow \quad \mathbf{T}\tilde{\mathbf{A}}_{\Phi} = \mathbf{A}_{\Phi}\mathbf{S} \quad \Longrightarrow \quad \tilde{\mathbf{A}}_{\Phi} = \mathbf{T}^{-1}\mathbf{A}_{\Phi}\mathbf{S} \tag{2.112}$$
(실제 좌표 매핑 흐름도는 Figure 2.11의 대수도식 참조)

* **행렬의 동치 (Equivalence, Definition 2.21)**: 가역 행렬 $\mathbf{S}, \mathbf{T}$에 대해 $\tilde{\mathbf{A}} = \mathbf{T}^{-1}\mathbf{A}\mathbf{S}$를 만족하면 두 행렬은 동치라고 정의합니다.
* **행렬의 닮음 (Similarity, Definition 2.22)**: 단일 공간 사상(정사각 행렬)에서 동일한 기저 변환이 가해져 $\tilde{\mathbf{A}} = \mathbf{S}^{-1}\mathbf{A}\mathbf{S}$가 성립하면 두 행렬은 닮음이라고 정의합니다. (Ch.4 고윳값 분해와 대각화의 토대)

---

### 2.7.3 상과 핵 (Image and Kernel)

선형 사상이 거치는 대표적인 두 부분공간인 **핵(Kernel)**과 **상(Image)**을 정의합니다.

### [정의 2.23] 핵과 상
선형 사상 $\Phi : V \to W$에 대하여:
$$\text{ker}(\Phi) := \Phi^{-1}(\mathbf{0}_W) = \{\mathbf{v} \in V \mid \Phi(\mathbf{v}) = \mathbf{0}_W\} \tag{2.122}$$
$$\text{Im}(\Phi) := \Phi(V) = \{\mathbf{w} \in W \mid \exists \mathbf{v} \in V: \Phi(\mathbf{v}) = \mathbf{w}\} \tag{2.123}$$
* **핵 (Kernel, Null Space)**: 사상 통과 후 공역의 **영벡터로 붕괴되어 사라지는** 정의역 내 벡터들의 집합입니다. (동차 연립방정식의 해집합과 동일)
* **상 (Image, Range)**: 사상을 타고 넘어가서 공역 상에 **도달 가능한** 실제 벡터들의 자취입니다. 행렬 표기법 상으로는 계수행렬의 열벡터들의 스팬 공간인 **열 공간(Column Space)**과 정확히 일치합니다.
* **단사 판정**: 선형 사상 $\Phi$가 일대일(Injective) 함수가 될 필요충분조건은 핵이 오직 영벡터로만 구성되는 것입니다: $\text{ker}(\Phi) = \{\mathbf{0}_V\}$

### [정리 2.24] 차원 정리 (Rank-Nullity Theorem)
> 유한 차원 공간 상의 선형 사상 $\Phi : V \to W$에 대하여, 핵의 차원과 상의 차원의 합은 언제나 정의역의 원래 차원과 일치한다:
> $$\dim(\text{ker}(\Phi)) + \dim(\text{Im}(\Phi)) = \dim(V) \tag{2.129}$$

이 정리는 매우 중대한 기하적 물리 보존법칙을 나타냅니다. 전체 차원 $\dim(V)$ 중 랭크 크기만큼 공간 상에 상으로 보존되어 살아남고, 나머지 차원은 영벡터로 납작하게 눌려 핵 공간 속으로 붕괴된다는 원리입니다.

---

# 2.8 아핀 공간 (Affine Spaces)

현실 세계의 직선이나 평면은 좌표계 원점($\mathbf{0}$)을 지나지 않는 경우가 흔합니다. 원점을 지나지 않는 오프셋 공간을 선형대수학으로 포섭하기 위해 **아핀 공간**을 활용합니다.

### 2.8.1 아핀 부분공간 (Affine Subspaces)

### [정의 2.25] 아핀 부분공간 (Affine Subspace)
벡터 공간 $V$와 임의의 고정된 오프셋 벡터 $\mathbf{x}_0 \in V$, 그리고 표준 부분공간 $U \subseteq V$에 대하여 다음과 같이 표현되는 부분집합 $L$을 $V$의 **아핀 부분공간(또는 선형 다양체, linear manifold)**이라 정의합니다.
$$L = \mathbf{x}_0 + U := \{\mathbf{x}_0 + \mathbf{u} \mid \mathbf{u} \in U\} \tag{2.130}$$
* $\mathbf{x}_0$를 **지지점(support point)**, 부분공간 $U$를 아핀 공간이 뻗어나가는 **방향 공간(direction space)**이라 지칭합니다. (머신러닝 Ch.12 SVM 등에서는 이를 **초평면, hyperplane**이라고 부름)
* 만약 지지점 $\mathbf{x}_0$가 부분공간 $U$ 내에 존재하지 않는다면 이 아핀 공간은 영벡터 $\mathbf{0}$을 포함할 수 없으므로, **표준 벡터 공간의 조건을 만족하지 못합니다**.

### 아핀 공간의 차원별 분류
* **1차원 아핀 부분공간**: **직선 (Line)**. $\mathbf{y} = \mathbf{x}_0 + \lambda \mathbf{b}_1$. 지지점과 1개의 방향 기저 벡터로 정의 (Figure 2.13 참조).
* **2차원 아핀 부분공간**: **평면 (Plane)**. $\mathbf{y} = \mathbf{x}_0 + \lambda_1 \mathbf{b}_1 + \lambda_2 \mathbf{b}_2$. 지지점과 2개의 독립 방향 벡터로 정의.
* **$n-1$차원 아핀 부분공간**: **초평면 (Hyperplane)**. 전체 차원이 $n$일 때 $n-1$차원을 갖는 경계면 공간.

> [!IMPORTANT]
> 임의의 비동차 연립방정식 $\mathbf{A}\mathbf{x} = \mathbf{b}$ ($\mathbf{b} \neq \mathbf{0}$)의 해집합은 언제나 $\mathbf{x}_0 + \text{ker}(\mathbf{A})$ 형태의 **아핀 부분공간**을 형성하며, 그 차원은 $\dim = n - \text{rk}(\mathbf{A})$가 됩니다.

---

### 2.8.2 아핀 사상 (Affine Mappings)

선형 사상에 지지점 방향으로의 평행 이동 연산을 조합한 상위 개념의 사상입니다.

### [정의 2.26] 아핀 사상 (Affine Mapping)
두 벡터 공간 $V, W$와 선형 사상 $\Phi : V \to W$, 그리고 공역 내의 평행 이동 벡터 $\mathbf{a} \in W$에 대하여 다음과 같이 매핑되는 함수 $\phi$를 **아핀 사상**이라 정의합니다.
$$\phi : V \to W, \quad \mathbf{x} \mapsto \mathbf{a} + \Phi(\mathbf{x}) \tag{2.132}$$
* 모든 아핀 사상은 선형 변환 $\Phi$를 거친 후에 평행 이동 변환 $\tau$를 적용하는 합성 함수 구조 $\phi = \tau \circ \Phi$로 고유하게 정의됩니다.
* 두 아핀 사상의 합성 사상 역시 항상 아핀 사상입니다.

---

# Related Concepts
* [MML Study Index](index.md)
* [ML Index](../index.md)

# Citations
* [Marc Peter Deisenroth, A. Aldo Faisal, Cheng Soon Ong, *Mathematics for Machine Learning* (Chapter 2)](../../../raw/notes/math_for_deeplearning/mml-book.pdf)
