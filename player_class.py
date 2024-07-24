class player():
    #Player's starting stats and items
    def __init__(self):
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
        
plr = player()

plr.hp = 120

plr.add_hp(10)

print(plr.hp)