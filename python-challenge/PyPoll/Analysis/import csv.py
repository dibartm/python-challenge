import csv
import os


# Add variable to load a file 
file_to_load = os.path.join("resources", "election_data.csv")
# Add a variable to save the final file 
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Start a total vote counter.
total_votes = 0

# Add candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# Add variables for the winning candidate, vote count and winning percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Use to read the csv and convert it into a list of dictionaries

with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    reader = csv.reader(election_data)

    # To read the header
    header = next(reader)

    # Read each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]


        # Create if for if name does not match any existing candidate 
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking candidate voter count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1



# Use to save results in text file 
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
    )
    print(election_results, end="")


    # Use to save final vote count to the text file.
    txt_file.write(election_results)

    # Save final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Use to retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

        # Use to print each candidate's voter count and percentage to the terminal
        
        print(candidate_results)
        #  Save the candidate results to the  text file.
        txt_file.write(candidate_results)

        # Use to find out winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)