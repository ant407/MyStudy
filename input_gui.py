import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

# 버튼을 누르면 실행될 함수
def show_text():
    # 1. 입력창(input_box)에 적힌 글자를 가져옵니다.
    user_text = input_box.text() 
    
    # 2. 결과 라벨(result_label)에 그 내용을 설정합니다.
    result_label.setText(f"당신이 쓴 글: {user_text}")

# 앱 설정
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("따라쟁이 프로그램")
layout = QVBoxLayout() # 위에서 아래로 쌓는 배치

# [입력창] 만들기
input_box = QLineEdit()
input_box.setPlaceholderText("여기에 아무거나 입력하세요") # 힌트 텍스트
layout.addWidget(input_box)

# [버튼] 만들기
button = QPushButton("출력하기")
button.clicked.connect(show_text) # 버튼 누르면 show_text 함수 실행
layout.addWidget(button)

# [결과 라벨] 만들기
result_label = QLabel("대기 중...")
layout.addWidget(result_label)

# 윈도우 표시
window.setLayout(layout)
window.show()

sys.exit(app.exec())