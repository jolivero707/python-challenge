# This is HW3 - Budget Case

# First I have to read the data

import os
import csv

csvpath = os.path.join('..', 'pyBank', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

count = 0
total = 0
revenue_changes = []
month = []
prev_rev = 0
total_rev_ch = 0
i = 0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print("Financial Analysis")
    print("___________________")
    month=[]
    # Read each row of data after the header
    for row in csvreader:
        month.append(row[0])
        count +=1
        total += float(row[1])
        if (count == 1):
        #    prev_rev = int(row[1])
            revenue_changes.append(0) 
            prev_rev = int(row[1])
        elif (count > 1):                           
             revenue_changes.append(int(row[1]) - prev_rev)
     #   revenue_changes =int(row[1]) - prev_rev
             prev_rev = int(row[1])
    
    print("Total months : " + str(count))    
    #print(count)
    print("Total: "+ '${:,.2f}'.format(total))
    
    #print(total)  
    #print(revenue_changes)
       
    min_rev_ch = 0
    max_rev_ch = 0
    ind_max = 0
    max_month = 0
    
    for row in revenue_changes:
        max_rev_ch = max(revenue_changes)
        min_rev_ch = min(revenue_changes)
    
        total_rev_ch += row
    
    ind_max = int((revenue_changes.index(max_rev_ch)))
    ind_min = int((revenue_changes.index(min_rev_ch)))
    
    #print(ind_max)
    
    count1 = 0
    
    #print(month)
    
   # for row in month:
#    if row == ind_max:
    max_month = month.pop(ind_max)
    min_month = month.pop(ind_min)
    #print(max_month)
    #print(min_month)
    
    #print('${:,.2f}'.format(total_rev_ch))
    #print(total_rev_ch)
    print("Average Change: " + '${:,.2f}'.format(total_rev_ch/(count-1)))
    print("Greatest Increase in Profits: " + max_month +"(" + '${:,.2f}'.format(max_rev_ch) +")" )
    print("Greatest Decrease in Profits: " + min_month +"(" + '${:,.2f}'.format(min_rev_ch) +")" )
    #print (max_rev_ch)
    #print (min_rev_ch)
        


