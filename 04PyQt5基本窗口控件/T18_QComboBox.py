# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/31 21:56
software: PyCharm

Description:
    it is cool!
"""
import sys
from PyQt5.QtWidgets import *


class ComboxDemo(QWidget):
    def __init__(self, parent=None):
        super(ComboxDemo, self).__init__(parent)
        self.setWindowTitle("Combox Demo")
        self.resize(300, 90)
        layout = QVBoxLayout()
        self.lbl = QLabel("")

        groupBox = QGroupBox("Checkboxes")
        groupBox.setFlat(True)

        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selection_change)

        layout.addWidget(self.cb)
        layout.addWidget(self.lbl)
        self.setLayout(layout)

    def selection_change(self, i):
        self.lbl.setText(self.cb.currentText())
        print("Items in the list are: ")
        for count in range(self.cb.count()):
            print("item" + str(count) + "=" + self.cb.itemText(count))
            print("Current index", i, "selection changed", self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxDemo = ComboxDemo()
    comboxDemo.show()
    sys.exit(app.exec_())
