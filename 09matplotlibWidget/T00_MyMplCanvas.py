# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/1 10:00
software: PyCharm

Description:
    通过创建一个类将FigureCanvas与QWidget联系起来
    使用from pylab import *时，对于random.randint(0, 10)要写为np.random.randint(0, 10)，否则无法识别
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pylab import *


class MyMplCanvas(FigureCanvas):
    """
    FigureCanvas的最终父类实际是QWidget
    """

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # 设置中文显示
        plt.rcParams["font.family"] = ["SimHei"]  # 用来正常显示中文标签
        plt.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号

        # 新建一个绘图对象
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        # 已经被取消了，现在已经自动了
        # self.axes.hold(False)   # 每次绘图时都不保留上一次绘图的结果

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        """
        定义FigureCanvas的尺寸策略，意思时设置FigureCanvas，使之尽可能向外填充空间
        """
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)

    """
    绘制静态图，可以在这里定义绘图逻辑
    """

    def start_static_plot(self):
        self.figure.suptitle("测试静态图")
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.axes.set_xlabel("静态图： X轴")
        self.axes.set_ylabel("静态图： Y轴")
        self.axes.grid(True)

    """
    定义绘制动态图函数，设置每隔一秒就会重新绘制一次图像，启动绘制动态图
    """

    def start_dynamic_plot(self, *args, **kwargs):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)  # 每隔一段时间触发一次update_figure()函数
        timer.start(1000)  # 触发的事件间隔为1秒

    """
    可以在这里修改动态图的逻辑
    """

    def update_figure(self):
        self.fig.suptitle("测试动态图")
        y = [np.random.randint(0, 10) for i in range(4)]
        self.axes.plot([0, 1, 2, 3], y, 'r')
        self.axes.set_xlabel("动态图： X轴")
        self.axes.set_ylabel("动态图： Y轴")
        self.axes.grid(True)
        self.draw()
