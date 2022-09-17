from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import Qt

class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi('./ui/printdetails.ui', self)

        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.showFullScreen()

        self.pushButton.clicked.connect(self.exit)

    def exit(self):
        print('gg')
        
