""" 
    data analysis with pandas
    DataFrame, Series, read_csv, filtering,
    groupby, describe, value_counts, basic plots
"""

# ------------------------------

import pandas as pd

import matplotlib.pyplot as plt

# ------------------------------

# Series

data = [10, 20, 30]

s = pd.Series(data)
# index with column print
print(s)

s = pd.Series([75, 50, 22], index = ["math", "science", "art"])
# series data set index math 75 
print(s)


# -----------------------------
# DataFrame

data = {
    "name": ["amit", "ravi", "kishan"],
    "age": [22, 20, 25],
    "marks": [85, 90, 88]
}

df = pd.DataFrame(data)
# 2d data print
print(df)


# create a data frame
data = [
    ["alice", 35],
    ["john", 34],
    ["doe", 30],
]

df = pd.DataFrame(data, columns=["name", "age"])
print(df)


# ------------------------------
# readcsv

df = pd.read_csv("data.csv")
# read data and print
print(df)

rjson = pd.read_json("contactlist.json")
# read json file
print(rjson)


# ------------------------------
# filtering

data = {
    "name": ["amit", "ravi", "kishan"],
    "age": [22, 20, 25],
    "marks": [85, 90, 88]
}

df = pd.DataFrame(data)

# filtering data by marks > 85
print("\nmarks filter....")
print(df[df["marks"] > 85])

print("\nage filter....")
print(df[df["age"] > 22])


# ----------------------------------
# describe

data = {
    "name": ["amit", "ravi", "kishan"],
    "age": [22, 20, 25],
    "marks": [85, 90, 88]
}

df = pd.DataFrame(data)
# it give statistic about numeric data
print(df.describe())


# ----------------------------------
# value_counts

data = {
    "name": ["amit", "ravi", "kishan", "ravi"]
}

df = pd.DataFrame(data)

# count name are appears how many times
vc =  df["name"].value_counts()
print(vc)


# ------------------------------------
# groupby

data = {
    "name": ["amit", "ravi", "amit", "ravi"],
    "subject": ["math", "sci", "math", "sci"],
    "marks": [85, 90, 92, 88]
}

df = pd.DataFrame(data)

# groupby using marks and name
gb = df.groupby("name")["marks"].mean()

# gb = df.groupby(["name", "subject"])["marks"].mean()
print(gb)


# ------------------------------------
# basic plots - help data visualize

"""plot chart"""
# df["marks"].plot()
# plt.show()

"""bar chart"""
# df["marks"].plot(x="name", y="marks", kind="bar")
# plt.show()

"""pie chart"""
# df["marks"].plot(kind="pie")
# plt.show()


