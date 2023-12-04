"""Interest rate Monthly payment calculator


Author:Maryam Alavi
"""
import random
import sys


def user():
    """user should be entering the username and pass"""
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    print("username: ", username)
    print("password: ", password)


user()


def generate_turnover_values():
    """
    Generate a list of 10 random turnover values.

    :return:
    List[float]: A list containing 10 random turnover values.
    """
    turnovers = [random.uniform(100000, 1000000) for _ in range(10)]
    return turnovers


def choice():
    """
    Display a menu for the user to choose between "Turnover" and "Loan Calculator."
    If the user chooses "Turnover," generate and print 10 random turnover values.
    If the user chooses "Loan Calculator," print a message indicating the choice.
    """
    print("Choose your option: ")
    print("1. Turnover")
    print("2. Loan Calculator")

    user_choice = input("Enter the number of your choice: ")

    if user_choice == "1":
        # Generate and print 10 random turnover values
        turnovers = generate_turnover_values()
        print("Random Turnover Values:")
        for turnover in turnovers:
            print(turnover)

        # Exit the program
        sys.exit()
    elif user_choice == "2":
        # Call the function or code for Loan Calculator
        print("You chose Loan Calculator.")
    else:
        print("Invalid choice. Please enter 1 or 2.")


choice()


def main():
    """here we can count the monthly payment of loan"""
    print(" This is a monthly payment loan calculator ")
    print("")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years: "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = (
            principal * monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    )

    print(f"The monthly payment for this loan is: {monthly_payment:.2f}")



main()
