"""
Learn about list()
"""


def main():
    """
    Test function
    :return:
    """
    s = "show how to do it".split()
    print(s, type(s))
    # Access by index
    print("s[3]:", s[3])
    print("last member:", s[len(s) - 1])  # very unpythonic
    # Use negative index
    print("s[-1]:", s[-1])
    # Slicing
    print(s)
    print("From 1 to one before the last member", s[1:-1])
    print("From 1 to three members", s[1:3])
    print("From 1 to the end", s[1:])
    print("From beg to the 3", s[:3])
    print("From beg to the end", s[:])
    # Make a copy of list
    t = s   # shallow copy
    print("s:", s)
    print("t:", t)
    print("t is s:", t is s)
    t = s[:] # deep copy
    # or this: t = s.copy()
    # or this: t = list(s)
    print("t is s:", t is s)
    print("t == s:", t == s)
    # Shallow copies
    # A list of list
    a = [[1, 2], [3, 4]]
    print(a, type(a))
    print("a[0]:", a[0])
    print("a[0][1]:", a[0][1])
    print("a[1][1]:", a[1][1])
    # Copy the list of list
    b = a[:]
    print("b is a", b is a)
    print("a[0]:", a[0])
    print("b[0]:", b[0])
    print("a[0] is b[0]", a[0] is b[0])
    # Let's change one element
    a[0] = [8, 9]
    print("Change a[0] to [8,9]")
    print("a[0]:", a[0])
    print("b[0]:", b[0])
    print("a[0] is b[0]", a[0] is b[0])
    print("a[1] is b[1]", a[1] is b[1])
    # modify a[1]
    a[1].append(5)
    print("a[1]:", a[1])
    print("b[1]:", b[1])
    print("a[1] is b[1]", a[1] is b[1])
    print("a:", a)
    print("b:", b)
    # Repetition
    c = [21, 37]
    d = c * 4
    print("c", c)
    print("d", d)
    # All point to the same object
    s = [[-1, 1]] * 5
    print(s)
    s[1].append(7)
    print(s)
    # index()
    w = "the quick brown fox jumps over the lazy dog".split()
    i = w.index('fox')
    print("The index of 'fox' entry is:", i, w[i])
    # If no index is found, it will throw a ValueError
    # i = w.index('cat')
    # print("The index of 'cat' entry is:", i, w[i])
    # Membership testing with: count()
    print("'the' value is ", w.count("the"))
    # Also test membership with: in, not in
    print(37 in [12, 22, 37, 99])
    print(78 not in [12, 22, 37, 99])
    # Removing elements from list: index and del
    w = "the quick brown fox jumps over the lazy dog".split()
    print(len(w), w)
    del w[3]        # delete using index
    print(len(w), w)
    # remove using: remove()
    w.remove("over")
    print(len(w), w)
    # same as
    del w[w.index('dog')]
    print(len(w), w)
    # Rearranging list of elements
    g = [1, 11, 21, 1211, 112111]
    print("g:", g)
    g.reverse()  # permanent change in order
    print("reverse g:", g)
    g.reverse()  # permanent change in order
    print("reverse again g:", g)

    # Sort method accepts two arguments:
    # key and reverse
    d = [21, 33, 11, 77, 88, 33, 101, 1]
    print("d:     ", d)
    d.sort()
    print("sort d:", d)
    d = [21, 33, 11, 77, 88, 33, 101, 1]
    d.sort(reverse=True)
    print("sort.reverse d:", d)
    # sort by key
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    w.sort(key=len)
    print(w)




if __name__ == '__main__':
    main()
    exit(0)