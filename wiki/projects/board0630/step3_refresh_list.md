---
type: Study Note
title: "[Step 3] 데이터 목록 동적 조회 및 TableModel 갱신 로직 구현"
description: 세 번째 커밋(ba1bfef) 분석 - 데이터베이스 조회 결과와 Swing JTable 간의 동적 리스트 바인딩 및 화면 갱신
tags: [java, swing, jdbc, mvc, step3]
timestamp: 2026-06-30
status: active
---

# Summary

본 단계에서는 세 번째 커밋([ba1bfef](file:///D:/java2026/Board0630))을 통해 데이터베이스의 데이터가 변경(추가)되었을 때, 이를 감지하고 메인 UI의 테이블 뷰(`JTable`)를 실시간으로 리프레시하는 `refreshList` 로직을 분석합니다.

---

# Key Ideas

## 1. `refreshList()` 메서드 도입
컨트롤러 내부에 데이터베이스로부터 전체 글 데이터를 다시 읽어와 뷰에 리스트를 갱신해 주는 전용 헬퍼 메서드인 `refreshList()`를 구현했습니다.

```java
private void refreshList() {
    List<BoardDTO> list = dao.selectAll(); // Model로부터 최신 목록 조회
    view.setTableData(list);               // View로 목록 데이터 전송
}
```

## 2. 목록 갱신 주기
목록은 프로그램의 수명 주기에서 다음 두 가지 시점에 갱신되어야 합니다.
- **초기 로딩 시점**: `BoardController` 생성자 실행 마지막 단계에서 `refreshList()`를 호출하여 실행하자마자 기존 저장된 DB 데이터가 화면에 출력되게 합니다.
- **데이터 추가 성공 시점**: 글쓰기 화면(`BoardWriteView`)에서 글 작성이 완료되어 DB 인서트(`dao.insert(dto)`)가 성공했을 때 즉각 호출하여 테이블 목록을 실시간으로 갱신합니다.

## 3. TableModel 리셋 및 데이터 재생성 (`setTableData`)
`JTable`의 뷰를 제어하기 위해 뷰 계층(`BoardListView`)에 구현된 `setTableData(List<BoardDTO> list)` 메서드는 매우 중요한 메커니즘을 가지고 있습니다.

```java
public void setTableData(List<BoardDTO> list) {
    tableModel.setRowCount(0);  // 1. 기존에 표에 표시되던 데이터 행들을 전부 제거 (초기화)
    
    // 2. 최신 목록 데이터를 순회하며 JTable에 행 추가
    for (BoardDTO dto : list) {
        tableModel.addRow(new Object[] {
                dto.getBoard_id(),
                dto.getTitle(),
                dto.getContent(),
                dto.getWriter(),
                dto.getCreated_at(),
        });
    }
}
```

- **`setRowCount(0)`의 필수성**: 이 메서드를 호출해 테이블 행을 0으로 리셋하지 않고 `addRow`를 호출하면 기존 리스트 아랫부분에 데이터가 누적되어 중복 출력되는 치명적인 버그가 발생합니다.
- **2차원 행 배열 매핑**: 자바 Swing의 `DefaultTableModel`은 데이터를 `Object[]` 형태의 1차원 행 배열로 입력받기 때문에, DTO의 필드값을 순서대로 추출해 배열 객체로 포장한 뒤 넘겨줍니다.

---

# Pro-Tips & Best Practices

- **비동기 갱신과 메인 스레드**: 현재 코드는 단일 스레드로 안전하게 Swing Event Dispatch Thread (EDT) 상에서 갱신이 일어나고 있습니다. 프로덕션 환경에서 대량의 DB를 질의할 경우 렉 현상이 유발될 수 있으므로, 향후 `SwingWorker` 등을 통한 백그라운드 질의 기법을 연계하여 개선할 수 있습니다.

---

# Next Actions & Remaining Tasks

- 글의 목록 조회와 작성이 실시간 연동되었으므로 다음은 사용자가 목록 중 특정 행을 클릭하여 상세한 내용(글 번호, 제목, 작성자, 내용, 등록일시)을 열람할 수 있는 **상세보기(`DetailView`) 기능**과 이에 대응하는 DB 단건 조회 처리가 요구됩니다. (Step 4에서 다룸)

---

# Related Concepts

- [DefaultTableModel API and row manipulation](../../cs/java/chapter-16.md)
- [Swing Event Dispatch Thread (EDT)](../../cs/java/chapter-16.md)
