# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/30 18:20
software: PyCharm

Description:
    气泡提示只有在鼠标悬停在空间上时才会出现
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip
from PyQt5.QtGui import QFont


class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Cambria', 10))
        self.setToolTip('这是个<b>气泡提示</b>')
        self.setGeometry(200, 300, 400, 400)
        self.setWindowTitle('气泡提示demo')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
