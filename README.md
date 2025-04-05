# Langshift

**Langshift** is a command-line tool designed to analyze sentences, detect their language (Arabic or English), and correct keyboard layout errors. It checks if a sentence is meaningful based on predefined wordlists and, if not, attempts to convert it to the correct layout (e.g., from an Arabic keyboard layout typed in English to proper Arabic script, or vice versa). This tool is particularly useful for bilingual users who accidentally type in the wrong keyboard layout.

This repository contains the `wordswitch-langscan` branch, which implements the core functionality of the Langshift tool.

---

## **Features**
- Detects whether a sentence is in Arabic or English based on Unicode ranges.
- Validates sentence meaning using Arabic and English wordlists.
- Converts text between Arabic and English keyboard layouts if the input is not meaningful.
- Simple CLI interface for real-time sentence analysis.

---

## **Prerequisites**
To run Langshift, ensure you have the following installed:
- **Python 3.8+**: The project is written in Python and requires a modern version.
- **Git**: To clone the repository.
- An internet connection (initially, to download the NLTK English word corpus).

---

## **Setup Instructions**

Follow these steps to set up and run the Langshift project on your machine:

### 1. Clone the Repository
Clone the repository and switch to the `wordswitch-langscan` branch:
```bash
git clone https://github.com/nawaf-ibrahim6/Langshift.git
cd Langshift
git checkout wordswitch-langscan
```

### 2. Prepare the Environment
Create a virtual environment (optional but recommended) and activate it:


#### on windows :
```
python -m venv venv
venv\Scripts\activate
```
#### On macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required Python packages listed in `requirements.txt` :
```
pip install -r requirements.txt
```
This installs the `nltk` library, which is used for English wordlist support.
### 4. Download NLTK Data
The project uses the **NLTK** `words` corpus for English word validation. The first time you run the tool, it will automatically download this corpus if it’s not already present. Alternatively, pre-download it with:
```
python -c "import nltk; nltk.download('words')"
```

### 5. Verify the Arabic Wordlist
Ensure the `arabic-wordlist-1.6.txt` file is present in the root directory. This file contains a list of Arabic words used for validation. It is managed with Git LFS (Large File Storage) due to its size.

If you encounter issues with Git LFS:

- Install Git LFS: `git lfs install`
- Pull the file: `git lfs pull`

## **Running the Project**
Once the environment is set up, run the Langshift tool:
```
python langshift.py
```

### **Usage**
- The tool starts a CLI prompt (`>>`).
- Type a sentence to analyze it.
- If the sentence is meaningful (based on the wordlists), it will be marked as valid (`[✓] Valid:`).
- If not, it will attempt to convert the keyboard layout and display the corrected version (`[✓] Converted:`).
- Type `none` to exit.

### **Example**
```
=== LanguageShift Tool ===
Type a sentence (or 'none' to exit)

>> مرحبا
[✓] Valid: مرحبا

>> lvpfh
[✓] Converted: مرحبا

>> hello
[✓] Valid: hello

>> اثممح
[✓] Converted: hello

>> none
```
## **Repository Structure**
Below is the full directory tree of the `Langshift` repository in the `wordswitch-langscan` branch:

```
Langshift/
│
├── .gitattributes              # Configures Git LFS for arabic-wordlist-1.6.txt
├── README.md                   # Project documentation (this file)
├── arabic-wordlist-1.6.txt     # Arabic wordlist for validation (managed by Git LFS)
├── langshift.py                # Main CLI entry point
├── requirements.txt            # Python dependencies
│
└── core/                       # Core logic modules
    ├── analyzer.py             # Language detection and conversion orchestration
    ├── convert.py              # Keyboard layout conversion logic
    ├── lang_scan.py            # Language detection and sentence analysis
    ├── maps.py                 # Keyboard layout mappings
    └── wordlist.py             # Wordlist loading and management
```    
### File Descriptions
- **`.gitattributes:`**

Configures Git LFS to manage the `arabic-wordlist-1.6.txt` file. It ensures the large text file is handled efficiently with Git Large File Storage.
Contents:

```
arabic-wordlist-1.6.txt filter=lfs diff=lfs merge=lfs -text
```
- **`arabic-wordlist-1.6.txt`**

A text file containing a list of Arabic words, one per line. Used by the tool to check if Arabic sentences are meaningful. Managed with Git LFS due to its size.

- **`langshift.py`**

The main entry point for the CLI tool. It:
1. Loads the Arabic wordlist.
2. Prompts the user for input.
3. Calls the core.analyzer module to detect language and meaning, and converts text if needed.
4. Runs an infinite loop until the user types none.


- **`requirements.txt`**


Lists the Python dependencies required to run the project. Currently includes:
```
nltk==3.8.1
```

- **`core/analyzer.py`**

Orchestrates high-level functionality:

`detect_and_check():` Detects the language (Arabic or English) and checks if the sentence is meaningful using the appropriate wordlist.

`convert_and_retry():` Converts the sentence to the opposite keyboard layout and rechecks for meaning.

- **`core/convert.py`**

Handles keyboard layout conversion:

`convert_keyboard_layout():` Takes a string and a mapping (e.g., Arabic-to-English) and converts each character accordingly, preserving case sensitivity.

- **`core/lang_scan.py`**

Provides language detection and sentence analysis utilities:

`get_script():` Identifies the language based on Unicode ranges (Arabic: 0x0600–0x08FF, English otherwise).

`sentence_has_meaning():` Checks if a sentence has a high ratio of recognized words (threshold: 70%) using fuzzy matching via `difflib`.

Helper functions: `clean_word()`, `get_words_in_sentence()`, `is_word_recognized()`.

- **`core/maps.py`**

Defines keyboard layout mappings:

`arabic_to_english:` A dictionary mapping Arabic characters to their English keyboard equivalents (e.g., `ض` → `q`).

`english_to_arabic:` The reverse mapping, generated dynamically.

- **`core/wordlist.py`**

Manages wordlist loading:
`WordListLoader` class: Loads English words from NLTK’s `words` corpus and Arabic words from `arabic-wordlist-1.6.txt`.

`Handles errors` (e.g., missing Arabic wordlist file) gracefully.

## **How It Works**

1. **Input**: User types a sentence into the CLI.

2. **Detection**: The tool identifies the language (Arabic or English) using Unicode ranges.

3. **Validation**: It checks if the sentence contains enough recognized words from the corresponding wordlist (Arabic or English).

4. **Conversion**: If the sentence isn’t meaningful, it converts the text to the opposite keyboard layout and rechecks.
5. **Output**: Displays the valid input or the corrected version.

## **Contributing**
Feel free to fork this repository, submit issues, or create pull requests. To contribute:

1. Fork the repo.

2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).

4. Push to your branch (`git push origin feature/your-feature`).

5. Open a pull request.

## **Contact**
For questions or feedback, reach out to [nawafibrahim666@gmail.com](mailto:nawafibrahim666@gmail.com) or open an issue at [https://github.com/nawaf-ibrahim6/Langshift](https://github.com/nawaf-ibrahim6/Langshift).