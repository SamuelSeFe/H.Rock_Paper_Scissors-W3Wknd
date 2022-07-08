from flask import render_template
from app import app
from modules.players import Player
from modules.roshambo import Game

@app.route('/roshambo')
def index():
    return render_template('index.html')
