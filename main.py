import tkinter as tk
import time

class Application(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.grid(sticky=tk.N+tk.E+tk.S+tk.W)
    self.create_widgets()
    self.update_kisses()

  #fix grid layout... or maybe switch to frames
  def create_widgets(self):
    self.total_kisses = 0.0
    self.total_kisses_per_second = 0.0

    self.kisses = tk.Label(self)
    self.kisses["text"] = "Kisses: " + str(self.total_kisses)
    self.kisses.grid(row = 1, column = 1)

    self.kisses_per_second = tk.Label(self)
    self.kisses_per_second["text"] = "Kisses per Second: " + str(self.total_kisses_per_second)
    self.kisses_per_second.grid(row = 2, column = 1)

    self.kiss = tk.Button(self)
    self.kiss["text"] = "Kiss The Kitty"
    self.kiss["command"] = self.kiss_click
    self.kiss.grid(row = 3, column = 1)

    self.total_lips = 150
    self.lips_base_cost = 15
    self.lips_cost = self.lips_base_cost
    self.lips_cps = 0.1

    self.total_lips_upgrades = 0
    self.upgrade_lips_base_cost = 10 * self.lips_base_cost
    self.upgrade_lips_cost = self.upgrade_lips_base_cost
    

    self.lips = tk.Button(self)
    self.lips["text"] = "Lips: " + str(self.total_lips) + "\nCost: " + str(self.lips_cost)
    self.lips["command"] = self.lips_click
    self.lips.grid(column = 2, rowspan = 3, sticky = tk.N+tk.S)

    self.upgrade_lips = tk.Button(self)
    self.upgrade_lips["text"] = "Upgrade Lips\nCost: " + str(self.upgrade_lips_cost)
    self.upgrade_lips["command"] = self.upgrade_lips_click
    self.upgrade_lips.grid(column = 3, rowspan = 3)

    #self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
    #self.quit.grid(column = 2, sticky = tk.S)

  def kiss_click(self):    
    self.total_kisses += 1
    self.kisses.configure(text = "Kisses: " + str(self.total_kisses))

  def lips_click(self):
    if self.total_kisses >= self.lips_cost:
      self.total_kisses -= self.lips_cost
      self.total_lips += 1
      self.lips_cost = round(self.lips_base_cost * (1.15 ** self.total_lips))
      self.total_kisses = round(self.total_kisses, 1)
      self.kisses.configure(text = "Kisses: " + str(self.total_kisses))
      self.lips.configure(text = "Lips: " + str(self.total_lips) + "\nCost: " + str(self.lips_cost))
    else: 
      print("You don't have enough kisses to buy lips!")

  #lips currently modeled after generic buildings... rework to actual cursor functionality
  def upgrade_lips_click(self):
    if self.total_kisses >= self.upgrade_lips_cost:
      self.total_kisses -= self.upgrade_lips_cost
      self.total_lips_upgrades += 1
      self.lips_cps *= 2
      self.upgrade_lips_cost = 5 * self.upgrade_lips_cost #WIP: follow x5, x10, x100...
      self.upgrade_lips.configure(text = "Upgrade Lips\nCost: " + str(self.upgrade_lips_cost))

  def update_kisses(self):
    self.total_kisses_per_second = round(self.total_lips * self.lips_cps, 1)
    self.total_kisses += self.total_kisses_per_second
    self.total_kisses = round(self.total_kisses, 1)
    self.kisses.configure(text = "Kisses: " + str(self.total_kisses))
    self.kisses_per_second.configure(text = "Kisses per Second: " + str(self.total_kisses_per_second))
    self.after(1000, self.update_kisses)

root = tk.Tk()
root.title("Kitty Kisser")

app = Application(master=root)
app.mainloop()