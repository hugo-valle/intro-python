"""
File learn about collection: Tuples, Strings, Range, List, Dictionaries, Sets
"""


def do_tuples():
    """
    Practice tuples
    :return: nothing
    """
    # Immutable sequence of arbitrary objects
    # Use () to define a tuple
    t = ("Ogden", 1.99, 2)
    print(t, type(t))
    print("Size ", len(t))
    print("One member:", t[0])   # by index notation
    # To iterate over a tuple
    for item in t:
        print(item)

    # Single tuples, must end with comma
    t1 = (6,)
    print(t1, type(t1))
    # Another way to create tuples
    # Parenthesis are optional
    t2 = 1, 2, 3, 5
    print(t2, type(t2))


def min_max(items):
    """
    Return the minimum and maximum elements of a collection
    :param items: collection
    :return: the minimum and maximum
    """
    return min(items), max(items)


def swap(obj1, obj2):
    """
    Swap value of the objects
    :param obj1: first
    :param obj2: second
    :return: values swapped
    """
    return obj2, obj1


def main():
    """
    Test function
    :return:
    """
    # do_tuples()
    output = min_max([56, 76, 11, 12, 90])
    print("min", output[0])
    print("max", output[1])
    # Tuple unpacking
    lower, upper = min_max([56, 76, 11, 12, 90])
    print("min", lower)
    print("max", upper)

    # Swap values
    a = "jelly"
    b = "bean"
    print(a, b)
    # Call your function
    a, b = swap(a, b)
    print(a, b)
    a, b = b, a
    print(a, b)


if __name__ == '__main__':
    main()
    exit(0)