def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()
def get_book_words(book_content):
    words = book_content.split()
    return len(words)

def main():
    filepath = 'books/frankenstein.txt'
    book_text = get_book_text(filepath)
    num_words = get_book_words(book_text)
    print(f"{num_words} words found in the document")    

main()