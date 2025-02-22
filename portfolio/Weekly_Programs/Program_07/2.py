# Write and test three functions that each take two words (strings) as parameters and
# return sorted lists (as defined above) representing respectively:
# Letters that appear in at least one of the two words.
# Letters that appear in both words.
# Letters that appear in either word, but not in both.
# Hint: These could all be done programmatically, but consider carefully what topic we
# have been discussing this week! Each function can be exactly one line

# Union
unionFunction = lambda value1, value2:list(set(value1) | set(value2))

# Intersection
intersectionFunction = lambda value1, value2:list(set(value1) & set(value2))

# Symmetric Difference
symmetricDifferenceFunction = lambda value1, value2:list(set(value1) ^ set(value2))

print("Letters that appear in at least one of the two words  = ",unionFunction("abcde", "aeiou"))
print("Letters that appear in both words \t\t\t\b\b= ",intersectionFunction("abcde", "aeiou"))
print("Letters that appear in either word, but not in both \t\b\b\b = ",symmetricDifferenceFunction("abcde", "aeiou"))