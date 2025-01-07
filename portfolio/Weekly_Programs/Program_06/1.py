# Write a function that accepts a positive integer as a parameter and then returns a
# representation of that number in binary (base 2).
# Hint: This is in many ways a trick question. Think!

import sys

Inputvalue = int(sys.argv[1:][0])
initialValue = Inputvalue
binaryValue = []

def myFunction(value):
    binaryInt = ''
    while value >= 1:
        remainder = value % 2
        binaryValue.append(remainder)
        value = value // 2

    if len(binaryValue) <8:
        apValue = 8 - len(binaryValue)
        binaryValue.extend(("0"*apValue))

    binaryValue.reverse()

    for value in binaryValue:
        binaryInt = binaryInt + str(value)
    
    return binaryInt

print("The Binary Value of ", initialValue, " : " ,myFunction(Inputvalue))