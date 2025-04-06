# Student Name: Kyla Sofocado
# Student Number: 1034672

from tkinter import N
import pandas as pd

df = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

print(df.head()) #Debug statement to show if the data is being read correctly.

#Displaying the average statisics of all applicable attibutes for all three species of iris in one line.
"""The three species in the csv file is setosa, versicolor, and virginica."""
print("\n")
print(df.groupby("species").mean()) #This displays the mean of all three species

"""Since the GroupBy() method only takes data from a specified column, and ignores the duplicate values. Hence why only one of each row is displayed."""
"""Implementing the mean() method calculates the mean of all the values in the column."""


