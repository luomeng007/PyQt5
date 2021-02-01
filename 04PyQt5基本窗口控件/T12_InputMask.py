# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/31 12:24
software: PyCharm

Description:
    it is so cool
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout


class LineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(LineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit的输入掩码例子")

        flo = QFormLayout()
        pIPLineEdit = QLineEdit()
        pMACLineEdit = QLineEdit()
        pDateLineEdit = QLineEdit()
        pLicenseLineEdit = QLineEdit()

        pIPLineEdit.setInputMask("000.000.000.000;_")
        pMACLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        pDateLineEdit.setInputMask("0000-00-00")
        pLicenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        flo.addRow('数字掩码', pIPLineEdit)
        flo.addRow('Mac掩码', pMACLineEdit)
        flo.addRow('日期掩码', pDateLineEdit)
        flo.addRow('日期掩码', pLicenseLineEdit)

        self.setLayout(flo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LineEditDemo()
    win.show()
    sys.exit(app.exec_())
