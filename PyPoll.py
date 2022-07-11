# the data we need to retrieve
#The total number of votes cast
# A cmplete list of candidates who received votes
#The percentage of votes each candidate won
#the total number of votes each candidate won



# indirect Path to load file
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_results.csv")
# Open the election results and read the file.

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.

# Initialize a total vote counter.
total_votes = 0
winning_count =0
winning_candidate=""
winning_percentage=0
# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

with open(file_to_load, "r") as election_data:
     file_reader = csv.reader(election_data)
    # Read the header row.
     headers = next(file_reader)

    # Print each row in the CSV file.
     for row in file_reader:
          # Add to the total vote count.
          total_votes += 1

          # Print the candidate name from each row.
          candidate_name = row[2]

          if candidate_name not in candidate_options:

               # Add the candidate name to the candidate list.
               candidate_options.append(candidate_name)

                    # 2. Begin tracking that candidate's vote count.
               candidate_votes[candidate_name] = 0
          # Add a vote to that candidate's count
          candidate_votes[candidate_name] += 1

     # Print the candidate vote dictionary.
     print(candidate_votes)  

# Determine the percentage of votes for each candidate by looping through the counts.
     # Iterate through the candidate list.
     for candidate_name in candidate_votes:
          # Retrieve vote count of a candidate.
          votes = candidate_votes[candidate_name]
          # Calculate the percentage of votes.
          vote_percentage = float(votes) / float(total_votes) * 100

          #  To do: print out each candidate's name, vote count, and percentage of
          # votes to the terminal.
          # 4. Print the candidate name and percentage of votes.
          print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")    
          # Determine winning vote count and candidate
          # Determine if the votes is greater than the winning count.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # If true then set winning_count = votes and winning_percent =
               # vote_percentage.
               winning_count = votes
               winning_percentage = vote_percentage
               # And, set the winning_candidate equal to the candidate's name.
               winning_candidate = candidate_name

               #  To do: print out the winning candidate, vote count and percentage to
               #   terminal.
               # To do: print out each candidate's name, vote count, and percentage of
               # votes to the terminal.
          print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
     winning_candidate_summary = (f"-------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"-------------------------\n")
     print(winning_candidate_summary)