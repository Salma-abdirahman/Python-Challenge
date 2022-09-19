# Python-Challenge

Aim of Python Challenge was to create Python scripts to analyse financial records (PyBank) and election votes (PyPoll).

First Steps:
  1 Create a repository for the challenge named Python-Challenge, clone to computer.
  2 Create a directory for PyBank and PyPoll.
  3 In each folder create:
    - main.py file - In this case the files are called main_pybank.py amd main_pypoll.py to avoid confusion.
    - A folder named Resources to contain CSV files used.
    - A folder named Analysis to contain .txt file that would show the results.
  4 Push these changes to Github.
  
Instructions for PyBank

In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses". (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:
  - The total number of months included in the dataset
  - The net total amount of "Profit/Losses" over the entire period
  - The changes in "Profit/Losses" over the entire period, and then the average of those changes
  - The greatest increase in profits (date and amount) over the entire period
  - The greatest decrease in profits (date and amount) over the entire period


Your analysis should look similar to the following:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

My Final result seen in budget_data_analysis.txt
<img width="518" alt="image" src="https://user-images.githubusercontent.com/111789352/191099258-018ba020-dcf2-4cf2-95b2-eab93a732968.png">

Instructions for PyPoll

In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:
  - The total number of votes cast
  - A complete list of candidates who received votes
  - The percentage of votes each candidate won
  - The total number of votes each candidate won
  - The winner of the election based on popular vote.


Your analysis should look similar to the following:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

My Final result seen in election_data_analysis.txt
<img width="510" alt="image" src="https://user-images.githubusercontent.com/111789352/191099745-e9cf2f61-c3a7-402c-afdf-4782f2d8b6f5.png">



