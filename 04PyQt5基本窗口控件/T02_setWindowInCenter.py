# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/29 18:38
software: PyCharm

Description:
    to show MainWindow at the center position

    QDesktopWidget() is a class to describe the screen
    QDesktopWidget().screenGeometry():
        get the size of screen
    size = self.geometry():
        get the size of QWidget
    self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))：
        move window to center of screen
"""
import sys
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow


class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('主窗口放在屏幕中间的例子')
        self.resize(370, 250)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
