from cProfile import label
from tkinter import *
from tkinter.ttk import *

class MainWindow:
    def __init__(self) -> None:
        self._controller = None
        self.app = None
        print("Created view")
    
    def register(self, controller):
        self._controller = controller
        if self._controller != None:
            print("Controller registered")
        else:
            print("Controller not registered")

    def refreshUI(self):
        self.app.destroy()
        self.launchApp()
        print("Hello World")

    def launchApp(self):
        self.app = Tk()
        self.app.title("YT-DLP GUI")
        self.app.geometry("600x400")

        self.style = Style()
        self.style.configure("Custom.TButton",foreground="white",
                                         background="black",
                                         padding=[20, 10, 20, 10],
                                         font = "Verdana 12 underline")

        self.style.configure("Custom.TFrame", bordercolor="blue", foreground="white", borderwidth=6)

        self.menu = Frame(self.app, style="Custom.TFrame")
        self.menu.grid(column=0, row=0)
        
        self.btn1 = Button(self.menu, text="Refresh View", style="Custom.TButton", command=self.refreshUI)
        self.btn1.grid(column=0, row=0, padx=10)

        self.dlBtn = Button(self.menu, text="Start Download", command=self._controller.startDownload)
        self.dlBtn.grid(column=0, row=1)

        self.fra2 = Frame(self.app)
        self.fra2.grid(column=1, row=0)
        
        self.entryBox = Text(self.fra2, width=40)
        self.entryBox.pack()

        self.app.mainloop()




