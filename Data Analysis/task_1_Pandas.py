# Student Name:   Kyla Sofocado
# Student Number: 1034672

import pandas as pd

# TODO: read the csv into a DataFrame and then fill in each print statement
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df.head()) #debug statement + checking data we're working with


#Finding the ratio of male to females  [Selection of Data]
"""This filters specifically the males and females from the dataset"""
male_count = df['Sex'] == 'male' 
female_count = df['Sex'] == 'female'
ratio_m_and_f = round((male_count.sum() / female_count.sum()),1)

#Finding the number of people per class [Groupby() method practice]
people_per_class = df.groupby('PClass').size() 


print() # 4. aggregates per class (note: groupby() method - mean,max,min,count)
print() # 5. aggregates per class and gender (note: groupby() method - mean,max,min,count)

#Display section
print(f"\n1. The number of people aboard was {len(df)}") 
print(f"\n2. The ratio of male to females passengers on board were: {ratio_m_and_f}")
print(f"\n3. The number of people per class were: {people_per_class}") 