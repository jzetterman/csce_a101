#########################################
# John Zetterman
# Assignment 2
# Date Completed: July 4, 2025
#
# Description: This program calculates travel time.
# Inputs: Two floats, distance and speed.
# Outputs: Prints the number of hours to travel based on the time factor.
#########################################

def travel_time(distance, speed, traffic_factor):
    normal_time = distance / speed
    time_with_traffic = normal_time * traffic_factor
    print(f'{time_with_traffic:.2f}')

def main():
    distance_in = float(input("Enter the distance: "))
    speed_in = float(input("Enter the speed in miles per hour: "))
    travel_time(distance_in, speed_in, 1.0)
    travel_time(distance_in, speed_in, 1.5)
    travel_time(distance_in, speed_in, 2.0)

if __name__ == "__main__":
    main()