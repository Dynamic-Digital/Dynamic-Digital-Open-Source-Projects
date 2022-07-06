from threading import Timer
from PySide6.QtCore import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWidgets import QApplication
from flask import Flask, render_template
import yt_dlp
from flask_classful import FlaskView
import sys
import jyserver.Flask as jsf

app = Flask(__name__)

@jsf.use(app) # Connect Flask object to JyServer
class App:
    def __init__(self): # Create an __init__ method
        self.count = 0
        self.urls = []
        self.downloadInfo = []

    def increment(self):
        self.count += 1
        print("hello World!") # Increment method for DOM
        self.js.document.getElementById('counter').innerHTML = self.count
    
    def startDownload(self):
        text: str = self.js.document.getElementById('URLInput').value
        self.urls = str(text).splitlines()
        for url in self.urls:
            print(url)
    
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

TestView.register(app,route_base = '/')

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

if __name__ == '__main__':
    Timer(0, function=lambda: app.run(debug=False)).start()
    ui("http://127.0.0.1:5000")
