---
type: Project
title: "Chapter 16-1: Student Management System (학생관리시스템 SMS 개발 화면 UI 정의서)"
description: "Java Swing과 MySQL 데이터베이스 연동을 기반으로 설계된 학사 행정 최적화용 학생관리시스템(SMS)의 서비스 설계, DB ERD 및 화면 UI 상세 사양을 분석합니다."
tags: [java, project, swing, mysql, ui-specification, db-design]
timestamp: 2026-06-19
status: active
---

# Goal
- **기획 서비스**: 학생관리시스템 (SMS, Student Management System)
- **기획 배경**: 학사 행정 관리 업무의 무결성을 확보하고 보안을 강화하기 위해, 파편화된 데이터를 단일 데이터베이스(RDBMS)로 통폐합하여 실시간으로 통제할 수 있는 시스템 구축이 요구됨.
- **기획 목적**:
  - 학생 인적 사항의 체계적인 전산 등록 및 정보 관리.
  - 학과 정보 및 학생 신상 정보의 실시간 동기화.
  - 학사 행정 서비스 운영 시 관리자 및 학생의 업무 편의성 극대화.
- **기대 효과**:
  - 서류 기반 수동 검증 대비 업무 처리 시간 **40% 단축**.
  - 데이터 유실 및 수동 입력 예외로 인한 휴먼 에러 발생률 **95% 감소**.
  - 직관적인 그래픽 인터페이스(UI)를 통한 학사 정보 조회 및 변경 편의성 제공.

# Current Status
- **채널/플랫폼**: 데스크톱 애플리케이션 (PC 타겟)
- **출시 예정**: 2026년 9월
- **구현 단계**: 현재 요구사항 정의 및 DB 모델링, 화면 UI 상세 설계서(Story Board) 작성이 완료된 v.0.1 상태이며, 향후 MVC 패턴 코드 구현 및 JDBC 연동 코딩 단계 진입 예정.

# Structure

### 1. 기술 스택 (System Tech Stack)
- **Front-end**: Java Swing (MVC 아키텍처 아키텍처 적용)
- **Back-end**: JDBC API & Custom MySQL Handler
- **Database**: MySQL Server 8.0
- **Library**: MySQL Connector/J (JDBC Driver)

### 2. 사용자 프로세스 (User Process Flow)
```
[시스템 구동] ──▶ [로그인 화면(SMS-01)] ──▶ [DB 인증 처리] ──▶ [대시보드 진입(SMS-02)]
                                                                       │
                         ┌─────────────────────────────────────────────┴──────────────┐
                         ▼                                                            ▼
                 [일반 학생 권한]                                              [학사 관리자 권한]
                         │                                                            │
         ┌───────────────┴───────────────┐                             ┌──────────────┴──────────────┐
         ▼                               ▼                             ▼              ▼              ▼
   [학생정보수정]                    [로그아웃]                  [학생정보등록]   [학과학생조회]   [로그아웃]
    (SMS-03)                          (SMS-02)                     (SMS-04)        (SMS-05)        (SMS-02)
```

### 3. 데이터베이스 설계 (ERD 상세 사양)

#### A. 학과 정보 테이블 (`departments`)
- **설명**: 대학 내 개설된 학과 정보를 관리하는 마스터 테이블.
- **칼럼 사양**:
  | Column | Type | Constraint | Description |
  |---|---|---|---|
  | `dept_code` | VARCHAR(10) | PK, NOT NULL | 학과 코드 (예: CS, ME 등) |
  | `dept_name` | VARCHAR(50) | NOT NULL | 학과명 (예: 컴퓨터공학, 기계공학 등) |

#### B. 학생 정보 테이블 (`students`)
- **설명**: 재학생의 인적 정보 및 로그인 자격 증명을 관리하는 테이블.
- **칼럼 사양**:
  | Column | Type | Constraint | Description |
  |---|---|---|---|
  | `student_id` | VARCHAR(15) | PK, NOT NULL | 학번 (로그인 ID 겸용) |
  | `password` | VARCHAR(100) | NOT NULL | 비밀번호 (평문 또는 해싱 처리 값) |
  | `name` | VARCHAR(30) | NOT NULL | 성명 |
  | `dept_code` | VARCHAR(10) | FK (departments.dept_code) | 소속 학과 코드 |
  | `phone` | VARCHAR(20) | NULL 허용 | 연락처 |

#### C. 관리자 계정 테이블 (`admins`)
- **설명**: 학사 시스템에 접속하여 학생을 등록/조회할 수 있는 최고 권한자 계정 테이블.
- **칼럼 사양**:
  | Column | Type | Constraint | Description |
  |---|---|---|---|
  | `admin_id` | VARCHAR(15) | PK, NOT NULL | 관리자 ID (로그인 ID) |
  | `password` | VARCHAR(100) | NOT NULL | 비밀번호 |
  | `admin_name` | VARCHAR(30) | NOT NULL | 관리자 성명 |

# How to Run
본 설계 사양을 바탕으로 코드를 구현하고 기동하는 가이드라인입니다.
1. **RDBMS 스키마 준비**: MySQL Server에 접속하여 `departments`, `students`, `admins` 테이블 생성 스크립트를 실행하고 초기 학과 데이터 및 관리자 가상 계정을 수동 삽입합니다.
2. **IDE 라이브러리 연동**: Eclipse 또는 IntelliJ 프로젝트의 Build Path에 `mysql-connector-java-8.0.XX.jar` 드라이버를 등록합니다.
3. **소스 컴파일 및 실행**: 메인 GUI 프레임 런처 클래스(`MainApp` 또는 `LoginView`)를 찾아 컴파일 및 Java Application 실행을 누르면 메인 로그인 폼(SMS-01)이 팝업됩니다.

# Key Decisions
- **권한별 역할 분리**: 로그인한 유저의 역할(Role)이 학생인지 관리자인지에 따라 대시보드의 활성 기능을 이원화하여 보안과 조작 권한을 격리함.
- **RDBMS FK 물리 제약 설정**: 학생 정보 추가(SMS-04) 시 가상의 존재하지 않는 학과 코드가 기입되는 것을 방지하기 위해 `students.dept_code` 칼럼에 `departments.dept_code`를 참조하는 Foreign Key 제약을 강제하여 참조 무결성을 보존함.

# UI Specification (화면 설계 사양)

### SMS-01: 메인화면 (로그인)
- **UI 구성**: 
  - 학생 및 관리자 구분을 위한 **라디오 버튼(Radio Button)** 제공.
  - 학번(아이디) 및 비밀번호 입력을 위한 텍스트 필드/패스워드 필드 배치.
  - 하단에 [로그인] 버튼 배치.
- **동작 시나리오 & 팝업 메시지**:
  - **로그인 성공 (학생)**: "??? 학생님 환영합니다." 얼럿 메시지 출력 후 학생용 대시보드로 리다이렉트.
  - **로그인 성공 (관리자)**: "??? 관리자님 환영합니다." 얼럿 메시지 출력 후 관리자용 대시보드로 리다이렉트.
  - **입력 필드 미기입**: 아이디나 비번 필드가 비어있을 때 [로그인] 클릭 시 "아이디와 비밀번호를 모두 입력해주세요." 메시지 발생.
  - **인증 불합격**: 잘못된 ID/PW 입력 시 "학번 또는 비밀번호를 확인하세요." 예외 안내창 출력.

### SMS-02: 대시보드 (Dashboard)
- **UI 구성**:
  - **학생 대시보드**: 로그인 정보 확인 영역("??? 학생님, 환영합니다.") 및 [학생정보수정], [로그아웃] 기능 메뉴 제공.
  - **관리자 대시보드**: 로그인 정보 확인 영역("??? 관리자님, 환영합니다.") 및 [학생정보조회], [학생정보추가], [로그아웃] 기능 메뉴 제공.
- **동작 시나리오**:
  - [로그아웃] 버튼 클릭 시, "로그아웃 하시겠습니까?" 메시지와 함께 [예], [아니오] 선택 모달창 팝업. [예] 클릭 시 세션을 클리어하고 로그인 폼(SMS-01)으로 귀환.

### SMS-03: 학생정보수정 (Student Modification)
- **UI 구성**:
  - 학번(로그인한 학생 본인의 학번 자동 매핑 및 비활성/Read-only 처리).
  - 변경할 [비밀번호] 및 [연락처] 입력 텍스트 필드.
  - 하단에 [수정] 실행 버튼 배치.
- **동작 시나리오**:
  - 필드 변경 후 [수정]을 클릭하면 데이터베이스에 `UPDATE students SET password = ?, phone = ? WHERE student_id = ?` 구문이 동작하고, 정상 수정 시 "수정 완료되었습니다." 메시지가 뜨며 이전 대시보드로 회귀.

### SMS-04: 학생정보등록 (Admin - Register Student)
- **UI 구성**:
  - 관리자가 입력할 학번, 비밀번호, 성명, 연락처 필드.
  - 학과 선택을 위한 **콤보박스(Combo Box)** 제공. 이 콤보박스의 리스트는 하드코딩되지 않고 데이터베이스 `departments` 테이블의 `dept_name` 목록을 읽어와 실시간 바인딩 처리함.
  - 하단에 [등록] 버튼 배치.
- **동작 시나리오**:
  - 관리자가 정보 입력 후 [등록]을 누르면 `INSERT` 구문이 작동하여 신규 재학생 계정이 생성되며, 성공 시 "등록 완료" 창을 표시하고 입력 폼을 리셋.

### SMS-05: 학과학생조회 (Admin - Department Query)
- **UI 구성**:
  - 상단에 검색 필터링을 위한 학과 선택 **콤보박스**와 [조회] 버튼 배치.
  - 하단에 엑셀 표 형태의 그리드 컴포넌트인 **JTable** 배치 (학번, 성명, 연락처 칼럼 정의).
- **동작 시나리오**:
  - 콤보박스에서 특정 학과를 선택하고 [조회]를 클릭하면 `SELECT name, id, phone FROM student WHERE dept_code = (선택한 학과의 코드)`와 같은 형태의 질의어가 수행되어 JTable의 로우(Row) 데이터로 바인딩되어 출력됨.

# Issues
- **비밀번호 평문 저장 취약점**: 초기 v.0.1 기획안에는 `students` 및 `admins` 테이블의 `password` 칼럼이 평문으로 관리되는 것으로 상정되어 있어, DB 노출 시 중대한 프라이버시 침해가 발생할 수 있음.
- **네트워크 레이턴시**: Swing UI 렌더링 스레드(Event Dispatch Thread)에서 무거운 JDBC 커넥션 및 쿼리 실행을 동기식으로 호출할 경우, 데이터베이스 응답 속도가 지연되면 UI 화면 전체가 먹통(Freeze) 상태가 되는 현상이 예측됨.

# Next Actions
- [ ] **패스워드 암호화**: SHA-256 또는 BCrypt 알고리즘을 추가하여 자바단에서 단방향 암호화 처리 후 DB에 적재하도록 계정 보안 모델 업그레이드.
- [ ] **비동기 쿼리 처리**: `SwingWorker` 클래스를 도입하여 네트워크 접근 및 DB 질의는 백그라운드 스레드에서 돌리고, 렌더링 스레드만 갱신하는 비동기 UI 처리 모델 구현.
- [ ] **UI 밸리데이션 강화**: 학번 필드 글자 수 제한(15자 내), 연락처 하이픈 형식 정규식 체크 로직 추가.

# Related Concepts
- **외래키 제약조건 (Foreign Key Constraint)**: 릴레이션 간 연관 관계를 유효하게 보장하며 데이터 불일치를 원천 방지하는 메커니즘.
- **데이터 바인딩 (Data Binding)**: RDBMS 결과 데이터 모델(`ResultSet`)을 화면 프레임워크 컴포넌트(JTable, JComboBox)에 유기적으로 투영하여 변경사항을 투명하게 동기화시키는 기술.

# Citations
* [16-1sms_miniproject.pdf](../../../raw/notes/java/16-1sms_miniproject.pdf)
