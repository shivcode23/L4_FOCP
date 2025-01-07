# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be le over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.


students = int(input("How many students? "))
groups = int(input("Required group size? "))
group = students // groups
left = students % groups

if group == 1 and left <= 1:
    print("There will be "+ str(group) +" group with "+ str(left) +" student left over.")
elif group == 1 and left > 1:
    print("There will be "+ str(group) +" group with "+ str(left) +" students left over.")
elif group > 1 and left <= 1:
    print("There will be "+ str(group) +" groups with "+ str(left) +" student left over.")
else:
    print("There will be "+ str(group) +" groups with "+str(left)+" students left over.")