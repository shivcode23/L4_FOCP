def calculate():
    while True:
        operation = input("Enter the mathematical operation : ")
        print(eval(operation))
        consent = input("Do you want to continue ? : ").lower()
        if consent != "yes":
            break

if __name__ == "__main__":
    calculate()