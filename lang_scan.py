import re
import torch
from langdetect import detect, DetectorFactory
from transformers import pipeline

# Ensure consistent language detection results
DetectorFactory.seed = 0

# Initialize a multilingual text classification model
classifier = pipeline("text-classification", model="distilbert-base-multilingual-cased", top_k=1)

def is_gibberish(text: str, threshold: float = 0.3) -> bool:
    """
    Determines if the given text is gibberish based on:
    1. Length and character composition (heuristic rules)
    2. Confidence score from a text classification model
    3. Character diversity ratio
    
    Args:
        text (str): The input text to analyze.
        threshold (float): Minimum confidence score to consider text as meaningful.
    
    Returns:
        bool: True if the text is classified as gibberish, False otherwise.
    """
    text = text.strip()
    
    # Check if the text is too short or contains only numbers/symbols
    if len(text) < 3 or re.match(r'^[\d\s\W]+$', text):
        return True
    
    # Evaluate text using the classification model
    try:
        result = classifier(text)[0][0]  # Extract top classification result
        if result['score'] < threshold:
            return True
    except Exception as e:
        print(f"Model classification error: {e}")
        return True
    
    # Calculate character diversity ratio (low ratio suggests repetition)
    unique_chars = len(set(text.lower()))
    diversity_ratio = unique_chars / len(text)
    if diversity_ratio < 0.1:  # Threshold to detect excessive repetition
        return True
    
    return False

def detect_language_and_gibberish(text: str) -> tuple[str, bool]:
    """
    Detects the language of the given text and determines if it is gibberish.
    
    Args:
        text (str): The input text to analyze.
    
    Returns:
        tuple[str, bool]: A tuple containing:
            - Language detected ('english', 'arabic', or 'gibberish')
            - Boolean indicating if the text is gibberish
    """
    try:
        lang = detect(text)
        
        if lang == "en" and not is_gibberish(text):
            return "english", False
        elif lang == "ar" and not is_gibberish(text):
            return "arabic", False
    except Exception as e:
        print(f"Language detection error: {e}")
    
    return "gibberish", True

# Sample test cases
sample_texts = [
    "Hello, how are you today?",         # Standard English
    "Yo wassup fam, how you holdin up?", # Casual English
    "مرحبا، كيف حالك اليوم؟",          # Standard Arabic
    "اهلا ياعم، عامل ايه؟",            # Egyptian Arabic dialect
    "flarbz quixotic zibberjab",        # Gibberish
    "12345 %^&*()",                     # Gibberish (symbols & numbers)
    "aaaaaaa bbbbb ccccc",              # Gibberish (repetitive patterns)
    "heyyy bro whats good?",            # Casual English with elongation
    "مشششكلة كبيرة يارجالة",           # Casual Arabic with repetition
    "do u wanna do smthn",              # Informal English
    "انا بدي العب طابة"                 # Informal Arabic
]

# Execute tests
for text in sample_texts:
    language, gibberish_flag = detect_language_and_gibberish(text)
    print(f"Text: '{text}' -> Language: {language}, Gibberish: {gibberish_flag}")
