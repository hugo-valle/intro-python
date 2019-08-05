"""
Learn dictionaries
Dictionaries maps keys to values.
In some languages are knows as associative arrays, or hashes, maps

Create them using { } containing a key-value pair.
Retrieve them by [key_value]
"""
d = {'alice': '801-123-45-8988',
     'pedro': '956-445-78-8966',
     'john': '651-321-66-4477'}
print(d, type(d))
# Access one element
print(d['pedro'])

# Add members to the dictionary, of names-> grades
roster = {}    # Empty dictionary
total = 0
while total < 3:
    # Get key value
    name = input("Enter a player's name")
    # Get value associated to key
    score = input("Enter score")
    # Add element to dictionary.
    # Note: If key value exist, it will update the value
    #       otherwise it wil be add it to the dict.
    roster[name] = score
    total += 1
# Print dictionary
print(roster)