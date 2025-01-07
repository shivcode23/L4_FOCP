# Another way to hide a message is to include the letters that make it up within
# seemingly random text. The letters of the message might be every fih character,
# for example. Write and test a function that does such encryption. It should
# randomly generate an interval (between 2 and 20), space the message out
# accordingly, and should fill the gaps with random letters. The function should
# return the encrypted message and the interval used.
# For example, if the message is "send cheese", the random interval is 2, and for
# clarity the random letters are not random:
# send cheese
# s e n d c h e e s e
# sxyexynxydxy cxyhxyexyexysxye



import sys, random

def encryptMessage(value):
    alphaValue = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encryptedValue = ""

    randomValue = random.randint(2, 20)
    randomChar = ''.join(random.choices(alphaValue, k=randomValue))

    for char in value:
        encryptedValue += char + randomChar

    return encryptedValue


if len(sys.argv) > 1:
    actionValue = ""
    values = sys.argv[1:]
    for value in values:
        actionValue+=value
    print(f"The Encrypted message of {value} is {encryptMessage(actionValue)}")
else:
    print("No input Provided !")