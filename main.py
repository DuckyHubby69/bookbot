from stats import count_words
from stats import count_characters
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents
def main():
    book_contents = get_book_text("books/frankenstein.txt")
    book_word_count = count_words(book_contents)
    print(f"{book_word_count} words found in the document")
    book_character_counts = count_characters(book_contents)
    for char, count in book_character_counts.items():
        print(f"'{char}': {count}")
main()
