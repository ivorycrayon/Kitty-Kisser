import tkinter as tk
import time

class Application(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_widgets()
    self.update_kisses()

  def create_widgets(self):
    self.total_kisses = 0
    self.kisses_per_second = 0

    self.total_lips = 0
    self.lips_base_cost = 15
    self.lips_cost = self.lips_base_cost


    self.kiss = tk.Button(self)
    self.kiss["text"] = "Kiss The Kitty"
    self.kiss["command"] = self.kiss_click
    self.kiss.pack()

    self.lips = tk.Button(self)
    self.lips["text"] = "Lips" + str(self.total_lips)
    self.lips["command"] = self.lips_click
    self.lips.pack(side = "right")

    self.kisses = tk.Label(self)
    self.kisses["text"] = "Kisses: " + str(self.total_kisses)
    self.kisses.pack(side = "top")

    self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
    self.quit.pack(side = "bottom")


  def kiss_click(self):    
		self.total_kisses += 1
    self.kisses.configure(text = "Kisses: " + str(self.total_kisses))

    print("You gave the kitty a kiss!")
    print("The kitty has been kissed:", self.total_kisses,"times")

  def lips_click(self):
    if self.total_kisses >= self.lips_cost:
      self.total_kisses -= self.lips_cost
      self.total_lips += 1
      self.kisses.configure(text = "Kisses: " + str(self.total_kisses))
      self.lips.configure(text = "Lips: " + str(self.total_lips))
    else: 
      print("You don't have enough kisses to buy lips!")

    print("The kitty has been kissed:", self.total_kisses,"times")

  def update_kisses(self):
    self.kisses_per_second = self.total_lips * 1
    self.total_kisses += self.kisses_per_second
    print("total kisses is: ", self.total_kisses)
    print("kps: ", self.kisses_per_second)
    self.kisses.configure(text = "Kisses: " + str(self.total_kisses))
    self.after(1000, self.update_kisses)



root = tk.Tk()
app = Application(master=root)


app.mainloop()