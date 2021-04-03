import os
import csv

#Create funciton for sum of profit loss
def summation(List_of_num):
    return sum(List_of_num)


csvpath= r'C:\Users\Arianne\Desktop\PythonStuff\Python_Challenge_Homework\python-challenge\PyBank\resources\budget_data.csv'
#Read function in CSV file:
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    
    Total_Months = 0
    maximum_profit= 0
    minimum_profit= 0
    Dictionary={"Date":[],"Profit_Loss":[]}
    for row in csvreader:
        
        #Total month
        Total_Months += 1

        #Create Date list and Profit loss lists
        Dictionary["Date"].append(row[0])
        Dictionary["Profit_Loss"].append(int(row[1]))

        #total Profit loss
        Total=summation(Dictionary["Profit_Loss"])

        #Average Profit Loss
        Average = Total_Months / Total

        #Find max and min
        if maximum_profit <= int(row[1]):
            maximum_profit=  int(row[1])
        if minimum_profit >= int(row[1]):
            minimum_profit= int(row[1])
        
    #match up max and min with appropriate date they are locations 25 for max and 44 for min
    #print(Dictionary["Profit_Loss"].index(maximum_profit)) 
    #print(Dictionary["Profit_Loss"].index(minimum_profit)) 
    #Print the summary
    print("Financial Analysis")
    print(f"Total Months: {Total_Months}")
    print(f"Total Profits: {Total}")
    print(f"Average Change: {Average}")
    print("Greatest Increase in Profits: " + Dictionary["Date"].pop(25), Dictionary["Profit_Loss"].pop(25))
    print("Greatest Decrease in Profits: " + Dictionary["Date"].pop(43), Dictionary["Profit_Loss"].pop(43))