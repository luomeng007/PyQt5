# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/31 15:38
software: PyCharm

Description:
    &Download:
        &: 这个符号可以将Alt + 对应的按键联系起来，按下按键组合即完成了对应操作, 如这里可以直接使用Alt + D来完成对应操作。
    self.btn1.toggle()：
        用以切换按钮的状态
    self.btn1.setCheckable(True)：
        设定按钮是否可以被选中，默认不能够被选中。设置True使得按钮可以被选中
    if self.btn1.isChecked():
        判断按钮当前是否是被选中的状态，
        观察可以发现。如果按钮被选中，我们可以看到按钮整个是浅蓝色的
    self.btn1.toggle()：
        更改按钮当前是否被选中的状态，即加或不加该语句，按钮初始时被选中的状态是相反的
"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Button demo")

        layout = QVBoxLayout()

        self.btn1 = QPushButton("Button1")
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda: self.which_btn(self.btn1))
        self.btn1.clicked.connect(self.btn_state)
        layout.addWidget(self.btn1)

        self.btn2 = QPushButton("image")
        self.btn2.setIcon(QIcon(QPixmap("./images/cat.png")))
        self.btn2.clicked.connect(lambda: self.which_btn(self.btn2))
        layout.addWidget(self.btn2)

        self.btn3 = QPushButton("Disabled")
        self.btn3.setEnabled(False)
        self.btn3.clicked.connect(lambda: self.which_btn(self.btn3))
        layout.addWidget(self.btn3)

        self.btn4 = QPushButton("&Download")
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda: self.which_btn(self.btn4))
        layout.addWidget(self.btn4)

        self.setLayout(layout)

    def btn_state(self):
        if self.btn1.isChecked():
            print("button pressed")

    # @staticmethod
    # 这里也可以加上staticmethod，然后去点self，并且在connect函数中去点self，应该也可以实现对应的功能
    def which_btn(self, btn):
        print("clicked button is: " + btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    btnDemo = Form()
    btnDemo.show()
    sys.exit(app.exec_())
