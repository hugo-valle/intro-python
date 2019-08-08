"""
Use flight class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def make_flight():
    flight = Flight("SN066",
                Aircraft("G-EUP",
                         "Airbus A319",
                         num_rows=22,
                         num_seats_per_row=6))
    # pp(flight._seating)
    flight.allocate_seat("02A", "Guido Van Rossum")  # python
    flight.allocate_seat("12B", "Rasmus Lerdorf")   # php
    flight.allocate_seat("15F", "Bjare Stroustrup")  #C++
    flight.allocate_seat("03A", "Larry Wall") # perl
    flight.allocate_seat("16F", "Yukihiro Matsumoto") # ruby
    return flight


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}"  \
            " Flight: {1} " \
            " Seat: {2}"    \
            " Aircraft: {3}" \
            " |".format(passenger, flight_number,
                        seat, aircraft)
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


def main():
    """
    Test function
    :return:
    """
    flight_1 = make_flight()
    pp(flight_1._seating)
    print("Available seats",
          flight_1.num_available_seats())
    flight_1.make_boarding_class(
        console_card_printer)



if __name__ == '__main__':
    main()
    exit(0)