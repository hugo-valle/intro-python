"""
Use flight class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def main():
    """
    Test function
    :return:
    """
    f1 = Flight("SN066",
                Aircraft("G-EUP",
                  "Airbus A319",
                  num_rows=22,
                  num_seats_per_row=6))
    # pp(f1._seating)
    f1.allocate_seat("02A", "Guido Van Rossum")  # python
    f1.allocate_seat("12B", "Rasmus Lerdorf")   # php
    f1.allocate_seat("15F", "Bjare Stroustrup")  #C++
    f1.allocate_seat("03A", "Larry Wall") # perl
    f1.allocate_seat("16F", "Yukihiro Matsumoto") # ruby
    pp(f1._seating)


if __name__ == '__main__':
    main()
    exit(0)