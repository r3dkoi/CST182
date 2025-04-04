# Student Name:   Kyla Sofocado
# Student Number: 1034672

import pandas as pd

# TODO: read the csv into a DataFrame and then fill in each print statement
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df.head()) #debug statement + checking data we're working with

#The no. of people aboard
print(f"\n1. The number of people aboard was {len(df)}") 

#Finding the ratio of male to females  [Selection of Data]
"""This filters specifically the males and females from the dataset"""
male_count = df['Sex'] == 'male' 
female_count = df['Sex'] == 'female'
ratio_m_and_f = round((male_count.sum() / female_count.sum()),1)

print(f"\n2. The ratio of male to females passengers on board were: {ratio_m_and_f}")


print() # 3. number of people per class (note: groupby() method)
print() # 4. aggregates per class (note: groupby() method - mean,max,min,count)
print() # 5. aggregates per class and gender (note: groupby() method - mean,max,min,count)
