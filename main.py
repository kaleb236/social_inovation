import sys
from PyQt5.QtWidgets import QApplication
from social_ui import Ui_MainWindow

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent,QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class ui_windows(QMainWindow):
    def __init__(self):
        super(ui_windows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.create_event('NX34RTY', '12:00')
        self.create_event('NX54RTB', '14:00')
        self.ui.home_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.patients_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.add_combo()
        self.create_video()
    
    def add_combo(self):
        self.ui.task_comb.addItems(["ilaç", "asistan"])
        self.ui.morning.addItems(['seç','7:00', '8:00'])
        self.ui.after_noon.addItems(['seç','12:00', '12:30'])
        self.ui.evening.addItems(['seç','19:00', '19:30'])
    
    def create_event(self, name, time):
        frame = QFrame()
        frame.setObjectName('event_frame')
        frame.setStyleSheet('''
        QFrame#event_frame{
        background-color: #19A7CE;
        border: 1px solid #19A7CE;
        border-radius: 10px;
        }
        QLabel{
        color: white;
        font: 75 12pt "Century Gothic";
        }
        ''')
        layout = QHBoxLayout(frame)
        label_name = QLabel()
        label_name.setText(f'{name}')
        label_time = QLabel()
        label_time.setText(f'{time}')
        layout.addWidget(label_time)
        layout.addWidget(label_name)
        self.ui.event_layout.addWidget(frame)
    
    def create_video(self):
        self.mediaplayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        self.ui.video_layout.addWidget(videowidget)
        self.mediaplayer.setVideoOutput(videowidget)
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('images/rob.mp4')))
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        self.mediaplayer.setPlaylist(self.playlist)
        self.mediaplayer.setMuted(True)
        self.mediaplayer.play()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ui_windows()

    win.show()
    sys.exit(app.exec_())
