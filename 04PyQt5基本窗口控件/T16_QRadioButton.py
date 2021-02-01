# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/31 16:23
software: PyCharm

Description:
    可不可以同时维持选中状态呢？
"""
import sys
from PyQt5.QtWidgets import *


class RadioDemo(QWidget):
    def __init__(self, parent=None):
        super(RadioDemo, self).__init__(parent)
        self.setWindowTitle("RadioButton demo")

        layout = QVBoxLayout()

        self.btn1 = QRadioButton("Button1")
        self.btn1.setCheckable(True)
        self.btn1.toggled.connect(lambda: self.btn_state(self.btn1))
        layout.addWidget(self.btn1)

        self.btn2 = QRadioButton("Button2")
        self.btn2.toggled.connect(lambda: self.btn_state(self.btn2))
        layout.addWidget(self.btn2)

        self.setLayout(layout)

    def btn_state(self, btn):
        if btn.text() == "Button1":
            if btn.isChecked():
                print(btn.text() + "is selected")
            else:
                print(btn.text() + "is deselected")

        if btn.text() == "Button2":
            if btn.isChecked():
                print(btn.text() + "is selected")
            else:
                print(btn.text() + "is deselected")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    radioDemo = RadioDemo()
    radioDemo.show()
    sys.exit(app.exec_())
