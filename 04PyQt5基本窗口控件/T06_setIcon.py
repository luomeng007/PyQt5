# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/1/30 17:59
software: PyCharm

Description:
    set icon for window
    we introduce two methods here. The second is a simplified one
"""
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget


class IconMethod01(QWidget):
    def __init__(self, parent=None):
        super(IconMethod01, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowIcon(QIcon('./icon/cat.ico'))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     icon = IconMethod01()
#     icon.show()
#     sys.exit(app.exec_())


# ======================================================================================================================


class IconMethod02(QWidget):
    def __init__(self, parent=None):
        super(IconMethod02, self).__init__(parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowIcon(QIcon('./icon/cat.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = IconMethod02()
    icon.show()
    sys.exit(app.exec_())
