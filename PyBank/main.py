import pandas as pd
import csv
import os

# Path to collect data from the Resources folder
pybank = "/Users/royjiang/Desktop/python-challenge/PyBank/Resources/budget_data.csv"

pybank_df = pd.read_csv(pybank)

pybank_df["Profit/Losses"].head()

total = pybank_df["Profit/Losses"].sum()

Total_month = len(pybank_df)

difference_df = pybank_df["Profit/Losses"].diff()

difference_df = difference_df.fillna(0)
average_difference = difference_df.sum()/(Total_month-1)


# Read in the CSV file
with open(pybank, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        great = difference_df.max()
        great_row = difference_df.idxmax() + 1
        great_month = pybank_df["Date"].iloc[great_row-1] 

        low = difference_df.min()
        low_row = difference_df.idxmin() + 1
        low_month = pybank_df["Date"].iloc[low_row-1] 


print("Finalcial Analysis")
print("----------------------")
print("Total Months:" + str(Total_month))
print("Total :" + "$"+str(total))
print("Average Change:" + str(average_difference))
print("Greatest Increase in Profit: " + great_month + "($" + str(great) + ")")

print("Greatest decrease in Profit: " + low_month + "($" + str(low) + ")")


output = '/Users/royjiang/Desktop/python-challenge/PyBank/output.txt'

#  Open the output file
with open(output, "w") as datafile:
    
    datafile.write("Finalcial Analysis")

    datafile.write("\n-------------------")

    datafile.write("\nTotal Months:" + str(Total_month))

    datafile.write("\nTotal :" + "$"+str(total))
    datafile.write("\nAverage Change:" + str(average_difference))
    datafile.write("\nGreatest Increase in Profit: " + great_month + "($" + str(great) + ")")
    datafile.write("\nGreatest decrease in Profit: " + low_month + "($" + str(low) + ")")
datafile.close()