#########################################
# John Zetterman
# Assignment 1, Problem 1
# May 29, 2025
#
# Description: This program calculates compound interest on a principal amount for X years.
# Inputs: Principal, Interest Rate, Compound Frequency, and Years
# Outputs: Prints the balance based on all inputs for X years.
#########################################

principal = float(input("What was the principal amount? "))
interest = float(input("What is the annual interest rate? "))
frequency = int(input("How often is interest compounded? "))
years = float(input("How many years will the account be left open? "))

rate = interest / 100
amount = principal * (1 + (rate / frequency)) ** frequency * years
print(f"${amount:.2f}")
