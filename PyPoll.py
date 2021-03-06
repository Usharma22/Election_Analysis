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
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.

winning_candidate=""
winning_count =0

winning_percentage=0


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
     #print(candidate_votes)  
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
