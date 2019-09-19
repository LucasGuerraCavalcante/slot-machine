# -*- coding: utf-8 -*-
import os, sys
import random as rd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def render_static():

    coins = 50

    return render_template('index.html', 
            coinsPlay = str(coins), a = "  ", b = "  ", c = "  ")


@app.route("/bet", methods=['POST'])

def bet():
    
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

    coins = 50
    a = "🍊"
    b = "🍉"
    c = "👾"


    return render_template('index.html',coinsPlay = str(coins), a = a, b = b, c = c)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)