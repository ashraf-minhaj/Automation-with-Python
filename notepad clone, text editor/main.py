"""
    Text Editor with Python


    author: ashraf minhaj
    mail  : ashraf_minhaj@yahoo.com
"""

""" install -
$ pip install tkinter
"""

# import everything needed from tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import sys

# menu button callback function
def saveFile():
    # open python, text files and all other files
    spath = asksaveasfilename(filetypes=[("Python Files", "*.py"),
                                         ("Text Files", "*.txt"), 
                                         ("All Files", "*.*")])
    with open(spath, 'w') as f:
        # get text from the editor
        contents = editor.get(1.0, END)
        #print(contents)
        f.write(contents) # write the texts into file
    root.title(f"My Text Editor  {spath}")

def openFile():
    opath = askopenfilename(filetypes=[("Python Files", "*.py"),
                                         ("Text Files", "*.txt"), 
                                         ("All Files", "*.*")])
    with open(opath, 'r') as f:
        # read the file
        contents = f.read()
        # add the texts of that file into the editor to edit
        editor.insert(END, contents)
    root.title(f"My Text Editor {opath}")

def exit():
    # close a python program
    sys.exit()

def helpBox():
    window = Toplevel()
    window.wm_title("Help")
    text = Label(window, text="Just google it dude!")
    text.pack()


# init
root = Tk()
root.title("My Text Editor")

# menubar section
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Open', command=openFile)
filemenu.add_command(label='Save', command=saveFile)
filemenu.add_command(label='Save As', command=saveFile)
filemenu.add_command(label='Exit', command=exit)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='Read Help', command=helpBox)

# add the filemenu to menubar
menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit')
menubar.add_cascade(label='View')
menubar.add_cascade(label='Help', menu=helpmenu)
root.config(menu=menubar)

# text edit section
editor = Text(root)
editor.pack(expand=True, fill=BOTH)  # to make it responsive

# run the app
root.mainloop()