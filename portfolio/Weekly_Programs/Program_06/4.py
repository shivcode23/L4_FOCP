# Computers are commonly used in encryption. A very simple form of encryption
# (more accurately "obfuscation") would be to remove the spaces from a message
# and reverse the resulting string. Write, and test, a function that takes a string
# containing a message and "encrypts" it in this way.

import sys

def myFunction(value):
    newValue = value.replace(" ", "")
    listValue = []
    for char in newValue:
        listValue.append(char)
    listValue.reverse()
    return ''.join(listValue)


if len(sys.argv) > 1:
    actionValue = ""
    values = sys.argv[1:]
    for value in values:
        actionValue+=value

    print(f"The Encrypted message of {value} is {myFunction(actionValue)}")
else:
    print("No input Provided !")