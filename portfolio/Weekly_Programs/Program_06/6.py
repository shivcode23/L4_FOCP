# Write a program that decrypts messages encoded as above

import sys

def decryptMessage(value1):
    
    staticChar = ""
    secretLengthMessage = []

    for i in range(int(len(value1)/2)):
        staticChar+=value1[1:][i]
        value2 = value1[1:].replace(staticChar, "")
        listValue = (staticChar,len(value2), value2)
        secretLengthMessage.append(listValue)

    smallestValueList = []
    for item in secretLengthMessage:
        smallestValueList.append(item[1])

    # print(min(smallestValueList))
    for item in secretLengthMessage:
        if item[1] == min(smallestValueList):
            secretValue = [item[0], item[1], value1[0]+item[2]]
            return secretValue



if len(sys.argv) > 1:
    actionValue = ""
    values = sys.argv[1:]
    for value in values:
        actionValue+=value
    print("length of original Value :",len(actionValue))
    decryptedMessage = decryptMessage(actionValue)
    print(f"The Decrypted message : \n Secret :{decryptedMessage[0]}\n Message : {decryptedMessage[2]}")
else:
    print("No input Provided !")