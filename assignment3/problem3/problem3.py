#########################################
# John Zetterman
# Assignment 3
# Date Completed: July 28, 2025
#
# Description: This program grades driver's license exams
# Inputs: The user enters a list of names. A list of boys names and a list
#         girls names are imported from files.
# Outputs: Prints whether or not the names were found in either list of names.
#########################################

def main():
    names = input("Enter name(s): ")
    name_list = names.split()

    girl_names_values = []
    with open('GirlNames.txt', 'r') as gf:
        girl_names = gf.readlines()
        girl_names_values = [girl_name.strip() for girl_name in girl_names]

    boy_names_values = []
    with open('BoyNames.txt', 'r') as bf:
        boy_names = bf.readlines()
        boy_names_values = [boy_name.strip() for boy_name in boy_names]

    for name in name_list:
        if name in girl_names_values and name in boy_names_values:
            print(f'{name} was found in the most popular list for boy and girl names.')
        elif name in girl_names_values:
            print(f'{name} was found in the most popular list of girl names.')
        elif name in boy_names_values:
            print(f'{name} was found in the most popular list of boy names.')
        else:
            print(f'{name} was not found in the list of most popular boy or girl names.')


if __name__ == "__main__":
    main()
