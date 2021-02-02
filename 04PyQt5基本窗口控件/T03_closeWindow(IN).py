# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/29 14:04
software: PyCharm

Description:
    self.setGeometry(300, 300, 350, 350):
        the first two parameters are placing position left and top
        the second two parameters are size of window
    self.setWindowTitle('点击按钮关闭窗口'):
        set the name of widget
    quit_.setGeometry(10, 10, 60, 35)
        the first two parameters are placing position left and top
        the second two parameters are size of window
    quit_.clicked.connect(self.close):
        execute QWidget.close() method after clicking quit_ button we create
    self.close:
        QWidget has a close method, so this self represents the instance WinForm we create.
"""
import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)

        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('点击按钮关闭窗口')
        quit_ = QPushButton('close', self)
        quit_.setGeometry(10, 10, 60, 35)
        quit_.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
    