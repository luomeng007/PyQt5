# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/31 22:39
software: PyCharm

Description:
    1. draw text
    2. draw points
    qp.drawPoint(x, y)：
        参数应该为整数，如果为float类型会有警告信息产生
"""
import sys, math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


# ======================================================================================================================
# draw text
# class Drawing(QWidget):
#     def __init__(self, parent=None):
#         super(Drawing, self).__init__(parent)
#         self.setWindowTitle("draw text in window")
#         self.resize(500, 200)
#         self.text = "welcome to learn PyQt5"
#
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.begin(self)
#         # 自定义绘制方法
#         self.drawText(event, painter)
#         painter.end()
#
#     def drawText(self, event, qp):
#         # 设置画笔的颜色
#         qp.setPen(QColor(168, 34, 3))
#         # 设置字体
#         qp.setFont(QFont("SimSun", 20))
#         # 绘制文字
#         qp.drawText(event.rect(), Qt.AlignCenter, self.text)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Drawing()
#     demo.show()
#     sys.exit(app.exec_())
# ======================================================================================================================
# draw points


class DrawingPoints(QWidget):
    def __init__(self, parent=None):
        super(DrawingPoints, self).__init__(parent)
        self.setWindowTitle("draw points in window")
        self.resize(300, 200)

    def paintEvent(self, event):
        # 初始化绘图工具
        qp = QPainter()
        # 开始在窗口中绘制
        qp.begin(self)
        # 自定义画点方法
        self.drawPoints(qp)
        # 结束在窗口中绘制
        qp.end()

    def drawPoints(self, qp):
        # 设置画笔的颜色
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            # 绘制正弦函数图形，它的周期是[-100, 100]
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DrawingPoints()
    demo.show()
    sys.exit(app.exec_())
