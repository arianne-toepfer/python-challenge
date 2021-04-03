import os
import csv

csvpath= r'C:\Users\Arianne\Desktop\PythonStuff\Python_Challenge_Homework\python-challenge\PyBank\resources\budget_data.csv'

#define functions for the columns to help with readability
def financial_analysis(bank):
    Date=str(bank[0])
    Profit_loss=int(bank[1])

    #Total month
    Total_Months=len(Date)

    #total Profit loss
    Total=sum(Profit_loss)

    #Average Profit loss change
    Average_profit = Total/Total_Months

    #greatest increase in profit data and amount
    max_profit=max(int(bank[1]))

    #greatest decrease in loss date and amounte
    min_profit= min(int(bank[1]))
    
    #print it pretty
    print("Financial Analysis")
    print("Total Months: " + Total_Months)
    print("Total: " + Total)
    print("Average Change: " + Average_profit)
    print("Greatest Increase in Profits: " + max_profit)
    print("Greatest Decrease in Profits: " + min_profit)

#Read function in CSV file:
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    for row in csvreader:
       financial_analysis(row)



