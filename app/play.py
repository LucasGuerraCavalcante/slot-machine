# -*- coding: utf-8 -*-
import os, sys
import random as rd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class coins():
    coins = None

data = coins()

@app.route('/')
def render_static():

    data.coins= 50

    return render_template('index.html', status='Bet some coins', 
    a=' ', b=' ', c=' ', coins=data.coins)

@app.route("/bet", methods=['GET','POST'])
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

    bet = request.form['betInput']
    bet = int(bet)

    if (data.coins < 0):

        return render_template('index.html', 
            status="Out of coins", sequence="Go back to '/' to play again",
            a='X', b='X', c='X', coins=0)

    elif (bet < 0):

        return render_template('index.html', 
            status="Missing a resonable bet value", sequence="Go back to '/' to play again",
            a='X', b='X', c='X', coins=0)

    elif (data.coins and bet) and (data.coins > 0 and bet > 0):

        data.coins -= bet

        game = [reel1[rd.randint(0,20)],reel2[rd.randint(0,23)],reel3[rd.randint(0,22)]]

        if game == ["7","7","7"]:

            prize = bet*200
            status = "YOU WON " + str(prize) + " coins!!!"
            data.coins += prize

            sequence = "Three 7 sequence"

            a = game[0]
            b = game[1]
            c = game[2]

        elif game == ["A", "A", "A"] or game == ["♠", "♠", "♠"] or game == ["♠", "♠", "A"]:

            prize = bet*100
            status = "YOU WON " + str(prize) + " coins!!!"
            data.coins += prize

            if game == ["A", "A", "A"]:
                sequence = "Three As sequence"
            elif game == ["♠", "♠", "♠"]:
                sequence = "Three Spades sequence"
            else:
                sequence = "Two Spades and one A sequence"

            a = game[0]
            b = game[1]
            c = game[2]

        elif game == ["♣","♣","♣"] or game == ["♣","♣", "A"]:

            prize = bet*18
            status = "YOU WON " + str(prize) + " coins!!!"
            data.coins += prize

            if game == ["♣","♣","♣"]:
                sequence = "Three Clubs sequence"
            else:
                sequence = "Two Clubs and one A sequence"

            a = game[0]
            b = game[1]
            c = game[2]

        elif game == ["♥", "♥", "♥"] or game == ["♥", "♥", "A"]:

            prize = bet*14
            status = "YOU WON " + str(prize) + " coins!!!"
            data.coins += prize

            if game == ["♥", "♥", "♥"]:
                sequence = "Three Hearts sequence"
            else:
                sequence = "Two Hearts and one A sequence"

            a = game[0]
            b = game[1]
            c = game[2]

        elif game == ["♦", "♦", "♦"] or game == ["♦", "♦", "A"]:

            prize = bet*10
            status = "YOU WON " + str(prize) + " coins!!!"
            data.coins += prize

            if game == ["♦", "♦", "♦"]:
                sequence = "Three Diamonds sequence"
            else:
                sequence = "Two Diamonds and one A sequence"

            a = game[0]
            b = game[1]
            c = game[2]

        elif game[0] == "☺" and  game[1] == "☺":

            prize = bet*5
            status = "YOU WON " + str(prize) + " coins!!!"
            data.coins += prize

            sequence = "Two Happy Faces sequence"

            a = game[0]
            b = game[1]
            c = game[2]

        elif game[0] == "☺":
            prize = bet*2
            status = "YOU WON " + str(prize) + " coins!!!"
            data.coins += prize

            sequence = "One Happy Face sequence"

            a = game[0]
            b = game[1]
            c = game[2]

        else:
            a = game[0]
            b = game[1]
            c = game[2]
            status = "Try again, good lucky"
            sequence = ''

        if data.coins < 0:
            data.coins = 0

        return render_template('index.html', status=status, sequence=sequence,
            a=a, b=b, c=c, coins=data.coins)

    else: 
        status = "Missing data"

        return render_template('index.html', status=status, sequence="Go back to '/' to play again",
            a='X', b='X', c='X', coins=0)

            
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)