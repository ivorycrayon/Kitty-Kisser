import tkinter as tk
import time

class Application(tk.Frame):

  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_widgets()

  def create_widgets(self):
    self.totalkisses = 0
    self.kissesPerSecond = 1

    self.labeltext = tk.StringVar()

    self.kiss = tk.Button(self)
    self.kiss["text"] = "Kiss The Kitty"
    self.kiss["command"] = self.kissClick
    self.kiss.pack()

    self.lips = tk.Button(self)
    self.lips["text"] = "Lips"
    self.lips["command"] = self.lipsClick
    self.lips.pack(side = "right")

    self.kisses = tk.Label(self)
    self.kisses["text"] = "Kisses: " + str(self.totalkisses)
    self.kisses.pack(side = "top")

    self.quit = tk.Button(self, text="QUIT", fg="red",
                          command=self.master.destroy)
    self.quit.pack(side = "bottom")


  def kissClick(self):    
    self.totalkisses += 1
    self.kisses.config(text = "Kisses: " + str(self.totalkisses))

    print("You gave the kitty a kiss!")
    print("The kitty has been kissed:", self.totalkisses,"times")

  def lipsClick(self):
    self.totalkisses -= 1
    self.kissesPerSecond += 1
    self.kisses.config(text = "Kisses: " + str(self.totalkisses))

    print("The kitty has been kissed:", self.totalkisses,"times")

    self.updateKisses()

  def updateKisses(self):
    now = time()
    self.totalkisses += self.kissesPerSecond
    self.kisses.config(text = "Kisses: " + str(self.totalkisses))
    self.after(10000, self.updateKisses())



root = tk.Tk()
app = Application(master=root)

app.updateKisses()
app.mainloop()