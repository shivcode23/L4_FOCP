# A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have le over.


totalSweet = int(input("How many sweets in Tub? "))
pupils = int(input("Number of pupils? "))
distribute = totalSweet // pupils
left = totalSweet % pupils

print("Number of sweet to give to each pupil = ", distribute)
print("Number of Sweet left = ", left)