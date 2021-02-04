# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/4 8:10
software: PyCharm

Description:
"""
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Fixed,
                                   QSizePolicy.Fixed)
        FigureCanvas.updateGeometry(self)

    def init_plot(self):
        A0 = 1
        lambda_ = 532 * pow(10, -9)
        w0 = 0.00001
        z0 = np.pi / lambda_ * pow(w0, 2)
        wz_max = w0 * np.sqrt(1 + (z0 / z0)) * 2
        num = 101

        X = np.linspace(-wz_max, wz_max, num)
        Y = np.linspace(-wz_max, wz_max, num)

        Z = np.linspace(-z0, z0, num)
        x, y, z = np.meshgrid(X, Y, Z)

        v = A0 * 1 / (1 + 1j * (z / z0)) * np.exp(-((pow(x, 2) + pow(y, 2)) / pow(w0, 2) / (1 + 1j * z / z0)))

        result = np.ones(num)
        for i in range(num):
            result[i] = np.abs(v[i][50][50])

        self.figure.suptitle("Gaussian Evolution")
        self.axes.plot(X, result)
        self.axes.set_xlabel("Distance")
        self.axes.set_ylabel("Amplitude")
        # self.axes.grid(True)
        self.draw()
