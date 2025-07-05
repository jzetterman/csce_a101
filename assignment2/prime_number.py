#########################################
# John Zetterman
# Assignment 2
# Date Completed: July 4, 2025
#
# Description: This program determines if a number is prime.
# Inputs: An integer to check for prime
# Outputs: Prints True or False depending on the prime status of the input number.
#########################################

def is_prime(n):
    prime = True
    for i in range(n):
        if i == 0 or i == 1 or i == n:
            continue
        if not n % i:
            prime = False
    return prime

def main():
    user_input = int(input("Enter a number: "))
    print(is_prime(user_input))

if __name__ == "__main__":
    main()