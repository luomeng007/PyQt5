# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/3 16:51
software: PyCharm

Description:
    when we click show in menu, we will see a message in statusBar for 5 seconds.
    it is so cool
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class StatusDemo(QMainWindow):
    def __init__(self, parent=None):
        super(StatusDemo, self).__init__(parent)
        self.setWindowTitle("StatusDemo 例子")
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("show")
        file.triggered[QAction].connect(self.processTrigger)

        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def processTrigger(self, q):
        if q.text() == "show":
            self.statusBar.showMessage(q.text() + "菜单选项被点击了", 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = StatusDemo()
    form.show()
    sys.exit(app.exec_())
