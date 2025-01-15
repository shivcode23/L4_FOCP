def calculator(number1, number2, operation):
    if operation == 1:
        return number1 + number2
    elif operation == 2:
        return number1 - number2
    elif operation == 3:
        return number1 * number2
    elif operation == 4:
        if number2 == 0:
            return "Division by zero not allowed."
        else:
            return number1 / number2
    elif operation == 5:
        if number2 == 0:
            return "Modulo Division by zero not allowed."
        else:
            return number1 % number2
    else:
        return "No operation Performed."

def main():
    while True:
        print("1. Enter 1 For Sum :\n2. Enter 2 For Subtraction :\n3. Enter 3 For Multiplication:\n4. Enter 4 For Division :\n5. Enter 5 For Reminder :")
        number1 = float(input("Enter the First Number : "))
        number2 = float(input("Enter the Second Number : "))
        operation = int(input("Enter the Operation Number : "))
        ans = calculator(number1, number2, operation)
        print(ans)
        redo = input("Calculate Again ? : yes/no : ").lower()
        if redo != "yes":
            break

if __name__ == "__main__":
    main()