# Write and test a function that takes an integer as its parameter and returns the
# factors of that integer. (A factor is an integer which can be multiplied by another to
# yield the original).



import sys

def myFunction(value):
    outputValue = []
    for i in range(1, value+1):
        if value % i == 0:
            outputValue.append(i)
    return outputValue


if len(sys.argv) > 1:
    value = abs(int(sys.argv[1:][0]))
    if value > 99999999:
        print("The Number is extremely Large. The Program may take longer to return !")
    else:
        print(f"The factor of {value} : {myFunction(value)}")
else:
    print("No input Provided !")