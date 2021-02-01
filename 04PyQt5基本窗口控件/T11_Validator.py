# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/31 12:04
software: PyCharm

Description:
    T for tutorial

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class LineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(LineEditDemo, self).__init__(parent)
        self.setWindowTitle('QLineEdit例子')

        flo = QFormLayout()
        pIntLineEdit = QLineEdit()
        pDoubleLineEdit = QLineEdit()
        pValidatorLineEdit = QLineEdit()

        flo.addRow('整型', pIntLineEdit)
        flo.addRow('浮点型', pDoubleLineEdit)
        flo.addRow('字母和数字', pValidatorLineEdit)

        pIntLineEdit.setPlaceholderText("整型")
        pDoubleLineEdit.setPlaceholderText("浮点型")
        pValidatorLineEdit.setPlaceholderText("字母和数字")

        # 整型，范围[1, 99]
        pIntValidator = QIntValidator()
        pIntValidator.setRange(1, 99)

        # 浮点型，范围[-360, 360], 精度：小数点后两位
        pDoubleValidator = QDoubleValidator()
        pDoubleValidator.setRange(-360, 360)
        pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)
        pDoubleValidator.setDecimals(2)

        # 字母和数字
        reg = QRegExp("[a-zA-Z0-9]+$")
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)

        # 设置验证器
        pIntLineEdit.setValidator(pIntValidator)
        pDoubleLineEdit.setValidator(pDoubleValidator)
        pValidatorLineEdit.setValidator(pValidator)

        self.setLayout(flo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LineEditDemo()
    win.show()
    sys.exit(app.exec_())
