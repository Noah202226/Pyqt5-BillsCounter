from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt

from .printdetails import SecondWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('./ui/main.ui', self)

        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        
        self.printButton.clicked.connect(self.showPrintDetails)
        
        self.center()

        self.spinBox1.textChanged.connect(self.calculateTotal)
        self.spinBox5.textChanged.connect(self.calculateTotal)
        self.spinBox10.textChanged.connect(self.calculateTotal)
        self.spinBox20.textChanged.connect(self.calculateTotal)
        self.spinBox50.textChanged.connect(self.calculateTotal)
        self.spinBox100.textChanged.connect(self.calculateTotal)
        self.spinBox200.textChanged.connect(self.calculateTotal)
        self.spinBox500.textChanged.connect(self.calculateTotal)
        self.spinBox1000.textChanged.connect(self.calculateTotal)

        self.deductions.textChanged.connect(self.calculateTotal)
      
    def center(self):
        frame = self.frameGeometry()
        desktopCenter = QDesktopWidget().availableGeometry().center()
        print(f'frame: {frame}, desktop: {desktopCenter}')
        frame.moveCenter(desktopCenter)
        self.move(frame.topLeft())

    def calculateTotal(self):
        print('calculation ...')
        if self.deductions.text() == "":
            self.deductions.setText("0")
            self.calculateTotal()
        else:
            self.totalof1.setText(str(int(self.spinBox1.value()) * 1))
            self.totalof5.setText(str(int(self.spinBox5.value()) * 5))
            self.totalof10.setText(str(int(self.spinBox10.value()) * 10))
            self.totalof20.setText(str(int(self.spinBox20.value()) * 20))
            self.totalof50.setText(str(int(self.spinBox50.value()) * 50))
            self.totalof100.setText(str(int(self.spinBox100.value()) * 100))
            self.totalof200.setText(str(int(self.spinBox200.value()) * 200))
            self.totalof500.setText(str(int(self.spinBox500.value()) * 500))
            self.totalof1000.setText(str(int(self.spinBox1000.value()) * 1000))

            totalAmount = (str(int(self.totalof1.text()) + 
                            int(self.totalof5.text()) + 
                            int(self.totalof10.text()) + 
                            int(self.totalof20.text()) + 
                            int(self.totalof50.text()) + 
                            int(self.totalof100.text()) + 
                            int(self.totalof200.text()) + 
                            int(self.totalof500.text()) + 
                            int(self.totalof1000.text())))

            self.totalAmount.setText(totalAmount)

            self.remainingAmount.setText(str(int(totalAmount) - int(self.deductions.text()))) 

    def showPrintDetails(self):
        win = SecondWindow()
        win.data.setPlainText((f'Total of 1: {self.totalof1.text()}\n'
                        f'Total of 5: {self.totalof5.text()}\n'
                        f'Total of 10: {self.totalof10.text()}\n'
                        f'Total of 20: {self.totalof20.text()}\n'
                        f'Total of 50: {self.totalof50.text()}\n'
                        f'Total of 100: {self.totalof100.text()}\n'
                        f'Total of 200: {self.totalof200.text()}\n'
                        f'Total of 500: {self.totalof500.text()}\n'
                        f'Total of 1000: {self.totalof1000.text()}\n\n'
                        f'Total Amount: {self.totalAmount.text()}\n'
                        f'Deduction: {self.deductions.text()}\n'
                        f'Remaining Amount: {self.remainingAmount.text()}\n'
                        ))
        # win.data.setPlainText(f'Total of 1: {self.totalof1.text()}\nTotalof5: {self.totalof5.text()}\nTotalof10: {self.totalof10.text()}\nTotalof20: {self.totalof20.text()}\nTotalof50: {self.totalof50.text()}\nTotalof100: {self.totalof100.text()}\nTotalof200: {self.totalof200.text()}\nTotalof500: {self.totalof500.text()}\nTotalof1000: {self.totalof1000.text()}\nDeduction: {self.deductions.text()}\nRemaining Amount: {self.remainingAmount.text()}\n')
        win.exec()