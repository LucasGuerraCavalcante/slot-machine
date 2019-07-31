# -*- coding: utf-8 -*-
import os, sys
import random as rd

initialCoins = 50

def playSlotMachine(coins):

    reel1 = ["🐍", # Python Snake (1)
            "🤖", "🤖", "🤖", # Robot (3)
            "🍉", "🍉", # Watermelon (2)
            "🔔", # Bell (1)
            "🍇", "🍇", "🍇", "🍇", "🍇", "🍇", "🍇", # Grape (7)
            "🍊", "🍊", "🍊","🍊", "🍊", # Orange (5)
            "🍒", "🍒"] # Cherrie (2)

    reel2 = ["🐍", # Python Snake (1)
            "🤖", "🤖", # Robot (2)
            "🍉", "🍉", # Watermelon (2)
            "🔔", "🔔", "🔔", "🔔", "🔔", # Bell (5)
            "🍇", "🍇", "🍇", # Grape (3)
            "🍊", "🍊", "🍊","🍊", "🍊", # Orange (5)
            "🍒", "🍒","🍒", "🍒", "🍒", "🍒"] # Cherrie (6)

    reel3 = ["🐍", # Python Snake (1)
            "🤖", # Robot (1)
            "🍉", "🍉", # Watermelon (2)
            "🔔", "🔔", "🔔", "🔔", "🔔", "🔔", "🔔", "🔔", # Bell (8)
            "🍇", "🍇", "🍇", # Grape (3)
            "🍊", "🍊", "🍊", "🍊", # Orange (4)
            "👾", "👾", "👾", "👾"] # Evil Alien (4)

    game = []

    if coins == 0:
        print("Out of coins! You can't play")
    else:
        coinsInserted  = False
        while coinsInserted  is False:
            print("\nHow many coins do you want to bet on the line?")
            bet = int(input("BET: "))
            if bet <= 0:
                print("\nInvalid value, try again")
                coinsInserted  = False
            elif bet <= coins:
                coinsInserted  = True
                coins = coins - bet
                game = [reel1[rd.randint(0,20)],reel2[rd.randint(0,23)],reel3[rd.randint(0,22)]]
                print("              .-------.")
                print("              |Jackpot|")
                print("  ____________|_______|____________")
                print(" |  __    __    ___  _____   __    |")  
                print(" | / _\  / /   /___\/__   \ / _\   |") 
                print(" | \ \  / /   //  //  / /\ \\ \  25|")  
                print(" | _\ \/ /___/ \_//  / /  \/_\ \ []|") 
                print(" | \__/\____/\___/   \/     \__/ []|")
                print(" |===_______===_______===_______===|")
                print(" ||*|\_     |*| _____ |*|\_     |*||")
                print(" ||*|| \ _  |*||     ||*|| \ _  |*||")
                print(" ||*| \_(_) |*||*BAR*||*| \_(_) |*||")
                print(" ||*| (_)   |*||_____||*| (_)   |*|| __")
                print(" ||*|_______|*|_______|*|_______|*||(__)")
                print(" |===_______===_______===_______===| ||")
                print(" ||*| _____ |*| _____ |*| _____ |*|| ||")
                print(" ||*||     ||*||     ||*||     ||*|| ||")
                print(" ||*|| " + game[0] + "   ||*|| " + game[1] + "   ||*|| " + game[2] + "   ||*|| ||")
                print(" ||*||_____||*||_____||*||_____||*|| ||")
                print(" ||*|_______|*|_______|*|_______|*||_//")
                print(" |===_______===_______===_______===|_/")
                print(" ||*|  ___  |*|   |   |*| _____ |*||")
                print(" ||*| |_  | |*|  / \  |*||     ||*||")
                print(" ||*|  / /  |*| /_ _\ |*||*BAR*||*||")             
                print(" ||*| /_/   |*|   O   |*||_____||*||")       
                print(" ||*|_______|*|_______|*|_______|*||")
                print(" |lc=___________________________===|")
                print(" |  /___________________________\  |")
                print(" |   |                         |   |")
                print("_|    \_______________________/    |_")
                print("(_____________________________________)")
                # print("{ [[" + game[0] + " ]] [[" + game[1] + " ]] [[" + game[2] + " ]] } / ")
            else:
                print("You don't have enough coins")
                coinsInserted  = False


playSlotMachine(coins = initialCoins)