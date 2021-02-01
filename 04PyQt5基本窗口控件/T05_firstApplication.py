# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/30 17:53
software: PyCharm

Description:
    app.exec_()可以带下划线也可以不带
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(300, 200)
window.move(250, 150)
window.setWindowTitle('Hallo, PyQt5')
window.show()
sys.exit(app.exec_())