# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/30 16:15
software: PyCharm

Description:
"""
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys


app = QApplication(sys.argv)
widget = QWidget()
button = QPushButton(widget)
button.setText('Button')

# 以QWidget左上角为（0， 0）点
button.move(20,  20)
widget.resize(300, 200)

# 以屏幕左上角为(0, 0)点
widget.move(250, 200)
widget.setWindowTitle('PyQt 坐标系统例子')

widget.show()


print('QWidget:')
print('w.x()=%d' % widget.x())
print('w.y()=%d' % widget.y())
print('w.width()=%d' % widget.width())
print('w.height()=%d' % widget.height())
print('QWidget.geometry:')
print('widget.geometry().x()=%d' % widget.geometry().x())
print('widget.geometry().y()=%d' % widget.geometry().y())
print('widget.geometry().width()=%d' % widget.geometry().width())
print('widget.geometry().height()=%d' % widget.geometry().height())


sys.exit(app.exec_())
