# This is HW3 - Budget Case

# First I have to read the data

import os
import csv

csvpath = os.path.join('..', 'pyPoll', 'election_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

count = 0


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    sort_src = []
    # Read each row of data after the header
    for row in csvreader:
        count +=1
        sort_src.append(row[2])
 
    print("Total Votes: " + str(count))
    
    seen = {}
    for row in sort_src:
        seen[row] = seen.get(row,0) + 1


    for r in seen:
            print(r,":",'{:.3%}'.format(seen[r]/count), + seen[r])
    
    newlist = list()
    newlist2 = list()
    for i in seen.keys():
        newlist.append(i)
    for i in seen.values():
        newlist2.append(i)
    max_vote = (max(newlist2))
    ind_max = int((newlist2.index(max_vote)))
    winner = newlist.pop(ind_max)
    #print(ind_max)
    #print(newlist)
    #print(newlist2)
    print("Winner: " + winner)

    # python /path/to/script/myscript.py > /path/to/output/myfile.txt