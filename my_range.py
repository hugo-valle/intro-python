"""
Learn about range() Collection
"""


def main():
    """
    Test function
    :return:
    """
    # Default
    for i in range(5):
        print(i)

    # Set the initial value: =5 to <10
    print("Now setting initial value")
    for i in range(5, 10):
        print(i)

    # Create a list from range
    l = list(range(5, 10))
    print(l, type(l))
    l2 = list(range(5, 10)) + list(range(30,40))
    print(l2, type(l2))
    # Step argument: (begin, stop, step)
    l3 = list(range(0, 20, 2))
    print(l3, type(l3))
    # Iteration over list using index notation
    s = [0, 2, 3, 4, 6]
    for i in range(len(s)):
        print(s[i])
    # Better way
    for v in s:
        print(v)

    # enumerate(): returns an iterable series
    t = [6, 789, 123, 98, 3, 22]
    for p in enumerate(t):
        print(p, p[0], p[1])
    # A better
    for i, v in enumerate(t):
        print("i = {}, v={}".format(i, v))



if __name__ == '__main__':
    main()
    exit(0)