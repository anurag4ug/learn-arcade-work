import re


def split_line(line):
    """Split a line of text into words."""
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def read_dictionary(file_name):
    """Read dictionary words from a file."""
    with open(file_name) as file:
        dictionary_list = [line.strip() for line in file]
    return dictionary_list


def search_words_in_file(dictionary_list, file_name, search_algorithm):
    """Search for words in a file using the given search algorithm."""
    with open(file_name) as file:
        for index, line in enumerate(file, start=1):
            line = line.strip()
            word_list = split_line(line)
            for word in word_list:
                search_algorithm(dictionary_list, word.upper(), index)


def linear_search(name_list, key, index):
    """Perform linear search for a key in a list."""
    current_list_position = 0
    while current_list_position < len(name_list) and name_list[current_list_position] != key:
        current_list_position += 1
    if current_list_position >= len(name_list):
        print(f"Linear Search - Line {index} not found: {key}")


def binary_search(name_list, key, index):
    """Perform binary search for a key in a sorted list."""
    lower_bound = 0
    upper_bound = len(name_list) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2
        if name_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif name_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    if not found:
        print(f"Binary Search - Line {index} not found: {key}")


def main():
    dictionary_list = read_dictionary("dictionary.txt")
    search_words_in_file(dictionary_list, "AliceInWonderland200.txt", linear_search)
    search_words_in_file(dictionary_list, "AliceInWonderland200.txt", binary_search)


if __name__ == "__main__":
    main()
