from flask import render_template
from app import app
from modules.players import Player
from modules.roshambo import Game

@app.route('/roshambo')
def index():
    return render_template('index.html')

@app.route('/roshambo/<input_p1>/<input_p2>')
def roshambo(input_p1, input_p2):
    return render_template('result.html', result=roshambo(input_p1, input_p2))
    # print(roshambo(input_p1, input_p2))
    # return render_template('result.html', result=Game(player1, player2.roshambo(input_p1, input_p2)))