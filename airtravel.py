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