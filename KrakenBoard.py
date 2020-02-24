
#!/usr/bin/python

import tkinter as tk
from tkinter import *
from tkinter import ttk


def buttonTest():
    tkMessageBox.showinfo( "Hello Python", "Hello World")

class FullScreenApp(object):
    def close_window(self,event):
        self.master.destroy()
    def quit_application(self):
        self.master.destroy()
    def __init__(self, master, **kwargs):
        # Initialize window
        self.master=master
        pad=3
        # Set to full screen
        master.attributes("-fullscreen", True)
        # Add exit condition
        master.bind('<Escape>', self.close_window)
        # Create tabbed screen
        tabs = ttk.Notebook(master)
        tab1 = ttk.Frame(tabs)
        tabs.add(tab1, text='Home')
        tabs.pack(expand = 1, fill = 'both')
        # Create frame grid
        for row in range(3):
            for column in range(3):
                if column == 2 and row == 2:
                    tk.Button(tab1, text = 'Exit', command = self.quit_application).grid(row = row, column = column, sticky = 'nesw')
                else:
                    tk.Button(tab1, text = 'R%s/C%s'%(row, column), command = buttonTest).grid(row = row, column = column, sticky = 'nesw')
                tab1.grid_columnconfigure(column, weight = 1)
            tab1.grid_rowconfigure(row, weight = 1)

root=tk.Tk()
app=FullScreenApp(root)
root.mainloop()