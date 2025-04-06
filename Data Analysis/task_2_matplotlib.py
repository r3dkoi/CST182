"""A scatter plot to plot age compared to fare"""
import pandas as pd
import matplotlib.pyplot as plt

df2 = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# TODO: Create a scatter plot comparing the age of each person to the fare they paid
print(df2.head()) #Debug statement to show if the data is being read correctly.


plt.scatter(df2["Age"], df2["Fare"])

#Labelling the graph
plt.title("Age vs Fare in the Titanic")

plt.xlabel("Age")
plt.ylabel("Fare")

plt.show()

