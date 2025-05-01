import sys
from stats import count_words
from stats import count_characters
from stats import sorted_list
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents
def main():
    #Check if argument was passed by user
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    book_word_count = count_words(book_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    book_character_counts = count_characters(book_contents)
    sorted_chars = sorted_list(book_character_counts)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()
