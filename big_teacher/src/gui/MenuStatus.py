import tkinter as tk
from tkinter import ttk
# Big Teacher module imports
import big_teacher.src.controller.MainPageController as MainPageController
import big_teacher.src.gui.SettingsGui as SettingsGui
import big_teacher.src.gui.TopLevelWindow as TopLevelWindow


class MenuBarGui(tk.Frame):
    '''
    Creates application menus
    '''
    def __init__(self, master, controller):
        '''
        Initialize menu bar for all pages
        '''
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller

        # Menubar setup
        menubar = tk.Menu(self.master)
        file_menu = tk.Menu(menubar, tearoff=0)
        edit_menu = tk.Menu(menubar, tearoff=0)
        controller.config(menu=menubar)
        self.grid(row=0, column=0)

        # Filemenu entries
        file_menu.add_command(label="Log Out", command=lambda: None)
        file_menu.add_command(label="", command=None)
        file_menu.add_command(label="Close", command=lambda: controller.destroy())

        file_menu.add_separator()

        file_menu.add_command(label="Exit", command=lambda: controller.destroy())
        menubar.add_cascade(label='File', menu=file_menu)

        # Edit_menu entries
        edit_menu.add_command(label="Settings", command=lambda: TopLevelWindow.SwitchWindow(master=self.master).new_window(SettingsGui.SettingsGui))
        menubar.add_cascade(label='Edit', menu=edit_menu)


class StatusBar(tk.Frame):
    '''
    Creates application status bar
    '''
    def __init__(self, master):
        '''
        Initialize status bar for all pages
        '''
        tk.Frame.__init__(self, master)
        self.master = master

        self.status_var = tk.StringVar()
        self.label = ttk.Label(self.master, relief=tk.SUNKEN, anchor=tk.W, textvariable=self.status_var)
        self.status_var.set('')
        self.master.grid_columnconfigure(0, weight=1)
        self.label.pack(fill=tk.X)
        self.pack(side=tk.BOTTOM, fill=tk.X)

    def status_set(self, msg):
        '''
        Sets status message in status bar label
        :params msg:String:message to display
        '''
        self.status_var.set(f' {msg}')

    def status_clear(self):
        '''
        Clears status bar label
        '''
        self.status_var.set('')
