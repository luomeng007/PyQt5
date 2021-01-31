# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/29 18:45
software: PyCharm

Description:
    QMainWindow.QPushButton():
        主窗口创建一个按钮
    self.button1.clicked.connect(self.onButtonClick)：
        将点击按钮事件与self.onButtonClick函数联系起来
    sender = self.sender()
        将发送信号的对象获取到，即我们按下去的关闭主窗口按钮
    qApp = QApplication.instance()：
        获取QApplication对象当前产生的实例
    qApp.quit()
        退出当前实例，即关闭了当前的主窗口
"""
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QApplication, QWidget
import sys


class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('关闭主窗口例子')
        self.button1 = QPushButton('关闭主窗口')
        self.button1.clicked.connect(self.onButtonClick)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self):
        # sender 是发送信号的对象
        sender = self.sender()
        print(sender.text() + '被按下了')
        qApp = QApplication.instance()
        qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
