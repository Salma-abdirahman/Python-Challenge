#PyPoll

#Importing the modules (Operating system library and Python file)
import os 
import csv

#Set the relative path to the csv file (Called it PyPollcsv), don't forget "" Changed to absolute as relative was not working.
PyPollcsv = "//Users//salma//Desktop//Python-Challenge//PyPoll//Resources//election_data.csv"

#Defining/intialising the variablies.
TotalVotes = 0

#Create a list for the data. Create Dictionaries.
compare_percentages = [] 

#Dictionary to hold the candiates and thier votes and percentages.
CandidateVotes = {} 
percentages = {} 

#For Candidate output.
compare_lib = {} 

#Holds place for the winning candidate.
Winner = "Winning candidate?" 


#read the data from PyPollcsv by opening as csv file.
with open(PyPollcsv, 'r') as csvfile:

    #splitting the data using commas (delimiter).
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read and print the header.
    header = next(csvreader)

    for line in csvreader:

        # Find the total number of votes
        TotalVotes = TotalVotes + 1 

        #Find and put unique candidates (not in candidate votes) and their votes into the dictionary.
        #If the candiate is unique, add them into the list with 1 vote.
        if line[2] not in CandidateVotes:
            CandidateVotes[line[2]] = 1
       #If not unique candiate and already is in the lost then add 1 vote.
        else:
            CandidateVotes[line[2]] += 1



#Finding the candidates percentage votes by divind the candidates votes by the total number of votes.
for candidate in CandidateVotes:
    percent_vote = CandidateVotes[candidate] / TotalVotes 
    #formatting the value/percentage.
    percent_vote_changed = "{:.3%}".format(percent_vote) 

    #Add the candidates percentage to the library.
    percentages[candidate] = percent_vote_changed

    #Add the candidates percentage to a list using append and then compare.
    compare_percentages.append(percent_vote_changed)
    compare_lib[percent_vote_changed] = candidate 

#Finding the winner
Winner = compare_lib[max(compare_percentages)]


#Printing all the lists and dictionaries. Dont forget to create the right spacing.
print('') 
print('Election Results')
print('-------------------------')
print(f'Total Votes: {TotalVotes}')
print('-------------------------')

#Create a loop so that each candiate could get results.
for candidate in CandidateVotes: 
    print(f'{candidate}: {percentages[candidate]} ({CandidateVotes[candidate]})')
print('-------------------------')
print(f'Winner: {Winner}')
print('-------------------------')


#Write the answer/results in the election_data_analysis file.
f = open("//Users//salma//Desktop//Python-Challenge//PyPoll//Analysis//election_data_analysis.txt", 'w')

#Creating the titles and answers structure.
f.write('Election Results\n')
f.write('-------------------------\n')
f.write(f'Total Votes: {TotalVotes}\n')
f.write('-------------------------\n')
for candidate in CandidateVotes:
    f.write(f'{candidate}: {percentages[candidate]} ({CandidateVotes[candidate]})\n')
f.write('-------------------------\n')
f.write(f'Winner: {Winner}\n')
f.write('-------------------------\n')
f.close()