from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QMessageBox, QHBoxLayout, QVBoxLayout

app = QApplication([])
win = QWidget()
win.setWindowTitle("Конкурс")
win.resize(400, 200)

question = QLabel('В якому році канал отримав "золоту кнопку" від YouTube?')
option1 = QRadioButton("2005")
option2 = QRadioButton("2010")
option3 = QRadioButton("2015")
option4 = QRadioButton("2020")

layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment=Qt.AlignCenter)

layout_H1 = QHBoxLayout()
layout_H1.addWidget(option1, alignment=Qt.AlignCenter)
layout_H1.addWidget(option2, alignment=Qt.AlignCenter)

layout_H2 = QHBoxLayout()
layout_H2.addWidget(option3, alignment=Qt.AlignCenter)
layout_H2.addWidget(option4, alignment=Qt.AlignCenter)

layout_main.addLayout(layout_H1)
layout_main.addLayout(layout_H2)
win.setLayout(layout_main)

def show_win():
    win_win = QMessageBox()
    win_win.setText("Правильно!\nВи виграли гіроскутер!")
    win_win.exec_()

def show_lose():
    lose_win = QMessageBox()
    lose_win.setText("Ні, 2015 року\nВи виграли фірмовий плакат")
    lose_win.exec_()

option1.clicked.connect(show_lose)
option2.clicked.connect(show_lose)
option3.clicked.connect(show_win)
option4.clicked.connect(show_lose)

win.show()
app.exec_()