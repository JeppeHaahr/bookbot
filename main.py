from stats import get_book_word_count
from stats import get_characters
from stats import sort_list
import sys

def main():
    if len(sys.argv) == 2:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {get_book_word_count(sys.argv[1])} total words")
        print("--------- Character Count -------")
        for chara in sort_list(get_characters(sys.argv[1])):
            print(f"{chara["char"]}: {chara["num"]}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()