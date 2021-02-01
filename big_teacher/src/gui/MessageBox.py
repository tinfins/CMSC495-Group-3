###############################################
# Purpose: Creates message box dialogs        #
#                                             #
# Licensed under the MIT license. See LICENSE #
# file in project root for details.           #
#                                             #
# https://github.com/tinfins/CMSC495-Group-3/ #
###############################################

import tkinter as tk
from tkinter import ttk, messagebox

class MessageBox(tk.Frame):
    def __init__(self):
        super().__init__()
        self.mbox = tk.messagebox

    def onError(self, message):
        self.mbox.showerror("Error", message)

    def onWarn(self, message):
        self.mbox.showwarning("Warning", message)

    def onInfo(self, message):
        self.mbox.showinfo("Information", message)

    def settingsBox(self):
        ttk.Label(self, text='Settings', font=(None, 12)).grid(row=0)
        ttk.Label(self, text='Host:').grid(row=1)
        ttk.Label(self, text='Port:').grid(row=2)
        ttk.Label(self, text='DB Name:').grid(row=3)

        hostVar = tk.StringVar()
        hostEntry = ttk.Entry(self, textvariable=hostVar).grid(row=1, column=1)
        portVar = tk.StringVar()
        portEntry = ttk.Entry(self, textvariable=portVar).grid(row=2, column=1)
        db_nameVar = tk.StringVar()
        db_nameEntry = ttk.Entry(self, textvariable=db_nameVar).grid(row=3, column=1)

        saveButton = ttk.Button(self, text="Save", command=None, width=10).grid(row=4)
        cancelButton = ttk.Button(self, text="Cancel", command=None, width=10).grid(row=4, column=1)

def main():
    root = tk.Tk()
    mbox = MessageBox()
    root.geometry('300x200+300+300')
    root.mainloop()