#Importing libraries
import time
import json
import player_class
import random

current_room = "vines_room"


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

#Displaying player healthbar
def player_healthbar():
    #ADD COLOUR!!!!!!!!!!!!!!!!!!!!!!!!!!!! AND ACTUAL CODE
    print("[IIIIIIII______]")


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
def inventory_list():
    #First number of the list of items
    number = 1
    #Iterating over items present
    for item in plr.inventory:
        #
        name = itemdata[item]["name"]
        uses = itemdata[item]["uses"]
        #Don't print the item if it has no uses left
        if uses == 0:
            pass
        #Print the item with uses if it has uses
        elif uses != "None":
            print("{}> {} ({})".format(number, name, uses))
            number += 1
        #If no uses, just print the item name
        else:
            print("{}> {}".format(number, name))
            number += 1


#FIGHTING FUNCTIONS
#Enter fighting 
def fight_state():
    print("fight state")

#Rollin' the fightin' dice
def enter_fight():
    if random.randint(0, 100) <= roomdata[current_room]["fightprob"]:
        spawn_enemy()
        fight_state()
        
#Spawn enemy
def spawn_enemy():
    print("enemy")


#ROOM FUNCTIONS
#Printing map with the player displayed in the room they're currently in
def map_position(room_num):
    s = """────────┐                                                                             
        └┐                                                                            
──────┐  └┐                                                                           
      └┐  └┐                                                                          
       └┐  └┐                                ┌──────┐                                 
        └┐  └┐                             ┌╥┘ ╤══╤ └┐    ┌──┐                        
         └┐  └──╥─────╥─────╥──────────────┘║ ╚╪═╦╪╝ │    │░•│                        
          └┐ .  ╢  .  ╢  .  ╢       .       ╢ ┌┴──┴┐ │  ┌─┘░ └─┐                      
           └────╨─────╨─────╨───────────────╨─┴────┴─┘  │░░  •░│                      
             │┼│                            ┌────────┐  │░•  ░░│                      
             │┼│ ┌▼▼▼▼┐ ┌──────┐ ┌──┐ ┌──┐ ┌┘ ~     ~└┐ │░  • ░│                      
             │┼└╥┘░  ░└╥┘░     └╥┘  └╥┘  └╥┘  ~     ~ └─┘     ░│                      
             │┼ ╢ ░ .  ╢   .  ░░╢ .  ╢  . ╢   ~     ~      ┬┬  │                      
             └┴─╨──────╨─┐▲▲▲▲┌──────────────────────────╥─┴┴─╥┘                      
                                             ┌──────┐                                 
                                           ┌─┘~     └─┐                               
                                          ┌┘~ ~     ~ └┐                              
                                          │ ~ ~     ~  │                              
                                          │~~~~~~~~~~~~│                              
                                          └────────────┘                              """
    sub = "."
    repl = "@"
    
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != room_num:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to the room_num we found the match so replace
    if i == room_num:
        return s[:find] + repl + s[find+len(sub):]
    return s



#INVESTIGATION FUNCTIONS
#Investigation state
def invst_state():
    print("investigate")


#SCORING FUNCTIONS
#

