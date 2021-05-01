# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/5 14:34
software: PyCharm

Description:
    basis of PyQt5
"""
# allow user handle the exit operation of the application
import sys

# import all necessary widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# create an instance of QApplication
# the reason for creating instance, QApplication object will do a lot initialization, like initialize in PyGame
# sys.argv allow us to make operation in command line
app = QApplication(sys.argv)
# if we do not want to operation in command line, we can directly do initialization like below
# app =QApplication([])

# create an instance of Gui
# QWidget is a Gui object
window = QWidget()
# set window title
window.setWindowTitle("PyQt5 App")
# set size of window
# first two parameters: the coordinates of window place (x, y)
# the second two parameters: the width and height of the window.
window.setGeometry(100, 100, 280, 80)
# show window on Gui object we create before
window.move(60, 15)
# here, we set the Msg_hello is the contained in window
# In PyQt5, if we do not set parent parameter, then widget will be at Top_Level
Msg_hello = QLabel("<h1>Hello, World!</h1>", parent=window)
Msg_hello.move(60, 15)

# show application's Gui
window.show()

# app.exec_() start application's event loop
# sys.exit(): exit application
# sys.exit(app.exec_()): exit application and cleanly clear memory.
sys.exit(app.exec_())