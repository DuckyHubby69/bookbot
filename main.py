from stats import count_words
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents
def main():
    book_contents = get_book_text("books/frankenstein.txt")
    book_word_count = count_words(book_contents)
    print(f"{book_word_count} words found in the document")
main()
