# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

import datetime
import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1
    
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = round(float(votes)/float(total_votes) * 100,1)
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")




