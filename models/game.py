from random import choice
from models.player import Player

class Game:
    def calculate_winner(self, player1, player2):
        player1.choice = player1.choice.lower()
        player2.choice = player2.choice.lower()
        valid_choice = ["rock", "paper", "scissors"]
        if player1.choice not in valid_choice or player2.choice not in valid_choice:
            return "error"
        if player1.choice == player2.choice:
            return None
        elif player1.choice == "rock":
            if player2.choice == "paper":
                return player2
            elif player2.choice == "scissors":
                return player1
        elif player1.choice == "paper":
            if player2.choice == "rock":
                return player1
            elif player2.choice == "scissors":
                return player2
        elif player1.choice == "scissors":
            if player2.choice == "rock":
                return player2
            elif player2.choice == "paper":
                return player1
    
    def generate_computer_player(self):
        computer_choice = choice(["rock", "paper", "scissors"])
        computer_player = Player("Computer", computer_choice)
        return computer_player
