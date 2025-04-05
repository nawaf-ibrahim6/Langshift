"""
High-level orchestration: detect, analyze, and convert if needed.
"""

from core.convert import convert_keyboard_layout
from core.lang_scan import get_script, sentence_has_meaning
from core.maps import arabic_to_english, english_to_arabic

def detect_and_check(sentence, wordlists):
    """
    Detects language and checks if sentence has meaning.
    """
    language = get_script(sentence)
    wordlist = wordlists.arabic_words if language == "Arabic" else wordlists.english_words
    has_meaning = sentence_has_meaning(sentence, wordlist, is_case_sensitive=(language == "Arabic"))
    return language, has_meaning

def convert_and_retry(sentence, language, wordlists):
    """
    Attempts conversion and rechecks for meaning.
    """
    mapping = arabic_to_english if language == "Arabic" else english_to_arabic
    converted = convert_keyboard_layout(sentence, mapping)
    new_language, has_meaning = detect_and_check(converted, wordlists)
    return converted if has_meaning else sentence
