from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

therme = False

def Change_therme():
    global therme
    if therme is True:
        main_win.setStyleSheet("background:black")
        therme = False
    else:
        main_win.setStyleSheet("background:white") 
        therme = True

def print_random():
    namber = str(randint(0, 1000000000000000000))
    namber_pluse.setText(namber)

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Casino")
vline = QVBoxLayout()

hello_text = QLabel("ЭТО РАНДОМ КАЗИНО!!!")
namber_pluse = QLabel("тут будет число")
random_btn = QPushButton("рандомное число")
black_therme_btn = QPushButton("Изменить тему!!!")
random_btn.clicked.connect(print_random)
black_therme_btn.clicked.connect(Change_therme)

vline.addWidget(hello_text, alignment= Qt.AlignCenter)
vline.addWidget(namber_pluse)
vline.addWidget(black_therme_btn)
vline.addWidget(random_btn)

main_win.setWindowIcon(QIcon("castle.ico"))

main_win.setLayout(vline)
main_win.resize(500,500)
main_win.show()
app.exec_() 
