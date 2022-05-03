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

    def download(self):
        self.text: str = self._view.entryBox.get("1.0", "end-1c")
        self.urlList = self.text.splitlines()
        self._model.downloader(self.urlList)
    
    def startDownload(self):
        dlThread = threading.Thread(target=self.download)
        dlThread.start()


if __name__ == "__main__":
    view = MainWindow()
    model = Brain()
    controller = Controller(view, model)