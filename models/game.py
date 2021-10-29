class Game:
    
    def calculate_winner(self, player1, player2):
        player1.choice = player1.choice.lower()
        player2.choice = player2.choice.lower()
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
        else:
            return None
