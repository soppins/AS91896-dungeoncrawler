import functions

fun = functions

#When player successfully investigates something, this function decides what occurs based on the focus that was successful
def invst_event(focus):
    
    #Library event:
    if focus == "bookshelf":
        #If player doesn't already have the riddle book:
        if fun.item_in_inventory("itm_r_bk") == False and fun.roomdata[fun.current_room]["locked"] == True:
            book_choice = int(input("Out of the numerous books resting in this bookshelf, two stand out to you.\nDo you remove book 1 or 2? "))
            
            if book_choice == 1:
                fun.unlock_exit()
                print("As you pull the book out, your hear a mechanism grinding away behind it.\nThe book stops moving about halfway off the bookshelf, and a metallic 'thunk' resonates throughout the quiet aisles.\nThe exit is now unlocked.")
                fun.invst_input()
                
            if book_choice == 2:
                print("You pull the first book out of the shelf. You blow the dust off the cover.")
                fun.item_add("itm_r_bk")
                fun.invst_input()
            else:
                fun.invst_input()
        #If player has already unlocked the door:
        elif fun.roomdata[fun.current_room]["locked"] == False:
            book_choice = input("One book on the bookshelf stands out to you.\nDo you remove it? (y/n) ").lower()
            
            if book_choice == "y":
                print("You pull the first book out of the shelf. You blow the dust off the cover.")
                fun.item_add("itm_r_bk")
            else:
                fun.invst_input()
        #If player already has the riddle book:
        else:
            book_choice = input("One book on the bookshelf stands out to you.\nDo you remove it? (y/n) ").lower()
            
            if book_choice == "y":
                print("You pull the first book out of the shelf. You blow the dust off the cover.")
                fun.item_add("itm_r_bk")
            else:
                fun.invst_input()
                
    if focus == "well":
        print("good job")