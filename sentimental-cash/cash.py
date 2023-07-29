from cs50 import get_int

    # Ask how many cents the customer is owed
    dollars = get_dollars()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print("\n", + coins)


def get_dollars():
    while True:
        dollars = get_int("How many dollars?: ")
        if dollars > 0:
            return dollars

def calculate_quarters():
    quarters = 0
    while dollars >= 25:
        dollars = dollars - 25
        quarters += 1
    return quarters

def calculate_dimes():
    dimes = 0
    while dollars >= 10:
        cents = cents - 10
        dimes += 1
    return dimes

def calculate_nickels():
    nickels = 0
    while cents >= 5:
        cents = cents - 5
        nickels += 1
    return nickels

def calculate_pennies():
    pennies = 0
    while cents >= 1:
        cents = cents - 1
        pennies += 1
    return pennies