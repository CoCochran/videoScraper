import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
import os

class App(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        App.makeWidgets(self)

    def makeWidgets(self):
        self.root = Tk()
        self.root.title("Video Scraper")

root = Tk()
app = App(root)
root.mainloop()