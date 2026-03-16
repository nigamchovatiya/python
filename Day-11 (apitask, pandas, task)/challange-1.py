"""
load csv dataset, calculate mean/max/min 
per group, generate a simple bar chart.
"""

# ------------------------------------

import pandas as pd
import matplotlib.pyplot as plt 

# ------------------------------------


# load infodata.csv file and print
data = pd.read_csv('info.csv')
print(data)


# calculate mean/max/min per group
# mean per group
print("\nMean per group:")
gb = data.groupby('Team 1')['Team 1 Runs'].mean()
print(gb)


# max per group
print("\nMax per group:")
gb = data.groupby('Team 1')['Team 1 Runs'].max()
print(gb)


# min per group
print("\nMin per group:")
gb = data.groupby('Team 1')['Team 1 Runs'].min()
print(gb)


# print bar chart
data.plot(x="Team 1", y="Team 1 Runs", kind="bar")
plt.show()

"""overall data bar chart show"""
# datashow = data.plot(kind='bar')
# plt.show()


