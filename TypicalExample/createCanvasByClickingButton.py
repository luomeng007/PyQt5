# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/4 9:23
software: PyCharm

Description:
    add Canvas after click button
"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from MyMplCanvas import PlotCanvas


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.title = 'add Canvas'
        self.mpl = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('add Canvas', self)
        button.move(500, 0)
        button.resize(140, 100)
        button.clicked.connect(self.plot_static)

        self.show()

    def plot_static(self):
        self.mpl = PlotCanvas(self, width=5, height=4)
        self.mpl.move(0, 0)
        self.mpl.init_plot()

        self.mpl.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
