---
type: Study Note
title: "[Step 6] 게시물 수정(Update) 처리 및 UI 상태 토글(EditMode)"
description: 마지막 커밋(f55d412) 분석 - 단일 뷰 내 상태 제어 플래그를 통한 모드 전환(수정/취소/완료) 및 DB 업데이트 구현
tags: [java, swing, jdbc, mvc, step6]
timestamp: 2026-06-30
status: active
---

# Summary

본 단계에서는 프로젝트의 마지막 커밋([f55d412](file:///D:/java2026/Board0630))을 통해 상세보기 창(`BoardDetailView`)의 컴포넌트들을 재활용하여 **읽기 모드**와 **수정 모드**를 교차하는 세련된 UI 상태 제어 설계와 데이터베이스의 수정(Update) SQL 연동 방법을 다룹니다.

---

# Key Ideas

## 1. 단일 UI에서의 두 가지 상태 플래그 제어 (`isEditMode`)
상세보기 뷰는 수정 모드인지 일반 열람 모드인지에 따라 화면 요소의 속성이 바뀝니다. 이를 위해 `isEditMode` 변수를 멤버 플래그로 두고 동적으로 뷰를 제어합니다.

```java
// BoardDetailView.java 내부 상태 스위칭 기법
private boolean isEditMode = false; // 기본값은 읽기 모드 (false)
private BoardDTO originalDTO;       // 취소에 대비하여 최초 원본 객체 참조

public void toggleEditMode() {
    isEditMode = !isEditMode; // true <-> false 반전
    
    txtTitle.setEditable(isEditMode);   // 제목 필드 쓰기 가능 여부 전환
    txtContent.setEditable(isEditMode); // 내용 필드 쓰기 가능 여부 전환
    
    if (isEditMode) {
        btnEdit.setText("완료");
        btnDelete.setText("취소");
    } else {
        btnEdit.setText("수정");
        btnDelete.setText("삭제");
        
        // 취소된 경우를 대비하여 화면 텍스트를 원본 데이터로 원상 복구 (Rollback)
        txtTitle.setText(originalDTO.getTitle());
        txtContent.setText(originalDTO.getContent());
    }
}
```
- **버튼 텍스트 다목적 전환**: 
  - 읽기 모드일 때: **[수정]** 버튼 클릭 시 수정 모드로 진입, **[삭제]** 버튼 클릭 시 글 삭제 수행.
  - 수정 모드일 때: **[완료]** 버튼 클릭 시 수정 사항 저장, **[취소]** 버튼 클릭 시 수정 중이던 데이터를 버리고 읽기 모드로 복구.

## 2. 컨트롤러에서의 버튼 액션의 역할 오버로딩 (Controller Logic)
컨트롤러는 뷰가 어떤 상태(`isEditMode`)냐에 따라 분기 처리를 명확하게 구현합니다.

### 2.1 [수정 / 완료] 버튼 핸들러
```java
detailView.setBtnEditListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        if (!detailView.isEditMode()) {
            // 1. 읽기 모드인 경우 -> 수정 모드로 전환
            detailView.toggleEditMode();
        } else {
            // 2. 수정 모드인 경우(완료 상태) -> DB에 수정 질의 요청
            dto.setTitle(detailView.getEditTitle());
            dto.setContent(detailView.getEditContent());

            if (dao.update(dto)) {
                JOptionPane.showMessageDialog(detailView, "게시글이 수정되었습니다.");
                detailView.toggleEditMode(); // 읽기 모드로 복귀
                refreshList();               // 메인 목록 동기화
            } else {
                JOptionPane.showMessageDialog(detailView, "수정에 실패하였습니다.");
            }
        }
    }
});
```

### 2.2 [삭제 / 취소] 버튼 핸들러
```java
detailView.setBtnDeleteListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        if (detailView.isEditMode()) {
            // 1. 수정 모드일 때 누른 취소 -> UI 상태만 원래대로 원복
            detailView.toggleEditMode();
        } else {
            // 2. 읽기 모드일 때 누른 삭제 -> 확인 창 띄운 후 실제 물리 삭제 진행
            int confirm = JOptionPane.showConfirmDialog(detailView, "정말 이 게시글을 삭제하시겠습니까?", ...);
            if (confirm == JOptionPane.YES_OPTION) {
                if (dao.delete(dto.getBoard_id())) {
                    detailView.dispose();
                    refreshList();
                }
            }
        }
    }
});
```

---

# Why it matters (Design Patterns)

- **UI 재활용 극대화**: 수정 화면을 별도의 다이얼로그나 프레임으로 분리하여 생성하는 대신, 기존 상세보기 프레임의 텍스트 컴포넌트 활성화 플래그(`setEditable`)를 조정하여 구현함으로써 리소스가 아끼고 코드 복잡성이 낮아집니다.
- **예외 복구 프로세스**: 수정 중에 잘못 기입하다가 취소를 누르더라도 `originalDTO`를 들고 있기 때문에 클라이언트 메모리 단에서 즉각 데이터를 기존 상태로 안전하게 복귀할 수 있습니다.

---

# Related Concepts

- [UI State Management (View State Patterns)](../../cs/java/chapter-16.md)
- [JDBC Update Statements](../../cs/java/chapter-16.md)
- [MVC Data Synchronization Flow](../../cs/java/chapter-16.md)
