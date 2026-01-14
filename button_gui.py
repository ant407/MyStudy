import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

# 버튼을 눌렀을 때 실행될 함수(기능)
def on_button_click():
    label.setText("버튼이 눌렸습니다! 🎉")
    label.setAlignment(Qt.AlignCenter) # 글자 가운데 정렬

# 앱과 윈도우 생성
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("이벤트 처리 예제")
window.resize(300, 200)

# 레이아웃(배치 도구) 생성 - 위젯을 세로로 정렬해줌
layout = QVBoxLayout()

# 1. 라벨(글자) 만들기
label = QLabel("버튼을 눌러보세요.")
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)

# 2. 버튼 만들기
button = QPushButton("누르기")
layout.addWidget(button)

# 3. 버튼과 함수 연결하기 (가장 중요!)
# 버튼이 클릭(clicked)되면 -> on_button_click 함수를 실행(connect)하라
button.clicked.connect(on_button_click)

# 윈도우에 레이아웃 적용
window.setLayout(layout)
window.show()

sys.exit(app.exec())