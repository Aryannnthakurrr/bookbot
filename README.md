# BookBot

BookBot is a command-line Python application that analyzes books for word count and character (alphabet) occurrences. It helps you quickly understand the textual makeup of any book in plain text format.

## Features
- **Word Count:** Calculates the total number of words in a book.
- **Character Analysis:** Counts the occurrences of each alphabet character (case-insensitive).
- **Sorted Output:** Displays character counts sorted by frequency.

## How It Works
BookBot reads a text file containing a book, analyzes its contents, and prints a summary including word count and the frequency of each alphabet character.

## Usage
```bash
python3 main.py <path_to_book>
```

### Example
```bash
python3 main.py books/frankenstein.txt
```

## Output
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 78345 total words
--------- Character Count -------
e: 12000
t: 9500
... (other characters)
```

## Requirements
- Python 3.x

## Project Structure
- `main.py` — Entry point for the CLI application
- `stats.py` — Functions for word and character analysis
- `books/` — Sample books in plain text format

## License
This project is for educational purposes.

---
BookBot is my first [Boot.dev](https://www.boot.dev) project!

