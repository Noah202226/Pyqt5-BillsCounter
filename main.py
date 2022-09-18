from ast import main
import sys

from PyQt5.QtWidgets import QApplication

from screens import main_screen

if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = main_screen.MainWindow()
    win.setFixedSize(600,550)
    win.show()

    sys.exit(app.exec_())
