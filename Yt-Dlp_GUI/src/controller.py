from viewTkinter import *
from brain import *
import yt_dlp
import threading
import os

class MyLogger:
    def __init__(self) -> None:
        self._controller = None
    
    def register(self, controller):
        self._controller: Controller = controller

    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            self._controller._view.debugLogVar.set(msg)
        else:
            self._controller._view.debugLogVar.set(msg)

    def info(self, msg):
        self._controller._view.debugLogVar.set(msg)

    def warning(self, msg):
        self._controller._view.debugLogVar.set(msg)

    def error(self, msg):
        self._controller._view.debugLogVar.set(msg)

class Controller:
    def __init__(self, view, model, logger) -> None:
        self._view: MainWindow = view
        self._model: Brain = model
        self._logger: MyLogger = logger
        self._view.register(self)
        self._logger.register(self)
        # print("Created Controller")
        self._view.launchApp()
        self._fileDir = " "

    def my_hook(self, d):
        """

        Controls the progress bar and updates it as the download progresses

        """
        self._view.progress["maximum"] = d["total_bytes"]
        if self._view.progress["value"] < d["total_bytes"]:
            self._view.progress["value"] = d["downloaded_bytes"]
            self._view.app.update_idletasks()

    def youtubeAPI(self):

        self.text: str = self._view.entryBox.get("1.0", "end-1c")
        self.urlList = self.text.splitlines()

        for url in self.urlList:
            # Gets the info from youtubedlp in an unserialisable format
            dirtyInfo = yt_dlp.YoutubeDL().extract_info(url, download=False)

            # converts info to serialisable dictionary
            cleanInfo = yt_dlp.YoutubeDL().sanitize_info(dirtyInfo)

            #call setview
            self.setView(cleanInfo)
            self.download(url)

    def setView(self, response):
        self._view.videoTitleText.set(response["title"])
        self._view.videoDescriptionText.set(response["description"])   

    def download(self, url):
        self.text: str = self._view.entryBox.get("1.0", "end-1c")
        self.urlList = self.text.splitlines()
        ydl_opts = {
            'download_archive': self._fileDir + "/downloaded.txt",
            # 'daterange': DateRange('20220422', '20220426'),
            'logger': self._logger,
            'format': 'mp4/best',
            'progress_hooks': [self.my_hook],
            'outtmpl': self._fileDir + '/%(uploader)s/%(title)s.%(ext)s',
            
        }
        self._model.downloader(ydl_opts, url)
    
    def startDownload(self):
        dlThread = threading.Thread(target=self.download)
        dlThread.start()


if __name__ == "__main__":
    view = MainWindow()
    model = Brain()
    logger = MyLogger()
    controller = Controller(view, model, logger)