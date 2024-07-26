#Importing libraries
import time
import json
import player_class
import random


#Opening json files for later use
with open("./json_files/item_data.json", "r") as read_file:
    itemdata = json.load(read_file)

with open("./json_files/room_data.json", "r") as read_file:
    roomdata = json.load(read_file)

#Attaching player class to object
plr = player_class.player()

#PLAYER
#Creating player object with a name
def create_player():
    name = input("What will you name your character? \n")
    confirm = input(f"You have chosen the name {name}. Proceed? (y/n) \n").lower()
    if confirm == "y":
        plr.name = name
    else:
        create_player()

#ITEM FUNCTIONS
#Adding item to inventory
def item_add(item):
    plr.inventory.append(item)
    print("'" + itemdata[item]["name"] + "' added to inventory.")
    print("(Description: " + itemdata[item]["description"]["summary"] + ")")

#Removing item from inventory
def item_rmv(item):
    plr.inventory.remove(item)
    print("'" + itemdata[item]["name"] + "' lost with use.")

#Lowering an item's number of uses with use of the item
def item_used(item):
    itemdata[item]["uses"]["summary"]
    
#Displaying items in player inventory


#FIGHTING FUNCTIONS
#


#ROOM FUNCTIONS
#


#INVESTIGATION FUNCTIONS
#


#SCORING FUNCTIONS
#


item_add("itm_wtr")
print(plr.inventory)
create_player()
print(plr.name)
item_rmv("itm_key")