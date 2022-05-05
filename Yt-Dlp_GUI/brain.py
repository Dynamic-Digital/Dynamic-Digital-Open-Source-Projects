import yt_dlp
from yt_dlp.utils import DateRange

URLS = ['https://www.youtube.com/watch?v=VbjURh01yXo']

class Brain():
    def __init__(self) -> None:
        print("Created Model")

    # def my_hook(self, d):
    #     """

    #     Controls the progress bar and updates it as the download progresses

    #     """

    #     widgets = [' [', progressbar.Percentage(), '] ',
    #         '[', d['filename'] , '] ',
    #         progressbar.Bar('*'),
    #         ' (', str(d['downloaded_bytes']), ' / ', str(d['total_bytes']), ') ',
    #         ]
    
    #     bar = progressbar.ProgressBar(maxval=d['total_bytes'], 
    #                                 widgets=widgets).start()

    #     if d['total_bytes'] > d['downloaded_bytes']:  
    #         bar.update(d['downloaded_bytes'])
    #     if d['status'] == 'finished':
    #         bar.update(d['total_bytes'])
    #         print('\n Done downloading, now post-processing ...')

    def downloader(self, ydl_opts, urls):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)

