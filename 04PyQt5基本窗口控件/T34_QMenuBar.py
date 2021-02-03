# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/3 14:35
software: PyCharm

Description:
    bar = self.menuBar(), here self means QMainWindow, which is in top level
    file = bar.addMenu("File"):
        File menu is added to the menu bar by addMenu() method.

    four method to add menu bar.

Attention:
    file.triggered[QAction].connect(self.process_trigger)
    [QAction]的括号是方括号，不是圆括号

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MenuDemo(QMainWindow):
    def __init__(self, parent=None):
        super(MenuDemo, self).__init__(parent)
        self.setWindowTitle("menu 例子")
        layout = QHBoxLayout()

        bar = self.menuBar()

        file = bar.addMenu("File")
        file.addAction("New")

        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        edit = file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")

        quit_ = QAction("Quit", self)
        file.addAction(quit_)
        file.triggered[QAction].connect(self.process_trigger)

        self.setLayout(layout)

    def process_trigger(self, q):
        print(q.text() + " is triggered")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MenuDemo()
    form.show()
    sys.exit(app.exec_())