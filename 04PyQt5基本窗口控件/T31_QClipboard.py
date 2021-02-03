# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/2/3 11:48
software: PyCharm

Description:
    two methods to show widgets, for example:
        1. use form.show() outside class
        2. use self.show() inside class
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Clipboard 例子")

        textCopyButton = QPushButton("&Copy Text")
        textPasteButton = QPushButton("Paste &Text")
        htmlCopyButton = QPushButton("C&opy HTML")
        htmlPasteButton = QPushButton("Paste &HTML")
        imageCopyButton = QPushButton("Co&py Image")
        imagePasteButton = QPushButton("Paste &Image")
        self.textLabel = QLabel()
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap("./images/cat.png"))

        layout = QGridLayout()
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(imageCopyButton, 0, 1)
        layout.addWidget(htmlCopyButton, 0, 2)
        layout.addWidget(textPasteButton, 1, 0)
        layout.addWidget(imagePasteButton, 1, 1)
        layout.addWidget(htmlPasteButton, 1, 2)
        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)

        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

        self.setLayout(layout)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("I've been clipped!")

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap("./images/cat1.png"))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
