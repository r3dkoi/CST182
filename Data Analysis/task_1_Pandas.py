# Student Name:   Kyla Sofocado
# Student Number: 1034672

import pandas as pd

# TODO: read the csv into a DataFrame and then fill in each print statement
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.head() #debug statement + checking data we're working with

print() # 1. number of people aboard (basic aggregate or length)
print() # 2. ratio of male to females (selecting data)
print() # 3. number of people per class (note: groupby() method)
print() # 4. aggregates per class (note: groupby() method - mean,max,min,count)
print() # 5. aggregates per class and gender (note: groupby() method - mean,max,min,count)
