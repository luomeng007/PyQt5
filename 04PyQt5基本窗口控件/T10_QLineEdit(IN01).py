# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/4 15:40
software: PyCharm

Description:
    self.label = QLabel("Salt:") is equal to two steps:
        1. self.label = QLabel()
        2 /self.label.setText("Salt:")
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QGridLayout


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.label = None
        self.line = None
        self.initUI()

    def initUI(self):
        # main window size, title and icon
        self.setMinimumSize(500, 350)
        self.setWindowTitle("Calculate a password hash in Linux")

        # lines for entering data
        self.label = QLabel("Salt:")
        self.line = QLineEdit()
        self.line.setPlaceholderText("e.g. $6$xxxxxxxx")

        # set layout
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.line, 0, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # show a widget
        self.show()


def main():
    app = QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
