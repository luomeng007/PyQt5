# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/31 11:52
software: PyCharm

Description:
    pNormalLineEdit.setPlaceholderText('Normal')
        设置没有填写的时候显示的文字
    flo.addRow('Normal', pNormalLineEdit):
        等同于在LineEdit元件前加了一个Label.
    当我们使用绝对位置进行LineEdit设置时，我们需要提前加上Label.
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout


class LineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(LineEditDemo, self).__init__(parent)
        self.setWindowTitle('QLineEdit 例子')

        flo = QFormLayout()
        pNormalLineEdit = QLineEdit()
        pNoEchoLineEdit = QLineEdit()
        pPasswordLineEdit = QLineEdit()
        pPasswordEchoOnEditLineEdit = QLineEdit()

        flo.addRow('Normal', pNormalLineEdit)
        flo.addRow("NoEcho", pNoEchoLineEdit)
        flo.addRow("Password", pPasswordLineEdit)
        flo.addRow("PasswordEchoOnEdit", pPasswordEchoOnEditLineEdit)

        pNormalLineEdit.setPlaceholderText('Normal')
        pNoEchoLineEdit.setPlaceholderText('NoEcho')
        pPasswordLineEdit.setPlaceholderText('Password')
        pPasswordEchoOnEditLineEdit.setPlaceholderText('PasswordEchoOnEdit')

        # 设置显示效果
        pNormalLineEdit.setEchoMode(QLineEdit.Normal)
        pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        pPasswordLineEdit.setEchoMode(QLineEdit.Password)
        pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(flo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LineEditDemo()
    win.show()
    sys.exit(app.exec_())
