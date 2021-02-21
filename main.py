import tkinter as tk
import time

class Game(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack(fill=tk.BOTH, expand=True)
    self.create_widgets()
    self.update_kisses()

  #fix pack layout...
  #reorganize code
  #add on hover, flavor text, descriptions, stats
  #add unlock conditions MAYBE
  #add large number conversion 
  #convert buildings to class
  #add kps to buttons
  def create_widgets(self):
    self.frame1 = tk.Frame(root, bg="yellow")
    self.frame2 = tk.Frame(root, bg="blue")
    self.frame3 = tk.Frame(root, bg="red")
    self.frame1.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
    self.frame2.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
    self.frame3.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)

    self.total_kisses = 100000.0
    self.total_kisses_per_second = 0.0
    self.base_kisses_per_click = 1
    self.kisses_per_click = self.base_kisses_per_click

    self.kisses = tk.Label(self.frame1)
    self.kisses["text"] = "Kisses: " + str(self.total_kisses)
    self.kisses.pack(fill=tk.BOTH, expand=True)
    
    self.kisses_per_second = tk.Label(self.frame1)
    self.kisses_per_second["text"] = "Kisses per Second: " + str(self.total_kisses_per_second)
    self.kisses_per_second.pack(fill=tk.BOTH, expand=True)

    self.kiss = tk.Button(self.frame1)
    self.kiss["text"] = "Kiss The Kitty"
    self.kiss["command"] = self.kiss_click
    self.kiss.pack(fill=tk.BOTH, expand=True)

    self.total_lips = 0
    self.base_lips_kps = 0.1
    self.lips_kps = self.base_lips_kps
    self.lips_base_cost = 15
    self.lips_cost = self.lips_base_cost

    self.total_lips_upgrades = 0
    self.upgrade_lips_base_cost = 100
    self.upgrade_lips_cost = self.upgrade_lips_base_cost

    self.total_cat_ladies = 0
    self.cat_lady_kps = 1
    self.cat_lady_base_cost = 100
    self.cat_lady_cost = self.cat_lady_base_cost
    
    self.total_cat_lady_upgrades = 0
    self.upgrade_cat_lady_base_cost = 10 * self.cat_lady_base_cost
    self.upgrade_cat_lady_cost = self.upgrade_cat_lady_base_cost

    self.lips = tk.Button(self.frame2)
    self.lips["text"] = "Lips: " + str(self.total_lips) + "\nCost: " + str(self.lips_cost) + "\nkps: " + str(self.lips_kps)
    self.lips["command"] = self.lips_click
    self.lips.pack(fill=tk.BOTH, expand=True)

    self.upgrade_lips = tk.Button(self.frame3)
    self.upgrade_lips["text"] = "Upgrade Lips\nCost: " + str(self.upgrade_lips_cost)
    self.upgrade_lips["command"] = self.upgrade_lips_click
    self.upgrade_lips.pack(fill=tk.BOTH, expand=True)

    self.cat_lady = tk.Button(self.frame2)
    self.cat_lady["text"] = "Cat Ladies: " + str(self.total_cat_ladies) + "\nCost: " + str(self.cat_lady_cost)
    self.cat_lady["command"] = self.cat_lady_click
    self.cat_lady.pack(fill=tk.BOTH, expand=True)

    self.upgrade_cat_lady = tk.Button(self.frame3)
    self.upgrade_cat_lady["text"] = "Upgrade Cat Ladies\nCost: " + str(self.upgrade_cat_lady_cost)
    self.upgrade_cat_lady["command"] = self.upgrade_cat_lady_click
    self.upgrade_cat_lady.pack(fill=tk.BOTH, expand=True)

    #self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
    #self.quit.pack(fill=tk.BOTH, expand=True)

  def kiss_click(self):
    self.total_kisses += round(self.kisses_per_click, 1)
    self.total_kisses = round(self.total_kisses,1)
    self.kisses.configure(text = "Kisses: " + str(self.total_kisses))

  def lips_click(self):
    if self.total_kisses >= self.lips_cost:
      self.total_kisses -= self.lips_cost
      self.total_lips += 1
      self.lips_cost = round(self.lips_base_cost * (1.15 ** self.total_lips))
      self.total_kisses = round(self.total_kisses, 1)

      self.kisses.configure(text = "Kisses: " + str(self.total_kisses))
      self.lips.configure(text = "Lips: " + str(self.total_lips) + "\nCost: " + str(self.lips_cost) + "\nkps: " + str(self.lips_kps))

    else: 
      print("You don't have enough kisses to buy lips!")

  def cat_lady_click(self):
    if (self.total_kisses >= self.cat_lady_cost):
      self.total_kisses -= self.cat_lady_cost
      self.total_cat_ladies += 1

      #self.update_building_bonus()

      self.cat_lady_cost = round(self.cat_lady_base_cost * (1.15 ** self.total_cat_ladies))
      self.total_kisses = round(self.total_kisses, 1)

      self.kisses.configure(text = "Kisses: " + str(self.total_kisses))
      self.cat_lady.configure(text = "Cat Ladies: " + str(self.total_cat_ladies) + "\nCost: " + str(self.cat_lady_cost))

    else: 
      print("You don't have enough kisses to buy a cat lady!")

  #lips currently modeled after generic buildings... rework to actual cursor functionality
  #currently half working.... validate that upgrade is purchased and why isn't kps updating base on boost?
  def upgrade_lips_click(self):
    if (self.total_lips_upgrades < 3):
      if (self.total_kisses >= self.upgrade_lips_cost):
        self.total_kisses -= self.upgrade_lips_cost
        self.total_lips_upgrades += 1
        self.base_lips_kps *= 2

        if (self.base_kisses_per_click == 1):
          self.base_kisses_per_click += 1
        else:
          self.base_kisses_per_click *= 2
        
        if (self.total_lips_upgrades == 1):
          self.upgrade_lips_cost *= 5  
        elif (self.total_lips_upgrades == 2):
          self.upgrade_lips_cost *= 20
        elif (self.total_lips_upgrades == 3):
          self.upgrade_lips_cost *= 10

        self.upgrade_lips.configure(text = "Upgrade Lips\nCost: " + str(self.upgrade_lips_cost))
        self.lips.configure(text = "Lips: " + str(self.total_lips) + "\nCost: " + str(self.lips_cost) + "\nkps: " + str(self.lips_kps))
      
      else: 
        print("You don't have enough kisses to upgrade your lips!")

    #maybe destroy and pack a new upgrade
    elif (self.total_lips_upgrades >= 3):
      if (self.total_kisses >= self.upgrade_lips_cost):
        self.total_kisses -= self.upgrade_lips_cost
        self.total_lips_upgrades += 1

        #self.lips_kps += (.1 * self.total_buildings)
        #self.kisses_per_click += (.1 * self.total_bulidings)        

        self.upgrade_lips.configure(text = "Upgrade Lips\nCost: " + str(self.upgrade_lips_cost))

      else: 
        print("You don't have enough kisses to upgrade your lips!")


  def upgrade_cat_lady_click(self):
    if (self.total_kisses >= self.upgrade_cat_lady_cost):
      self.total_kisses -= self.upgrade_cat_lady_cost
      self.total_cat_lady_upgrades += 1
      self.cat_lady_kps *= 2

      if (self.total_cat_lady_upgrades == 1):
        self.upgrade_cat_lady_cost *= 5
      elif (self.total_cat_lady_upgrades == 2):
        self.upgrade_cat_lady_cost *= 10
      else:
        self.upgrade_cat_lady_cost *= 100

      self.upgrade_cat_lady.configure(text = "Upgrade Cat Ladies\nCost: " + str(self.upgrade_cat_lady_cost))

    else:
      print("You don't have enough kisses to upgrade your cat ladies!")

  def update_building_bonus(self):
    self.total_buildings = self.total_cat_ladies #any non lips buildings
    self.building_bonus = round((.1 * self.total_buildings),1)

    print("total non lips buildings is ", self.total_buildings)
    print("building bonus is ", self.building_bonus)

    self.lips_kps = round(self.building_bonus + self.base_lips_kps, 1)
    self.kisses_per_click = round(self.building_bonus + self.base_kisses_per_click, 1)

    print("lips kps is", self.lips_kps)
    print("click kps is ", self.kisses_per_click)

    #self.kisses_per_second.configure(text = "Kisses per Second: " + str(self.total_kisses_per_second))

  def update_kisses(self):
    self.total_kisses_per_second = round((self.total_lips * self.lips_kps) + (self.total_cat_ladies * self.cat_lady_kps), 2)
    self.total_kisses += round(.1 * self.total_kisses_per_second, 2)
    self.total_kisses = round(self.total_kisses, 2)

    self.update_building_bonus()

    self.lips.configure(text = "Lips: " + str(self.total_lips) + "\nCost: " + str(self.lips_cost) + "\nkps: " + str(self.lips_kps))
    self.kisses.configure(text = "Kisses: " + str(self.total_kisses))
    self.kisses_per_second.configure(text = "Kisses per Second: " + str(self.total_kisses_per_second))
    
    self.after(100, self.update_kisses)

root = tk.Tk()
root.title("Kitty Kisser")

game = Game(master=root)
game.mainloop()