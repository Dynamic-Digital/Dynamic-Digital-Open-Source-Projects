import yt_dlp
import tkinter.filedialog as filedialog
from yt_dlp.utils import DateRange

URLS = ['https://www.youtube.com/watch?v=VbjURh01yXo']

class Brain():
    def __init__(self) -> None:
        print("Created Model")

    def downloader(self, ydl_opts, urls):
        print(urls)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
    
    def getInfo(self, url) -> str:
        info = yt_dlp.YoutubeDL().sanitize_info(yt_dlp.YoutubeDL().extract_info(url, download=False))
        print(info)
    
    

