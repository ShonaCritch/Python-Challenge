# Modules
import os
import csv
# Set path for file
Budget_Data_csv = os.path.join("..","shona","Bootcamp_Course","GIT_repos","Python-Challenge","PyBank","Resources","Budget_data.csv")
with open (Budget_Data_csv) as Budget_csv:
    csvreader = csv.reader(Budget_csv, delimiter=",")
    csv_header = next(Budget_csv)
    print(f"Header: {csv_header}")