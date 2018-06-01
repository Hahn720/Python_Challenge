import os
import pandas as pd

#Import test .csv files
#csv_path=os.path.join('election_data_1.csv')
csv_path=os.path.join('election_data_2.csv')

election=pd.read_csv(csv_path, encoding='utf-8')

print(election.head())

#Total number of votes
total=election['Voter ID'].count()
print(total)

#List of candidates
cand=election['Candidate'].unique()
print(cand)

#Percentage of votes per candidate and number of votes per candidate
candidate=election.groupby('Candidate')
count=candidate.count()

percent=(count/total)*100

print(percent)
print(count)

#Print winner
winner=percent['County'].sort_values(ascending=False)

print('Winner:{}'.format(winner.index[0]))