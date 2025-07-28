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

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

with open('1994_Weekly_Gas_Averages.txt', 'r') as gp:
    gas_prices = [line.strip() for line in gp.readlines()]

prices = [float(price) for price in gas_prices]
x = list(range(52))

plt.plot(x, prices, label='Gas Prices', color='blue', linewidth=2)
plt.title('1994 Gas Prices By Week')
plt.xlabel('Weeks in Year')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()
