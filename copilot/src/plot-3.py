import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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
            # Convert seconds to datetime.time object and add to time_data
            seconds = float(row[1])
            time_data.append(datetime.datetime.fromtimestamp(seconds).time())
            current_data.append(float(row[3]))

# Plot the current vs time
plt.plot(time_data, current_data)

# Set the labels for the X and Y axes
plt.xlabel('Time')
plt.ylabel('Current')

# Format the x-axis to display time in H:M:S format
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.SecondLocator(interval=3600))  # set interval to 1 hour
plt.gcf().autofmt_xdate()  # auto format the date on the x-axis to avoid overlapping

# Display the plot
plt.show()