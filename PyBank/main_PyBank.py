#Importing the modules (Operating system library and Python file)
import os
import csv

#Set the relative path to the csv file (Called it Pybankcsv), don't forget "" Changed to absolute as relative was not working.
PyBankcsv = "//Users//salma//Desktop//Python-Challenge//PyBank//Resources//budget_data.csv"

#Defining/intialising the variablies.
TotalMonths = 0
Total = 0
old = 0

#Create a list for the data. This should inve the list for increase or decrease and a list for the dates.
IncreaseDecreaseList = []
DateList = []

#read the data from PyBankcsv by opening as csv file.
with open(PyBankcsv, 'r') as csvfile:

    #splitting the data using commas (delimiter).
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read and print the header.
    header = next(csvreader)

    for line in csvreader:

        #Set the date and add it to the list.
        date = line[0] 
        DateList.append(date)

        #Find the increase and decrease and add them to the list.
        change = int(line[1]) - old 
        IncreaseDecreaseList.append(change) 

        #Finding the total months in the data.
        TotalMonths = TotalMonths + 1 

        #Finding the average profit and loss of the dat.
        Total = Total + int(line[1]) 
        old = int(line[1]) 
    
    del IncreaseDecreaseList[0] 
    

    #Adding the changes to find the average change
    total = sum(IncreaseDecreaseList) 
   
    #Using the total to find the average change by dividing it by the total months-1.
    average_change = total / (TotalMonths - 1) 

    #round the value to 2.d.p
    avg_change = round(average_change, 2) 
    
    #Finding the maximum and minimum profit change.
    prof_incr = max(IncreaseDecreaseList)
    prof_decr = min(IncreaseDecreaseList)

    #Maximum and Minimum Increase shown in list and thier dates to get index value.
    index_incr = IncreaseDecreaseList.index(prof_incr) + 1
    index_decr = IncreaseDecreaseList.index(prof_decr) + 1

    #Finding the Maxiumum and Minimum dates in DateList using the index number.
    date_max_incr = DateList[index_incr]
    date_max_decr = DateList[index_decr]


#Printing (make sure to create enough spacing using print(''))
print('') 
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {TotalMonths}')
print(f'Total: ${Total}')
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: {date_max_incr} (${prof_incr})')
print(f'Greatest Decrease in Profits: {date_max_decr} (${prof_decr})')
print('') 

#Write the answer/results in the budget_data_analysis file.
f = open("//Users//salma//Desktop//Python-Challenge//PyBank//Analysis//budget_data_analysis.txt", 'w')

#Creating the titles and answers structure.
f.write('Financial Analysis\n')
f.write('----------------------------\n')
f.write(f'Total Months: {TotalMonths}\n')
f.write(f'Total: ${Total}\n')
f.write(f'Average Change: ${avg_change}\n')
f.write(f'Greatest Increase in Profits: {date_max_incr} (${prof_incr})\n')
f.write(f'Greatest Decrease in Profits: {date_max_decr} (${prof_decr})\n')
f.close()
