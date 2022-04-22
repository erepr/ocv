import sys
from PyQt6.QtWidgets import (QApplication, QWidget)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from latest import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec())


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.initializeUI()
        self.show()

    #def initializeUI(self):

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())