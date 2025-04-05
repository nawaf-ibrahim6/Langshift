"""
Keyboard layout mappings for conversion between Arabic and English layouts.
"""

arabic_to_english = {
    'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't',
    'غ': 'y', 'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p',
    'ش': 'a', 'س': 's', 'ي': 'd', 'ب': 'f', 'ل': 'g',
    'ا': 'h', 'ت': 'j', 'ن': 'k', 'م': 'l',
    'ئ': 'z', 'ء': 'x', 'ؤ': 'c', 'ر': 'v', 'لا': 'b',
    'ى': 'n', 'ة': 'm', 'و': ',', 'ز': '.', 'ظ': ']', 'ط': '[', 'ذ': '`', 'د': "'", '؛': ';'
}

english_to_arabic = {v: k for k, v in arabic_to_english.items()}
