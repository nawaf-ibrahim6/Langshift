"""
CLI entry point for analyzing sentences and correcting layout.
"""

from core.analyzer import detect_and_check, convert_and_retry
from core.wordlist import WordListLoader

def main():
    wordlists = WordListLoader('arabic-wordlist-1.6.txt')
    print("=== LanguageShift Tool ===")
    print("Type a sentence (or 'none' to exit)\n")

    while True:
        user_input = input(">> ")
        if user_input.lower() == 'none':
            break

        language, meaningful = detect_and_check(user_input, wordlists)
        if meaningful:
            print("[✓] Valid:", user_input)
        else:
            converted = convert_and_retry(user_input, language, wordlists)
            print("[✓] Converted:", converted)

if __name__ == "__main__":
    main()
