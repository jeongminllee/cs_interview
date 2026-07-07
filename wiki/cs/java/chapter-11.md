---
type: Study Note
title: "Chapter 11: Swing Components I (스윙 컴포넌트 1)"
description: "스윙 컴포넌트들의 최상위 공통 속성을 제공하는 JComponent 클래스의 주요 메서드를 살펴보고, JLabel, JButton, JCheckBox, JRadioButton, JTextField, JTextArea, JList, JComboBox, JSlider 등 핵심 컴포넌트들의 생성과 이벤트 제어 방식을 상세히 학습합니다."
tags: [java, swing, jcomponent, jlabel, jbutton, jcheckbox, jradiobutton, jtextfield, jtextarea, jlist, jcombobox, jslider]
timestamp: 2026-06-19
status: active
---

# 1. 스윙 컴포넌트 공통 메서드: JComponent

모든 스윙 컴포넌트는 `javax.swing.JComponent`를 상속받습니다. `JComponent`는 컴포넌트의 외형 제어, 포커스 관리, 툴팁 지정 등 공통 기능을 정의하는 추상 클래스입니다.

### 1) 주요 공통 메서드
* **배경색 및 전경색 설정**:
  * `void setBackground(Color c)`: 컴포넌트의 배경색을 설정합니다.
  * `void setForeground(Color c)`: 글자색 등 전경색을 설정합니다.
* **글꼴(Font) 지정**:
  * `void setFont(Font f)`: 컴포넌트 내부 텍스트의 글꼴, 스타일, 크기를 지정합니다 (예: `new Font("Arial", Font.ITALIC, 20)`).
* **컴포넌트 활성화/비활성화**:
  * `void setEnabled(boolean b)`: `true`이면 활성화 상태가 되며, `false`이면 컴포넌트가 회색으로 비활성화되고 사용자의 입력과 이벤트 반응을 받지 못합니다.
* **위치 및 크기 조회**:
  * `int getX()`, `int getY()`: 부모 컨테이너 기준 컴포넌트의 좌측 상단 모서리 좌표를 구합니다.
  * `int getWidth()`, `int getHeight()`: 컴포넌트의 가로, 세로 크기를 픽셀 단위로 구합니다.
* **투명도 제어**:
  * `void setOpaque(boolean b)`: `true`로 설정하면 컴포넌트가 불투명 상태가 되어 설정한 배경색이 정상적으로 화면에 나타납니다. 만약 일부 컴포넌트(예: `JLabel`)의 배경색이 바뀌지 않는다면 투명 상태(`opaque == false`)이기 때문이므로 `setOpaque(true)`를 선행 호출해야 합니다.

---

# 2. JLabel (레이블)

`JLabel`은 사용자가 직접 편집할 수 없으며, 단순 문자열(텍스트)이나 이미지(그림)를 컴포넌트화하여 화면에 출력할 때 사용합니다.

### 1) 주요 생성자
* `JLabel()`: 텍스트와 이미지가 없는 빈 레이블을 생성합니다.
* `JLabel(String text)`: 지정한 문자열 텍스트를 출력하는 레이블을 생성합니다.
* `JLabel(Icon image)`: 지정한 이미지를 출력하는 레이블을 생성합니다.
* `JLabel(String text, Icon image, int hAlign)`: 텍스트와 이미지를 수평 정렬(`hAlign`) 값에 맞추어 출력하는 레이블을 생성합니다.
  * `hAlign` 상수: `SwingConstants.LEFT`, `SwingConstants.CENTER`, `SwingConstants.RIGHT`

### 2) 이미지 레이블 구현
자바 GUI에서 png, gif, jpg 등 이미지 파일을 읽어오기 위해서는 `ImageIcon` 클래스를 사용해야 합니다.
```java
ImageIcon beauty = new ImageIcon("images/beauty.jpg"); // 이미지 로드
JLabel imageLabel = new JLabel(beauty); // 이미지 레이블 생성

// 텍스트와 이미지 결합 및 중앙 정렬 레이블 생성 예시
ImageIcon normalIcon = new ImageIcon("images/normalIcon.gif");
JLabel combinedLabel = new JLabel("전화하세요", normalIcon, SwingConstants.CENTER);
```

---

# 3. JButton (버튼)

`JButton`은 마우스로 선택(클릭)할 수 있는 버튼 모양의 컴포넌트로, 클릭 시 `ActionEvent`가 발생합니다.

### 1) 주요 생성자
* `JButton()`: 빈 버튼을 생성합니다.
* `JButton(String text)`: 지정한 텍스트가 표시되는 버튼을 생성합니다.
* `JButton(Icon image)`: 지정한 이미지가 표시되는 이미지 버튼을 생성합니다.
* `JButton(String text, Icon image)`: 텍스트와 이미지가 함께 표시되는 버튼을 생성합니다.

### 2) 3개 상태별 이미지 처리
`JButton`은 마우스 조작 상태에 따라 서로 다른 이미지를 동적으로 출력할 수 있습니다.
1. **보통 상태 (Normal Icon)**: 버튼이 눌리지 않았을 때 기본 출력되는 이미지입니다 (`setIcon(Icon)`).
2. **마우스 오버 상태 (Rollover Icon)**: 마우스 포인터가 버튼 위로 올라갈 때 출력되는 이미지입니다 (`setRolloverIcon(Icon)`).
3. **눌려진 상태 (Pressed Icon)**: 버튼을 마우스로 누르고 있는 동안 출력되는 이미지입니다 (`setPressedIcon(Icon)`).

```java
ImageIcon normal = new ImageIcon("images/normalIcon.gif");
ImageIcon rollover = new ImageIcon("images/rolloverIcon.gif");
ImageIcon pressed = new ImageIcon("images/pressedIcon.gif");

JButton btn = new JButton("Call", normal);
btn.setRolloverIcon(rollover);
btn.setPressedIcon(pressed);
```

### 3) 버튼/레이블 내부 정렬 (Alignment)
컴포넌트 영역 내부에서 텍스트와 이미지의 배치 위치를 조정할 수 있습니다.
* **수평 정렬**: `setHorizontalAlignment(int align)`
  * `SwingConstants.LEFT`, `SwingConstants.CENTER`, `SwingConstants.RIGHT`
* **수직 정렬**: `setVerticalAlignment(int align)`
  * `SwingConstants.TOP`, `SwingConstants.CENTER`, `SwingConstants.BOTTOM`

---

# 4. JCheckBox (체크박스)와 ItemEvent

`JCheckBox`는 **선택(Selected)**과 **비선택(Deselected)**의 두 가지 상태만 가지며, 여러 옵션 중 다중 선택(Multiple Selection)을 허용할 때 사용됩니다.

### 1) 생성 방식
* `JCheckBox c = new JCheckBox("사과");` // 기본 비선택 상태의 체크박스
* `JCheckBox c = new JCheckBox("배", true);` // 선택된 상태로 초기화된 체크박스

### 2) ItemEvent 처리
체크박스의 선택 상태가 마우스나 키보드 조작에 의해 변경되면 `ItemEvent`가 발생하며, 이를 처리하기 위해 `ItemListener` 인터페이스의 `itemStateChanged(ItemEvent e)` 메서드를 구현해야 합니다.

```java
JCheckBox apple = new JCheckBox("사과");
apple.addItemListener(new ItemListener() {
    public void itemStateChanged(ItemEvent e) {
        if(e.getStateChange() == ItemEvent.SELECTED) {
            System.out.println("사과가 선택되었습니다.");
        } else {
            System.out.println("사과가 해제되었습니다.");
        }
    }
});
```
* **`e.getStateChange()`**: 상태가 변한 결과를 확인합니다 (`ItemEvent.SELECTED` 혹은 `ItemEvent.DESELECTED` 반환).
* **`e.getItem()`**: 이벤트를 발생시킨 원인 객체(체크박스 컴포넌트 객체 레퍼런스)를 반환합니다.

---

# 5. JRadioButton (라디오 버튼)

`JRadioButton`은 여러 개의 선택지 중 **단 하나만 선택**할 수 있도록 보장하는 컴포넌트입니다.

### 1) 버튼 그룹 (ButtonGroup) 구성
라디오 버튼들을 동일한 **`ButtonGroup`** 객체에 추가해주어야 상호 배타적인 단일 선택(Single Selection)이 작동합니다. 그룹으로 묶이지 않으면 독립적으로 여러 개가 체크될 수 있습니다.
```java
// 1. 버튼 그룹 생성
ButtonGroup group = new ButtonGroup();

// 2. 라디오 버튼 컴포넌트 생성
JRadioButton apple = new JRadioButton("사과");
JRadioButton pear = new JRadioButton("배", true); // 기본 선택 상태
JRadioButton cherry = new JRadioButton("체리");

// 3. 버튼 그룹에 라디오 버튼 삽입 (상호 배제 동작 활성화)
group.add(apple);
group.add(pear);
group.add(cherry);

// 4. 컨테이너에도 컴포넌트를 물리적으로 부착해주어야 함
container.add(apple);
container.add(pear);
container.add(cherry);
```

---

# 6. JTextField (텍스트 필드)와 JTextArea (텍스트 영역)

사용자로부터 직접 문자열 텍스트 입력을 처리하는 텍스트 컴포넌트입니다.

### 1) JTextField (한 줄 텍스트 입력창)
* **특징**: 단 한 줄의 텍스트만 입력받는 컴포넌트입니다.
* **이벤트**: 입력창 안에서 글자를 타이핑하고 **`<Enter>` 키를 입력하면 `ActionEvent`가 발생**하여 이벤트를 처리할 수 있습니다.
* **주요 메서드**:
  * `String getText()`: 입력되어 있는 문자열을 가져옵니다.
  * `void setText(String t)`: 입력창의 내용을 `t` 문자열로 교체합니다.
  * `void setEditable(boolean b)`: `false`로 주면 입력을 막는 읽기 전용 상태로 전환합니다.
  * `void setFont(Font f)`: 입력 문자열의 폰트를 변경합니다.

```java
JTextField tf = new JTextField(20); // 20열 크기의 텍스트 필드 생성
tf.addActionListener(new ActionListener() {
    public void actionPerformed(ActionEvent e) {
        String input = tf.getText(); // 입력값 조회
        System.out.println("User input: " + input);
        tf.setText(""); // 입력창 클리어
    }
});
```

### 2) JTextArea (여러 줄 텍스트 영역)
* **특징**: 여러 행과 열로 이루어진 텍스트 입력창입니다.
* **스크롤바 지원 필수**: `JTextArea`는 스크롤바를 내장하고 있지 않습니다. 따라서 텍스트 양이 영역을 초과했을 때 정상적으로 스크롤되도록 하려면 **`JScrollPane`**에 감싸서 화면에 배치해야 합니다.
* **주요 메서드**:
  * `void append(String str)`: 기존 내용 뒤에 새로운 문자열 `str`을 이어붙입니다.

```java
JTextArea ta = new JTextArea(7, 20); // 7행 20열 크기
JScrollPane scrollPane = new JScrollPane(ta); // 스크롤팬에 부착
container.add(scrollPane); // 화면 배치
```

---

# 7. JList<E> (리스트)

`JList`는 여러 아이템의 목록을 리스트 형태로 화면에 출력하여 사용자가 1개 혹은 여러 개의 항목을 선택할 수 있도록 제공하는 컴포넌트입니다. JDK7부터 제네릭(Generic) 타입을 지원합니다.

### 1) 생성 및 아이템 제공
* **객체 배열 기반 생성**:
  ```java
  String[] fruits = {"apple", "banana", "kiwi"};
  JList<String> strList = new JList<>(fruits);
  ```
* **벡터(Vector) 기반 생성**:
  ```java
  Vector<String> v = new Vector<>();
  v.add("홍길동");
  JList<String> nameList = new JList<>(v);
  ```
* **빈 리스트 생성 후 동적 데이터 반영 (`setListData`)**:
  ```java
  JList<String> nameList = new JList<>();
  v.add("김홍남");
  nameList.setListData(v); // 새로운 벡터 데이터 갱신
  ```

### 2) 데이터 변경 시 유의사항
`JList` 생성 시 인자로 사용했던 배열이나 벡터 객체를 소스 코드에서 변경하더라도 화면에 리스트 항목들이 즉각 갱신되지 않습니다. 수정 사항을 반영하려면 반드시 변경된 컬렉션 객체를 담아 **`setListData()` 메서드를 재호출**해야 컴포넌트 뷰가 리프레시됩니다.

---

# 8. JComboBox<E> (콤보박스)

`JComboBox`는 평소에는 한 줄의 텍스트 필드로 표시되다가, 우측 버튼을 누르면 드롭다운(Dropdown) 형태로 확장 목록 리스트를 표시하는 컴포넌트입니다.

### 1) 콤보박스 생성 및 사용 예시
```java
String[] fruits = {"apple", "banana", "kiwi"};
JComboBox<String> strCombo = new JComboBox<>(fruits); // 배열로 생성

// 혹은 빈 콤보박스 생성 후 동적 삽입
JComboBox<String> nameCombo = new JComboBox<>();
nameCombo.addItem("kitae");
nameCombo.addItem("jaemoon");
```

### 2) 이벤트 처리와 아이템 조회
콤보박스 항목을 다른 것으로 선택하면 **`ActionEvent`**가 유발됩니다.
* **`int getSelectedIndex()`**: 현재 선택된 아이템의 인덱스 번호(0-indexed)를 리턴합니다.
* **`Object getSelectedItem()`**: 선택된 항목 객체의 레퍼런스를 리턴합니다.

---

# 9. JSlider (슬라이더)

`JSlider`는 사용자가 특정 범위 내의 수치 값을 마우스로 손잡이(Knob)를 드래그하여 직관적으로 조절할 수 있도록 설계된 컴포넌트입니다.

### 1) 주요 속성 및 생성
```java
// 수평 방향, 최소 0, 최대 200, 초기값 100을 가지는 슬라이더 생성
JSlider slider = new JSlider(JSlider.HORIZONTAL, 0, 200, 100);

// 눈금 표시 설정
slider.setPaintTicks(true);         // 눈금을 화면에 그림
slider.setPaintLabels(true);        // 수치 라벨(0, 50, 100...) 표시
slider.setPaintTrack(true);         // 트랙 라인 가시화
slider.setMajorTickSpacing(50);     // 주 눈금 간격 50px
slider.setMinorTickSpacing(10);     // 보조 눈금 간격 10px
```

### 2) ChangeEvent 처리
슬라이더의 값이 손잡이 조작에 의해 실시간으로 바뀔 때마다 **`ChangeEvent`**가 유발되며, `ChangeListener` 인터페이스의 `stateChanged(ChangeEvent e)`를 재정의하여 슬라이더 값을 제어합니다.
* **`int getValue()`**: 슬라이더의 현재 정수 값을 리턴합니다.
* **`void setValue(int n)`**: 프로그램 내부에서 강제로 손잡이의 위치를 `n` 값의 위치로 조절합니다.

```java
slider.addChangeListener(new ChangeListener() {
    public void stateChanged(ChangeEvent e) {
        int val = slider.getValue(); // 현재 슬라이더 눈금 값 가져오기
        System.out.println("Slider Value: " + val);
    }
});
```

---

# Citations
* [11Swing.pdf](../../../raw/notes/java/11Swing.pdf)
