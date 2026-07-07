---
type: Study Note
title: "[Step 4] 상세보기 뷰(DetailView) 연동 및 단건 조회"
description: 네 번째 커밋(e8f12b3) 분석 - 테이블 행 선택 기능, DB 단건 조회(selectDetail) 및 상세보기 UI 연동
tags: [java, swing, jdbc, mvc, step4]
timestamp: 2026-06-30
status: active
---

# Summary

본 단계에서는 네 번째 커밋([e8f12b3](file:///D:/java2026/Board0630))을 통해 목록 화면에서 특정 행을 더블클릭하거나 선택하여 '상세보기' 버튼을 눌렀을 때, DB에서 해당하는 글 1건만 조회(`selectDetail`)하여 팝업 창(`BoardDetailView`)을 통해 출력하는 매커니즘을 상세 분석합니다.

---

# Key Ideas

## 1. DB 단건 조회 쿼리 구현 (`BoardDAO.selectDetail`)
게시글 식별자(`board_id`)인 고유 ID 값을 조건절로 걸어 데이터베이스에서 레코드를 한 건만 가져옵니다.

```java
public BoardDTO selectDetail(int id) {
    BoardDTO board = null;
    String query = "SELECT * FROM board WHERE board_id = ?";
    try {
        Connection conn = DBConnection.getConnection();
        PreparedStatement pstmt = conn.prepareStatement(query);
        pstmt.setInt(1, id);
        ResultSet rs = pstmt.executeQuery();
        if (rs.next()) {
            board = new BoardDTO(
                    rs.getInt("board_id"), 
                    rs.getString("title"), 
                    rs.getString("content"), 
                    rs.getString("writer"), 
                    rs.getString("created_at"));
        }
    } catch (Exception e) {
        e.printStackTrace();
    }    
    return board;
}
```
- **리소스 반환**: 결과 셋을 돌려 한 행만 존재할 것이므로 `while` 루프 대신 `if (rs.next())` 조건 분기로 레코드를 읽어 DTO 객체를 세팅합니다.
- *참고*: 이 커밋 시점에 차후 구현할 `delete(int board_id)`와 `update(BoardDTO board)`의 뼈대 쿼리 로직이 DAO에 미리 포함되었습니다.

## 2. 테이블 선택 행 ID 추출 (`BoardListView.getSelectId`)
사용자가 `JTable` 목록 중 선택한 행의 고유 식별값(ID)을 추출하여 비즈니스 레이어로 던지는 UI 처리가 추가되었습니다.

```java
public int getSelectId() {
    int row = table.getSelectedRow(); // 1. 현재 테이블에서 사용자가 선택한 행 번호(Index) 획득
    if (row == -1) { 
        return -1; // 선택된 행이 없는 경우 -1 반환
    }
    return (int) table.getValueAt(row, 0); // 2. 선택 행의 0번째 열(ID 컬럼)의 값을 가져와 캐스팅
}
```

## 3. 상세보기 화면 설계 (`BoardDetailView`)
글 내용을 조회하는 화면은 글쓰기 화면과 달리 초기에는 **읽기 전용(Read-only)**이어야 합니다.
- **DTO 주입 생성자**: `BoardDetailView(BoardDTO dto)` 생성자를 호출할 때 조회해 온 DTO를 직접 넘겨받아 폼 내부를 채웁니다.
- **비활성화 (`setEditable(false)`)**: 제목, 작성자, 작성일, 본문 텍스트 컴포넌트들에 대해 `setEditable(false)` 처리를 가해 사용자가 상세조회 모드에서 함부로 텍스트를 고쳐 쓸 수 없도록 기본 UI 속성을 적용합니다.

```java
// BoardDetailView.java 생성자 내부 일부
txtTitle = new JTextField(dto.getTitle());
txtTitle.setEditable(false); // 수정 불가 지정
```

## 4. 컨트롤러 제어 흐름 (`BoardController.DetailView`)
1. 사용자가 상세보기 버튼 클릭 시 리스너가 작동합니다.
2. `view.getSelectId()`를 확인하여 사용자가 글을 선택하지 않은 상태라면 안내 팝업을 띄우고 돌려보냅니다.
3. 선택된 유효 ID가 있다면 `dao.selectDetail(id)`를 호출합니다.
4. 정상적으로 레코드가 리턴되었다면 `new BoardDetailView(dto)`를 생성하여 화면에 띄웁니다.

---

# Design Decisions

- **단일 테이블 셀 값 추출**: `table.getValueAt(row, 0)` 방식은 ID가 항상 0번째 컬럼에 고정되어 배치되어 있다는 전제 하에 단순하게 동작합니다. 컬럼 배치가 바뀔 가능성이 있다면 모델의 메타데이터를 추적하여 바인딩하는 방법이 안정적입니다.
- **상세보기 내 버튼**: 현재 `BoardDetailView` 하단에 수정과 삭제 버튼이 추가되어 배치되어 있으나, 실질적인 비즈니스 로직 연동은 다음 단계에서 한 단계씩 진행됩니다.

---

# Related Concepts

- [Prepared Statement Bindings and SQL parameters](../../cs/java/chapter-16.md)
- [JTable.getSelectedRow() and getValueAt()](../../cs/java/chapter-16.md)
