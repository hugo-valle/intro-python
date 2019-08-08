"""
An Flight Class. Model for aircraft flights
"""


class Flight:
    """
    A Flight with a particular passenger aircraft
    """
    def __init__(self, number, aircraft):
        if len(number) != 5:
            raise ValueError("Invalid flight number length {}" .format(number))
        if not number[:2].isalpha():
            raise ValueError("No airline code {}" .format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}" .format(number))
        if not number[2:].isdigit():
            raise ValueError("Invalid route code {}" .format(number))

        self._number = number # implementation details begin with '_'
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + \
                        [{letter:None for letter in seats} for _ in rows]

    def number(self):
        return self._number[2:]

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        """
        Allocate a seat to a passenger
        :param seat: A seat designator such as '12C', '21F'
        :param passenger: The passenger name
        :return:
        """
        rows, seat_letter = self._aircraft.seating_plan()

        letter = seat[-1]   # take the letter from the seat
        if letter not in seat_letter:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row{}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number{}".format(row))

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))
        # Assign the seat
        self._seating[row][letter] = passenger

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_class(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(),
                         self._aircraft.model())

    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))


class Aircraft:

    def __init__(self, registration, model,
                 num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row


    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return(range(1, self._num_rows + 1),
               "ABCDEFGHJK"[:self._num_seats_per_row])



def main():
    """
    Test function
    :return:
    """
    pass


if __name__ == '__main__':
    main()
    exit(0)