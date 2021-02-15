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
    '''
    Create message boxes in new window
    '''
    def __init__(self):
        super().__init__()
        self.mbox = tk.messagebox

    def onError(self, message):
        '''
        Error messages
        '''
        self.mbox.showerror("Error", message)

    def onWarn(self, message):
        '''
        Warning messages
        '''
        self.mbox.showwarning("Warning", message)

    def onInfo(self, message):
        '''
        Info messages
        '''
        self.mbox.showinfo("Information", message)


def main():
    root = tk.Tk()
    mbox = MessageBox()
    root.geometry('300x200+300+300')
    root.mainloop()