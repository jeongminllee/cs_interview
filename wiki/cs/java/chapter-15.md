---
type: Study Note
title: "Chapter 15: Java Database Connectivity (JDBC)"
description: "자바와 관계형 데이터베이스 관리시스템(RDBMS)을 연동하기 위한 표준 기술인 JDBC의 개념, 아키텍처 및 핵심 API(Connection, Statement, ResultSet)의 활용법을 분석합니다."
tags: [java, database, jdbc, sql, mysql, resultset]
timestamp: 2026-06-19
status: active
---

# Summary
JDBC(Java Database Connectivity)는 자바 프로그램이 RDBMS에 접속하고 SQL 질의를 수행하여 그 결과를 처리할 수 있도록 인터페이스를 제공하는 표준 자바 API입니다. 특정 DB 엔진에 종속되지 않는 독립적 프로그래밍을 지원하며, 본 문서에서는 환경 구축법, DB 기본 조작(CRUD) SQL문, 그리고 연결 및 트랜잭션 수행에 핵심적인 클래스군(`DriverManager`, `Connection`, `Statement`, `ResultSet`)의 상세 사용법을 설명합니다.

# Why it matters
- **데이터베이스 독립성**: 애플리케이션 개발자는 각 DB 회사(Oracle, MySQL, PostgreSQL 등)의 상세 프로토콜을 알 필요 없이, 동일한 JDBC API 인터페이스 표준에 맞춰 코드를 작성하고 각 사의 드라이버(`Connector`)만 교체하면 RDBMS를 마이그레이션할 수 있습니다.
- **자원 해제의 의무성**: JDBC 연결 개체는 데이터베이스 서버와의 소켓(Socket) 세션 및 하드웨어 리소스를 사용하므로, 사용 종료 시 가비지 컬렉션(GC)에 의존하지 않고 명시적으로 닫아주지 않으면 서버가 커넥션 풀 부족으로 다운될 수 있습니다.

# Key Ideas

1. **JDBC 아키텍처 구조**:
   - **자바 애플리케이션 (Java Application)**: 표준 JDBC API 호출.
   - **JDBC API (`java.sql`, `javax.sql`)**: 자바 표준인 `Connection`, `Statement`, `ResultSet` 인터페이스 정의.
   - **JDBC 드라이버 매니저 (`DriverManager`)**: 알맞은 드라이버를 로드하고 데이터베이스 연결을 조율.
   - **JDBC 드라이버 (JDBC Driver)**: DB 개발사에서 표준 인터페이스를 구현한 `.jar` 파일 (예: `mysql-connector-j-8.0.31.jar`).
   - **데이터베이스 (Database)**: 실제 SQL 쿼리가 실행되고 데이터가 적재되는 물리 계층.

2. **이클립스 개발 환경 드라이버 경로 지정**:
   - 프로젝트 우클릭 -> **Properties** 선택.
   - **Java Build Path** 메뉴 진입 -> **Libraries** 탭 선택.
   - **Classpath** 영역을 클릭한 후, 우측의 **Add External JARs...** 선택.
   - 다운로드받은 `mysql-connector-java-8.0.XX.jar` (또는 최신 버전의 `mysql-connector-j-8.0.XX.jar`) 파일을 선택하고 적용(**Apply and Close**).

3. **데이터베이스 기본 작업 (MySQL 기준)**:
   - **스키마 생성**: MySQL Workbench 등 클라이언트를 사용하여 데이터베이스 스키마 생성 (예: `sampledb`).
   - **테이블 생성**: 학적 관리를 위한 `student` 테이블 생성.
     ```sql
     CREATE TABLE student (
         name VARCHAR(10) NOT NULL,
         dept VARCHAR(20) NOT NULL,
         id CHAR(7) PRIMARY KEY
     );
     ```
   - **저장할 초기 데이터 예시**:
     | id | name | dept |
     |---|---|---|
     | `1091011` | 김철수 | 컴퓨터시스템 |
     | `0792012` | 최고봉 | 멀티미디어 |
     | `0494013` | 이기자 | 컴퓨터공학 |

4. **핵심 SQL 구문**:
   - **검색 (SELECT)**:
     `SELECT name, dept, id FROM student WHERE dept = '컴퓨터공학';`
   - **추가 (INSERT)**:
     `INSERT INTO student (name, dept, id) VALUES ('김철수', '컴퓨터시스템', '1091011');` (문자형 데이터는 반드시 단일 인용부호 `'`로 감싸야 함)
   - **수정 (UPDATE)**:
     `UPDATE student SET dept = '컴퓨터공학' WHERE name = '최고봉';`
   - **삭제 (DELETE)**:
     `DELETE FROM student WHERE name = '최고봉';`

5. **JDBC 주요 클래스 및 API**:
   - **`Connection` (연결 객체)**:
     - 물리적 데이터베이스와의 세션을 세팅합니다.
     - `DriverManager.getConnection(url, user, password)`를 통해 생성합니다.
     - MySQL의 기본 포트는 `3306`이며, 로컬 시스템인 경우 호스트를 `localhost`로 지정합니다. (예: `jdbc:mysql://localhost:3306/sampledb`)
   - **`Statement` (질의 송신 객체)**:
     - SQL 구문을 실행하여 데이터베이스에 전달하는 역할을 합니다.
     - `Connection.createStatement()` 메서드로 생성합니다.
     - 주요 실행 메서드:
       - `ResultSet executeQuery(String sql)`: SELECT 쿼리를 실행할 때 사용하며, 쿼리 결과를 담은 `ResultSet` 객체를 반환합니다.
       - `int executeUpdate(String sql)`: INSERT, UPDATE, DELETE 등 테이블 내용에 변경을 주는 DML(Data Manipulation Language) 쿼리를 실행할 때 사용하며, 쿼리 수행으로 영향을 받은 행(레코드)의 개수를 반환합니다.
   - **`ResultSet` (결과 집합 객체)**:
     - SELECT 쿼리 수행 후 데이터베이스 서버로부터 리턴된 로우(Row)들을 가리키는 커서(Cursor)를 관리하는 객체입니다.
     - 초기 상태의 커서는 첫 번째 행 이전(Before first row)을 가리키고 있어, 실제 데이터를 추출하기 전에 반드시 커서를 이동시켜야 합니다.
     - **커서 이동 메서드**:
       - `boolean next()`: 커서를 다음 행으로 이동시킵니다. 이동한 행에 데이터가 존재하면 `true`, 없으면 `false`를 리턴하여 루프 제어(`while`)에 핵심적입니다.
       - `boolean previous()`: 커서를 이전 행으로 이동시킵니다.
       - `boolean first()`: 커서를 결과 집합의 첫 번째 행으로 강제 이동시킵니다.
       - `boolean last()`: 커서를 결과 집합의 마지막 행으로 이동시킵니다.
       - `boolean absolute(int row)`: 지정된 행 번호(1-indexed)로 커서를 절대 위치 이동시킵니다.
     - **데이터 추출 메서드 (`getXxx`)**:
       - `getString("칼럼명")` 또는 `getString(칼럼인덱스)` 형식으로 칼럼의 타입에 대응하는 메서드를 호출하여 데이터를 자바 변수로 매핑합니다 (예: `getInt()`, `getDouble()`).

# Examples
자바 애플리케이션에서 MySQL 데이터베이스에 연결하고, 데이터를 삽입, 조회, 수정 및 삭제하는 실무 지향적 소스 코드입니다.

### 1. 데이터베이스 연결 수립 예제
```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JDBC_Connect {
    public static void main(String[] args) {
        Connection conn = null;
        try {
            // MySQL Driver 로드 및 연결 설정 (MySQL 8.0 이상은 자동으로 로드되나 명시적 로드가 보장성 제공)
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            String url = "jdbc:mysql://localhost:3306/sampledb?serverTimezone=UTC&useSSL=false";
            String user = "root";
            String password = "YOUR_PASSWORD_HERE"; // 실제 환경에 맞는 패스워드
            
            conn = DriverManager.getConnection(url, user, password);
            System.out.println("데이터베이스 연결 성공!");
        } catch (ClassNotFoundException e) {
            System.err.println("JDBC 드라이버 로드 실패: " + e.getMessage());
        } catch (SQLException e) {
            System.err.println("데이터베이스 연결 오류: " + e.getMessage());
        } finally {
            // 자원 닫기 예제 (일반적으로 Connection은 데이터 변경/조회 완료 후 닫음)
            if (conn != null) {
                try { conn.close(); } catch (SQLException e) {}
            }
        }
    }
}
```

### 2. 데이터 검색 (SELECT) 및 레코드 출력 예제
```java
import java.sql.*;

public class JDBC_Select {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/sampledb?serverTimezone=UTC";
        String user = "root";
        String password = "YOUR_PASSWORD_HERE";

        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        try {
            conn = DriverManager.getConnection(url, user, password);
            stmt = conn.createStatement();
            
            // 모든 학생 데이터 검색
            String sql = "SELECT * FROM student";
            rs = stmt.executeQuery(sql);

            System.out.println("--- 학생 명단 ---");
            while (rs.next()) {
                // 칼럼 이름으로 추출
                String id = rs.getString("id");
                String name = rs.getString("name");
                // 칼럼 순서 인덱스(1-based)로 추출 (dept는 2번째 칼럼이라 가정할 경우)
                String dept = rs.getString(2); 
                
                System.out.printf("학번: %s | 이름: %s | 학과: %s\n", id, name, dept);
            }
        } catch (SQLException e) {
            System.err.println("쿼리 실행 에러: " + e.getMessage());
        } finally {
            // 리소스 역순 폐쇄 (자원 방출 누락 방지)
            try { if (rs != null) rs.close(); } catch (Exception e) {}
            try { if (stmt != null) stmt.close(); } catch (Exception e) {}
            try { if (conn != null) conn.close(); } catch (Exception e) {}
        }
    }
}
```

### 3. 데이터 추가, 수정, 삭제 (INSERT, UPDATE, DELETE) 예제
```java
import java.sql.*;

public class JDBC_Update {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/sampledb?serverTimezone=UTC";
        String user = "root";
        String password = "YOUR_PASSWORD_HERE";

        Connection conn = null;
        Statement stmt = null;

        try {
            conn = DriverManager.getConnection(url, user, password);
            stmt = conn.createStatement();

            // 1. 레코드 추가 (INSERT)
            String insertSql = "INSERT INTO student (name, id, dept) VALUES ('아무개', '0893012', '컴퓨터공학')";
            int insertedRows = stmt.executeUpdate(insertSql);
            System.out.println("추가된 행 개수: " + insertedRows);

            // 2. 레코드 수정 (UPDATE)
            String updateSql = "UPDATE student SET id = '0189011' WHERE name = '아무개'";
            int updatedRows = stmt.executeUpdate(updateSql);
            System.out.println("수정된 행 개수: " + updatedRows);

            // 3. 레코드 삭제 (DELETE)
            String deleteSql = "DELETE FROM student WHERE name = '아무개'";
            int deletedRows = stmt.executeUpdate(deleteSql);
            System.out.println("삭제된 행 개수: " + deletedRows);

        } catch (SQLException e) {
            System.err.println("SQL 처리 에러: " + e.getMessage());
        } finally {
            try { if (stmt != null) stmt.close(); } catch (Exception e) {}
            try { if (conn != null) conn.close(); } catch (Exception e) {}
        }
    }
}
```

# Related Concepts
- **PreparedStatement**: `Statement` 클래스를 상속받는 인터페이스로, SQL 쿼리를 데이터베이스로 보내기 전에 미리 컴파일(Pre-compile)하여 캐싱합니다. SQL Injection 공격을 원천 차단하고 바인딩 변수(`?`)를 사용하여 가독성과 성능을 향상시키는 실무 핵심 패턴입니다.
- **Connection Pool**: 데이터베이스 세션 연결은 막대한 자원을 필요로 하므로, 런타임에 수시로 연결을 열고 닫는 대신 미리 여러 개의 `Connection` 객체를 풀(Pool)에 만들어두고 재사용하여 부하를 경감하는 기법입니다 (예: HikariCP).

# Citations
* [15JDBC.pdf](../../../raw/notes/java/15JDBC.pdf)
