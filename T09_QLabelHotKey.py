# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/30 22:05
software: PyCharm

Description:
    可以使用alt + N 键切换到输入框1
    可以使用alt + P 键切换到输入框2
"""
import sys
from PyQt5.QtWidgets import *


class QlabelDemo(QDialog):
    def __init__(self):
        super(QlabelDemo, self).__init__()

        self.setWindowTitle('QLabel 例子')
        nameLb1 = QLabel('&Name', self)
        nameEd1 = QLineEdit(self)
        nameLb1.setBuddy(nameEd1)

        nameLb2 = QLabel('&Password', self)
        nameEd2 = QLineEdit(self)
        nameLb2.setBuddy(nameEd2)

        btnOk = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLb1, 0, 0)
        mainLayout.addWidget(nameEd1, 0, 1, 1, 2)

        mainLayout.addWidget(nameLb2, 1, 0)
        mainLayout.addWidget(nameEd2, 1, 1, 1, 2)

        mainLayout.addWidget(btnOk, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


def link_hovered():
    print("当鼠标滑过label2标签是，触发事件。")


def link_clicked():
    print("当鼠标点击label4标签时，触发事件。")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    labelDemo = QlabelDemo()
    labelDemo.show()
    sys.exit(app.exec_())
