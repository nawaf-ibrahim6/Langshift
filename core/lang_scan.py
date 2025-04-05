"""
Language script detection and sentence analysis helpers.
"""

import difflib

def get_script(text: str) -> str:
    """
    Detects if the sentence is in Arabic or English based on Unicode range.
    """
    for char in text:
        if char.isalpha() and (0x0600 <= ord(char) <= 0x06FF or
                               0x0750 <= ord(char) <= 0x077F or
                               0x08A0 <= ord(char) <= 0x08FF):
            return "Arabic"
    return "English"

def clean_word(word: str) -> str:
    return ''.join(c for c in word if c.isalpha())

def get_words_in_sentence(sentence: str):
    return [clean_word(w) for w in sentence.split() if clean_word(w)]

def is_word_recognized(word, word_list, fuzzy_cutoff=0.8):
    return word in word_list or bool(difflib.get_close_matches(word, word_list, n=1, cutoff=fuzzy_cutoff))

def sentence_has_meaning(sentence: str, word_list: set, is_case_sensitive=False, threshold=0.7):
    """
    Checks if the sentence contains a high-enough ratio of known words.
    """
    words = get_words_in_sentence(sentence)
    if not words:
        return False

    recognized = sum(
        is_word_recognized(w.lower() if not is_case_sensitive else w, word_list)
        for w in words
    )
    return recognized / len(words) >= threshold
