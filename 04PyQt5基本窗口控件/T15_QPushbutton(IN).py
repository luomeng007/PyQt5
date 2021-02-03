# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/3 11:48
software: PyCharm

Description:
    two methods to create buttons
        1.only give the name of button
            button = QPushButton("Button1")
        2. give the name of button and the widget which we want to add button to.
            button = QPushButton('PyQt5 button', self)
            the second parameter is the current widget we want to add.

        button.move(100, 70):
            move the button to a relative position corresponding to current main widget

Problem:
    what is the mean of @pyqtSlot(), no idea!!!


"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100, 70)
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
