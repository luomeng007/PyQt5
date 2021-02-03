# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/3 10:19
software: PyCharm

Description:
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    label = QLabel()
    label.setPixmap(QPixmap("./images/cat.png"))
    vbox = QVBoxLayout()
    vbox.addWidget(label)
    win.setLayout(vbox)
    win.show()
    sys.exit(app.exec_())
