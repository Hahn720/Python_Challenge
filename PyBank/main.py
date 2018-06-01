import os
import pandas as pd

#Import test .csv files
#csv_path = os.path.join('budget_data_1.csv')
csv_path=os.path.join('budget_data_2.csv')

budget = pd.read_csv(csv_path, encoding='utf-8')

#Count number of entries
ct= budget['Date'].count()
print(ct)

#Total Sum
sum=budget['Revenue'].sum()
print(sum)

#Average difference
difference=budget['Revenue'].diff()
count=difference.count()
sum_diff=difference.sum()

average=sum_diff/count

print(average)

#Prepwork for locating differences
budget['Diff']= budget['Revenue']-budget['Revenue'].shift(1)
diffbud=budget

edit=diffbud.drop(columns=['Revenue'])

#Highest difference
high=edit.loc[edit['Diff'].idxmax()]
print(high)

#Lowest difference
low=edit.loc[edit['Diff'].idxmin()]
print(low)