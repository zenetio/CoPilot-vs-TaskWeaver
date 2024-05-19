import csv
import matplotlib.pyplot as plt
import sys
import datetime

# Command line arguments for initial and final data
initial_data = sys.argv[1]
final_data = sys.argv[2]

# Convert the initial and final data to datetime objects
initial_data = datetime.datetime.strptime(initial_data, "%H:%M:%S %d/%m/%y")
final_data = datetime.datetime.strptime(final_data, "%H:%M:%S %d/%m/%y")

# Open the file
with open('dataset.txt', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    
    # Initialize lists to store the time and current data
    time_data = []
    current_data = []
    
    # Iterate over each row in the file
    for row in reader:
        # Convert the timestamp to a datetime object
        timestamp = datetime.datetime.strptime(row[0], "%H:%M:%S %d/%m/%y")
        
        # If the timestamp is within the specified range
        if initial_data <= timestamp <= final_data:
            # Add the time and current data to their respective lists
            seconds = float(row[1])
            time_data.append(seconds)
            current_data.append(float(row[3]))

# Plot the current vs time
plt.plot(time_data, current_data)

# Set the labels for the X and Y axes
plt.xlabel('Time (seconds)')
plt.ylabel('Current')

# Display the plot
plt.show()