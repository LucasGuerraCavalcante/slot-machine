# -*- coding: utf-8 -*-
import os, sys
import random as rd

coins = 50

reel1 = ["🐍", # Python Snake (1)
            "💻", "💻", "💻", # Computer (3)
            "🍉", "🍉", # Watermelon (2)
            "🔔", # Bell (1)
            "🍇", "🍇", "🍇", "🍇", "🍇", "🍇", "🍇", # Grape (7)
            "🍊", "🍊", "🍊","🍊", "🍊", # Orange (5)
            "🍒", "🍒"] # Cherrie (2)

reel2 = ["🐍", # Python Snake (1)
            "💻", "💻", # Computer (2)
            "🍉", "🍉", # Watermelon (2)
            "🔔", "🔔", "🔔", "🔔", "🔔", # Bell (5)
            "🍇", "🍇", "🍇", # Grape (3)
            "🍊", "🍊", "🍊","🍊", "🍊", # Orange (5)
            "🍒", "🍒","🍒", "🍒", "🍒", "🍒"] # Cherrie (6)

reel3 = ["🐍", # Python Snake (1)
            "💻", # Computer (1)
            "🍉", "🍉", # Watermelon (2)
            "🔔", "🔔", "🔔", "🔔", "🔔", "🔔", "🔔", "🔔", # Bell (8)
            "🍇", "🍇", "🍇", # Grape (3)
            "🍊", "🍊", "🍊", "🍊", # Orange (4)
            "👾", "👾", "👾", "👾"] # Evil Alien (4)

game = []

print("\n|===_________===_______===_________===")
print("|*| Welcome to Python Slot Machine |*|")
print("|===_________===_______===_________===\n")

playingGame = False
while playingGame is False:
        print("Pres [[1]] to Play [[0]] to Exit or [[2]] to see the Rules\n")
        option = int(input("Option: "))
        if option == 2:
            print("Rules\n")
            playingGame = False
        elif option == 1:
            playingGame = True
            coinsInserted  = False
            while coinsInserted  is False:
                print("\nYou have " + str(coins) + " coins to play")
                print("\nHow many coins do you want to bet on the line?")
                bet = int(input("BET: "))
                if bet <= 0:
                    print("\nInvalid value, try again")
                    coinsInserted  = False
                elif bet <= coins:
                    coinsInserted  = True
                    coins = coins - bet
                    game = [reel1[rd.randint(0,20)],reel2[rd.randint(0,23)],reel3[rd.randint(0,22)]]
                    print("\n              .-------.")
                    print("              |       |")
                    print("  ____________|_______|____________")
                    print(" |  __    __    ___  _____   __    |")  
                    print(" | / _\  / /   /___\/__   \ / _\   |") 
                    print(" | \ \  / /   //  //  / /\ \\ \  25|")  
                    print(" | _\ \/ /___/ \_//  / /  \/_\ \ []|") 
                    print(" | \__/\____/\___/   \/     \__/ []|")
                    print(" |===_______===_______===_______===| __")
                    print(" ||*|_______|*|_______|*|_______|*||(__)")
                    print(" |===_______===_______===_______===| ||")
                    print(" ||*| _____ |*| _____ |*| _____ |*|| ||")
                    print(" ||*||     ||*||     ||*||     ||*|| ||")
                    print(" ||*|| " + game[0] + "   ||*|| " + game[1] + "   ||*|| " + game[2] + "   ||*|| ||")
                    print(" ||*||_____||*||_____||*||_____||*|| ||")
                    print(" ||*|_______|*|_______|*|_______|*||_//")
                    print(" |===_______===_______===_______===|_/")      
                    print(" |lc=___________________________===|")
                    print(" |  /___________________________\  |")
                    print(" |   |                         |   |")
                    print("_|    \_______________________/    |_")
                    print("(_____________________________________)\n")
                else:
                    print("You don't have enough coins")
                    coinsInserted  = False
        elif option == 0:
            print("\n Bye!")
            break
        else:
            print("\nInvalid value, try again")
            playingGame  = False

