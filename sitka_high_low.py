# Brian Preston
# module4.2
# My Code now reflects to opens with a welcome message explaining how to select high or low temperatures, or to exit. 
# A while loop provides a menu until the user chooses to exit, displaying a red graph for the highs or a blue graph for the lows. 
# When user then selects exit, the program displays a goodbye message and then will exit.

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Instructions for the user
print("Welcome to the Weather Data Viewer!")
print("Select '1' for Highs, '2' for Lows, or '3' to Exit.\n")

# Load data from CSV file
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            # Convert and store date, high, and low values
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            highs.append(int(row[5]))
            lows.append(int(row[6]))
        except ValueError:
            # Skip rows with invalid data and print a message
            print(f"Skipping row with invalid data: {row}")

# Function to plot data
def plot_data(dates, temps, label, color):
    plt.plot(dates, temps, color=color)
    plt.title(f"Daily {label} Temperatures - 2018")
    plt.ylabel("Temperature (F)")
    plt.show()

# Main menu loop
while True:
    choice = input("Enter 1 for Highs, 2 for Lows, or 3 to Exit: ")

    if choice == '1':
        plot_data(dates, highs, "High", "red")
    elif choice == '2':
        plot_data(dates, lows, "Low", "blue")
    elif choice == '3':
        print("Exiting program. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

