from stats import get_num_words
from stats import get_character_count
from stats import get_list_of_chars

import sys
def get_book_text(path: str):
    with open(path) as f:
        file_content = f.read()
        return file_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    num_words = get_num_words(content)
    num_chars = get_character_count(content) 
    char_list = get_list_of_chars(num_chars)

    print("============ BOOKBOT ============\n" +
        "Analyzing book found at books/frankenstein.txt...\n"
        "----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(len(char_list)):
        if char_list[i][0].isalpha():
            print(f"{char_list[i][0]}: {char_list[i][1]}")
main()


