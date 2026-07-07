---
type: Study Note
title: "[Step 5] 게시물 삭제(Delete) 처리 및 컨펌 모달"
description: 다섯 번째 커밋(5de0352) 분석 - 상세보기 화면에서의 게시글 삭제 연동, 안전 삭제용 컨펌 모달 처리
tags: [java, swing, jdbc, mvc, step5]
timestamp: 2026-06-30
status: active
---

# Summary

본 단계에서는 다섯 번째 커밋([5de0352](file:///D:/java2026/Board0630))을 통해 상세보기 창(`BoardDetailView`)의 삭제 버튼 클릭 시, 오동작 방지를 위한 2차 확인 모달 창을 띄운 뒤 데이터베이스에서 해당 레코드를 안전하게 삭감(Delete)하고 메인 화면의 목록을 동기화하는 과정을 심층 분석합니다.

---

# Key Ideas

## 1. 하단 버튼 패널 리팩토링 및 리스너 등록
상세보기 뷰(`BoardDetailView`)의 하단 레이아웃을 깔끔하게 유지하고 버튼들을 묶어서 남쪽 영역에 고정하기 위해 `JPanel`을 신설했습니다.

```java
// BoardDetailView.java 내부 리팩토링
JPanel botPanel = new JPanel();
botPanel.add(btnEdit);
botPanel.add(btnDelete);
add(botPanel, BorderLayout.SOUTH);
```
또한 외부의 컨트롤러가 삭제 버튼 이벤트를 감지하고 주입할 수 있도록 리스너 바인딩 메서드를 추가했습니다.
```java
public void setBtnDeleteListener(ActionListener listener) {
    btnDelete.addActionListener(listener);
}
```

## 2. 안전 삭제를 위한 컨펌(Confirm) 대화상자 도입
게시글 삭제 작업은 영구히 복구할 수 없는 중대한 쓰기 작업이므로, 사용자 클릭 실수 방지를 위한 안전장치(`JOptionPane.showConfirmDialog`)를 설계합니다.

```java
int confirm = JOptionPane.showConfirmDialog(
        detailView, 
        "정말 이 게시글을 삭제하시겠습니까?",
        "삭제 확인",
        JOptionPane.YES_NO_OPTION); // 예/아니오 옵션만 노출

if (confirm == JOptionPane.YES_OPTION) {
    // YES를 누른 경우에만 물리 삭제 수행
    if (dao.delete(dto.getBoard_id())) {
        JOptionPane.showMessageDialog(detailView, "게시글이 삭제되었습니다.");
        detailView.dispose(); // 상세화면을 닫음
        refreshList();        // 메인 리스트 갱신
    } else {
        JOptionPane.showMessageDialog(detailView, "삭제에 실패하였습니다.");
    }
}
```
- **`JOptionPane.YES_NO_OPTION`**: 단순 확인 버튼 대신 '예(YES)', '아니오(NO)' 버튼을 명시적으로 분리하여 유저의 응답 상태(`confirm`)에 따른 조건 분기를 가능하게 합니다.

## 3. 삭제 완료 후의 리소스 정리 흐름
성공적으로 삭제가 완료되면 다음 순서대로 후속 조치를 취해야 합니다:
1. "게시글이 삭제되었습니다"라는 알림으로 사용자에게 성공 피드백 제공.
2. 이미 DB에서 삭제되어 유효하지 않은 상세화면 창을 `detailView.dispose()`로 안전하게 메모리 해제 및 닫기 처리.
3. 메인 목록에 여전히 남아 있는 삭제된 글을 안 보이게끔 **`refreshList()`를 즉각 연동**하여 UI-DB 정합성을 최신으로 동기화.

---

# Design Decisions

- **물리 삭제 vs 논리 삭제**: 현재 `BoardDAO.delete()` 메서드는 실제 SQL `DELETE` 문을 수행하여 레코드를 완전히 파괴하는 물리 삭제(Hard Delete)를 따르고 있습니다. 실무에서는 복구 가능성을 위해 `deleted_at` 등의 컬럼을 업데이트하는 논리 삭제(Soft Delete) 기법을 자주 사용합니다.

---

# Next Actions & Remaining Tasks

- 이제 최종적으로 상세보기 창에서 글을 수정할 수 있는 **수정(Update) 기능**을 추가해야 합니다.
- 수정 기능을 구현할 때, 읽기 전용 상태였던 상세보기 창을 유연하게 수정 가능 모드로 뷰의 상태(State)를 토글하고 수정 완료 시 DB를 업데이트하는 유기적인 UI 제어가 요구됩니다. (Step 6에서 해결)

---

# Related Concepts

- [JOptionPane.showConfirmDialog API](../../cs/java/chapter-16.md)
- [Window Resource Disposing (JFrame.dispose)](../../cs/java/chapter-16.md)
