# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
total_sum = 0
nchange = 0
nchange_total = 0
nxt_profit = 0
months = []
greatest_increase = 0
greatest_decrease = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    for row in reader:
        months.append(row[1])
        first_profit = int(row[1])
        break

    # Track the total and net change
    total_sum = first_profit
    
    # Process each row of data
    for row in reader:
        months.append(row[0])

        # Track the total
        total_sum += int(row[1])

        # Track the net change
        nxt_profit = int(row[1])
        nchange = nxt_profit - first_profit
        nchange_total += nchange

        # Calculate the greatest increase in profits (month and amount)
        if nchange > greatest_increase:
            greatest_increase = nchange
            gi_month = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if nchange < greatest_decrease:
            greatest_decrease = nchange
            gd_month = row[0]
        
        first_profit = nxt_profit

# Calculate the average net change across the months
avg_change = nchange_total / (len(months)-1)

# Generate the output summary & print the output
output = (
    "Financial Analysis\n"
    "-------------------\n"
    f"Total Months: {len(months)}\n"
    f"Total: ${total_sum}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {gi_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {gd_month} (${greatest_decrease})\n"
)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
