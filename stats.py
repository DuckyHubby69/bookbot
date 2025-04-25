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
def sorted_list(book_character_counts):
    char_counts_list = []
    for char, count in book_character_counts.items():
        char_dict = {"char": char, "num": count}
        char_counts_list.append(char_dict)
    char_counts_list.sort(reverse=True, key=lambda dict: dict["num"])
    return char_counts_list
