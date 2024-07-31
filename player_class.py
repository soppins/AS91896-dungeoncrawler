class player():
    #Player's starting stats and items. Name defined by 'name_player()' function
    def __init__(self):
        self.name = "Gertibald"
        self.hp = 100
        self.damage = 23
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

class enemy():
    #Enemies' starting health will be determined by the 'spawn_enemy()' function
    def __init__(self, health):
        self.hp = health
        self.damage = 17
    
    #Removing hp from enemy
    def rem_hp(self, amount):
        self.hp -= amount
        #Defining a minimum health level
        if self.hp < 0:
            self.hp = 0
            
    #Attacking player
    def attack(self, target):
        target.hp -= self.damage