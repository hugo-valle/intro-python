"""
An Flight Class. Model for aircraft flights
"""


class Flight:
    """
    A Flight with a particular passenger aircraft
    """
    def __init__(self, number):
        if len(number) != 5:
            raise ValueError("Invalid flight number length {}" .format(number))
        if not number[:2].isalpha():
            raise ValueError("No airline code {}" .format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}" .format(number))
        if not number[2:].isdigit():
            raise ValueError("Invalid route code {}" .format(number))
        self._number = number # implementation details begin with '_'

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


def main():
    """
    Test function
    :return:
    """
    pass


if __name__ == '__main__':
    main()
    exit(0)