class player():
    #Player's starting stats and items. Name defined by 'name_player()' function
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = ["itm_key", "itm_sword"]
        
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

    #Attacking
    def attack(self, target):

class enemy():
    #Enemies' starting health will be determined by the 'spawn_enemy()' function
    def __init__(self, health):
        self.hp = health
    
    #Removing hp from enemy
    def rem_hp(self, amount):
        self.hp -= amount
        #Defining a minimum health level
        if self.hp < 0:
            self.hp = 0