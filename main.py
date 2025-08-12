def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

from stats import get_book_word_count
from stats import get_characters
from stats import sort_list

def main():
    #print(get_book_text("books/frankenstein.txt"))
    print(f"{get_book_word_count("books/frankenstein.txt")} words found in the document")
    print(sort_list(get_characters("books/frankenstein.txt")))

main()