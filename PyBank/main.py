import os
import csv
# make list for profit and loss
profit_loss = []
# make variable for total pl

# Set path for file
Budget_Data_csv = os.path.join("..","shona","Bootcamp_Course","GIT_repos","Python-Challenge","PyBank","Resources","Budget_data.csv")
# Open and read csv
with open(Budget_Data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # First row is a header 
    csv_header = next(csv_file)
    # count rows as months and print result
    months = len(list(csv_file))
    for row in csv_file:
        amount = int(row[2])
        profit_loss.append(amount)
        total_pl = sum(amount)
print("Total number of months covered is = "+str(months))
print(" and the total profit and loss across these months is = $"+str (total_pl))