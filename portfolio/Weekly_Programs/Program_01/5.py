# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "le over"
# group.


noOfStudentPerGroup = 24
group1 = 113//noOfStudentPerGroup
group1leftOver = 113%noOfStudentPerGroup
group2 = 175//noOfStudentPerGroup
group2leftOver = 175%noOfStudentPerGroup
group3 = 120//noOfStudentPerGroup
group3leftOver = 120%noOfStudentPerGroup

print("There will be total ", (group1+group2+group3), "Group.")
print("There will be ", (group1leftOver+group2leftOver+group3leftOver), "Student left over.")