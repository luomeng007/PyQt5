# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/31 22:10
software: PyCharm

Description:
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class SpinDemo(QWidget):
    def __init__(self, parent=None):
        super(SpinDemo, self).__init__(parent)
        self.setWindowTitle("SpinBox Demo")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.l1 = QLabel("current value: ")
        self.l1.setAlignment(Qt.AlignCenter)
        self.l1.setText("current value: 0")

        layout.addWidget(self.l1)

        self.sp = QSpinBox()
        layout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.value_change)

        self.setLayout(layout)

    def value_change(self):
        self.l1.setText("current value: " + str(self.sp.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    spinDemo = SpinDemo()
    spinDemo.show()
    sys.exit(app.exec_())
