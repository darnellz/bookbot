
from stats import word_count, character_count, sorted_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv.pop()
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_count = character_count(text)
    sorted_char = sorted_dict(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    for char in sorted_char:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
    return

def get_book_text(Filepath):
    with open(Filepath) as f:
        return f.read()

main()
 