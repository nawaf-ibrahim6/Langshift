"""
Handles loading and storing Arabic and English wordlists.
"""

import nltk
import sys
from nltk.corpus import words

class WordListLoader:
    def __init__(self, arabic_path):
        self.english_words = self.load_english_words()
        self.arabic_words = self.load_arabic_words(arabic_path)

    def load_english_words(self):
        try:
            nltk.data.find('corpus/words')
        except LookupError:
            nltk.download('words')
        return set(words.words())

    def load_arabic_words(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return set(line.strip() for line in f)
        except FileNotFoundError:
            print(f"Arabic wordlist not found at {path}")
            sys.exit(1)
