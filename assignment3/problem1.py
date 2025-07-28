#########################################
# John Zetterman
# Assignment 3
# Date Completed: July 28, 2025
#
# Description: This program performs several sorting and mathematical
#              operations on a list of 20 numbers input from the user.
# Inputs: A string of number values
# Outputs: Prints out a summary displaying the lowest number, highest number,
#          total or sum of all numbers, and the average of all numbers.
#########################################

def main():
    numbers = input("Please enter 20 numbers separated by a space:")
    # Split the input and convert them to int type. I found that sorting
    # before converting to int sometimes resulted in unexpected number sorting
    # because it sorts strings based on the character's ascii/hexadecimal value.
    # (i.e. 10 will be lower than 2 when sorted)
    num_list = [int(x) for x in numbers.split()]

    lowest_number = sorted(num_list)[0]
    highest_number = sorted(num_list, reverse=True)[0]
    num_total = sum(num_list)
    avg_number = num_total / len(num_list)

    print('Summary of your numbers')
    print(f'Lowest number: {lowest_number}')
    print(f'Highest number: {highest_number}')
    print(f'Sum of all numbers: {num_total}')
    print(f'Average of all numbers: {avg_number}')

if __name__ == "__main__":
    main()
