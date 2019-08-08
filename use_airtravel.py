"""
Use flight class
"""
from airtravel import Flight


def main():
    """
    Test function
    :return:
    """
    f1 = Flight("SN066")
    print(f1.number(), f1.airline())
    # f2 = Flight("ab345")
    f2 = Flight("AB352")
    print(f2.number(), f2.airline())
    # Could use: Flight.number(f)


if __name__ == '__main__':
    main()
    exit(0)