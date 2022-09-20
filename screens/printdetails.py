from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt, QRect, QRectF, QPointF
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QBrush, QColor, QTextCursor
from PyQt5.QtPrintSupport import QPrinter

from datetime import datetime

class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi('./ui/printdetails.ui', self)

        self.printButton.clicked.connect(self.exit)

    def exit(self):
        print('printing')
        cursor = QTextCursor(self.data.document())
        cursor.setPosition(0)
        self.data.setTextCursor(cursor)

        self.data.insertPlainText(f'Date: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\nBills for: {self.billfor.text()}\nDeduction Name: {self.deductionName.text()}\n\n')
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPrinterName('XP-58')
        painter = QPainter()

        painter.begin(printer)
        painter.setRenderHint(QPainter.Antialiasing)
        # rect = QRect(10,10, 200,500)
        # painter.drawRect(rect)
        
        # painter.drawText(rect, Qt.AlignCenter, self.data.toPlainText())

        # Create Path
        path = QPainterPath()
        # Set painter colors to given values.
        pen = QPen(QColor(192, 192, 192), Qt.SolidLine)
        painter.setPen(pen)
        brush = QBrush(QColor(192, 192, 192))
        painter.setBrush(brush)

        rect = QRectF(0,0,400,500)

        path.addRoundedRect(rect, 10, 10)
        painter.setClipPath(path)

        painter.fillPath(path,painter.brush())
        # painter.strokePath(path,painter.pen())
        painter.drawText(rect,Qt.AlignLeft, self.data.toPlainText())

        painter.end()

        self.close()
        

