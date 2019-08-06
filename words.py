"""
Get a file from the web:
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: Count number of words in document
"""
from urllib.request import urlopen


def fetch_words(filename):
    """
    Count words in url file
    :param filename: url to file
    :return: a list with the items
    """
    count = 0
    data = []       # empty list
    with urlopen(filename) as story:
        for line in story:
            words = line.decode('utf-8').split()  # split with space as separator
            # print(words)
            for word in words:
                data.append(word)
    return data


def print_items(items):
    """
    Print elements of the collection
    :param items: A collections of objects
    :return: nothing
    """
    for item in items:
        print(item)


def main():
    """
    Test function for words library
    :return: nothing
    """
    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    words = fetch_words(file)
    print_items(words)


if __name__ == '__main__':
    main()
    exit(0)
