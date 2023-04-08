import os
from threading import Timer
from PySide6.QtCore import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWidgets import *
from flask import Flask, render_template
import yt_dlp
from flask_classful import FlaskView
import sys
import jyserver.Flask as jsf
import brain

app = Flask(__name__)

class MyLogger:
    def __init__(self) -> None:
        self._controller = None

    def register(self, controller):
        self._controller = controller

    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            self._controller.setMessageDownloadProgress(msg)
        else:
            self._controller.setMessageDownloadProgress(msg)

    def info(self, msg):
        self._controller.setMessageDownloadProgress(msg)

    def warning(self, msg):
        self._controller.setMessageDownloadProgress(msg)

    def error(self, msg):
        self._controller.setMessageDownloadProgress(msg)

@jsf.use(app) # Connect Flask object to JyServer
class App:
    def __init__(self): # Create an __init__ method
        self.count = 0
        self.urls = []
        self.downloadInfo = []
        self.brain: brain.Brain = brain.Brain()
        self._logger = MyLogger()
        self._fileDir = "~"
        self._logger.register(self)
        

    def increment(self):
        self.count += 1
        print("hello World!") # Increment method for DOM
        self.js.document.getElementById('counter').innerHTML = self.count
    
    def selectDownloadDir():
        fileDialog = QFileDialog()
        fileDialog.fileMode = QFileDialog.Directory

    def setMessageDownloadProgress(self, msg):
        print(msg)

    def my_hook(self, d):
        """

        Controls the progress bar and updates it as the download progresses

        """
        self.js.document.getElementById("downloadProgress").max = d["total_bytes"]
        if self.js.document.getElementById("downloadProgress").value < d["total_bytes"]:
            self.js.document.getElementById("downloadProgress").value = d["downloaded_bytes"]
    
    def registerController(self, controller):
        self.controller = controller
    
    def startDownload(self):
        print("downloading now")
        text: str = self.js.document.getElementById('URLInput').value
        self.urls = str(text).splitlines()
        ydl_opts = {
            'download_archive': "./downloaded.txt",
            'logger': self._logger,
            'format': 'mp4/best',
            'progress_hooks': [self.my_hook],
            'outtmpl': self._fileDir + '/%(uploader)s/%(title)s.%(ext)s',
            
        }
        self.brain.downloader(ydl_opts, self.urls)
    
    def PrintInput(ctx, input):
        print(input)
    
    def getInformation(self):
        self.js.document.getElementById('buttonGrid').innerHTML = ""
        self.urls = str(self.js.document.getElementById('URLInput').value).splitlines()
        for url in self.urls:
            videoInfo = yt_dlp.YoutubeDL().sanitize_info(yt_dlp.YoutubeDL().extract_info(url, download=False))
            self.js.showDownloadInfo(videoInfo["description"], videoInfo["title"], videoInfo["thumbnail"], videoInfo["view_count"])

class TestView(FlaskView):

    def index(self):
    # http://localhost:5000/
        return App.render(render_template('index.html'))

TestView.register(app, route_base = '/')

# Define function for QtWebEngine
def ui(location):
    qt_app = QApplication()
    web = QWebEngineView()
    web.setWindowTitle("YT-DLP GUI")
    web.resize(900, 800)
    web.setZoomFactor(1)
    web.load(QUrl(location))
    web.show()
    sys.exit(qt_app.exec_())

if __name__ == "__main__":
    Timer(0, function=lambda: app.run(debug=False)).start()
    ui("http://127.0.0.1:5000")
