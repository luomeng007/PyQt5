# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/31 23:25
software: PyCharm

Description:
    this is so cool
"""
import sys
from PyQt5.QtWidgets import *
from T00_MyMplCanvas import MyMplCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.layout = None
        self.mpl = None
        self.mpl_ntb = None
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        # 如果想要在初始化时就呈现静态图，请取消这行注释
        # self.mpl.start_static_plot()
        # 如果想要在初始化时就呈现动态图，请取消这行注释
        # self.mpl.start_dynamic_plot()
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的工具栏

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    # ui.mpl.start_static_plot()  # 测试静态图效果
    ui.mpl.start_dynamic_plot()  # 测试动态图效果
    ui.show()
    sys.exit(app.exec_())
