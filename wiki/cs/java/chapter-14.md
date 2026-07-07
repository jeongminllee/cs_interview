---
type: Study Note
title: "Chapter 14: Java File Input/Output (자바 파일 입출력)"
description: "자바의 입출력 스트림(Stream) 개념과 바이트/문자 스트림 분류, 그리고 성능 향상을 위한 버퍼 스트림(BufferedReader/BufferedWriter) 활용법을 다룹니다."
tags: [java, file-io, stream, buffered-stream, swing-lab]
timestamp: 2026-06-19
status: active
---

# Summary
자바의 파일 입출력(File I/O) 시스템은 스트림(Stream)을 기본 단위로 하며, 버퍼링 기술 및 다양한 필터 스트림을 결합하여 데이터를 효율적으로 읽고 쓸 수 있는 구조를 제공합니다. 본 문서에서는 입출력 스트림의 원리, 바이트 스트림과 문자 스트림의 차이, 성능을 극대화하는 버퍼 스트림, 그리고 Swing GUI와 연동한 파일 탐색기 실습 예제(LAB)를 상세하게 설명합니다.

# Why it matters
- **자원 관리 및 예외 처리**: 입출력(I/O)은 시스템 리소스를 직접 점유하므로 예외 상황(`IOException`)에 강인해야 하며, 사용 완료 후 반드시 `close()`를 통해 자원을 반환해야 시스템 누수(Memory Leak / File Descriptor Exhaustion)를 방지할 수 있습니다.
- **성능 최적화**: 디스크 I/O는 메모리 연산에 비해 매우 느립니다. 버퍼(Buffer) 스트림을 사용하면 여러 번에 걸친 디스크 접근을 단 한 번으로 통합하여 시스템 콜(System Call) 횟수를 획기적으로 줄일 수 있습니다.

# Key Ideas
1. **스트림(Stream)의 정의 및 특징**:
   - 스트림은 데이터의 순차적인 흐름을 추상화한 소프트웨어 모듈입니다.
   - **단방향성 (Unidirectional)**: 입력 스트림과 출력 스트림이 철저하게 분리되어 있으며, 단일 스트림으로 동시에 양방향 전송을 처리할 수 없습니다.
   - **선입선출 (FIFO)**: 스트림에 들어온 순서대로 데이터가 차례대로 나가는 큐(Queue) 구조를 따릅니다.
2. **입출력 스트림의 분류**:
   - **바이트 스트림 (Byte Stream)**:
     - 데이터를 8비트(1바이트) 단위로 그대로 전송합니다.
     - 이미지, 비디오, 오디오, 실행 파일과 같은 바이너리(Binary) 데이터 처리에 적합합니다.
     - 최상위 클래스: `InputStream`, `OutputStream`
     - 파일 입출력 구현 클래스: `FileInputStream`, `FileOutputStream`
   - **문자 스트림 (Character Stream)**:
     - 데이터를 16비트(2바이트) 단위의 문자(Character) 단위로 전송합니다. 자바의 문자 자료형인 `char`은 내부적으로 UTF-16 방식을 취하므로 1문자당 2바이트를 할당받기 때문입니다.
     - 텍스트 파일(메모장, HTML 등)의 글자가 깨지지 않도록 유니코드로 인코딩/디코딩 작업을 수행합니다.
     - 최상위 클래스: `Reader`, `Writer`
     - 파일 입출력 구현 클래스: `FileReader`, `FileWriter`
3. **주요 메서드 비교 (문자 스트림 기준)**:
   - `FileReader` / `FileWriter`의 핵심 API:
     | 메서드 시그니처 | 설명 |
     |---|---|
     | `int read()` | 스트림으로부터 한 문자(2바이트)를 읽어 반환합니다. 더 이상 읽을 데이터가 없는 끝(EOF)에 도달하면 `-1`을 반환합니다. |
     | `int read(char[] cbuf)` | 데이터를 여러 개 읽어서 문자 배열인 `cbuf`에 채우고, 실제로 읽어들인 문자의 개수를 반환합니다. EOF 도달 시 `-1`을 반환합니다. |
     | `void write(int c)` | 지정한 하나의 문자를 출력 스트림에 씁니다. |
     | `void write(char[] cbuf)` | `cbuf` 문자 배열에 들어 있는 전체 내용을 스트림에 출력합니다. |
     | `void write(String str)` | 주어진 문자열 전체를 출력 스트림에 출력합니다. |
     | `void write(char[] cbuf, int off, int n)` | 문자 배열 `cbuf`의 `off` 오프셋부터 `n`개의 문자만큼 스트림에 출력합니다. |
4. **버퍼 스트림 (Buffered Stream)을 통한 성능 향상**:
   - 디스크 또는 네트워크로 데이터를 전송할 때, 매번 한 바이트 혹은 한 문자 단위로 요청(System Call)을 보내는 대신 메모리 버퍼(보통 8KB)를 내부에 두어 데이터를 모았다가 한꺼번에 입출력을 수행합니다.
   - **보조 스트림 연결 구조**:
     ```java
     // 파일 입력에 버퍼 적용
     BufferedReader fin = new BufferedReader(new FileReader("menu.txt"));
     // 파일 출력에 버퍼 적용
     BufferedWriter fout = new BufferedWriter(new FileWriter("new_menu.txt"));
     ```
   - **버퍼 스트림의 주요 메서드**:
     - `String readLine()`: 한 줄(개행 문자 `\n` 또는 `\r\n` 기준) 전체를 한 번에 문자열로 읽어서 반환합니다. 스트림의 끝에 도달하면 `null`을 반환합니다.
     - `void newLine()`: 플랫폼에 독립적인 줄 바꿈을 위해, 현재 OS 시스템의 표준 줄 바꿈 문자(Windows는 `\r\n`, Unix/Linux는 `\n`)를 출력 스트림에 씁니다.
     - `void flush()`: 아직 출력 스트림의 버퍼가 가득 차지 않았더라도, 버퍼링되어 대기 중인 모든 잔류 데이터를 즉시 물리적인 출력 장치(디스크 등)로 방출합니다.
     - `void close()`: 스트림을 안전하게 닫습니다. 이때 버퍼에 남아있던 데이터를 자동으로 `flush()`한 후 시스템 자원을 릴리즈합니다.

# Examples / LAB Code (Swing File Explorer)
Swing 컴포넌트(`JFileChooser`, `JTextArea`, `JScrollPane`, `JMenuBar`, `JMenuItem`)와 자바 파일 입출력 API를 결합하여 텍스트 파일을 열고 편집한 뒤 다시 저장할 수 있는 GUI 메모장 애플리케이션의 구현 예제입니다.

```java
import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;

public class Swing extends JFrame {
    // 텍스트를 입력하고 보여줄 영역
    JTextArea tf = new JTextArea(5, 20);

    public Swing() {
        setTitle("File 예제");
        setSize(350, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        
        // 상단 메뉴 바 및 메뉴 설정
        createMenu();
        
        tf.setLineWrap(true);      // 단어 단위 줄 바꿈 활성화
        tf.setWrapStyleWord(true); // 완전한 단어 기준으로 줄바꿈
        
        // 스크롤바가 포함된 텍스트 영역을 중앙에 추가
        add(new JScrollPane(tf), BorderLayout.CENTER);
        setVisible(true);
    }

    private void createMenu() {
        JMenuBar mb = new JMenuBar();
        JMenu fileMenu = new JMenu("File");
        JMenuItem saveItem = new JMenuItem("Save");
        
        // 파일 저장 (Save) 이벤트 리스너 정의
        saveItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser chooser = new JFileChooser();
                // 텍스트 파일(.txt) 필터 설정
                FileNameExtensionFilter filter = new FileNameExtensionFilter("텍스트 파일(*.txt)", "txt");
                chooser.setFileFilter(filter);
                
                int ret = chooser.showSaveDialog(null);
                if (ret != JFileChooser.APPROVE_OPTION) {
                    return; // 사용자가 저장을 취소한 경우
                }
                
                File file = chooser.getSelectedFile();
                // 사용자가 .txt 확장자를 직접 쓰지 않은 경우 자동 생성 처리
                if (!file.getName().endsWith(".txt")) {
                    file = new File(file.getAbsolutePath() + ".txt");
                }
                
                // 버퍼 스트림을 통한 파일 쓰기 시도
                try {
                    BufferedWriter bw = new BufferedWriter(new FileWriter(file));
                    String contents = tf.getText();
                    bw.write(contents);
                    bw.close(); // 스트림을 닫으며 버퍼 내용을 flush 및 close
                    JOptionPane.showMessageDialog(null, "성공적으로 저장되었습니다.");
                } catch (IOException io) {
                    JOptionPane.showMessageDialog(null, "파일 저장 중 오류가 발생했습니다.");
                }
            }
        });

        JMenuItem openItem = new JMenuItem("Open");
        // 파일 열기 (Open) 이벤트 리스너 정의
        openItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser chooser = new JFileChooser();
                FileNameExtensionFilter filter = new FileNameExtensionFilter("텍스트 파일(*.txt)", "txt");
                chooser.setFileFilter(filter);
                
                int ret = chooser.showOpenDialog(null);
                if (ret != JFileChooser.APPROVE_OPTION) {
                    return; // 사용자가 열기를 취소한 경우
                }
                
                File file = chooser.getSelectedFile();
                
                // 버퍼 스트림을 통한 파일 읽기 시도
                try {
                    BufferedReader br = new BufferedReader(new FileReader(file));
                    tf.setText(""); // 기존 입력 내용 초기화
                    String line = "";
                    while ((line = br.readLine()) != null) {
                        tf.append(line + "\n"); // 한 줄씩 텍스트 영역에 추가
                    }
                    br.close(); // 읽기 완료 후 자원 반환
                } catch (IOException io) {
                    JOptionPane.showMessageDialog(null, "파일을 읽어오는 중 오류가 발생했습니다.");
                }
            }
        });

        // 메뉴 구성 완성
        fileMenu.add(saveItem);
        fileMenu.add(openItem);
        mb.add(fileMenu);
        setJMenuBar(mb);
    }

    public static void main(String[] args) {
        new Swing();
    }
}
```

# Related Concepts
- **Try-With-Resources**: Java 7 이상부터 제공되는 문법으로, `AutoCloseable`을 구현하는 리소스(스트림 객체 등)를 `try(...)` 괄호 안에 선언하면 블록을 탈출할 때 예외 발생 여부와 상관없이 자동으로 `close()`가 호출되어 예외 처리와 안전한 자원 관리를 보장합니다.
- **Standard I/O Streams**: 자바 시스템이 구동될 때 기본적으로 활성화되는 표준 스트림인 `System.in`(키보드 입력), `System.out`(콘솔 출력), `System.err`(에러 출력)도 각각 바이트/문자 스트림의 변형 형태입니다.

# Citations
* [14자바파일입출력.pdf](../../../raw/notes/java/14자바파일입출력.pdf)
