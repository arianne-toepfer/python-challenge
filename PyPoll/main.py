import os
import csv
csvpath= r'C:\Users\Arianne\Desktop\PythonStuff\Python_Challenge_Homework\python-challenge\PyPoll\Resources\election_data .csv'

#create list of candidates,the percentage of votes they won, and the total number of votes they won
#percentage of votes
#find the winner of the election
#print it pretty

#Read function in CSV file:
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    votes=0
    candidates = []
    voteCounter = []
    for row in csvreader:
        #total votes
        votes += 1

        #finding candidates and adding them to a list then use that list to find how many votes are recieved  
        if not candidates:
            candidates.append(row[2])
            voteCounter.append(0)
        
        for candidate in candidates:
            if row[2] not in candidates :
                candidates.append(row[2])
                voteCounter.append(0)

        if row[2] in candidates :
            index = candidates.index(row[2])
            voteCounter[index] += 1

#Print Results
    print("Election Results")
    print(f"Total Votes: {votes}")
    print(f"{candidates[0]} : {((int(voteCounter[0]) / votes)*100)} ( {voteCounter[0]} )")
    print(f"{candidates[1]} : {((int(voteCounter[1]) / votes)*100)} ( {voteCounter[1]} )")
    print(f"{candidates[2]} : {((int(voteCounter[2]) / votes)*100)} ( {voteCounter[2]} )")
    print(f"{candidates[3]} : {((int(voteCounter[3]) / votes)*100)} ( {voteCounter[3]} )")
    print(f'Winner: {}')
