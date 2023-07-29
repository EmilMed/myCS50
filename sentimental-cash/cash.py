from cs50 import get_float


def get_cents():
    while True:
        cents = get_float("How many dollars?: ")
        if cents > 0:
            break

def calculate_quarters():
    quarters = 0
    while cents >= 25:
        cents = cents - 25
        quarters += 1
    return quarters

def calculate_dimes():
    dimes = 0
    while cents >= 10:
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