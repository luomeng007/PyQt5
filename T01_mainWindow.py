# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/29 18:04
software: PyCharm

Description:
    create main window

Code analyse:
    Now, MainWindow belongs to class QMainWindow. So the self in program represents the class QMainWindow.
    the we could use resize method in QMainWindow class to set the size of window, and use statusBar() method to
    create 状态栏， Then use showMessage() to show message in 状态栏.

Illustration:
    QMainWindow.resize(400, 200):
        set the size of window
            the first parameter is width
            the second parameter is height
    QMainWindow.statusBar():
        create 状态栏
    QMainWindow.status.showMessage("这是状态提示", -1):
        show message in 状态栏
        the first parameter is string type for message to show
        the second parameter is the time to show message, the unit is ms. For example. 5000 for showing 5s.
        if we want to keep showing message all the time, we could set time as -1.
    QMainWindow.setWindowTitle("PyQt MainWindow例子")
        the parameter is string type, for setting the title of window
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(400, 200)
        self.status = self.statusBar()
        self.status.showMessage("这是状态提示", 5000)  # show 5s
        self.setWindowTitle("PyQt MainWindow例子")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # set the icon of current window
    app.setWindowIcon(QIcon('./cat.ico'))
    form = MainWindow()
    # this is necessary, or we cannot see the window
    form.show()
    sys.exit(app.exec_())
