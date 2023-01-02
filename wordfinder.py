"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):
        '''creates alist of words from a text file found using path'''
        file = open(path)
        self.list_of_words = self.parse(file)
        file.close()
        print(f"{len(self.list_of_words)} words read")
    
    def parse(self, file):
        """Parse dict_file -> list of words."""
        return [w.strip() for w in file]

    def random(self):
        """Return random word."""
        return random.choice(self.list_of_words)



class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    """
    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""
        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]