# import os module
import os
# import module to read csv
import csv
dirname = os.path.dirname(__file__)
data = os.path.join(dirname,"Resources", "election_data.csv")


#variable to hold total votes
total = 0

#dict to assign vote counts to candidates
votecount = {}

# Open the CSV
with open(data) as csvfiles:
    # set delimiter for columns
    csvreader =csv.reader(csvfiles, delimiter = ",") 
    # skip the header
    csvheader = next(csvreader)
    #loop to gain data
    for row in csvreader:
        #Tally total votes
        total = total + 1
        #loop to create keys and assign them values. Key is the name of the candidate. The value is the vote count for the respective candidate.
        if row[2] not in votecount:
            #adding a new key into dictionary with intial value 1
            votecount[row[2]] = 1
            # if key is already there, adds to the vote count
        else:
            votecount[row[2]] = votecount[row[2]] + 1

#Printing Output
def analysis():
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total}")
    print("-------------------------")
    #variable to adjudicate the winner of the election
    winner = ""
    #loop to print results
    for x in votecount:
        # Print results, converting vote percentage using the round function
        print(f'{x}: {round(100 * votecount[x] / total, 3):.3f}% ({votecount[x]})')
        #conditional loop to find the winner
        if winner == "":
            winner = x
        elif votecount[x] >= votecount[winner]:
            winner = x 
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')

#terminal
print(analysis())
#path to write the results 
main_analysis = os.path.dirname(__file__)
passageFile = os.path.join(dirname, "mainanalysis.txt")
#write results into text file
outF = open(main_analysis,'w')
#write using writelines
outF.writelines(analysis())
outF.close()
