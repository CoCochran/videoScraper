from tkinter import *
from tkinter import ttk

class App(Frame):
    def __init__(self, parent=None, width=100, height=100, entry=""): #creates the application window
        Frame.__init__(self, parent)
        
        #creates the variables
        self.parent = parent
        self.width = width
        self.height = height 

        dimensions = f"{self.width}x{self.height}" #formats the diminsions to be used in the geometry function

        self.parent.geometry(dimensions) #resizes the window to default dimensions specfied by the creation of the class object
        self.parent.resizable(False, False) #locks window dimensions
        App.makeWidgets(self)

    
    def takeEntry(self):
        userEntry = self.entry.get()

    
    def makeWidgets(self): #makes the elements of the window
        self.parent.title("Video Scraper") #create window title
        App.URL_entry(self)

    
    def URL_entry(self): #creates a quit button using Tk().destroy
        
        #create label and place it
        entryLabel = ttk.Label(self.parent, text="Input a URL...")
        entryLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        #create entry and place it
        self.entry = ttk.Entry(self.parent, width = int(self.width - (self.width * 0.85))) #pretty self explanatory
        self.entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        #entry.place(relx=0.5, rely=0.5, anchor=CENTER) #places the button relative to window center

        #create submit button and place it
        submitButton = ttk.Button(self.parent, text="Submit", command=self.takeEntry)
        submitButton.place(relx=0.5, rely=0.6, anchor=CENTER)
    
def createApp(entry):
    width = 250
    height = 250

    root = Tk() #silly tkinter magic
    app = App(root, width, height, entry) #creates class object for the application
    root.mainloop() #silly tkinter magic

