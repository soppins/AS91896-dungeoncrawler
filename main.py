#Importing libraries
import time
import player_class
import functions

#Attaching player class to object
plr = player_class.player()

#Attaching functions to fun. prefix
fun = functions


print("Here's a little preview of what part of the gameloop will be like.\nOnce you enter a new room in the game, you have a chance of entering a fight.\nAfter this, you are then provided with a description of the new room.\nYou can then use items or investigate your surroundings.\nThis is a preview of the investigation system.")
time.sleep(10)
print(fun.map_position())
time.sleep(3)
print(f"current location: {fun.current_room}")
time.sleep(1)
fun.invst_input()
