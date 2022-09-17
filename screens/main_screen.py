from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from .printdetails import SecondWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('./ui/main.ui', self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()

        self.pushButton.clicked.connect(self.exit)
        self.pushButton_2.clicked.connect(self.showPrintDetails)

    def exit(self):
        print('exit')
        self.close()
        
    def showPrintDetails(self):
        print('opening')
        win = SecondWindow()
        win.exec()
        print('done')