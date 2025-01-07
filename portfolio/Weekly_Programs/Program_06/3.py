# Write and test a function that determines if a given integer is a prime number. A
# prime number is an integer greater than 1 that cannot be produced by multiplying
# two other integers.



import sys

def myFunction(value):
    truthSample = []
    for i in range(1,value+1):
        global divValue
        divValue = value / i
        if int(str(divValue).split(".")[1]) == 0:
            truthSample.append("true")

    if len(truthSample) == 2:
        return True

if len(sys.argv) > 1:
    value = abs(int(sys.argv[1:][0]))
    if myFunction(value):
        print(f"The Number {value} is Prime Number !")
    else:
        print(f"The Number {value} is Not a Prime Number !")
else:
    print("No input Provided !")