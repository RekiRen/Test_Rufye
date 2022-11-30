from PyQt.Core import Qt
from PyQt.QtWidgets import (QApplication, QWidget,
 QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit)

from final_win import *
from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
    def initUI(self):
        self.fio = QLabel(txt_name)
        self.fio_edit = QLineEdit(txt_hintname)
        self.yer = QLabel(txt_age)
        self.yer_edit = QLineEdit(txt_hintage)
        self.text1 = QLabel(txt_test3)
        self.btn1 = QPushButton(txt_starttest1)
        self.btn1_edit = QLineEdit(txt_hinttest1)
        self.text2 = QLabel(txt_hinttest1)
        self.text2_edit = QPushButton(txt_starttest2)
        self.text3 = QLabel(txt_test3)
        self.text3_edit = QPushButton(txt_starttest3)
        self.zero1_edit = QLineEdit(txt_hinttest2)
        self.zero2_edit = QLineEdit(txt_hinttest3)
        self.otp = QPushButton(txt_sendresults)
        self.time = QLabel(txt_timer)

        self.lay_l = QVBoxLayout()
        self.lay_l.addwidget(self.fio, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.fio_edit, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.yer, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.yer_edit, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.text1, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.btn1, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.btn1_edit, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.text2, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.text2_edit, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.text3, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.text3_edit, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.zero1_edit, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.zero2_edit, alignment = Qt.ALignLeft)
        self.lay_l.addwidget(self.otp, alignment = Qt.ALignLeft)

        self.lay_r = QVBoxLayout()
        self.lay_r.addwidget(self.time, alignment = Qt.ALignCenter)

        self.lay_g = QHBoxLayout()
        self.lay_g.addLayout(self.lay_l)
        self.lay_g.addLayout(self.lay_r)
        self.setLayout(self.lay_g)

    def next_click(self):
        self.hide()
        self.tw = FinalWin()

    def connects(self):
        self.otp.clicked.connecr(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)