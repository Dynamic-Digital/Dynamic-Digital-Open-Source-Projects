from bleach import clean
from view import *
from brain import *
import yt_dlp
import threading
import json
import requests as webrequests
import os
import googleapiclient.discovery

class Controller:
    def __init__(self, view, model) -> None:
        self._view: MainWindow = view
        self._model: Brain = model
        self._view.register(self)
        # print("Created Controller")
        self._view.launchApp()

    def my_hook(self, d):
        """

        Controls the progress bar and updates it as the download progresses

        """
        self._view.progress["maximum"] = d["total_bytes"]
        if self._view.progress["value"] < d["total_bytes"]:
            self._view.progress["value"] = d["downloaded_bytes"]
            self._view.app.update_idletasks()

    def youtubeAPI(self):
        #TODO Remove in Production
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = ""

        self.text: str = self._view.entryBox.get("1.0", "end-1c")
        self.urlList = self.text.splitlines()

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

        for url in self.urlList:
            # Gets the info from youtubedlp in an unserialisable format
            dirtyInfo = yt_dlp.YoutubeDL().extract_info(url, download=False)

            # converts info to serialisable dictionary
            cleanInfo = yt_dlp.YoutubeDL().sanitize_info(dirtyInfo)

            request = youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=cleanInfo["id"]
            )
            response = request.execute()
            self.setView(response)
            self.download(url)

    def setView(self, response):
        self._view.videoTitleText.set(response["items"][0]["snippet"]["title"])
        self._view.videoDescriptionText.set(response["items"][0]["snippet"]["description"])   

    def download(self, url):
        self.text: str = self._view.entryBox.get("1.0", "end-1c")
        self.urlList = self.text.splitlines()
        ydl_opts = {
            'download_archive': "./downloaded.txt",
            # 'daterange': DateRange('20220422', '20220426'),
            'format': 'mp4/best',
            'progress_hooks': [self.my_hook],
            'outtmpl': '%(uploader)s/%(title)s.%(ext)s',
            
        }
        self._model.downloader(ydl_opts, url)
    
    def startDownload(self):
        dlThread = threading.Thread(target=self.download)
        dlThread.start()


if __name__ == "__main__":
    view = MainWindow()
    model = Brain()
    controller = Controller(view, model)