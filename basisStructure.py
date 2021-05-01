# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/5/1 11:02
software: PyCharm

Description:
    basic structure of PyQt5
        normal structure
        class structure
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# normal structure
app = QApplication(sys.argv)

window = QMainWindow()

window.move(100, 100)

window.show()

sys.exit(app.exec_())


# class structure
class App(QMainWindow):
    # App instance is at top-level
    def __init__(self, parent=None):
        super(App, self).__init__(parent)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec_())
