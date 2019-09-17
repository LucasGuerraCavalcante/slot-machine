# -*- coding: utf-8 -*-
import os, sys
import random as rd

# This is the initial version of the game, a simple and "primitive" game to play using the terminal.
# The purpose of this project was to turn this into a web application.

coins = 50

reel1 = [
            "🐍", # Python Snake (1)
            "💻", "💻", "💻", # Computer (3)
            "🍉", "🍉", # Watermelon (2)
            "🔔", # Bell (1)
            "🍇", "🍇", "🍇", "🍇", "🍇", "🍇", "🍇", # Grape (7)
            "🍊", "🍊", "🍊","🍊", "🍊", # Orange (5)
            "🍒", "🍒"] # Cherrie (2)

reel2 = [
            "🐍", # Python Snake (1)
            "💻", "💻", # Computer (2)
            "🍉", "🍉", # Watermelon (2)
            "🔔", "🔔", "🔔", "🔔", "🔔", # Bell (5)
            "🍇", "🍇", "🍇", # Grape (3)
            "🍊", "🍊", "🍊","🍊", "🍊", # Orange (5)
            "🍒", "🍒","🍒", "🍒", "🍒", "🍒"] # Cherrie (6)

reel3 = [
            "🐍", # Python Snake (1)
            "💻", # Computer (1)
            "🍉", "🍉", # Watermelon (2)
            "🔔", "🔔", "🔔", "🔔", "🔔", "🔔", "🔔", "🔔", # Bell (8)
            "🍇", "🍇", "🍇", # Grape (3)
            "🍊", "🍊", "🍊", "🍊", # Orange (4)
            "👾", "👾", "👾", "👾"] # Evil Alien (4)

game = []

print("\n   |===_________===_______===_________===")
print("|*|   Welcome to Python Slot Machine Game |*|")
print("   |===_________===_______===_________===\n")

playingGame = False
while playingGame is False:
        print("Type [[1]] to Play [[0]] to Exit or [[2]] to see the Rules\n")
        option = int(input("Option: "))
        if option == 2:
            print("\nRules\n")
            print(" reel1 reeel2 reel3")
            print(" [🐍 ]  [🐍 ]  [🐍 ]  Three Python Snakes 200 coins x Bet Value")
            print(" [💻 ]  [💻 ]  [💻 ]  Three Computers 100 coins x Bet Value")
            print(" [🍉 ]  [🍉 ]  [🍉 ]  Three Watermelons 100 coins x Bet Value")
            print(" [🍉 ]  [🍉 ]  [💻 ]  Two Watermelons and one Computer 100 coins x Bet Value")
            print(" [🔔 ]  [🔔 ]  [🔔 ]  Three Bells 18 coins x Bet Value")
            print(" [🔔 ]  [🔔 ]  [💻 ]  Two Bells and one Computer 18 coins x Bet Value")
            print(" [🍇 ]  [🍇 ]  [🍇 ]  Three Grapes 14 coins x Bet Value")
            print(" [🍇 ]  [🍇 ]  [💻 ]  Two Grapes and one Computer 14 coins x Bet Value")
            print(" [🍊 ]  [🍊 ]  [🍊 ]  Three Oranges 10 coins x Bet Value")
            print(" [🍊 ]  [🍊 ]  [💻 ]  Two Oranges and one Computer 10 coins x Bet Value")
            print(" [🍒 ]  [🍒 ]  [ANY]  Two Cherries 5 coins x Bet Value")
            print(" [🍒 ]  [ANY] [ANY]  One Cherry 2 coins x Bet Value")
            print("Beware with the evil aliens! They can ruin your sequence.\n")
            playingGame = False
        elif option == 1:
            playingGame = True
            coinsInserted  = False
            leverDown = True
            while leverDown is True:
                if coins <= 0:
                        print("\nYou don't have enough coins\n")
                        leverDown = False
                        coinsInserted = True
                else:
                    while coinsInserted  is False:
                        print("\nYou have " + str(coins) + " coins to play")
                        print("\nHow many coins do you want to bet on the line?")
                        bet = int(input("BET: "))
                        if coins <= 0:
                            print("\nYou don't have enough coins\n")
                            leverDown = False
                            coinsInserted = True
                        elif bet > 0 and bet <= coins:
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
                            print(" |  |___________________________|  |")
                            print(" |   |                         |   |")
                            print("_|    |_______________________|    |_")
                            print("(_____________________________________)\n")
                            # ------------------------------------------------------------
                            if game == ["🐍","🐍","🐍"]:
                                prize = bet*200
                                coins += prize
                                print("YOU WON " + str(prize) + " coins!!!")
                                print("Now you have " + str(coins) +  " to gamble!!!\n")
                                print("It's your lucky day\n")
                            elif game == ["💻", "💻", "💻"] or game == ["🍉", "🍉", "🍉"] or game == ["🍉", "🍉", "💻"]:
                                prize = bet*100
                                coins += prize
                                print("YOU WON " + str(prize) + " coins!!!")
                                print("Now you have " + str(coins) +  " to gamble!!!\n")
                                print("It's your lucky day\n")
                            elif game == ["🔔","🔔","🔔"] or game == ["🔔","🔔", "💻"]:
                                prize = bet*18
                                coins += prize
                                print("YOU WON " + str(prize) + " coins!!!")
                                print("Now you have " + str(coins) +  " to gamble!!!\n")
                                print("It's your lucky day\n")
                            elif game == ["🍇", "🍇", "🍇"] or game == ["🍇", "🍇", "💻"]:
                                prize = bet*14
                                coins += prize
                                print("YOU WON " + str(prize) + " coins!!!")
                                print("Now you have " + str(coins) +  " to gamble!!!\n")
                                print("It's your lucky day\n")
                            elif game == ["🍊", "🍊", "🍊"] or game == ["🍊", "🍊", "💻"]:
                                prize = bet*10
                                coins += prize
                                print("YOU WON " + str(prize) + " coins!!!")
                                print("Now you have " + str(coins) +  " to gamble!!!\n")
                                print("It's your lucky day\n")
                            elif game[0] == "🍒" and  game[1] == "🍒":
                                prize = bet*5
                                coins += prize
                                print("YOU WON " + str(prize) + " coins!!!")
                                print("Now you have " + str(coins) +  " to gamble!!!\n")
                                print("It's your lucky day\n")
                            elif game[0] == "🍒":
                                prize = bet*2
                                coins += prize
                                print("YOU WON " + str(prize) + " coins!!!")
                                print("Now you have " + str(coins) +  " to gamble!!!\n")
                                print("It's your lucky day\n")
                            else:
                                ("You didn't win coins this time\n")
                            # ------------------------------------------------------------
                            print("Let's play again?\n")
                            print("Type [[1]] to YES or any number to NO")
                            again = int(input("Yes or No?: "))
                            # ------------------------------------------------------------
                            if again == 1:
                                leverDown = True
                                coinsInserted = False
                            else:
                                print("You left the game with " + str(coins) + " coins!")
                                leverDown = False
                        else:
                            print("\nInvalid value, try again")
                            print("Maybe you don't have this quantity of coins")
                            coinsInserted  = False
        elif option == 0:
            print("\n Bye!\n ")
            break
        else:
            print("\nInvalid value, try again")
            playingGame  = False

