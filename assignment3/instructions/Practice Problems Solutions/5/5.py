# 5. Expense Pie Chart

import matplotlib.pyplot as plt

def main():
    # Open the expense file.
    expense_file = open('expenses.txt', 'r')

    # Read the file contents into a list.
    expenses = expense_file.readlines()

    # Close the file.
    expense_file.close()

    # Strip the newline from each element.
    for i in range(len(expenses)):
        expenses[i] = expenses[i].rstrip('\n')

    # Create the slice labels.
    slice_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
    
    # Create a pie chart from the values.
    plt.pie(expenses, labels=slice_labels)

    # Add a title.
    plt.title('Monthly Expenses')

    # Display the pie chart.
    plt.show()

# Call the main function.
if __name__ == '__main__':
    main()