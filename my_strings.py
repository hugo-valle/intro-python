"""
Learn more about strings
"""


def main():
    """
    Test function
    :return:
    """
    s1 = "This is super cool"
    print("Size of s1", len(s1))
    # Concatenation "+"
    s2 = "Weber" + "State" + "University"
    print(s2)
    # If you need to join large strings, use the join() method
    # Instead of + operator
    teams = ["Real Madrid", "Barcelona", "Manchester United"]
    record = ":".join(teams)
    print(record)
    # record = "\n".join(teams)
    # print(record)
    # Split record
    print("Split rec", record.split(":"))
    # Partitioning Strings
    # You can use the "dummy" object: _
    departure, _, arrival = "London:Edinburgh".partition(":")
    print(departure, arrival)
    t = "London:Edinburgh".partition(":")
    print(t, type(t))
    # String formatting using format()
    print("The age of {0} is {1}".format("Mario", 34))
    print("The age of {0} is {1}, and the birthday of {0} is {2}".format(
        "Mario", 34, "August 12th"))
    # Omitting the index
    print('The best numbers are {} and {}'.format(4, 22))
    # By field name
    print("Current position {latitude} {longitude}".format(
        latitude="60 N", longitude="5E" ))
    # print elements of list
    print("Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(
        pos=(85.6, 23.3, 99.0) ))
    # Second version of "format": print(f"{var}") python 3.7 or greater
    # fname = "Waldo"
    # lname = "Weber"
    # print(f"The WSU mascot is {fname} {lname}")



if __name__ == '__main__':
    main()
    exit(0)