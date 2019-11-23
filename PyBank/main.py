## BANK FINANCIAL ANALYSIS
# Script Dependencies
import os
import pandas as pd

# Open CSV file resource
csvfile = "Resources/budget_data.csv"
budget_df = pd.read_csv(csvfile)
budget_index_df = budget_df.set_index("Profit/Losses")
# print(budget_df.head()) #test readability

# Formulas
months_count = budget_df["Date"].count()
total_profit = budget_df["Profit/Losses"].sum()
profit_diff_avg = round((budget_df["Profit/Losses"]-budget_df["Profit/Losses"].shift(1)).mean(), 2)
max_profit = budget_df["Profit/Losses"].max()
max_month = budget_index_df.loc[max_profit,"Date"]
min_profit = budget_df["Profit/Losses"].min()
min_month = budget_index_df.loc[min_profit,"Date"]

# Print Preview
print("-----------------------------------")
print("~ FINANCIAL ANALYSIS PREVIEW ~")
print("-----------------------------------")
print(f"Total Months: {months_count}")
print(f"Total: ${total_profit}")
print(f"Average monthly Profit/Loss: ${profit_diff_avg}")
print(f"Largest Profit: {max_month}, ${max_profit}")
print(f"Largest Loss: {min_month}, ${min_profit}")
print("-----------------------------------")
print(f"* See new text report 'budget_report.txt'")
print(" ")

# Create file and destination:
output_path = os.path.join("budget_report.txt")

# Write Report
with open(output_path, 'w', newline='') as text_file:
    text_file.write("FINANCIAL ANALYSIS:" + "\n")
    text_file.write("-----------------------------------" + "\n")
    text_file.write(f"Total Months: {months_count}" + "\n")
    text_file.write(f"Total: ${total_profit}" + "\n")
    text_file.write(f"Average monthly Profit/Loss: ${profit_diff_avg}" + "\n")
    text_file.write(f"Largest Profit: {max_month}, ${max_profit}" + "\n")
    text_file.write(f"Largest Loss: {min_month}, ${min_profit}")

# Close
text_file.close