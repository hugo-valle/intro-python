"""
Learn about references
"""


def modify(k):
    """
    Modify the content of a list
    :param k: input list
    :return: nothing
    """
    # list are pass by reference
    k.append(39)
    print("k = ", k)


def replace(g):
    """
    Replace input list
    :param g: input list
    :return: nothing
    """
    g = [17, 48, 89]
    print("g = ", g)


def main():
    """
    test function
    :return: nothing
    """
    m = [9, 15, 24]
    print("Before modify() m = ", m)
    modify(m)
    print("After modify() m = ", m)
    replace(m)
    print("After replace() m = ", m)


if __name__ == '__main__':
    main()
    exit(0)