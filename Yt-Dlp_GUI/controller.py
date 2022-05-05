from view import *
from brain import *
import threading

class Controller:
    def __init__(self, view, model) -> None:
        self._view: MainWindow = view
        self._model: Brain = model
        self._view.register(self)
        print("Created Controller")
        self._view.launchApp()

    def my_hook(self, d):
        """

        Controls the progress bar and updates it as the download progresses

        """
        self._view.progress["maximum"] = d["total_bytes"]
        if self._view.progress["value"] < d["total_bytes"]:
            self._view.progress["value"] = d["downloaded_bytes"]
            self._view.app.update_idletasks()
        

    def download(self):
        self.text: str = self._view.entryBox.get("1.0", "end-1c")
        self.urlList = self.text.splitlines()
        ydl_opts = {
            'download_archive': "./downloaded.txt",
            # 'daterange': DateRange('20220422', '20220426'),
            'format': 'mp4/best',
            'progress_hooks': [self.my_hook],
            'outtmpl': '%(uploader)s/%(title)s.%(ext)s',
            
        }
        self._model.downloader(ydl_opts, self.urlList)
    
    def startDownload(self):
        dlThread = threading.Thread(target=self.download)
        dlThread.start()


if __name__ == "__main__":
    view = MainWindow()
    model = Brain()
    controller = Controller(view, model)