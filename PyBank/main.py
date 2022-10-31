import csv
import numpy as np

#open file
pybank_csv = "/Users/royjiang/Desktop/python-challenge/PyBank/Resources/budget_data.csv"
# Read in the CSV file
with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    rowcount = 0
    profit_loss = 0
    change_list = []
    pre_value = 0
    list_date = []
    # Loop through the data
    for row in csvreader:
        rowcount+=1
        #find total profit or loss
        profit_loss = profit_loss + int(row[1])
        change =  int(row[1]) - pre_value
        pre_value = int(row[1])
        change_list.append(change)
        great  = max(change_list)
        list_date.append(row[0])

    
    change_list[0] = 0       
    total_change = 0
    for num in change_list:
        total_change = total_change + num



end_list = list(zip(change_list, list_date))

value, date = max(end_list)     
value_low, date_low = min(end_list)



      
# find total months
total = rowcount
average_change = total_change/(total - 1)

print("Finalcial Analysis")
print("----------------------")
print("Total Months:" + str(total))
print("Total :" + "$"+str(profit_loss))
print("Average Change:" + str(round(average_change,2)))
print("Greatest Increase in Profit: " + date + " ($" + str(value) + ")")
print("Greatest decrease in Profit: " + date_low + " ($" + str(value_low) + ")")




output = '/Users/royjiang/Desktop/python-challenge/PyBank/output.txt'

#  Open the output file
with open(output, "w") as datafile:
    
    datafile.write("Finalcial Analysis")

    datafile.write("\n-------------------")

    datafile.write("\nTotal Months:" + str(total))

    datafile.write("\nTotal :" + "$"+ str(profit_loss))
    datafile.write("\nAverage Change:" + str(round(average_change,2)))
    datafile.write("\nGreatest Increase in Profit: " + date + " ($" + str(value) + ")")
    datafile.write("\nGreatest decrease in Profit: " + date_low + " ($" + str(value_low) + ")")

    
datafile.close()