# import os module
import os
# import module to read csv
import csv
dirname = os.path.dirname(__file__)
budget = os.path.join(dirname,"Resources", "budget_data.csv")

#setting variables
months = 0
totalprofit= 0
change = 0
increase = 0
profitdate = ""
lossdate = ""
decrease = 0
#setting a list for average change
changelist = []
with open(budget) as csvfiles:
  # CSV reader specifies delimiter and variable that holds contents
  csvreader = csv.reader(csvfiles, delimiter=",")
  # Read the header row first
  csv_header = next(csvreader)
  # loop through row of data after the header
  for row in csvreader:
    #counts months
    months = months + 1
    # sum total profit/loss
    totalprofit = totalprofit + int(row[1])
    # finding the differences between a cell and the next, then appending them to a list
    change = int(row[1]) - change
    changelist.append(change)
    #finding greatest increase and decrease    
    if increase < change:
      increase = change
      profitdate = str(row[0])
    if decrease > change:
      decrease = change
      lossdate = str(row[0])
    change = int(row[1])
#Removing first index value as not a true difference
changelist.pop(0)
#Print the results!
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {months}")
print(f"Total: ${totalprofit}") 
print(f"Average Change ${round(sum(changelist) / len(changelist), 2):.2f}")
print(f"Greatest Increase in Profits: {profitdate} (${increase})")
print(f"Greatest Decrease in Profits: {lossdate} (${decrease})")
