# Assignment: Find the factors of a number


def find_divisible_integers():
    user_input = input("Enter a positive integer: ")
    user_input = int(user_input)

    for n in range(1, user_input+1):
        if user_input % n == 0:
            print(str(n) + " is a divisor of " + str(user_input))


find_divisible_integers()
