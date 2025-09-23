def get_book_words(book_content):
    words = book_content.split()
    return len(words)

def get_book_characters(book_content):
    char_count = {}
    for char in book_content.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
#     Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
#     Use the .sort() method:
#     Use a helper function to return the "num" key of each dictionary for comparison.
#     Sort the list from greatest to least by the count.
def sort_on(items):
    return items["num"]

def sort_characters_by_count(char_count):
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(key=sort_on, reverse=True)
    return char_list
