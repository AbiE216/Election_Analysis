#The data we need to retrieve 
#add our dependencies
import csv
import os
    #Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
    #Assign  a variable to the save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")
    #Initialize a total vote counter
total_votes = 0
    #Declare a new list
candidate_options = []
    #Declare and empty dictionary
candidate_votes ={}

# the winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

    #Open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
   
    #read the file object with the reader function
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        #if candidate name not already represented add to the list, otherwise ignore
        if candidate_name not in candidate_options:
        #add name to the list
            candidate_options.append(candidate_name) 
        #begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidates count
        candidate_votes[candidate_name] += 1 

        #Save the results to a text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
#Determinig the percentage of votes per candidate
# iterate through the candidate list
    for candidate_name in candidate_votes:
    #retieve the votes for each candidate
        votes = candidate_votes[candidate_name]
    #get the percentage each candidate won
        vote_percentage = float(votes) / float(total_votes)*100       
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 
        print(candidate_results)
        txt_file.write(candidate_results)
    #Determine the winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
        
          
        winning_candidate_summary = (
            f"-----------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage:{winning_percentage:.1f}%\n" 
            f"-----------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
#print(winning_candidate_summary)




#1. The total number of votes cast 
#2. The total number of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on the popular vote. 

#close the file after analysis
   
