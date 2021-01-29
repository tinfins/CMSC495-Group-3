import tkinter as tk
from ttkthemes import ThemedStyle
import MenuBarGui
import LoginGui
import testPage


class MainApplication(tk.Tk):
    """
    Main entry point for GUI portion of application
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Container to stack frames
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Style application theme
        # Install ttkthemes (pip install ttkthemes)
        style = ThemedStyle(self.container)
        style.set_theme("breeze")

        # Create frames
        self.frames = {}
        # Each view/page should be added as a frame in the style shown below
        self.frames["Login"] = LoginGui.Login_Gui(parent=self.container, controller=self)
        self.frames["Test Page"] = testPage.Test_Page(parent=self.container, controller=self)
        
        # Set frames in container
        # Each frame must have a layout in the style below
        self.frames["Login"].grid(row=1, column=0, sticky="nsew")
        self.frames["Test Page"].grid(row=1, column=0, sticky="nsew")
        
        self.show_frame("Login")

        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        # Shows menu on all views but the login view
        if page_name != "Login":
            MenuBarGui.Menu_Bar_Gui(parent=self.container, controller=self)
        self.title(page_name)
        frame.tkraise()
    

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
    