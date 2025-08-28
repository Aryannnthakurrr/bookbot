import sys
from stats import get_num_words, get_character_counts, get_sorted_chars

def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)

    character_counts = get_character_counts(book_text)  

    sorted_characters = get_sorted_chars(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()