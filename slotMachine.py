import random

initialCoins = 50

def playSlotMachine(coins):

    reel1 = ["7", "BAR", "BAR", "BAR", "WM", "WM", "BELL", "GP", "GP", "GP", "GP", "GP", "GP", "GP", "OR", "OR", "OR",
            "OR", "OR", "CH", "CH"]

    reel2 = ["7", "BAR", "BAR", "WM", "WM", "BELL", "BELL", "BELL", "BELL", "BELL", "GP", "GP", "GP", "OR", "OR", "OR",
            "OR", "OR", "CH", "CH",
            "CH", "CH", "CH", "CH"]

    reel3 = ["7", "BAR", "WM", "WM", "BELL", "BELL", "BELL", "BELL", "BELL", "BELL", "BELL", "BELL", "GP", "GP", "GP",
            "OR", "OR", "OR", "OR",
            "LM", "LM", "LM", "LM"]

    game = []

    if coins == 0:
        print("Out of coins! You can't play")
    else:
        coinsInserted  = False
        while coinsInserted  is False:
            print("\nHow many coins do you want to bet on the line?")
            bet = int(input("BET: "))
            if bet <= 0:
                print("Invalid value, try again")
                coinsInserted  = False
            elif bet <= coins:
                coinsInserted  = True
                coins = coins - bet
                game = [reel1[random.randint(0,20)],reel2[random.randint(0,23)],reel3[random.randint(0,22)]]
                return print(game), print(coins)
            else:
                print("You don't have enough coins")
                coinsInserted  = False


playSlotMachine(coins = initialCoins)