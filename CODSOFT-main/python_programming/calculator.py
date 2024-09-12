def user_input():
    try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        operation = int(
            input("\nSelect the operation :\n1.\t+\n2.\t-\n3.\t*\n4.\t/\n5.\t^\n\n")
        )

    except ValueError:
        print("Error: Invalid values")
        exit()

    if (operation == 4 and num2 == 0) or operation not in [1, 2, 3, 4, 5]:
        print("Error : invalid input, Please Try Again")
        operation = 0

    return num1, num2, operation


def calc(a, b, op):
    if op == 1:
        return a + b

    elif op == 2:
        return a - b

    elif op == 3:
        return a * b

    elif op == 4:
        return a / b

    elif op == 5:
        return a**b


def main():
    x, y, operator = user_input()

    if operator:
        print(f"Output :==> {calc(x, y, operator)}")


main()
