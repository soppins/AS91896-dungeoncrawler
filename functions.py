#Importing non-core libraries
import time
import json
import classes
import random
import os

#Opening json files for later use
with open("./json_files/item_data.json", "r") as read_file:
    itemdata = json.load(read_file)

with open("./json_files/room_data.json", "r") as read_file:
    roomdata = json.load(read_file)

#Attaching classes to objects
plr = classes.player()
enmy = classes.enemy()

#SETTING CURRENT ROOM FOR TESTING:
current_room = "vine_room"



#PROGRAM FUNCTIONS
#Opening text
def open_text():
    clear_terminal()
    print("You are a thief.\nYou must utilise your skills in investigation and combat to obtain the golden Fish Idol hidden deep within...")
    time.sleep(4)

#Main menu
def main_menu():
    print("""

░       ░░░░      ░░░  ░░░░░░░░  ░░░░  ░░░      ░░░        ░░        ░░       ░░
▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒  ▒  ▒▒  ▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒
▓       ▓▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓▓▓▓▓        ▓▓  ▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓▓      ▓▓▓▓       ▓▓
█  ████  ██        ██  ████████   ██   ██        █████  █████  ████████  ███  ██
█       ███  ████  ██        ██  ████  ██  ████  █████  █████        ██  ████  █
\n>start\n>config\n>close\n\n[Enter an option from this list]\n """)
    choice = input("").lower()
    if choice == "start":
        game_start()
    elif choice == "config":
        print("no settings :-)\n")
        time.sleep(.5)
        clear_terminal()
        main_menu()
    elif choice == "close":
        print("Are you sure you want to close the program?")
        confirm = yes_no()
        if confirm == True:
            game_end()
        else:
            main_menu()
    else:
        print("Invalid input.")
        time.sleep(.5)
        clear_terminal()
        main_menu()


    print("The air around you grows colder and damper as you descend the stone spiral staircase into Balwater...")
    time.sleep(.5)
    print("Finally, the staircase ends and you are facing an old wooden door that seems to be rotting on its hinges.\nYou push the door open.") 


#Starts the game (accessible on death or when investigating a room.)
def game_start():
    clear_terminal()
    plr.name
    plr.name = naming_player()
    room_movement("vine_room")

#Closes the game (accessible on death or when investigating a room.)
def game_end():
    clear_terminal()
    print("bye")
    
#Presents a y/n option that can be recalled if the user inputs the wrong thing
def yes_no():
    choice = input("\n[y/n]\n").lower()
    if choice == "y":
        return True
    elif choice == "n":
        return False
    else:
        yes_no()

#PLAYER
#Naming player object
def naming_player():
    username = input("What will you name your character? \n")
    print(f"You have chosen the name {username}. Proceed?")
    choice = yes_no()
    if choice == True:
        print(username)
    elif choice == False:
        naming_player()
    else:
        choice = yes_no()

#Displaying healthbar of chosen character
def healthbar(object):
    print(f"\n{object.name} HP: {object.hp}/100\n")
    
#Death
def player_death():
    clear_terminal()
    print("you died")
    restart = input("restart? (y/n)").lower()
    if restart == "y":
        main_menu()
    else:
        game_end()


#TERMINAL FUNCTIONS
#Clears all previous text in the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#Awaits any input from the user to continue (used to print clumps of story one at a time)
def continue_confirm() -> None:
    input("\n[Press Enter to continue]\n")


#ITEM FUNCTIONS
#Adding item to inventory
def item_add(item):
    plr.inventory.append(item)
    if type(itemdata[item]["uses"]) in itemdata[item]:
        itemdata[item]["uses"] += 1
    print("'" + itemdata[item]["name"] + "' added to inventory.")
    print("(Description: " + itemdata[item]["description"]["summary"] + ")")

#Removing item from inventory
def item_rmv(item):
    if type(itemdata[item]["uses"]) in itemdata[item]:
        itemdata[item]["uses"] -= 1
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
            print("> {}".format(name))
            
#Inventory system
def inventory():
    inventory_list()
    item_choice = input("What would you like to inspect?")
    print(itemdata[item_choice]["description"]["detailed"])
    print("Would you like to use this item?")
    usechoice = yes_no()
    if usechoice == True:
        print(itemdata[item_choice]["use_text"])

#When player uses an item, this function decides what occurs based on the current_room's data and the item's data.
#Each room can only have one successful item, so this is effectively determining the event by the room the player is in.
def item_event(item):
    global current_room
    if item in roomdata[current_room]["items"]["use"]:
        if item == "itm_trch":
            unlock_exit()
            print(itemdata[item]["use_text"])
    else:
        print("Unable to use item.")
    


#FIGHTING FUNCTIONS
#Enter fighting 
def fight_state():
    fighting = True
    
    spawn_enemy()
    
    
    #Player remains in fighting state until either enemy or player dies
    while fighting == True:
        clear_terminal()
        healthbar(enmy)
        healthbar(plr)
        
        enmy.attack(plr)
        healthbar(enmy)
        healthbar(plr)
        continue_confirm()
        
        input("type 'hit' to hit\n")
        plr.attack(enmy)
        healthbar(enmy)
        healthbar(plr)
        continue_confirm()
        
        if plr.hp == 0:
            print("Your wounds become too much for you to handle. You fall to the ground in pain and fatigue, never to rise again.")
            player_death()
            break
        if enmy.hp == 0:
            fighting == False
            print("The skeleton collapses.\nIts bones and sword clatter to the ground in a cacophany which is quickly stifled by the quiet stone walls.")
            add_score(500)
            break    

#Deciding whether to spawn enemy
def check_fight():
    global current_room
    if random.randint(0, 100) <= roomdata[current_room]["fight_prob"]:
        fight_state()
    else:
        pass
        
#Spawn enemy
def spawn_enemy():
    enmy.spawn()
    print("Suddenly, a section of the floor cracks.\nFlagstones are upturned as a hand bursts out of the ground.\nFrom earth rises a bony figure that pulls a corroded sword with it.\nClumps of clay and stone fall away from the skeleton's bones as it steadies itself on its feet and points the sword directly at you.")
    continue_confirm()
    print("You unsheathe your own blade.")


#ROOM FUNCTIONS
#The function that allows the player to move between rooms
def room_movement(room):
    global current_room
    
    #Allowing this function to modify the current_room variable for other functions
    current_room = room
    while current_room != "end_room":
        clear_terminal()
        print(map_position())
        time.sleep(1)
        describe_room()
        continue_confirm()
        check_fight()
        invst_input()
        print("Exit room?")
        print("[exit: {}]".format(roomdata[current_room]["exit"]["1"]))
        choice = yes_no()
        if choice == True:
            room_movement(roomdata[current_room]["exit"]["1"])

#Prints current_room's entry text. Allows the player to view the room description again if they forgot what was mentioned
def describe_room():
    print(roomdata[current_room]["description"]["entry"])

#Printing map with the player displayed in the room they're currently in
def map_position():
    s = """PLACEHOLDER MAP-THIS IS A TEST OF MAKING AN ASCII ART MAP, AND DOES NOT REPRESENT THE FINAL LAYOUT OF THE DUNGEON
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
                                          └────────────┘\n"""
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


#SCORING FUNCTIONS
#Adds to the player's score depending on what the player is getting score from
def add_score(amount = int):
    plr.score += amount
    print(f"{amount} andded to score.\nCurrent score: {plr.score}")


#INVESTIGATION FUNCTIONS
#Selects the event to be run by the invst_event function
def invst_selection(room, investigating):
    if investigating in roomdata[room]["investigation"]["answers"]:
        return roomdata[room]["investigation"]["function"]
    else:
        return None

#Function will run a specific investigation on an item if the player is in the right room
def invst_input():
    global current_room
    investigating = input("What do you investigate?\n[Enter an object to focus on, or type 'done' stop investigating.]\n").lower()
    
    if investigating == "done":
        return
    
    #If the player's focus is one of the correct inputs for the room they're currently in,
    focus = invst_selection(current_room, investigating)
    #then run the function for that focus.
    if focus != None:
        if invst_event(focus) == "run":
            invst_input()
        else:
            pass
            
    else:
        print("You find nothing.")
        invst_input()
        
#When player successfully investigates something, this function decides what occurs based on the focus that was successful.
#Each room can only have one successful focus, so this is effectively determining the event by the room the player is in.
def invst_event(focus):
    global current_room
    
    #Vine room event:
    if focus == "torch":
        if item_in_inventory("itm_trch") == False:
            item_add("itm_trch")
        else:
            print("Nothing of interest.")
        
    #Library event:
    if focus == "bookshelf":
        #If player hasn't done anything:
        if item_in_inventory("itm_r_bk") == False:
            while True:
                try:
                    book_choice = int(input("Out of the numerous books resting in this bookshelf, two stand out to you.\nDo you remove book 1 or 2? "))
                    break
                except ValueError:
                    print("Invalid input.")
                
            if book_choice == 1:
                print("You pull the first book out of the shelf. You blow the dust off the cover.")
                item_add("itm_r_bk")
                return "run"
                
                
            if book_choice == 2:
                unlock_exit()
                print("As you pull the book out, your hear a mechanism grinding away behind it.\nThe book stops moving about halfway off the bookshelf, and a metallic 'thunk' resonates throughout the quiet aisles.\nThe exit is now unlocked.")
                return "run"
            else:
                return "run"
        #If player has already unlocked the door:
        elif roomdata[current_room]["locked"] == False and item_in_inventory("itm_r_bk") == False:
            book_choice = input("One book on the bookshelf stands out to you.\nDo you remove it? (y/n) ").lower()
            
            if book_choice == "y":
                print("You pull the first book out of the shelf. You blow the dust off the cover.")
                item_add("itm_r_bk")
                return "run"
            else:
                return "run"
        #If player already has the riddle book:
        elif item_in_inventory("itm_r_bk") == True and roomdata[current_room]["locked"] == True:
            book_choice = input("One book on the bookshelf stands out to you.\nDo you remove it? (y/n) ").lower()
            
            if book_choice == "y":
                unlock_exit()
                print("As you pull the book out, your hear a mechanism grinding away behind it.\nThe book stops moving about halfway off the bookshelf, and a metallic 'thunk' resonates throughout the quiet aisles.\nThe exit is now unlocked.")
                return "run"
            else:
                return "run"
        else:
            print("No other books on the bookshelf seem important.")
                
    if focus == "well":
        print("unfinished")
