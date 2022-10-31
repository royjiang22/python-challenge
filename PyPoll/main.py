import csv
import numpy as np

#open file
pypoll_csv = "/Users/royjiang/Desktop/python-challenge/PyPoll/Resources/election_data.csv"

with open(pypoll_csv, 'r') as pypoll_csvfile:

    # Split the data on commas
    csvreader = csv.reader(pypoll_csvfile, delimiter=',')

    header = next(csvreader)
    rowcount = 0
    
    name_list = [ ]
    # Loop through the data
    for row in csvreader:
        rowcount+=1
        names = str(row[2])
        name_list.append(names)
    
    res = np.array(name_list)
    unique_res = np.unique(res)

name1 = name_list.count("Charles Casper Stockham")
name2 = name_list.count("Diana DeGette")
name3 = name_list.count("Raymon Anthony Doane")

name1_percentage = (name1/rowcount)*100
name2_percentage = (name2/rowcount)*100
name3_percentage = (name3/rowcount)*100


print("Election Results")
print("----------------------")
print("Total Votes: " + str(rowcount))
print("----------------------")
print(unique_res[0] + ": " + str(round(name1_percentage,3)) + "% " + "(" + str(name1) + ")")
print(unique_res[1] + ": " + str(round(name2_percentage,3)) + "% " + "(" + str(name2) + ")")
print(unique_res[2] + ": " + str(round(name3_percentage,3)) + "% " + "(" + str(name3) + ")")
print("----------------------")

if name1_percentage > name2_percentage and name1_percentage > name2_percentage:
    print("Winner: " + unique_res[0])
elif name2_percentage > name1_percentage and name2_percentage > name3_percentage:
    print("Winner: " + unique_res[1])
else:
    print("Winner: " + unique_res[2])

print("----------------------")

output2 = '/Users/royjiang/Desktop/python-challenge/PyPoll/analysis/output.txt'


#  Open the output file
with open(output2, "w") as datafile:
    
    datafile.write("Election Results")
    datafile.write("\n-------------------")
    datafile.write("\nTotal Votes: " + str(rowcount))
    datafile.write("\n-------------------")

    datafile.write("\n" + unique_res[0] + ": " + str(round(name1_percentage,3)) + "% " + "(" + str(name1) + ")")
    datafile.write("\n" + unique_res[1] + ": " + str(round(name2_percentage,3)) + "% " + "(" + str(name2) + ")")
    datafile.write("\n" + unique_res[2] + ": " + str(round(name3_percentage,3)) + "% " + "(" + str(name3) + ")")
    datafile.write("----------------------")
    datafile.write("\ndatafile.writeWinner: " + unique_res[1])

datafile.close()
