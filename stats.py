def count_words(book_contents):
    book_words = book_contents.split()
    word_count = len(book_words)
    return word_count
def count_characters(book_contents):
    counts = {}
    lower_case = book_contents.lower()
    for char in lower_case:
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts[char] = 1
    return counts
