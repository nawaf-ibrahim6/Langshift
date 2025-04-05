
"""
Handles keyboard layout conversion.
"""

def convert_keyboard_layout(text: str, mapping: dict) -> str:
    """
    Converts a sentence based on a keyboard layout mapping.
    """
    return ''.join(
        mapping.get(char.lower(), char).upper() if char.isupper() else mapping.get(char.lower(), char)
        for char in text
    )
