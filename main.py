#Importing libraries
import time
import player_class as plr
import functions as fun

#Attaching player class to object
plr = plr.player()

print("Here's a little preview of what part of the gameloop will be like.\nOnce you enter a new room in the game, you have a chance of entering a fight.\nAfter this, you are then provided with a description of the new room.\nYou can then use items or investigate your surroundings.\nThis is a preview of the investigation system.\nCheck the code for the work I've done, most of it is commented.")
time.sleep(5)
print(fun.map_position())
time.sleep(3)
print(f"current location: {fun.current_room}")
time.sleep(1)
fun.invst_input()
