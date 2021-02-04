# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/4 17:10
software: PyCharm

Description:
    we do not need to define specific layout, just use .move() to define absolute position
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("PyQt Line Edit example")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        button = QPushButton('OK', self)
        button.clicked.connect(self.clickMethod)
        button.resize(200, 32)
        button.move(80, 60)

    def clickMethod(self):
        print('Your name: ' + self.line.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
