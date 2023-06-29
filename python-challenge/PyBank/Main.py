# import libraries
import os
import csv

# Create the path for budget_data
budget_csv = os.path.join("Resources", "budget_data.csv")

# read csv data
with open(budget_csv) as my_file:
    csvreader = csv.DictReader(my_file, delimiter=",")

    # Create a list for 'Date' and for 'Profit/Losses' 
    l_month = []
    l_profit = []

    # Store both of my columns into separate lists using 'append'
    for row in csvreader:
        l_month.append(row["Date"])
        l_profit.append(row["Profit/Losses"])

    

    # calculate the total for the second column
    total = 0
    for i in range(0, len(l_profit)):
        total = int(total) + int(l_profit[i])
        
    

    # Calculate the monthly change in revenue
    rev_change = [] 

    for i in range(1, len(l_profit)):
        rev_change.append(int(l_profit[i]) - int(l_profit[i - 1]))
        
    #calculate the average revenue change
    rev_avg = round(sum(rev_change) / len(rev_change), 2)
    

    max_increase = max(rev_change)
    
    max_decrease = min(rev_change)
    


    # Print section
    print(" ")
    
    print("Financial Analysis")

    print("----------------------------")

    print("Total Months: " + str(len(l_month)))

    print("Total: " + str(total))

    print("Average Change: " + "$" + str(rev_avg))

    print(
        "Greatest Increase in Profits: " +
        str(l_month[rev_change.index(max(rev_change)) + 1]) +
        " " + "($" + str(max_increase) + ")"
        )
        
    print(
        "Greatest Decrease in Profits: " +
        str(l_month[rev_change.index(min(rev_change)) + 1]) +
        " " + "($" + str(max_decrease) + ")"
        )
        
        
    # export a text file with the results
    file = open("evidence.txt", "w")

    file.write("Financial Analysis" + "\n")
    
    file.write("Total Months: " + str(len(l_month)) + "\n")
    file.write("Total: " + str(total) + "\n")
    file.write("Average Change: " + "$" + str(rev_avg) + "\n")
    file.write(
        "Greatest Increase in Profits: " +
        str(l_month[rev_change.index(max(rev_change)) + 1]) +
        " " + "($" + str(max_increase) + ")" + "\n"
    )
    file.write(
       "Greatest Decrease in Profits: " +
        str(l_month[rev_change.index(min(rev_change)) + 1]) +
        " " + "($" + str(max_decrease) + ")" + "\n" 
    )  

    file.close()  