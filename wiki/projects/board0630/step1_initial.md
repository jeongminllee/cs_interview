---
type: Study Note
title: "[Step 1] MVC 뼈대 구축 및 DTO/DAO 기본 구조"
description: 최초 커밋(3a2cc62) 분석 - Swing 화면 뼈대와 DB 커넥션, 모델 클래스의 초기 구현체
tags: [java, swing, jdbc, mvc, step1]
timestamp: 2026-06-30
status: active
---

# Summary

본 단계에서는 프로젝트의 최초 커밋([3a2cc62](file:///D:/java2026/Board0630))을 통해 MVC 아키텍처의 구성 요소들을 생성하고, Swing 컴포넌트를 이용한 화면의 배치 및 JDBC 연결을 위한 공통 유틸리티의 구현 방법을 다룹니다.

---

# Key Ideas

## 1. 데이터베이스 접속 관리 (`DBConnection`)
데이터베이스 접속을 담당하는 `DBConnection` 클래스는 애플리케이션의 설정 파일(`db.properties`)로부터 접속 정보를 동적으로 읽어옵니다.

- **static 초기화 블록**: 클래스가 메모리에 처음 로드될 때 단 한 번만 실행되는 static 블록을 활용하여 드라이버를 로드합니다. 이는 드라이버가 중복 로드되는 오버헤드를 막아줍니다.
- **Properties 활용**: DB 접속 URL, 계정명, 비밀번호를 소스 코드 내에 하드코딩하지 않고 외부 프로퍼티 파일로 분리하여 보안성과 환경 전환 유연성을 높였습니다.

```java
public class DBConnection {
    private static Properties properties = new Properties();
    
    static {
        try (InputStream input = new FileInputStream("db.properties")){
            properties.load(input);
            Class.forName(properties.getProperty("db.driver"));
        } catch (IOException e) {
            System.out.println("db 정보 파일 읽기 오류");
            e.printStackTrace();
        } catch (ClassNotFoundException ex) {
            System.out.println("MYSQL 드라이버 오류");
            ex.printStackTrace();
        }
    }
    
    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(
                properties.getProperty("db.url"),
                properties.getProperty("db.user"),
                properties.getProperty("db.password"));
    }
}
```

## 2. 데이터 모델 계층 (`DTO` & `DAO`)
- **BoardDTO (Data Transfer Object)**: 테이블 `board`의 레코드 컬럼과 1:1 매칭되는 필드(`board_id`, `title`, `content`, `writer`, `created_at`)를 정의합니다. 레이어 간 데이터 전달을 수행합니다.
- **BoardDAO (Data Access Object)**: 비즈니스 질의를 전담하는 객체입니다.
  - `insert(BoardDTO board)`: `PreparedStatement`를 이용하여 게시글 파라미터를 안전하게 바인딩한 후 인서트 질의를 실행합니다.
  - `selectAll()`: 모든 게시글 데이터를 조회하여 `List<BoardDTO>` 형태로 변환합니다.

## 3. UI 컴포넌트 (`View` Layer)
- **BoardListView**: `JTable`과 `DefaultTableModel`을 사용하여 게시글 목록을 표 형태로 배치합니다. 하단 패널에 "글쓰기", "상세보기" 버튼을 추가했습니다. `isCellEditable`을 오버라이드하여 테이블 셀의 직접 수정을 불가능하게 설정했습니다.
- **BoardWriteView**: 사용자가 제목, 작성자, 본문 내용을 기입할 수 있는 입력 폼 화면입니다. `FlowLayout`을 기반으로 심플하게 컴포넌트들을 추가했습니다.

---

# Warning & Checkpoints

- **컨트롤러의 부재**: 이 커밋 시점에서는 `Main` 클래스에서 단지 `new BoardWriteView()`를 직접 인스턴스화하여 화면에 노출시키는 형태입니다. 
- UI 이벤트에 대한 리스너 처리가 아직 아무것도 정의되지 않아 화면의 버튼을 클릭해도 반응하지 않습니다.
- DB 처리를 수행할 DAO를 프레젠테이션 계층에서 어떻게 제어할 것인지에 대한 설계가 다음 단계(Step 2)에서 보완됩니다.

---

# Related Concepts

- [JDBC Connection Lifecycle](../../cs/java/chapter-16.md)
- [Swing JTable Layout](../../cs/java/chapter-16.md)
- [Properties File Handling in Java](../../cs/java/chapter-13.md)
