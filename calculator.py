#!/usr/bin/env python3

# Created by: Hertz Antonella
# Created on: May, 12, 2022.
# This program asks user to enter a sign and 2 numbers
# they want to perform, calculate it and check for errors.


def calculate(sign, first_num, second_num):
    if sign == "+":
        output = first_num + second_num
    elif sign == "-":
        output = first_num - second_num
    elif sign == "%":
        output = first_num % second_num
    elif sign == "*":
        output = first_num * second_num
    elif sign == "/":
        output = first_num / second_num
    return output


def main():
    user_sign = input("Enter the operator you want to perform(+,-,*,%,/): ")
    print("")

    if (
        user_sign == "+"
        or user_sign == "-"
        or user_sign == "%"
        or user_sign == "*"
        or user_sign == "/"
    ):

        first_num = input("Enter first_number: ")
        # ask for the first numbers
        try:
            first_num = float(first_num)

            second_num = input("Enter second_number: ")
            # ask for the second number
            try:
                second_num = float(second_num)

                user_output = calculate(user_sign, first_num, second_num)

                print(
                    "{} {} {} is {:,.1f}.".format(
                        first_num, user_sign, second_num, user_output
                    )
                )
                print("")

            except Exception:
                print(
                    "{} is an invalid input,Please enter numbers only".format(
                        second_num
                    )
                )
        except Exception:
            print("{}is an invalid input,Please enter numbers only.".format(first_num))

    else:
        print("Please enter the following signs only (+,-,*,%,/)")


if __name__ == "__main__":
    main()
