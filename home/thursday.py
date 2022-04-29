from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QDate, QTime, QTimer, pyqtSignal, QThread
import serial

input_buffer = []
new_str = ""
msg2 =  ["waiting for messages"]

style_sheet = """
    QPushButton#pushButton_23{
        background-color: #3e990c;
        border-radius: 5px;
        padding: 6px;
        color: #FFFFFF
    }
"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000) 

        self.init_serial()
        self.worker = WorkerThread()
        self.worker.start()   

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 323)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #8f120b;\n"
                                    " border-color: #dbd7d7;\n"
                                    "border-width: 2px; \n"
                                    "border-style: solid;\n"
                                    "border-radius: 4px;\n"
                                    "padding: 10px;\n"
                                    " font: bold 18px Courier")
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 60, 250, 51))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #3e990c;\n"
                                   " border-color: #dbd7d7;\n"
                                   " border-width: 2px; \n"
                                   "border-style: solid;\n"
                                   "border-radius: 4px;\n"
                                   "padding: 10px; \n"
                                   " font: bold 18px Courier")
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 30, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 130, 411, 31))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Upto 16 Chars only")
        self.lineEdit.setInputMask("9999999999999999;")
        
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 160, 491, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")

        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 21, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.zero)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 40, 21, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.one)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 40, 21, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.two)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 40, 21, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.three)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 40, 21, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.four)

        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 40, 21, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.five)

        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 40, 21, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.six)

        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 40, 21, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.seven)

        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(250, 40, 21, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.eight)

        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(280, 40, 21, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.nine)

        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_13.setGeometry(QtCore.QRect(350, 40, 31, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.backspace)
        
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_14.setGeometry(QtCore.QRect(310, 40, 31, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.esc)
        
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_15.setGeometry(QtCore.QRect(160, 70, 31, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_16.setGeometry(QtCore.QRect(200, 70, 31, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_17.setGeometry(QtCore.QRect(290, 70, 31, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 70, 41, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_19.setGeometry(QtCore.QRect(60, 70, 31, 23))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_20.setGeometry(QtCore.QRect(100, 70, 51, 23))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_21.setGeometry(QtCore.QRect(240, 70, 41, 23))
        self.pushButton_21.setObjectName("pushButton_21")
        
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_23.setGeometry(QtCore.QRect(390, 40, 81, 23))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(self.ent)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def init_serial(self):
        global ser          
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = 'COM4'
        ser.timeout = 10
        ser.open()          
        if ser.isOpen():
            print ('Open: ' + ser.portstr)
    
    def updateDateTime(self):
        self.label_2.setText(msg2[0][2:])

    def zero(self):
        input_buffer.append(self.pushButton.text())
        self.lineEdit.setText(new_str.join(input_buffer))
        print(new_str.join(input_buffer))

    def one(self):
        input_buffer.append(self.pushButton_2.text())
        self.lineEdit.setText(new_str.join(input_buffer))
        print(new_str.join(input_buffer))

    def two(self):
        input_buffer.append(self.pushButton_3.text())
        self.lineEdit.setText(new_str.join(input_buffer))
        print(new_str.join(input_buffer))

    def three(self):
        input_buffer.append(self.pushButton_4.text())
        self.lineEdit.setText(new_str.join(input_buffer))
        print(new_str.join(input_buffer))

    def four(self):
        input_buffer.append(self.pushButton_5.text())
        self.lineEdit.setText(new_str.join(input_buffer))
        print(new_str.join(input_buffer))

    def five(self):
        input_buffer.append(self.pushButton_6.text())
        self.lineEdit.setText(new_str.join(input_buffer))
        print(new_str.join(input_buffer))

    def six(self):
        input_buffer.append(self.pushButton_7.text())
        self.lineEdit.setText(new_str.join(input_buffer))
        print(new_str.join(input_buffer))

    def seven(self):
        input_buffer.append(self.pushButton_8.text())
        self.lineEdit.setText(new_str.join(input_buffer))
        print(new_str.join(input_buffer))

    def eight(self):
        input_buffer.append(self.pushButton_9.text())
        self.lineEdit.setText(new_str.join(input_buffer))
        print(new_str.join(input_buffer))

    def nine(self):
        input_buffer.append(self.pushButton_10.text())
        self.lineEdit.setText(new_str.join(input_buffer))
        print(new_str.join(input_buffer))

    def esc(self):
        input_buffer.clear()
        self.lineEdit.setText(new_str.join(input_buffer))
        print(new_str.join(input_buffer))

    def backspace(self):
        try:
            input_buffer.pop(-1)
            self.lineEdit.setText(new_str.join(input_buffer))
            print(new_str.join(input_buffer))
        except:
            pass     

    def ent(self):
        send = new_str.join(input_buffer)
        if len(send)>16:
            l = send[:16]
            self.label_3.setText(l)
            arr2 = bytes(l, 'ascii')
            ser.write(arr2)
            print(l)
        else:
            self.label_3.setText(send)
            arr3 = bytes(send, 'ascii')
            ser.write(arr3)
            print(send)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Aircraft #1 Rx"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", "Aircraft #1 Tx"))
        self.pushButton.setText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "2"))
        self.pushButton_4.setText(_translate("MainWindow", "3"))
        self.pushButton_5.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setText(_translate("MainWindow", "6"))
        self.pushButton_8.setText(_translate("MainWindow", "7"))
        self.pushButton_9.setText(_translate("MainWindow", "8"))
        self.pushButton_10.setText(_translate("MainWindow", "9"))
        self.pushButton_13.setText(_translate("MainWindow", "<<"))
        self.pushButton_14.setText(_translate("MainWindow", "ESC"))
        self.pushButton_15.setText(_translate("MainWindow", "TGT"))
        self.pushButton_16.setText(_translate("MainWindow", "LL"))
        self.pushButton_17.setText(_translate("MainWindow", "RR"))
        self.pushButton_18.setText(_translate("MainWindow", "CNFM"))
        self.pushButton_19.setText(_translate("MainWindow", "ACK"))
        self.pushButton_20.setText(_translate("MainWindow", "ALOK"))
        self.pushButton_21.setText(_translate("MainWindow", "ABRT"))
        self.pushButton_23.setText(_translate("MainWindow", "ENT"))

class WorkerThread(QThread):
    def run(self):
        while 1:
                if ser.in_waiting > 0:
                    data_in = ser.readline()
                    msg2.insert(0, str(data_in))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(style_sheet) 
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
