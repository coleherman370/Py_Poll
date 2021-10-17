# Tasks requested
# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

import csv
import os
from datetime import datetime

start_time = datetime.now()
# Global variables
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election_analysis.txt initially so that txt can be written to at any point without overwritting file's current content
with open (file_to_save,'w') as txt_file:

    with open(file_to_load) as election_data:
        # Access the election_results.csv 
        file_reader = csv.reader(election_data)
        # Exclude header information from counts performed below
        header = next(file_reader)
        # Sum the total votes
        for row in file_reader:
            total_votes += 1
            candidate_name = row[2]

            # Identify unique candidate names, add unique names to list of names, add unique names to vote dictionary
            if candidate_name not in candidate_options:
                candidate_options.append(candidate_name)
                candidate_votes[candidate_name] = 0   
            # Add the vote count in vote dictionary of the candidates
            candidate_votes[candidate_name] += 1
        
        # Generate string for election_analysis.txt header and sum of total votes. Write to txt file
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")                       
        txt_file.write(election_results)

        for candidate_name in candidate_votes:

            # Calculate the percentage of total votes for each candidate
            votes = candidate_votes[candidate_name]
            vote_percentage = round(float(votes)/float(total_votes) * 100,1)
            # Generate string for each candidate containing their name, vote percent, and sum of votes. Write string to election_analysis.txt     
            candidate_results =  f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
            txt_file.write(candidate_results)      
            
            # Identify the candidate with the largest number of votes
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name   

                # Generate election results string
                winning_candidate_summary = (
                    f"-------------------------\n"
                    f"Winner: {winning_candidate}\n"
                    f"Winning Vote Count: {winning_count:,}\n"
                    f"Winning Percentage: {winning_percentage:.1f}%\n"
                    f"-------------------------\n")
        
        # Write the election results to election_analysis.txt
        txt_file.write(winning_candidate_summary)

# Open and read election_analysis.txt to print within Command Line
txt = os.path.join("Analysis", "election_analysis.txt")
txt = open(txt,'r')
txt_content = txt.read()
print(txt_content)
end_time = datetime.now()
print("Duration of PyPoll.py: {}".format(end_time - start_time))
input('Press any button to close PyPoll:')    




