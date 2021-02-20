import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        <create the rest of your GUI here>

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

""""
The important things to notice are:

I don't use a wildcard import. I import the package as "tk", which requires that I prefix all commands with tk.. This prevents global namespace pollution, plus it makes the code completely obvious when you are using Tkinter classes, ttk classes, or some of your own.

The main application is a class. This gives you a private namespace for all of your callbacks and private functions, and just generally makes it easier to organize your code. In a procedural style you have to code top-down, defining functions before using them, etc. With this method you don't since you don't actually create the main window until the very last step. I prefer inheriting from tk.Frame just because I typically start by creating a frame, but it is by no means necessary.

If your app has additional toplevel windows, I recommend making each of those a separate class, inheriting from tk.Toplevel. This gives you all of the same advantages mentioned above -- the windows are atomic, they have their own namespace, and the code is well organized. Plus, it makes it easy to put each into its own module once the code starts to get large.

Finally, you might want to consider using classes for every major portion of your interface. For example, if you're creating an app with a toolbar, a navigation pane, a statusbar, and a main area, you could make each one of those classes. This makes your main code quite small and easy to understand:

class Navbar(tk.Frame): ...
class Toolbar(tk.Frame): ...
class Statusbar(tk.Frame): ...
class Main(tk.Frame): ...

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.statusbar = Statusbar(self, ...)
        self.toolbar = Toolbar(self, ...)
        self.navbar = Navbar(self, ...)
        self.main = Main(self, ...)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)

"""