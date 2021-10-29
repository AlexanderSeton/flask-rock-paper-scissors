import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1", "rock")

    def test_player_has_name(self):
        self.assertEqual("Player 1", self.player1.name)
    
    def test_player_has_choice(self):
        self.assertEqual("rock", self.player1.choice)
