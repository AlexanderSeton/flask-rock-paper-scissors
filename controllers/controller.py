from flask import render_template, request
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
def open_computer_vs_human_page():
    return render_template("play.html", title="Computer Opponent")

@app.route("/play", methods=["POST"])
def get_result_against_computer():
    game1 = Game()
    human_name = request.form["name"]
    human_choice = request.form["choice"]
    human_player = Player(human_name, human_choice)
    computer_player = game1.generate_computer_player()
    winner = game1.calculate_winner(human_player, computer_player)
    if winner == None:
        return render_template("index.html", title="Result", player1_name=human_player.name, player1_choice=human_player.choice, player2_name=computer_player.name, player2_choice=computer_player.choice, winner_name="Draw")
    else:
        return render_template("index.html", title="Result", player1_name=human_player.name, player1_choice=human_player.choice, player2_name=computer_player.name, player2_choice=computer_player.choice, winner_name=winner.name)
