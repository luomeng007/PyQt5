# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/3 16:45
software: PyCharm

Description:
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ToolBarDemo(QMainWindow):
    def __init__(self, parent=None):
        super(ToolBarDemo, self).__init__(parent)
        self.setWindowTitle("toolbar 例子")
        self.resize(300, 200)

        layout = QVBoxLayout()

        tb = self.addToolBar("File")

        new = QAction(QIcon("./images/cat.png"), "new", self)
        tb.addAction(new)

        open_ = QAction(QIcon("./images/cat.png"), "open", self)
        tb.addAction(open_)

        save = QAction(QIcon("./images/cat.png"), "save", self)
        tb.addAction(save)
        tb.actionTriggered[QAction].connect(self.toolbtnpressed)

        self.setLayout(layout)

    def toolbtnpressed(self, a):
        print("pressed tool button is " + a.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ToolBarDemo()
    form.show()
    sys.exit(app.exec_())
