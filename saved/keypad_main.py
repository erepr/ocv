import sys
from PyQt6.QtWidgets import (QApplication, QWidget,
 QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from keypad import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initializeUI()
        self.show()

    def initializeUI(self):
        """Set up the application's GUI."""
        # Update other line_edit features
        # Set the max number of characters allowed
        self.ui.lineEdit_1.setMaxLength(1)
        # User can only enter ints from 0-9
        self.ui.lineEdit_1.setValidator(QIntValidator(0, 9))
        # Widget does not accept focus
        self.ui.lineEdit_1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        self.ui.lineEdit_2.setMaxLength(1)
        self.ui.lineEdit_2.setValidator(QIntValidator(0, 9))
        self.ui.lineEdit_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        self.ui.lineEdit_3.setMaxLength(1)
        self.ui.lineEdit_3.setValidator(QIntValidator(0, 9))
        self.ui.lineEdit_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        self.ui.lineEdit_4.setMaxLength(1)
        self.ui.lineEdit_4.setValidator(QIntValidator(0, 9))
        self.ui.lineEdit_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.passcode = 8618

        # Add signal/slot connections for buttons
        self.ui.pushButton_0.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_0.text()))
        self.ui.pushButton_1.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_1.text()))
        self.ui.pushButton_2.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_2.text()))
        self.ui.pushButton_3.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_3.text()))
        self.ui.pushButton_4.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_4.text()))
        self.ui.pushButton_5.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_5.text()))
        self.ui.pushButton_6.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_6.text()))
        self.ui.pushButton_7.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_7.text()))
        self.ui.pushButton_8.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_8.text()))
        self.ui.pushButton_9.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_9.text()))
        self.ui.pushButton_hash.clicked.connect(self.checkPasscode)

    def numberClicked(self, text_value):
        """When a button with a digit is pressed, check if the text for QLineEdit widgets are empty. If empty,
        set the focus to the correct widget and enter text value."""
        if self.ui.lineEdit_1.text() == "":
            self.ui.lineEdit_1.setFocus()
            self.ui.lineEdit_1.setText(text_value)
            self.ui.lineEdit_1.repaint() # ensure that text is updated in the QLineEdit widgets
        elif (self.ui.lineEdit_1.text() != "") and (self.ui.lineEdit_2.text() == ""):
            self.ui.lineEdit_2.setFocus()
            self.ui.lineEdit_2.setText(text_value)
            self.ui.lineEdit_2.repaint()
        elif (self.ui.lineEdit_1.text() != "") and (self.ui.lineEdit_2.text() != "") and (self.ui.lineEdit_3.text() == ""):
            self.ui.lineEdit_3.setFocus()
            self.ui.lineEdit_3.setText(text_value)
            self.ui.lineEdit_3.repaint()
        elif (self.ui.lineEdit_1.text() != "") and (self.ui.lineEdit_2.text() != "") and (self.ui.lineEdit_3.text() != "") and (self.ui.lineEdit_4.text() == ""):
            self.ui.lineEdit_4.setFocus()
            self.ui.lineEdit_4.setText(text_value)
            self.ui.lineEdit_4.repaint()

    def checkPasscode(self):
        """Concatenate the text values from the 4 QLineEdit widgets, and check to see if the passcode entered by
        user matches existing passcode."""
        entered_passcode = self.ui.lineEdit_1.text() + self.ui.lineEdit_2.text() + self.ui.lineEdit_3.text() + self.ui.lineEdit_4.text()
        if len(entered_passcode) == 4 and int(entered_passcode) == self.passcode:
            QMessageBox.information(self, "Valid Passcode!", "Valid Passcode!", QMessageBox.StandardButton.Ok)
            self.close()
        else:
            QMessageBox.warning(self, "Error Message", "Invalid Passcode.", QMessageBox.StandardButton.Close)
            self.ui.lineEdit_1.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_1.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Keypad = MainWindow()
    sys.exit(app.exec())