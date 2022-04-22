import sys
from PyQt6.QtWidgets import (QApplication, QWidget,)
from PyQt6.QtCore import Qt
from vlc import Ui_MainWindow
import vlc
import sys
import os.path

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = setupUi()
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.ui.setupUi(self)
        self.initializeUI()
        self.show()

    def initializeUI(self):
        self.ui.playbutton.clicked.connect(self.PlayPause)
        self.ui.volumeslider.setValue(self.mediaplayer.audio_get_volume())
        self.ui.volumeslider.setToolTip("Volume")
        self.ui.volumeslider.valueChanged.connect(self.setVolume)

        self.timer = QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updateUI)

    def PlayPause(self):
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.playbutton.setText("Play")
            self.isPaused = True
        else:
            if self.mediaplayer.play() == -1:
                self.OpenFile()
                return
            self.mediaplayer.play()
            self.playbutton.setText("Pause")
            self.timer.start()
            self.isPaused = False
            
    def OpenFile(self, filename=None):
        self.media = self.instance.media_new(filename)
        self.mediaplayer.set_media(self.media)
        self.media.parse()
        self.setWindowTitle(self.media.get_meta(0))
        if sys.platform == "win32": 
            self.mediaplayer.set_hwnd(self.videoframe.winId())
        self.PlayPause()
        
    def setVolume(self, Volume):
        self.mediaplayer.audio_set_volume(Volume)
        
    def updateUI(self):
        if not self.mediaplayer.is_playing():
            self.timer.stop()
            if not self.isPaused:
                self.Stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = Player()
    player.show()
    #player.resize(640, 480)
    if sys.argv[1:]:
        player.OpenFile('rtsp://192.168.1.106:554/user=admin&password=admin@1234&channel=4&stream=0.sdp')
    sys.exit(app.exec_())