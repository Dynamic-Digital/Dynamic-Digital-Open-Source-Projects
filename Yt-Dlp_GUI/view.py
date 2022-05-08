from pathlib import Path
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os

class MainWindow:
    def __init__(self) -> None:
        self._controller = None
        self.app = None
        # print("Created view")
    
    def register(self, controller):
        self._controller = controller
        # if self._controller != None:
        #    # print("Controller registered")
        # else:
        #     print("Controller not registered")

    def refreshUI(self):
        self.app.destroy()
        self.launchApp()
        # print("Hello World")
    
    def chooseDir(self):
        self._controller._fileDir = filedialog.askdirectory(title="Choose Download Directory", initialdir=Path.home())
        print(self._controller._fileDir)

    def launchApp(self):

        # Start app

        self.app = Tk()
        self.app.title("YT-DLP GUI")
        self.app.geometry("1000x600")

        # Tkinter Styles

        self.style = Style()
        self.style.configure("Custom.TButton",foreground="white",
                                         background="black",
                                         padding=[20, 10, 20, 10],
                                         font = "Verdana 12 underline")
        self.style.configure("Custom.TFrame", bordercolor="blue", foreground="white", borderwidth=6)

        # Left Side Menu

        self.menu = Frame(self.app, style="Custom.TFrame")
        self.menu.grid(column=0, row=0, sticky="N")
        
        self.btn1 = Button(self.menu, text="Refresh View", command=self.refreshUI, width=15)
        self.btn1.grid(column=0, row=0, padx=10)

        self.dlBtn = Button(self.menu, text="Start Download", command=self._controller.youtubeAPI, width=15)
        self.dlBtn.grid(column=0, row=1, padx=10)

        self.choosedlDir = Button(self.menu, text="Choose Download Dir", command=self.chooseDir)
        self.choosedlDir.grid(column=0, row=2)

        # URL input Panel

        self.fra2 = Frame(self.app)
        self.fra2.grid(column=1, row=0, sticky="N")
        
        self.entryBox = Text(self.fra2, width=40)
        self.entryBox.grid(column=0, row=0)

        self.progress = Progressbar(self.fra2, mode="determinate", length=300)
        self.progress.grid(column=0, row=1)

        self.debugLogVar = StringVar()
        self.debugLogVar.set("Debug Area")
        self.debugLog = Label(self.fra2, textvariable=self.debugLogVar)
        self.debugLog.grid(column=0, row=2)

        # Video Info Panel
        self.videoInfoContain = Frame(self.app, height=70)
        self.videoInfoContain.grid(column=2, row=0, sticky="N")

        self.videoTitleText = StringVar()
        self.videoTitleText.set("Video Title")
        self.videoTitle = Label(self.videoInfoContain, textvariable=self.videoTitleText, font=("Arial", 15), wraplength=500)
        self.videoTitle.grid(column=0, row=0, padx=60, pady=20)
        
        self.videoDescriptionText = StringVar()
        self.videoDescriptionText.set("Video Description")
        self.videoDescription = Label(self.videoInfoContain, wraplength=300, textvariable=self.videoDescriptionText)
        self.videoDescription.grid(column=0, row=1)

        self.app.mainloop()




