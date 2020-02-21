
#!/usr/bin/python

import tkinter as tk
from tkinter import *

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        # Initialize window
        self.master=master
        pad=3
        # Set to fullscreen
        master.attributes("-fullscreen", True)
        #master.geometry("{0}x{1}+0+0".format(
        #    master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        # Add exit condition
        master.bind('<Escape>',self.close_window)
        # Create frame grid
        for row in range(3):
            for column in range(3):
                tk.Label(master, text='R%s/C%s'%(row, column), borderwidth = 1).grid(row = row, column = column)

    def close_window(self,event):
        self.master.destroy()

root=tk.Tk()
app=FullScreenApp(root)
root.mainloop()