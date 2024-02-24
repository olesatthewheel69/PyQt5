from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

win = QWidget()
win.setWindowTitle("Генератор")
win.resize(400, 200)

text = QLabel("Натисни, щоб дізнатися переможця!")
winner = QLabel("?")
button = QPushButton("Згенерувати")

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
win.setLayout(line)

def show_winner():
    text.setText("Переможець:")
    winner.setText(str(randint(1, 100)))

button.clicked.connect(show_winner)

win.show()
app.exec_()