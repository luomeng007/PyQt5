# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/4 9:29
software: PyCharm

Description:
    button2.show():
        to show button on current main widget, it is necessary.
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("my window")
        self.setGeometry(10, 10, 320, 300)

        # creating a button to be clicked
        button1 = QPushButton('Button-1', self)
        button1.move(100, 70)
        button1.clicked.connect(self.on_click)  # button1

    @pyqtSlot()
    def on_click(self):
        print('Button-2 will be created')
        button2 = QPushButton('Button-2', self)
        button2.move(100, 200)
        button2.show()  # +++


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
