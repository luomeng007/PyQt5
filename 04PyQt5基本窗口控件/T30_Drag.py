# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/3 10:23
software: PyCharm

Description:
    self.setAcceptDrops(True):
        设定允许拖拽

Attention:
    一定要注意初始化函数是__init__而不是__int__!!!!

    self.addItem(e.mimeData().text())中的mimeData()必须加括号，否则错误
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Combo(QComboBox):
    def __init__(self, title, parent):
        super(Combo, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lo = QFormLayout()
        lo.addRow(QLabel("请把左边的文本框拖拽到右边的下拉菜单中"))
        edit = QLineEdit()
        edit.setDragEnabled(True)
        com = Combo("Button", self)
        lo.addRow(edit, com)
        self.setLayout(lo)
        self.setWindowTitle("简单的拖拽例子")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
