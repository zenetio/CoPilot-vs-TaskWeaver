import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Open the file located at "H:\\Projects\\TaskWeaver\\project\\sample_data\\dataset.csv"
with open("H:\\Projects\\TaskWeaver\\project\\sample_data\\dataset.csv", "r") as f:
    # Load the file using the csv reader function
    df = pd.read_csv(f)

# Save the created script in a file named 'plot.py'
with open("plot.py", "w") as f:
    f.write(df.to_string())

# The dataset.csv file is time-series dataset with a csv format that has 4 columns: TIMESTAMP,TIME,RAW,CURRENT
# The RAW column will will not be used.
# The TIMESTAMP is in the format '%H:%M:%S %d/%m/%y', TIME in seconds, and the CURRENT is float
df = df.set_index("TIMESTAMP")
df = df.drop("RAW", axis=1)
#df = df.astype({"TIME": "time", "CURRENT": "float"})
#df = df.astype({"TIME": "datetime", "CURRENT": "float"})

# Using TIMESTAMP as index, read data in the range between "12:16:09 17/05/24" and "14:54:12 17/05/24"
df = df.loc["12:16:09 17/05/24":"14:54:12 17/05/24"]

# Plot the graphic of the CURRENT
df.CURRENT.plot()
plt.xlabel("Time")
plt.ylabel("Current (A)")
plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M:%S'))
plt.gcf().autofmt_xdate()  # auto format the date on the x-axis to avoid overlapping
# Show the x-axis and y-axis string labels in the graphic, or 'Time' and 'Current (A)', respectively.
plt.show()