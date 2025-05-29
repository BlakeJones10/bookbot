import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import get_word_count, get_character_count, sort_on


def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
    return book_text


def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    words = get_word_count(book_text)
    characters = get_character_count(book_text)
    sorted_characters = sort_on(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_characters:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


main()
