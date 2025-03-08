
"""
This is just a simple test file to verify if the methods are behaving as expected.

Classes:
    Game: The main class of the game.

Functions:
    is_valid(text): check if the word is valid in a given grid of letters
    can_make_word(word, letters): check if the word can be made with the letters

"""

from collections import Counter



class Game:
    grid = None

    def __init__(self):
        """Attribute a random grid of size 9"""
        self.grid = "OQUWRBAZE"

    def can_make_word(self, word, letters):
        """Check if the word can be made with the letters"""
        word_counts = Counter(word.upper())
        letter_counts = Counter(letters.upper())

        for letter, count in word_counts.items():
            if letter not in letter_counts or letter_counts[letter] < count:
                return False
        return True

    def is_valid(self, word) -> bool:
        """Check if the word is valid"""
        return self.can_make_word(word, self.grid)
