# 2. Population Data

# The program assumes that all population changes are positive.
# That is, that each year the population was larger than the
# previous year.

def main():

    # Setup variables
    yearly_change = []
    change = 0.0
    total_change = 0.0
    average_change = 0.0
    greatest_increase = 0.0
    smallest_increase = 0.0
    greatest_year = 0
    smallest_year = 0

    # Constant for the base year
    BASE_YEAR = 1950
    
    # Open the file for reading.
    input_file = open('USPopulation.txt', 'r')
        
    # Read all the lines in the file into a list.
    yearly_population = input_file.readlines()
        
    # Turn all read strings into numbers.
    for i in range(len(yearly_population)):
        yearly_population[i] = float(yearly_population[i])

    # Calculate the change in population size for each two years.
    for i in range(1, len(yearly_population)):
        change = yearly_population[i] - yearly_population[i-1]
        yearly_change.append(change)

        # If this is the first year, set trackers to its value.
        if i==1:
            greatest_increase = change
            smallest_increase = change
            greatest_year = 1
            smallest_year = 1

        # This is not the first change in population size.
        # Update trackers if relevant.
        else:
            if change > greatest_increase:
                greatest_increase = change
                greatest_year = i
                    
            elif change < smallest_increase:
                smallest_increase = change
                smallest_year = i

    total_change = float(sum(yearly_change))
    average_change = total_change / len(yearly_change)

    print(f'The average annual change in population '
            f'during the time period is {average_change:,.2f}')
    print(f'The year with the greatest increase in population was '
            f'{BASE_YEAR + greatest_year}')
    print(f'The year with the smallest increase in population was '
            f'{BASE_YEAR + smallest_year}')

# Call the main function.
if __name__ == '__main__':
    main()