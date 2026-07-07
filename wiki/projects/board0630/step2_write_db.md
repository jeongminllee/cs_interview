---
type: Study Note
title: "[Step 2] BoardController 및 글 작성 DB 연동 구현"
description: 두 번째 커밋(83efd36) 분석 - MVC 컨트롤러 구현을 통한 뷰와 모델의 상호작용 및 글쓰기 저장 연동
tags: [java, swing, jdbc, mvc, step2]
timestamp: 2026-06-30
status: active
---

# Summary

본 단계에서는 두 번째 커밋([83efd36](file:///D:/java2026/Board0630))을 다룹니다. 이 커밋에서는 프로그램의 제어 흐름을 전담하는 `BoardController`를 전격 도입하고, 글쓰기 화면(`BoardWriteView`)에 입력된 데이터를 추출해 데이터베이스(`BoardDAO`)에 영속적으로 인서트하는 과정을 구현합니다.

---

# Key Ideas

## 1. MVC 중재자로서의 `BoardController` 신설
뷰와 모델은 서로의 존재를 모른 채 온전히 격리되어야 재사용성과 유지보수성이 극대화됩니다. `BoardController`는 이 두 계층을 중재합니다.
- **의존성 주입 (Dependency Injection)**: 컨트롤러 생성 시 `BoardListView`와 `BoardDAO`의 참조를 주입받아 관리합니다.
- **이벤트 위임**: 뷰에서 발생하는 이벤트를 컨트롤러가 수신하여 비즈니스 로직(DB 저장, 창 전환 등)을 실행하도록 바인딩합니다.

```java
public class BoardController {
    private BoardListView view;
    private BoardDAO dao;

    public BoardController(BoardListView view, BoardDAO dao) {
        this.view = view;
        this.dao = dao;
        
        // 뷰의 글쓰기 버튼 이벤트 리스너를 컨트롤러에 위임
        view.setBtnWriteListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                WriteView(); // 글쓰기 화면 호출
            }
        });
    }
    // ...
}
```

## 2. 뷰(View)의 데이터 캡슐화 및 리스너 등록 인터페이스
- **BoardListView**: 컨트롤러가 버튼 이벤트를 감지할 수 있도록 `setBtnWriteListener(ActionListener listener)` 메서드를 노출합니다.
- **BoardWriteView**: 텍스트 필드와 텍스트 에어리어의 데이터를 내부로 숨기고(private), 외부(컨트롤러)에서 필요할 때만 가져갈 수 있게 Getter 메서드(`getTitle()`, `getWriter()`, `getContent()`, `getBtnSave()`)를 구현합니다.

```java
// BoardWriteView.java
public String getTitle() { return txtTitle.getText(); }
public String getWriter() { return txtWriter.getText(); }
public String getContent() { return txtContent.getText(); }
public JButton getBtnSave() { return btnSave; }
```

## 3. 글 저장 비즈니스 로직
컨트롤러 내의 `WriteView()` 메서드는 새 글 쓰기 화면을 띄우고, 저장 버튼(`btnSave`)의 이벤트를 처리합니다:
1. `BoardWriteView` 객체를 동적으로 인스턴스화하여 화면에 표시합니다.
2. 사용자가 저장 버튼을 누르면, 화면의 getter 메서드들을 통해 입력값을 읽어와 `BoardDTO` 객체에 바인딩합니다.
3. `dao.insert(dto)`를 호출하여 데이터베이스에 등록합니다.
4. 성공 여부에 따라 다이얼로그 메시지(`JOptionPane.showMessageDialog`)를 띄우고 성공 시 `writeView.dispose()`로 창을 닫습니다.

---

# Why it matters (Design Choice)

`Main.java`는 이제 다음과 같이 실행 진입점의 역할만 명확하게 수행합니다:
```java
public static void main(String[] args) {
    BoardDAO dao = new BoardDAO();
    BoardListView view = new BoardListView();
    new BoardController(view, dao); // 뷰와 모델을 컨트롤러로 묶어 동작 개시
}
```
프레젠테이션 코드가 비즈니스나 DB 트랜잭션 로직과 분리됨으로써 UI 디자인이 변경되거나 DB 드라이버가 변경되어도 각각 독립적으로 변경 및 테스트할 수 있습니다.

---

# Next Actions & Remaining Tasks

- 글을 정상적으로 작성해 DB에 등록하는 데는 성공했으나, **메인 목록 화면(`BoardListView`)에 작성한 글이 즉시 업데이트되지 않습니다.**
- 프로그램을 재실행해야만 DB에 들어간 글을 볼 수 있는 상태이므로, 데이터 입력 완료 즉시 테이블 리스트를 새로 갱신하는 기능이 요구됩니다. (Step 3에서 보완)

---

# Related Concepts

- [ActionListener Interface in Java](../../cs/java/chapter-16.md)
- [Anonymous Inner Class](../../cs/java/chapter-16.md)
- [JOptionPane Dialogs](../../cs/java/chapter-16.md)
