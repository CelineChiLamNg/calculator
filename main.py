from calculator import Calculator

if __name__ == '__main__':

    calc = Calculator()

    # ask user to pick number to start with
    calc.memory = float(input("What number do you want to start with?\n"))

    # calculator loop
    while True:
        # ask user to pick an operation
        operation = int(input("Please pick one of the following operations 1/2/3/4/5:"
                              "\n1. Addition"
                              "\n2. Subtraction"
                              "\n3. Multiplication"
                              "\n4. Division"
                              "\n5. Root"
                              "\n")
                        )

        # make sure it is a valid operation or else ask to enter operation number again
        if operation in [1, 2, 3, 4, 5]:
            result = 0
            # ask for second number and operate accordingly
            if operation == 5:
                index = int(input("Enter root index:"))
                result = calc.root(index)
            elif operation < 5:
                second_number = float(input(f"Enter the second number to operate with {calc.memory}\n"))
                if operation == 1:
                    result = calc.addition(second_number)
                elif operation == 2:
                    result = calc.subtraction(second_number)
                elif operation == 3:
                    result = calc.multiplication(second_number)
                elif operation == 4:
                    result = calc.division(second_number)

            # print out result, either error message or final value
            if isinstance(result, str):
                print(result)
            else:
                print(f"The answer is {result}.")

        else:
            print("Invalid input")    # if input is not between 1-5, ask how to proceed


        # ask what how to proceed
        proceed = input(f"Do you want to"
                        f"\n1. Continue"
                        f"\n2. Clear calculator"
                        f"\n3. End session"
                        f"\nPlease enter number 1/2/3"
                        f"\n")

        if proceed in ("1", "2", "3"):
            if proceed == "1":
                print(f"The number we are working with is {calc.memory}")
            if proceed == "2":
                calc.reset()
                print(f"The number we are working with is {calc.memory}")
            elif proceed == "3":
                print("Calculator ended")
                break
        else:
            print("Invalid input")
