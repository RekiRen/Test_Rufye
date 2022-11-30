from PyQt.Core import Qt
from PyQt.QtWidgets import (QApplication, QWidget,
 QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit)

from instr import*

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
    def initui (self):
        self.ruf = QLabel(txt_workheart)
        self.rab = QLabel(txt_index)

        self.lay_1 = QVBoxLayout()
        self.lay_l.addwidget(self.ruf, alignment = Qt.ALignCenter)
        self.lay_l.addwidget(self.rab, alignment = Qt.ALignCenter)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)