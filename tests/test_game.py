from src.longest_word.game import Game


class TestGame:
    def test_game_initialization(self):
        game = Game()
        assert game.is_valid("BAROQUE") is True
        assert game.is_valid("JACKTOKE") is False
