"""
Module for demonstration  the use generator execution
"""


def take(count, iterable):
    """
    Take items from the front of an iterable
    :param count: The maximum number of items to retrieve
    :param iterable: The source series
    :yields: At most 'count' items for 'iterable'
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    """
    Test the take() function
    """
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def distinct(iterable):
    """
    Return unique items by eliminating duplicates
    :param iterable: The source series
    :yields: Unique elements in order from 'iterable'
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)


def main():
    # run_take()
    # run_distinct()
    run_pipeline()


if __name__ == '__main__':
    main()
    exit(0)