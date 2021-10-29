import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game1 = Game()
        self.player1 = Player("Player 1", "rock")
        self.player2 = Player("Player 2", "paper")
        self.player3 = Player("Player 3", "scissors")

    def test_rock_draws_with_rock(self):
        self.assertEqual(None, self.game1.calculate_winner(self.player1, self.player1))
    
    def test_paper_draws_with_paper(self):
        self.assertEqual(None, self.game1.calculate_winner(self.player2, self.player2))
    
    def test_scissors_draws_with_scissors(self):
        self.assertEqual(None, self.game1.calculate_winner(self.player3, self.player3))

    def test_rock_looses_to_paper(self):
        self.assertEqual(self.player2, self.game1.calculate_winner(self.player1, self.player2))
    
    def test_rock_beats_scissors(self):
        self.assertEqual(self.player1, self.game1.calculate_winner(self.player1, self.player3))
    
    def test_paper_beats_rock(self):
        self.assertEqual(self.player2, self.game1.calculate_winner(self.player2, self.player1))
    
    def test_paper_looses_to_scissors(self):
        self.assertEqual(self.player3, self.game1.calculate_winner(self.player2, self.player3))

    def test_scissors_looses_to_rock(self):
        self.assertEqual(self.player1, self.game1.calculate_winner(self.player3, self.player1))
    
    def test_scissors_beats_paper(self):
        self.assertEqual(self.player3, self.game1.calculate_winner(self.player3, self.player2))
