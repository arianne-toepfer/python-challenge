import os
import csv
csvpath= r'C:\Users\Arianne\Desktop\PythonStuff\Python_Challenge_Homework\python-challenge\PyPoll\Resources\election_data .csv'

def election_results(poll):
    #total Votes
    Total= len(poll[1])

    #dictionary of candidates,the percentage of votes they won, and the total number of votes they won
    candidates=[]
    count=1
    for x in range(poll[1]):
        if x 
    #find the winner of the election

    #print it pretty



#Read function in CSV file:
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    for row in csvreader:
       