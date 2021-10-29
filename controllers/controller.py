from flask import render_template
from app import app
from models.player import Player
from models.game import Game

@app.route("/welcome")
def welcome():
    return render_template("welcome.html", title="Welcome")

@app.route("/<choice1>/<choice2>")
def index(choice1, choice2):
    game1 = Game()
    player1 = Player("Player 1", choice1)
    player2 = Player("Player 2", choice2)
    winner = game1.calculate_winner(player1, player2)
    print(winner)
    if winner == "error":
        return "Error"
    elif winner == None:
        return render_template("index.html", title="Result", player1_name=player1.name, player1_choice=player1.choice, player2_name=player2.name, player2_choice=player2.choice, winner_name="Draw")
    else:
        return render_template("index.html", title="Result", player1_name=player1.name, player1_choice=player1.choice, player2_name=player2.name, player2_choice=player2.choice, winner_name=winner.name)

@app.route("/play")
def play_against_computer():
    return "Play vs computer"
