# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has give you the following tasks to comple the elections audit of a recent local congression election. 

1. Calculate the total number of Votes cast. 
2. Get a complete lis  of candidates who recieved votes.
3. Calculate the total number of votes each candidate won.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular votes.
6. Calculate the turnout rate for each county.
7. Determine which county had the highest turnout. 


## Resources
-Data Source: election_results.csv
-Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election-Audit Results: 
### The analysis of the election show that:
-There were "369,711" votes cast in the election
-The candidates were:
  - Charles Casper Stockham
  - Diane DeGette
  - Raymon Anthony Doane
 -The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote with 85,213 votes
  - Diana DeGette received 73.8% of the vote with 272,892 votes
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes
 -The winner of the election was:
  - Diana DeGette, who receieved 73.8% of the votes with 272,892 votes. 
 -The county turnout results were:
  -Jefferson county: Had 10.5% turnout with 38,855 votes.
  -Denver county: Had 82.8% turnout with 306,055 votes
  -Arapahoe county: 6.7% turnout with 24,801.
 -The highest turn out was Denver county with 82.8% of the vote. 

 ## Election-Audit Summary
 As commissioned, a code was created to analyze the election results. This code however could be used to analyze any elections with a few modifications, the file_to_load path would need to be updated to the preferred csv file, the index identifying candidate or county may need to be altered depending on which row they fall into, the variables for county can be altered if they want to use this for states as opposed to counties, and at any point a new text file could be created which would alter the file_to_save portion of the coding. This code is flexible and can cover a wide range of different elections, with a few easy alterations. 
