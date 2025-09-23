from stats import get_book_words
from stats import get_book_characters
from stats import sort_characters_by_count

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    filepath = 'books/frankenstein.txt'
    book_text = get_book_text(filepath)
    num_words = get_book_words(book_text)
    char_count_dict = get_book_characters(book_text)
    print_report(filepath, num_words, char_count_dict)

def print_report(filepath, num_words, char_count_dict):
    print(f"{num_words} words found in the document")  
    print(char_count_dict) 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sort_characters_by_count(char_count_dict):
        if not entry['char'].isalpha():  # Only print alphabetic characters
            continue
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()