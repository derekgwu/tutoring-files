import time
import os
import random

#this generate a set of colors for the users to memorize
def generate_move(current_turn):
    bank = ["red", "blue", "green", "yellow"]
    for i in range(0, current_turn):
        move = bank[random.randrange(0,4)]
        print(move)
        time.sleep(2)

        #develop a system to store the outputs (hint data structure!)

    #clears terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    #likely want to return the data structure

#your code here!

