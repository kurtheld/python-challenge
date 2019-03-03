# Import os Module to create file path
import os

# Import csv module to read .csv file
import csv

# Set path for file for PyBank
csvpath = os.path.join("election_data.csv")
# csvpath = 'election_data.csv'

# Check path
# print(csvpath)

# Open the CSV file
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # list header row
    header_row = next(csv_reader, None)

    # List Variables  
    line_count = 0
    total_votes = 0
    cand_list = []
    cand_totals = []
    index = 0
    highest = 0
    highest_name = ""

#   functionality
    for row in csv_reader:
        total_votes += 1
        if row[2] in cand_list:
            # Candidates on the list
            index = cand_list.index(row[2])
            cand_totals[index] += 1
        else:
            # Candidates NOT on the list
            cand_list.append(row[2])
            cand_totals.append(1)
    
  # Print Results
    print("")
    print("")
    print("Election Results")
    print("----------------------------")
    print("Total Votes:",total_votes)
    print('----------------------------')
    line_count = 0
    max = len(cand_list)
    for max in cand_list:
        percentage = cand_totals[line_count] / total_votes * 100
        print(f'{cand_list[line_count]}: {percentage:.3f}% ({cand_totals[line_count]})')
        if percentage > highest:
           highest = percentage
           highest_name = cand_list[line_count]
        line_count += 1
    print("----------------------------")
    print("Winner: ", highest_name)
    print("----------------------------")