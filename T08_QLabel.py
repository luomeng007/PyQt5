# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/30 18:54
software: PyCharm

Description:
    如何设置字体的颜色

    label1.setAlignment(Qt.AlignCenter)
        设置文本框剧中显示
    label3.setAlignment(Qt.AlignCenter)
        设置文本框靠右显示

    this example is so cool!
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette


class WindowDemo(QWidget):
    def __init__(self):
        super(WindowDemo, self).__init__()

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # 初始化标签空间
        label1.setText('这是一个文本标签')
        label1.setAutoFillBackground(True)
        # 设定背景颜色
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.yellow)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI 应用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/cat.png"))

        label4.setText("<A href='https://blog.csdn.net/u011699626/article/details/113397056'>"
                       "numpy.mgrid()函数虚数参数问题</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')

        # 在窗口布局中添加控件
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        # 允许label1空间访问超链接
        label1.setOpenExternalLinks(True)
        # 打开允许访问超链接，默认是不允许，需要使用setOpenExternalLinks(True)允许浏览器访问超链接
        # 将下面的参数概为True就可以进行超链接访问了
        label4.setOpenExternalLinks(False)
        # 点击文本框绑定槽事件
        label4.linkActivated.connect(link_clicked)

        # 滑过文本框绑定槽事件
        label2.linkHovered.connect(link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel 例子')


def link_hovered():
    print("当鼠标滑过label2标签时，触发事件。")


def link_clicked():
    print("当鼠标点击label4标签时，触发事件。")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec_())
