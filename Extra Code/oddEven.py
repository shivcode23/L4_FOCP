print("Simple Odd / Even Finder for Positive Integer")
number = input("Enter the Number : ")

odd = [1, 3, 5, 7, 9]

def checkEvenOdd(number):
    try:
        if not number.isdigit():
            return "Not an integer"
        else:
            if int(number[-1:]) in odd:
                return "Odd Number"
            else:
                return("Even Number")
    except Exception as e:
        return e

def main():
    print(checkEvenOdd(number))


if __name__ == "__main__":
    main()