# 5. The Unix spell command is a simple spell-checker. It prints out all the words in a
# text file that are not found in a dictionary. Write and test an implementation of this,
# that takes a file name as a command-line argument.
# Note: You may want to simplify the program at first by testing with a text file that
# does not contain any punctuation. A complete version should obviously be able to
# handle normal files, with punctuation.

import os, sys

# The filepath Of dictionary. Change if you want to use Another file as dictionary wordlist.
dictionaryFile = "/usr/share/dict/words"

# check whether dictionaryFile exist or not
if not os.path.exists(dictionaryFile):
    print(f"Dictionary file {dictionaryFile} does not exist")
    print(f"This path is in linux only, please run this code on linux machine")
    sys.exit(1)



def checkSpelling(misspellWord):
    with open(dictionaryFile) as file:
        fileLines = [line.strip().lower() for line in file]
        return misspellWord.lower() in fileLines


def flatten_and_concatenate(lst):
    # Flatten the list and convert all elements to strings
    flattened = [' '.join(item) if isinstance(item, list) else str(item) for item in lst]
    # Join the flattened elements into a single string
    return ' '.join(flattened)


if len(sys.argv) > 1:
    fileName = sys.argv[1:][0]
    try:
        with open(fileName, "r") as file:
            lines = file.readlines()
            for words in lines:
                lineSplit = words.split()
                dictLines = []
                for linesplitWord in lineSplit:
                    if not checkSpelling(linesplitWord.replace(".", "")):
                        dictLines.append([f"\033[31m{linesplitWord}\033[0m"])
                    else:
                        dictLines.append(linesplitWord)
                result = flatten_and_concatenate(dictLines)
                print(result)
    except FileNotFoundError:
        print(f"The file {fileName} doesnot exist")
else:
    print("No input Provided !")
    print("Usage: python 5.py <Filename>")