# Write and test a function that takes a string as a parameter and returns a sorted list
# of all the unique letters used in the string. So, if the string is cheese, the list
# returned should be ['c', 'e', 'h', 's'].


def myFunction(value):
    valueSet = set(value)
    return list(valueSet)

print(myFunction("cheese"))