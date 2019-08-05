"""
Learn about lists
Unlike strings, lists are mutable.
You can update, and append elements to it
"""
# use [ ] de define a list
l = [1, 2, 3]
print("List ", l, type(l))
# A list of objects (any type)
a = ["apple", "orange", "pear"]
# Access by index notation
print(a, a[1])
# Replace an element
a[0] = "tomatoes"
print(a, a[1])
a[1] = 3.14
print(a, a[1])

# Begin with an empty list
names = []
# Ask user to enter 3 names, and add them to the list
total = 0
while total < 3:
    name = input("Enter a name")
    names.append(name)
    total = total + 1
# Display list
print(names)
