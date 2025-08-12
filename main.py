from stats import get_book_word_count
from stats import get_characters
from stats import sort_list

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_book_word_count("books/frankenstein.txt")} total words")
    print("--------- Character Count -------")
    for chara in sort_list(get_characters("books/frankenstein.txt")):
        print(f"{chara["char"]}: {chara["num"]}")
    #print(sort_list(get_characters("books/frankenstein.txt")))

main()