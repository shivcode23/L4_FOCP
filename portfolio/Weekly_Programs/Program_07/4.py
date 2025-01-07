# One approach to analysing some encrypted data where a substitution is suspected
# is frequency analysis. A count of the dierent symbols in the message can be used
# to identify the language used, and sometimes some of the letters. In English, the
# most common letter is "e", and so the symbol representing "e" should appear most
# in the encrypted text.
# Write a program that processes a string representing a message and reports the six
# most common letters, along with the number of times they appear. Case should
# not matter, so "E" and "e" are considered the same.
# Hint: There are many ways to do this. It is obviously a dictionary, but we will want
# zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
# best to ignore that initially, and then check the usual resources for the runes.



letters = "dfadbufmfouiosjfjegmfbmavjdbkdvzjowpdfhvitseecwvztjqjyeinjnsfwbydnurvetbryjvxjxngpvtqqouckfxppdnqwoivurgzprlpwqsvqocoyxloihiuszf"
letters2 = letters.lower().replace(" ", "") #Makes every character lowercase and removes extra spaces
uniqueLetters2 = set(letters2)
countList = dict({char:letters2.count(char) for char in uniqueLetters2 if letters2.count(char) > 1})

# The reaseon valueSet is dict is because it will hold unique counts.
valueSet = set()
for keys, value in countList.items():
    valueSet.add(value)

# Converted set into list
charRepitionList = list(valueSet)[-6:]
charRepitionList.reverse()


listItem = [list(), list(),list(),list(),list(), list()]

for i,listElement in enumerate(charRepitionList, 0):
    for key,value in countList.items():
        if value == listElement:listItem[i].append(key)

for value1, value2 in zip(listItem, charRepitionList):
    print(', '.join(value1), " Has Been Repeated ", value2, " Times !")