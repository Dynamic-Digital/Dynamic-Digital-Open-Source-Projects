import yt_dlp
from yt_dlp.utils import DateRange

URLS = ['https://www.youtube.com/watch?v=VbjURh01yXo']

class Brain():
    def __init__(self) -> None:
        print("Created Model")

    def downloader(self, ydl_opts, urls):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)

