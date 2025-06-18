def main()
    while True
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5 Exit")

        choice = input("Enter your choice: ")

        if choice == 1:
            a = int(input("Enter first number: ")
            b = int(input("Enter second number: "))
            print("Sum is: ", a + b)

        elif choice = 2:
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print("Difference is: " + a - b)

        elif choice == "3"
            a = float(input("Enter first number"))
            b = float(input("Enter second number"))
            print("Product is: ", a * b

        elif choice == 4:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            if b == 0
                print("Cannot divide by zero")
            else:
                print("Quotient is: ", a // b)

        elif choice == '5':
            break
        else
            print("Invalid choice, try again!"

main()
