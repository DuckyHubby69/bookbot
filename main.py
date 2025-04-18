def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents
def main():
    book_contents = get_book_text("books/frankenstein.txt")
    print(book_contents)
main()
