"""
List Comprehensions
Readable, expressive, and effective.
"""
from math import factorial, sqrt
from pprint import pprint as pp


def is_prime(num):
    """
    Determine if the number is prime
    :param num: number to test
    :return: True for prime numbers
            False for non-prime numbers
    """
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def main():
    """
    Test function
    :return:
    """
    words = "Today I am very happy to learn about list comprehensions".split()
    # print(words)
    data = []   # empty list
    for word in words:
        # Some analysis ...
        data.append(word)
    # "Filter" data
    print(data)

    # Task: Find the length of the first 20
    # Factorial numbers
    info = [] # empty list
    for x in range(20):
        # print(factorial(x))
        info.append(len(str(factorial(x))))
    # Print info
    pp(info)
    # Use a list comprehension: [ ]
    info2 = [len(str(factorial(x))) for x in range(200)]
    pp(info2)

    # Set Comprehensions: { }
    info3 = {len(str(factorial(x))) for x in range(200)}
    pp(info3)

    # Dictionary Comprehensions
    nba_teams = {'jazz':'SLC', 'warriors':'OAKLAND', 'lakers':'LA', 'clippers':'LA'}
    pp(nba_teams)
    teams_nba = {city:mascot for mascot, city in nba_teams.items()}
    pp(teams_nba)

    # Filter predicates
    primes = [x for x in range(10001) if is_prime(x)]
    print(len(primes), primes)



if __name__ == '__main__':
    main()
    exit(0)