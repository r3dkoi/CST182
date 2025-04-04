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

#Finding the number of people per class [1, 2, 3 class] [Groupby() method practice]
people_per_class = df.groupby('Pclass').size()

#Finding the mean, max, min, and count of people per class [Groupby() method - mean,max,min practice]
    # Calculate the aggregation of the data
average_per_class = df.groupby('Pclass').size().mean()
maximum_per_class = df.groupby('Pclass').size().max()
minimum_per_class = df.groupby('Pclass').size().min()

#Calculate the number of males and females per class using existing variables
male_count_per_class = df[male_count].groupby('Pclass').size()
female_count_per_class = df[female_count].groupby('Pclass').size()

#Calculating the rest of the aggregations for males and females per class
average_males_per_class = df[male_count].groupby('Pclass').size().mean()
average_females_per_class = df[female_count].groupby('Pclass').size().mean()
maximum_males_per_class = df[male_count].groupby('Pclass').size().max()
maximum_females_per_class = df[female_count].groupby('Pclass').size().max()
minimum_males_per_class = df[male_count].groupby('Pclass').size().min()
minimum_females_per_class = df[female_count].groupby('Pclass').size().min()


#Display section
print(f"\n1. The number of people aboard was {len(df)}") 
print(f"\n2. The ratio of male to females passengers on board were: {ratio_m_and_f}")
print(f"\n3. Number of people in each class: ")
for pclass, count in people_per_class.items():
    print(f"   Class {pclass} = {count} people")
print(f"\n4. The average amount of people per class was: {average_per_class:.1f}")
print(f"\n5. The maximum amount of people per class was: {maximum_per_class}")
print(f"\n6. The minimum amount of people per class was: {minimum_per_class}")

print(f"\n7. The total count of males per class were: ")
for pclass, count in male_count_per_class.items():
    print(f"   Class {pclass} = {count} males")
print(f"\n8. The average amount of males per class were: {average_males_per_class:.1f}")
print(f"\n9. The maximum amount of males per class were: {maximum_males_per_class}")
print(f"\n10. The minimum amount of males per class were: {minimum_males_per_class}")

print(f"\n11. The total count of females per class were: ")
for pclass, count in female_count_per_class.items():
    print(f"   Class {pclass} = {count} females")
print(f"\n12. The average amount of females per class were: {average_females_per_class:.1f}")
print(f"\n13. The maximum amount of females per class were: {maximum_females_per_class}")
print(f"\n14. The minimum amount of females per class were: {minimum_females_per_class}")









