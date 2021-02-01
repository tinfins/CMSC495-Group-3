#pylint:disable=W0108
import tkinter as tk
import MessageBox

class Menu_Bar_Gui(tk.Frame):
    """
    Creates application menus
    """ 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Menubar setup
        menubar = tk.Menu(self.parent)
        filemenu = tk.Menu(menubar, tearoff=0)
        editmenu = tk.Menu(menubar, tearoff=0)
        controller.config(menu = menubar)
        self.grid(row=0,column=0)

        # Filemenu entries
        filemenu.add_command(label = "Open", command = None)
        filemenu.add_command(label = "Save", command = None)
        filemenu.add_command(label = "Save As", command = None)
        filemenu.add_command(label = "Close", command = lambda: controller.destroy())

        filemenu.add_separator()

        filemenu.add_command(label = "Exit", command = lambda: controller.destroy())
        menubar.add_cascade(label = 'File', menu = filemenu)

        # Editmenu entries
        editmenu.add_command(label = "Settings", command = lambda: MessageBox.MessageBox().settingsBox())
        menubar.add_cascade(label = 'Edit', menu = editmenu)
