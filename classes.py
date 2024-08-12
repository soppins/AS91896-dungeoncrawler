#Importing non-core libraries
import random

class player():
    #Player's starting stats and items. Name defined by 'name_player()' function
    def __init__(self):
        self.name = "Gertibald"
        self.hp = 100
        self.damage = 23
        self.ribs = 0
        self.score = 0
        self.inventory = ["itm_key", "itm_swrd"]
        
    #Adding hp to player
    def add_hp(self, amount):
        self.hp += amount
        #Defining a maximum health level
        if self.hp > 100:
            self.hp = 100
    
    #Removing hp from player
    def rem_hp(self, amount):
        self.hp -= amount
        #Defining a minimum health level
        if self.hp < 0:
            self.hp = 0
    
    #Resetting hp to full
    def reset_hp(self):
        self.hp = 100

    #Attacking enemy
    def attack(self, target):
        target.hp -= self.damage
        if target.hp < 0:
            target.hp = 0
        print("Your sword swings and sticks into the side of the skeleton. A raspy shriek escapes its skull as you rip the sword back out, taking a rib with it.")

class enemy():
    #Enemies' starting health will be determined by the spawn function
    def __init__(self):
        self.name = "Skeleton"
        self.hp = 0
        self.damage = 0
    
    #Resets and randomises the enemy's health on the spawn of a new instance
    def spawn(self):
        self.hp = random.randint(20, 80)
        self.damage = random.randint(5, 20)
    
    #Removing hp from enemy
    def rem_hp(self, amount):
        self.hp -= amount
        #Defining a minimum health level
        if self.hp < 0:
            self.hp = 0
            
    #Attacking player
    def attack(self, target):
        target.hp -= self.damage
        if target.hp < 0:
            target.hp = 0
        print("The skeleton swings at you with its rusty blade, leaving bleeding gashs across your body.")
        
        