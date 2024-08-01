#Importing libraries
import time
import json
import player_class
import random
import events

#Opening json files for later use
with open("./json_files/item_data.json", "r") as read_file:
    itemdata = json.load(read_file)

with open("./json_files/room_data.json", "r") as read_file:
    roomdata = json.load(read_file)

#Attaching player class to object
plr = player_class.player()

#Attaching event functions to evt. prefix
evt = events

#SETTING CURRENT ROOM FOR TESTING:
current_room = "library_room"



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
    #ADD COLOUR!!!!!!!!!!!!!!!!!!!!!!!!!!!! AND ACTUAL CODE to make it related ro player health
    print("[IIIIIIII______]")
    print(f"{plr.hp}/100")


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

#Checks if a specified item is already in the player's inventory
def item_in_inventory(item):
    return True if item in plr.inventory else False

#Lowering an item's number of uses with use of the item (no need to check whether an item has uses remaining or not, as the user won't be able to see items with 0 uses in inventory)
def item_used(item):
    itemdata[item]["uses"]["summary"] -= 1
        
    
#Displaying items in player inventory
def inventory_list():
    #First number of the list of items
    number = 1
    #Iterating over items present
    for item in plr.inventory:
        #Defining official name and number of uses of current item
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

#Deciding whether to spawn enemy
def enter_fight():
    if random.randint(0, 100) <= roomdata[current_room]["fight_prob"]:
        spawn_enemy()
        fight_state()
    else:
        pass
        
#Spawn enemy
def spawn_enemy():
    print("enemy")


#ROOM FUNCTIONS
#Printing map with the player displayed in the room they're currently in
def map_position():
    s = """PLACEHOLDER MAP-THIS WAS A TEST OF MAKING AN ASCII ART MAP, BUT DOES NOT REPRESENT THE FINAL LAYOUT OF THE DUNGEON
────────┐                                                                             
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
    map_num = roomdata[current_room]["map_number"]
    sub = "."
    repl = "@"
    
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != map_num:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to the room_num we found the match so replace
    if i == map_num:
        return s[:find] + repl + s[find+len(sub):]
    return s

#Unlocking current room exit door
def unlock_exit():
    roomdata[current_room]["locked"] = False


#INVESTIGATION FUNCTIONS
# 
def invst_selection(room, investigating):
    if investigating in roomdata[room]["investigation"]["answers"]:
        return roomdata[room]["investigation"]["function"]
    else:
        return None

#Function will run a specific investigation on an item if the player is in the right room
def invst_input():
    investigating = input("What do you investigate?\n[Enter 'books' or 'bookshelf' to initiate test, enter 'done' to stop investigating.]\n").lower()
    
    if investigating == "done":
        return
    
    #If the player's focus is one of the correct inputs for the room they're currently in,
    focus = invst_selection(current_room, investigating)
    #then run the function for that focus.
    if focus != None:
        evt.invst_event(focus)   
    else:
        print("You find nothing.")
        invst_input()


#SCORING FUNCTIONS
#

