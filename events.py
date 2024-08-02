#This file is currently is the worst state due to the weird things ive had to do to get this kind of working for the hand-in without fixing the strange logic issues I'm having

import json

#Opening json files for later use
with open("./json_files/item_data.json", "r") as read_file:
    itemdata = json.load(read_file)

with open("./json_files/room_data.json", "r") as read_file:
    roomdata = json.load(read_file)

#I'm re-calling these functions, the class, and the json files in this file because there's some sort of circular import error that breaks this and i dont have the time to fix it right now

import player_class as plr

plr = plr.player()
current_room = "library_room"

#Adding item to inventory
def item_add(item):
    plr.inventory.append(item)
    print("'" + itemdata[item]["name"] + "' added to inventory.")
    print("(Description: " + itemdata[item]["description"]["summary"] + ")")

#Checks if a specified item is already in the player's inventory
def item_in_inventory(item):
    return True if item in plr.inventory else False

#Unlocking current room exit door
def unlock_exit():
    roomdata[current_room]["locked"] = False
    
    


#When player successfully investigates something, this function decides what occurs based on the focus that was successful.
#Each room can only have one successful focus, so this is effectively determining the event by the room the player is in.
def invst_event(focus):
    
    #Library event (particularly spaghetti-code-ey):
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
