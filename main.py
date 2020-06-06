from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as ScrolledText
import subprocess

def get_name(*args):
    file_name_v.set(filedialog.askopenfilename(initialdir="/", title="Select file"))

def open_f(*args):
    proc = subprocess.run(["xxd", file_name_v.get()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.stderr:
        messagebox.showerror(title="Error", message=proc.stderr.decode("utf-8"))
        return    
    line = proc.stdout
    editor.insert(END, line)
    
def save_f(*args):
    f = open("test", "w+")
    f.write(editor.get("@0,0", END))
    f.close()
    proc = subprocess.run(["xxd", "-r", "test"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.stderr:
        messagebox.showerror(title="Error", message=proc.stderr.decode("utf-8"))
        return
    line = proc.stdout.decode("utf-8")
    f = open(file_name_v.get(), "w")
    f.write(line)
    f.close()

def save_as(*args):
    filename = filedialog.asksaveasfilename(initialdir = "/", title = "Save file")
    f = open("test", "w+")
    f.write(editor.get("@0,0", END))
    f.close()
    proc = subprocess.run(["xxd", "-r", "test"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.stderr:
        messagebox.showerror(title="Error", message=proc.stderr.decode("utf-8"))
        return
    line = proc.stdout.decode("utf-8")
    f = open(filename, "w")
    f.write(line)
    f.close()

root = Tk()
root.geometry("500x500")
current_file_n = "" 
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=2)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=2)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)

file_name_v = StringVar()
file_n = ttk.Entry(textvariable=file_name_v)
file_n.grid(column=0, row=0, sticky="nw")

ttk.Button(mainframe, text="open", command=open_f).grid(column=0, row=1)
ttk.Button(mainframe, text="save", command=save_f).grid(column=0, row=2, sticky="s")
ttk.Button(mainframe, text="save as", command=save_as).grid(column=1, row=2, sticky="sw")

ttk.Label(mainframe, text="openfile").grid(column=1, row=0, sticky="nw")

file_n.bind('<1>', get_name)

editor = ScrolledText.ScrolledText(root)
editor.grid(column=0, row=3, columnspan=2, sticky="n")
root.mainloop()
