def convert_keyboard_layout(text: str, mapping: dict) -> str:
    """
    Convert the input text from one keyboard layout to another using the provided mapping.
    
    Args:
        text (str): The input text in the source layout.
        mapping (dict): A dictionary mapping source characters to target characters.
    
    Returns:
        str: The converted text.
    """
    converted = []
    for char in text:
        # Use lower-case mapping for letters; preserve the original case
        lower_char = char.lower()
        if lower_char in mapping:
            mapped_char = mapping[lower_char]
            # Preserve case: if original char is uppercase, convert result to uppercase.
            converted.append(mapped_char.upper() if char.isupper() else mapped_char)
        else:
            converted.append(char)
    return "".join(converted)

# Define mapping for Arabic to English using a typical QWERTY layout.
arabic_to_english = {
    'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't', 'غ': 'y',
    'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p',
    'ج': '[', 'د': ']', 
    'ش': 'a', 'س': 's', 'ي': 'd', 'ب': 'f', 'ل': 'g',
    'ا': 'h', 'ت': 'j', 'ن': 'k', 'م': 'l',
    'ك': ';', 'ط': "'",
    'ئ': 'z', 'ء': 'x', 'ؤ': 'c', 'ر': 'v',
    # For keys with composite characters (e.g. "لا"), you may need to handle them separately.
    # In this example, we'll map a single key for 'لا' if required.
    'لا': 'b',
    'ى': 'n', 'ة': 'm'
}

# Generate the reverse mapping (English to Arabic)
# Note: If the mapping isn't one-to-one (i.e. two Arabic letters map to the same English letter),
# this reverse mapping might be ambiguous and may require manual adjustments.
english_to_arabic = {v: k for k, v in arabic_to_english.items()}

# Sample texts to demonstrate conversion in both directions:
gibberish_arabic = "ه شة ىشصشب"
gibberish_english = "انا نواف"

# Convert from Arabic gibberish (typed on Arabic layout) to English
converted_to_english = convert_keyboard_layout(gibberish_arabic, arabic_to_english)
print("Converted Arabic to English:", converted_to_english)

# Convert from English gibberish (typed on English layout) to Arabic
converted_to_arabic = convert_keyboard_layout(gibberish_english, english_to_arabic)
print("Converted English to Arabic:", converted_to_arabic)