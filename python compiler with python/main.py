"""
Creating a Python Text Editor with Python

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
import tkinter
import subprocess

# save code path
code_path = ''

# menu button callback function
def saveFileAs():
    # open python files
    global code_path
    code_path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
    with open(code_path, 'w') as f:
        # get text from the editor
        contents = editor.get(1.0, END)
        #print(contents)
        f.write(contents) # write the texts into file

    root.title(f"Python Text Editor  {code_path}")

def save():
    # save the currently opened file
    global code_path
    contents = editor.get(1.0, END)

    if (contents != '') and code_path == '':
        # if content found but the file is new and not saved
        saveFileAs()
        return
    
    if contents == '':
        # if nothing is typed in editor
        # do nothing
        return
    
    # now save the file
    with open(code_path, 'w') as f:
        f.write(contents) # write the texts into file
    
    
def openFile():
    global code_path
    code_path = askopenfilename(filetypes=[("Python Files", "*.py")])
    with open(code_path, 'r') as f:
        # read the file
        contents = f.read()
        # add the texts of that file into the editor to edit
        editor.delete('1.0', END)
        editor.insert(END, contents)

    root.title(f"Python Text Editor  {code_path}")

def exit():
    # close a python program
    sys.exit()

def run():
    # run the python program
    global code_path
    print(code_path)
    if code_path == '':
        # in case of empty path
        #print("Invalid path, open a file or create one")
        window = Toplevel()
        window.wm_title("Error")
        text = Label(window, text="Invalid path, open a file or create one")
        text.pack()
        return
    # run python file
    command = 'python ' + code_path
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    output, error = process.communicate()
    #print(type(output))
    # convert the byte data into string - decode("utf-8")
    terminal_output.insert(END, output.decode("utf-8"))  # output of code 
    terminal_output.insert(END, error.decode("utf-8"))   # error

def saveAndRun():
    # save file then run
    save()
    run()
    

# init
root = Tk()
root.title("Python Text Editor")

# menubar section
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Open', command=openFile)
filemenu.add_command(label='Save', command=save)
filemenu.add_command(label='Save As', command=saveFileAs)
filemenu.add_command(label='Exit', command=exit)

run_menu = Menu(menubar, tearoff=0)
run_menu.add_command(label='Run', command=run)
run_menu.add_command(label='Save and Run', command=saveAndRun)

# add the filemenu to menubar
menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Run', menu=run_menu)
root.config(menu=menubar)

# *** frame that contains editor
frame1 = Frame(root, bd=10)
frame1.pack(expand=1, fill=BOTH)

# text edit section
editor = Text(frame1)
editor.pack(expand=1, fill=BOTH)  # to make it responsive

# *** terminal text section
frame2 = Frame(root, bd=10, height=5)
frame2.pack( expand=1, fill=BOTH)

terminal_output = Text(frame2, height=5)
terminal_output.pack( expand=True, fill=BOTH, side=BOTTOM)  # to make it responsive

# run the app
root.mainloop()