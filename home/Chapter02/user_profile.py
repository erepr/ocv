import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtCore import pyqtSignal, QThread
import random
import serial

msg = []
yellow = [(0, 0)]
blue = [(0, 0)]
red = [(0, 0)]

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 747, 792)
        self.setWindowTitle("Map")

        self.setUpMainWindow()
        self.show()
      

    def setUpMainWindow(self):

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("kandivli.png"))

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("yellow.png"))

        self.label1 = QLabel(self)
        self.label1.setPixmap(QPixmap("blue.png"))

        self.label2 = QLabel(self)
        self.label2.setPixmap(QPixmap("circle.png"))
        
        self.timer = QTimer(self)
        self.timer2 = QTimer(self)
        self.timer3 = QTimer(self)
        self.timer.timeout.connect(self.reload)
        self.timer2.timeout.connect(self.reload1)
        self.timer3.timeout.connect(self.reload2)
        self.timer.start(2000)
        self.timer2.start(2000)
        self.timer3.start(2000)
        
        self.init_serial()
        self.worker = WorkerThread()
        self.worker.start()   

    def reload(self):
        self.createImageLabels() 

    def reload1(self):
        self.createImageLabels1() 

    def reload2(self):
        self.createImageLabels2() 

    def createImageLabels(self):
        self.label.move(yellow[0][0], yellow[0][1])

    def createImageLabels1(self):
        self.label1.move(blue[0][0], blue[0][1])

    def createImageLabels2(self):
        self.label2.move(red[0][0], red[0][1])

    def init_serial(self):
        global ser          
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = 'COM12'
        ser.timeout = 10
        ser.open()          
        if ser.isOpen():
            print ('Open: ' + ser.portstr)

class WorkerThread(QThread):
    def run(self):
        while 1:
                if ser.in_waiting > 0:
                    data_in = ser.readline()
                    
                    def filter(str):
                        if (str[2] == "&") & (str[24] == "*"):
                            return yellow
                        if (str[2] == "+") & (str[24] == ":"):
                            return blue
                        if (str[2] == "!") & (str[24] == "#"):
                            return red
                    try:
                        x = int(data_in[2:4]) + float(data_in[4:11]) / 60
                        y = int(data_in[12:15]) + float(data_in[15:22]) / 60
                        def getpx(y, x):
                            res_width = 747
                            res_height = 792
                            x1 = 72.866
                            x2 = 72.868
                            y1 = 19.209
                            y2 = 19.211
                            x = x-x1
                            y = y2-y
                            res_x = x*(res_width/(x2-x1))
                            res_y = y*(res_height/(y2-y1))
                            filter(str(data_in)).insert(0, (round(res_x-12.5), round(res_y-12.5)))
                            return round(res_x-12.5), round(res_y-12.5)
                        print(getpx(x, y))                      
                    except:
                        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())