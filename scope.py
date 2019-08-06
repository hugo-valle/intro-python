"""
Learn about scoping in Python
"""
count = 0    # global object


def show_count():
    """
    Display the current count
    :return: nothing
    """
    print(count)


def set_count(num):
    """
    Set global counter to input
    :param num: input number
    :return: nothing
    """
    global count
    count = num


def main():
    """
    Test function
    :return:
    """
    show_count()
    set_count(9)
    show_count()


if __name__ == '__main__':
    main()
    exit(0)