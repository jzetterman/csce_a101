#########################################
# John Zetterman
# Assignment 2
# Date Completed: July 4, 2025
#
# Description: This program converts feet to inches.
# Inputs: The number of feet as a float.
# Outputs: Prints the number of inches with 2 decimals of precision.
#########################################

def feet_to_inches(feet):
    return feet * 12

def main():
    input_feet = float(input("Enter the number of feet to convert to inches: "))
    print(f'{feet_to_inches(input_feet):.2f}')

if __name__ == "__main__":
    main()