"""
This is just a simple test file to verify if the methods are behaving as expected.

Classes:
    Game: The main class of the game.

Functions:
    is_valid(text): check if the word is valid in a given grid of letters

"""
from src.longest_word.game import Game



"""Test the Game class"""
class TestGame:
    """Let's test if the game is working as expected"""
    def test_game_is_valid(self):
        """Test the Game is_valid method"""
        game = Game()
        assert game.is_valid("BAROQUE") is True
        assert game.is_valid("JACKTOKE") is False
