from Tkinter import *
import tkMessageBox as mbox
import Tkinter, Tkconstants, tkFileDialog
import ttk
import os.path
import getHTML
import urllib2

# Init()
root = Tk()
root.title("Read And View File Avi") # Title
root.resizable(0,0) # removing maximum
root.geometry("750x400+150+150") # Size && Location Appear Form
value = ""
dictFile = {}
# ---

# Methods

def checkHostLink():
    if entryHost.get() == '':
        mbox.showerror("Error", "Link URL is not exist. Try again!!!")
        return
    
    try:
        ret = urllib2.urlopen(entryHost.get())
    except:
        mbox.showerror("Error", "Web Server is not exist. Try again!!!")
        return

    global dictFile
    dictFile = { i.split("/")[len(i.split("/"))-1]:i for i in getHTML.getHTML(entryHost.get()) }
    # return getHTML.getHTML(entryHost.get())
    for i in dictFile.keys():
        lb.insert(END,i)

def onSelect(val):
    sender = val.widget
    idx = sender.curselection()
    global value
    value = sender.get(idx)
    var.set(value)

def onOpen():
    root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("avi files","*.avi"),("all files","*.*")))
    appendToList(root.filename)

def appendToList(addName):
    addName = addName.encode('ascii','ignore')
    stringName = addName.split("/")[len(addName.split("/"))-1]
    dictFile[stringName] = addName
    lb.insert(END, stringName)    

def onExit():
    quit()

def onError():
    mbox.showerror("Error", "Could not open file. Try Again!!!")

def playVideo():
    import readFileAvi
    readFileAvi.CaptureVideo(dictFile[value])

def checkFileExist(fileName):
    if fileName != "":
        return os.path.isfile(fileName)

def onInfo():
        mbox.showinfo("Information", "Project Read and View File Avi")

def onHelp():
        mbox.askquestion("Question", "All Questions Are Welcome")

# ---

# Properties
# Label
label1 = Label(root, text="List File Avi")
label1.config(width=25)
label1.config(font=("Courier", 15))
label1.grid(row=0, column=0)
# ---

# Entry
entryHost = Entry(root)
entryHost.config(width=25)
entryHost.grid(row=0, column=1)
# ---

# Button
checkButton = Button(text='Check Host', command=checkHostLink, width=15)
checkButton.config(font=("Courier", 10))
checkButton.grid(row=0, column=2)
# ---

# List box 
lb = Listbox(root, height=15, width=20)
lb.grid(row=1, column=0)
lb.bind("<<ListboxSelect>>", onSelect)

var = StringVar()
labelInfo = Label(text=0, textvariable=var, width = 25)
labelInfo.config(font=("Courier", 15))
labelInfo.grid(row=2, column=0);
# ---

# Button [BrowseButton]
BrowseButton = Button(text="Browse", command=onOpen, width=25)
BrowseButton.config(font=("Courier", 10))
BrowseButton.grid(row=1, column=1)
# ---

# Menu
menuBar = Menu(root)
root.config(menu=menuBar)
fileMenu = Menu(menuBar)
fileMenu.add_command(label="Open", command=playVideo)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=onExit)
menuBar.add_cascade(label="File", menu=fileMenu)

fileMenu1 = Menu(menuBar)
fileMenu1.add_command(label="Help", command=onHelp)
fileMenu1.add_separator()
fileMenu1.add_command(label="About", command=onInfo)
menuBar.add_cascade(label="Help", menu=fileMenu1)
# ---

# Button [Open File]
OpenButton = Button(text="Open File", command=playVideo, width=25)
OpenButton.config(font=("Courier", 10))
OpenButton.grid(row=3, column=0, sticky = W)
# ---

# Button Close
closeButton = Button(text="Close", command=onExit, width=25)
closeButton.config(font=("Courier", 10))
closeButton.grid(row=3, column=1)
# ---
# --- 
root.mainloop()