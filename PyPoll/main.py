### ELECTION ANALYSIS
# Script Dependencies
import os
import pandas as pd

# >>> Open CSV file resource and define dataframe
csvfile = "Resources/election_data.csv"
election_df = pd.read_csv(csvfile)
    # # ------ dataframe preview ------ 
    # print(election_df.head()) 
    # # headers preview
    # print(election_df.columns) = ['Voter ID', 'County', 'Candidate']

# >>> Find total number of votes 
all_votes = election_df["Candidate"].count()
    # # ------ total preview ------ 
    # print(all_votes)
    # print(all_votes.dtype) # confirmed that value is int32

# >>> Summary: Group by Candidates
candidate_summary_df = election_df.groupby(["Candidate"])
# Count number of votes by Candidate group
candidate_summary_df = candidate_summary_df.count()
# Total Votes - Take the totals counted above and assign to name "Total Votes"
candidate_summary_df["Total Votes"] = candidate_summary_df["Voter ID"]
# Percent Votes - Add a percent column and format to rounded %
candidate_summary_df["Percent Votes"] = ((candidate_summary_df["Total Votes"] / all_votes)*100).map("{:,.1f}%".format)
# Finalize new data frame and reset index from the groupby
final_summary_df = (candidate_summary_df[["Total Votes","Percent Votes"]]).reset_index()
    # # ------ Preview Final Summary ------
    # print(final_summary_df)

# >>> Find the winner
most_votes = final_summary_df["Total Votes"].max()
    # # ------ preview most votes for a candidate ------
    # print(most_votes)
winner_name = final_summary_df.loc[final_summary_df["Total Votes"] == most_votes, "Candidate"].values[0]
    # # ------ preview winner name ------
    # print(winner_name)

# >>> PRINT PREVIEW
print("-----------------------------------")
print("~ ELECTION RESULTS PREVIEW ~")
print("-----------------------------------")
print(f"All Votes Cast: {all_votes}")
print("Results:")
print(final_summary_df)
print("-----------------------------------")
print(f"Popular vote winner: {winner_name} with {most_votes} votes!")
print("-----------------------------------")
print(f"* See new text report 'election_report.txt'")
print("")

# >>> Create file and destination:
output_path = os.path.join("election_report.txt")

# Write Report
with open(output_path, 'w', newline='') as text_file:
    text_file.write("ELECTION RESULTS:" + "\n")
    text_file.write("-----------------------------------" + "\n")
    text_file.write(f"All Votes Cast: {all_votes}" + "\n")
    text_file.write(f"{final_summary_df}" + "\n")
    text_file.write("-----------------------------------" + "\n")
    text_file.write(f"Popular vote winner: {winner_name} with {most_votes} votes!")
    
# Close
text_file.close