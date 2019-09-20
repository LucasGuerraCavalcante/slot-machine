# -*- coding: utf-8 -*-
import os, sys
import random as rd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def render_static():

    coins = 50

    return render_template('index.html', 
            coinsPlay = str(coins), a = " ", b = " ", c = " ")


@app.route("/bet", methods=['POST'])

def bet():
    
    reel1 = [
                "7", # 7 (1)
                "A", "A", "A", # A (bar) (3)
                "♠", "♠", # Spades (Watermelon) (2)
                "♣", # Clubs (Bell) (1)
                "♥", "♥", "♥", "♥", "♥", "♥", "♥", # Hearts (Grape) (7)
                "♦", "♦", "♦","♦", "♦", # Diamonds (Orange) (5)
                "☺", "☺"] # Happy Face (Chery) (2)

    reel2 = [
                "7", # 7 (1)
                "A", "A", # A (bar) (2)
                "♠", "♠", # Spades (Watermelon)  (2)
                "♣", "♣", "♣", "♣", "♣", # Clubs (Bell) (5)
                "♥", "♥", "♥", # Hearts (Grape) (3)
                "♦", "♦", "♦","♦", "♦", # Diamonds (Orange) (5)
                "☺", "☺","☺", "☺", "☺", "☺"] # Happy Face (Chery) (6)

    reel3 = [
                "7", # 7 (1)
                "A", # A (bar) (1)
                "♠", "♠", # Spades (Watermelon)  (2)
                "♣", "♣", "♣", "♣", "♣", "♣", "♣", "♣", # Clubs (Bell) (8)
                "♥", "♥", "♥", # Hearts (Grape) (3)
                "♦", "♦", "♦", "♦", # Diamonds (Orange) (4)
                "☹", "☹", "☹", "☹"] # Sad Face (Lemon) (4)

    coins = 50

    if coins != 0:
        game = [reel1[rd.randint(0,20)],reel2[rd.randint(0,23)],reel3[rd.randint(0,22)]]
        if game == ["7","7","7"]:
            #prize = bet*200
            #coins += prize
            status = "YOU WON  coins!!!"
            print("It's your lucky day\n")
            a = game[0]
            b = game[1]
            c = game[2]
        elif game == ["A", "A", "A"] or game == ["♠", "♠", "♠"] or game == ["♠", "♠", "A"]:
            #prize = bet*100
            #coins += prize
            status = "YOU WON  coins!!!"
            a = game[0]
            b = game[1]
            c = game[2]
        elif game == ["♣","♣","♣"] or game == ["♣","♣", "A"]:
            #prize = bet*18
            #coins += prize
            status = "YOU WON  coins!!!"
            a = game[0]
            b = game[1]
            c = game[2]
        elif game == ["♥", "♥", "♥"] or game == ["♥", "♥", "A"]:
            #prize = bet*14
            #coins += prize
            status = "YOU WON  coins!!!"
            a = game[0]
            b = game[1]
            c = game[2]
        elif game == ["♦", "♦", "♦"] or game == ["♦", "♦", "A"]:
            #prize = bet*10
            #coins += prize
            status = "YOU WON  coins!!!"
            a = game[0]
            b = game[1]
            c = game[2]
        elif game[0] == "☺" and  game[1] == "☺":
            #prize = bet*5
            #coins += prize
            status = "YOU WON  coins!!!"
            a = game[0]
            b = game[1]
            c = game[2]
        elif game[0] == "☺":
            #prize = bet*2
            #coins += prize
            status = "YOU WON  coins!!!"
            a = game[0]
            b = game[1]
            c = game[2]
        else:
            a = game[0]
            b = game[1]
            c = game[2]
            status = "No luck today"


    return render_template('index.html',coinsPlay = str(coins), 
            a = a, b = b, c = c, space = "",
            status = status)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)