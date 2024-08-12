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
current_room = "library_room"


#PROGRAM FUNCTIONS
#Main menu
def main_menu():
    clear_terminal()
    print("""WELCOME TO DUNJING!\n>start\n>config\n>close""")
    choice = input("")
    if choice == "start":
        game_start()
    elif choice == "config":
        print("no settings :-)\n")
        main_menu()
    elif choice == "close":
        confirm = input("Are you sure you want to close the program? (y/n)\n")
        if confirm == "y":
            game_end()
        else:
            main_menu()
    else:
        main_menu()
        

#Starts the game (accessible on death or when investigating a room.)
def game_start():
    print("hi")

#Closes the game (accessible on death or when investigating a room.)
def game_end():
    print("bye")
    


#PLAYER
#Naming player object
def naming_player():
    username = input("What will you name your character? \n")
    confirm = input(f"You have chosen the name {username}. Proceed? (y/n) \n").lower()
    if confirm == "y":
        return username
        
    else:
        naming_player()

#Displaying healthbar of chosen character
def healthbar(object):
    print(f"{object.name} HP: {object.hp}/100")
    
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


#FIGHTING FUNCTIONS
#Enter fighting 
def fight_state():
    fighting = True
    
    spawn_enemy()
    healthbar(enmy)
    healthbar(plr)
    
    #Player remains in fighting state until either enemy or player dies
    while fighting == True:
        clear_terminal()
        input("type 'hit' to hit\n")
        plr.attack(enmy)
        continue_confirm()
        print(enmy.hp)
        print(plr.hp)
        enmy.attack(plr)
        print(enmy.hp)
        print(plr.hp)
        continue_confirm()
        
        if plr.hp == 0:
            print("Your wounds become too much for you to handle. You fall to the ground in pain and fatigue, never to rise again.")
            player_death()
            break
        if enmy.hp == 0:
            print("The skeleton collapses.\nIts bones and sword clatter to the ground in a cacophany which is quickly stifled by the quiet stone walls.")
            print("[add to score]")
            break
        break    

#Deciding whether to spawn enemy
def check_fight():
    if random.randint(0, 100) <= roomdata[current_room]["fight_prob"]:
        fight_state()
    else:
        pass
        
#Spawn enemy
def spawn_enemy():
    enmy.spawn()
    print("Suddenly, a section of the floor cracks.\nFlagstones are upturned as a hand bursts out of the ground.\nFrom the dirt rises a bony figure that pulls a corroded sword with it.\nClumps of clay and stone fall away from the skeleton's bones as it steadies itself on its feet and points the sword directly at you.")
    continue_confirm()
    print("You unsheathe your own blade.")


#ROOM FUNCTIONS
#The function that allows the player to move between rooms
def room_movement():
    current_room = "vine_room"
    while current_room != "end_room":
        describe_room()
        continue_confirm()
        check_fight()
        
#Prints current_room's entry text. Allows the player to view the room description again if they forgot what was mentioned
def describe_room():
    print("hello" + roomdata[current_room]["description"]["entry"])

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


#SCORING FUNCTIONS
#Adds to the player's score depending on what the player is getting score from



#INVESTIGATION FUNCTIONS
#Selects the event to be run by the invst_event function
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
                unlock_exit()
                print("As you pull the book out, your hear a mechanism grinding away behind it.\nThe book stops moving about halfway off the bookshelf, and a metallic 'thunk' resonates throughout the quiet aisles.\nThe exit is now unlocked.")
                return "run"
                
            if book_choice == 2:
                print("You pull the first book out of the shelf. You blow the dust off the cover.")
                item_add("itm_r_bk")
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
