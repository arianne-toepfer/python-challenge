import os
import csv
csvpath= r'C:\Users\Arianne\Desktop\PythonStuff\Python_Challenge_Homework\python-challenge\PyPoll\Resources\election_data .csv'

#def election_results(poll):
#total Votes
#create list of candidates,the percentage of votes they won, and the total number of votes they won
#percentage of votes
#find the winner of the election
#print it pretty

#Read function in CSV file:
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    votes=0
    count=1
    for row in csvreader:
        #total votes
        votes += 1

        #finding candidates
        candidates = []
        for x in range(int(row[1])):
            if x not in candidates:
                candidates.append(x)
                count+=1
    
    print(votes)
    print(candidates)
