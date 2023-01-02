"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):
        '''creates alist of words from a text file found using path'''
        file = open(path)
        self.list_of_words = [line.strip() for line in file]
        file.close()
        print(f"{len(self.list_of_words)} words read")

    def random(self):
        """Return random word."""
        return random.choice(self.list_of_words)