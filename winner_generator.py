from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

def print_random():
    namber = str(randint(0, 100))
    namber_pluse.setText(namber)

app = QApplication([])
main_win = QWidget()
vline = QVBoxLayout()

hello_text = QLabel("ЭТО РАНДОМ КАЗИНО!!!")
namber_pluse = QLabel("место для числа")
random_btn = QPushButton("рандомное число")
random_btn.clicked.connect(print_random)

vline.addWidget(hello_text, alignment= Qt.AlignCenter)
vline.addWidget(namber_pluse)
vline.addWidget(random_btn)

main_win.setWindowIcon(QIcon("castle.ico"))

main_win.setLayout(vline)
main_win.resize(500,500)
main_win.show()
app.exec_() 
