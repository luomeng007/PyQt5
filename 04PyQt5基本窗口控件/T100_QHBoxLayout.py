# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/5/1 11:26
software: PyCharm

Description:
    the usage of QHboxLayout
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QHBoxLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        self.left_list = QListWidget()
        self.left_list.insertItem(0, "Contact")
        self.left_list.insertItem(1, "Personal")
        self.left_list.insertItem(2, "Educational")

        hbox = QHBoxLayout()
        hbox.addWidget(self.left_list)

        # add this layout on QMainWindow
        self.setLayout(hbox)


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
