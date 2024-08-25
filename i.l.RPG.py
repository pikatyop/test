from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint
from time import *

def right_answer():
    victory_win = QMessageBox()
    victory_win.setText("Ви виграли зустріч з творцями каналу!")
    victory_win.exec()
def wrong_answer():
    victory_win = QMessageBox()
    victory_win.setText("Пощастить іншим разом!")
    victory_win.exec()
app = QApplication([])
win = QWidget()
win.setWindowTitle("Конкурс від Crazy People")
win.move(30,60)
win.resize(400,200)


text = QLabel("Як звали першого ютуб-блогера, який набрав 100000000 підписників?")

ans1 = QRadioButton("PewDiePie")
ans2 = QRadioButton("Рет і Лінк")
ans3 = QRadioButton("SlivkiShow")
ans4 = QRadioButton("TheBrian")
ans5 = QRadioButton("Mister Max")
ans6 = QRadioButton("EeOneGuy")
ans7 = QRadioButton("EeOneGuy")
ans8 = QRadioButton("EeOneGuy")
ans9 = QRadioButton("EeOneGuy")
main = QVBoxLayout()
lay1 = QHBoxLayout()
lay2 = QHBoxLayout()
lay3 = QHBoxLayout()
lay4 = QHBoxLayout()



lay1.addWidget(text, alignment = Qt.AlignCenter)
lay2.addWidget(ans1, alignment = Qt.AlignCenter)
lay2.addWidget(ans2, alignment = Qt.AlignCenter)
lay2.addWidget(ans3, alignment = Qt.AlignCenter)
lay3.addWidget(ans4, alignment = Qt.AlignCenter)
lay3.addWidget(ans5, alignment = Qt.AlignCenter)
lay3.addWidget(ans6, alignment = Qt.AlignCenter)
lay4.addWidget(ans7, alignment = Qt.AlignCenter)
lay4.addWidget(ans8, alignment = Qt.AlignCenter)
lay4.addWidget(ans9, alignment = Qt.AlignCenter)
main.addLayout(lay1)
main.addLayout(lay2)
main.addLayout(lay3)
main.addLayout(lay4)

win.setLayout(main)
ans1.clicked.connect(right_answer)
ans2.clicked.connect(wrong_answer)
ans3.clicked.connect(wrong_answer)
ans4.clicked.connect(wrong_answer)
ans5.clicked.connect(wrong_answer)
ans6.clicked.connect(wrong_answer)
ans7.clicked.connect(wrong_answer)
ans8.clicked.connect(wrong_answer)
ans9.clicked.connect(wrong_answer)
win.show()
app.exec_()