import os
import pandas as pd

#Import test .csv files
#csv_path = os.path.join('budget_data_1.csv')
csv_path=os.path.join('budget_data_2.csv')

budget = pd.read_csv(csv_path, encoding='utf-8')

print(budget)

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

#Highest entry
high=budget.loc[budget['Revenue'].idxmax()]
print(high)

#Lowest entry
low=budget.loc[budget['Revenue'].idxmin()]
print(low)