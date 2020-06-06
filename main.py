from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import subprocess

def get_name(*args):
    file_name_v.set(filedialog.askopenfilename(initialdir="/", title="Select file"))

def open_f(*args):
    proc = subprocess.run(["xxd", file_name_v.get()], stdout=subprocess.PIPE)
    line = proc.stdout.decode("utf-8")
    editor.insert(END, line)
    


root = Tk()
root.geometry("500x500")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

file_name_v = StringVar()

ttk.Label(mainframe, text="openfile").grid(column=1, row=0)
file_n = ttk.Entry(textvariable=file_name_v)
file_n.grid(column=0, row=0)
file_n.bind('<1>', get_name)
ttk.Button(mainframe, text="open", command=open_f).grid(column=0, row=1)

editor = Text()
editor.grid(column=0, row=2)
root.mainloop()
# root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
# print (root.filename)
