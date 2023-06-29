# import libraries
import os
import csv

# Create path
election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as my_file:
    csvreader = csv.DictReader(my_file, delimiter=",")
    
    ballot = []
    county = []
    candidate = []
    

    for row in csvreader:
        ballot.append(row["Ballot ID"])
        county.append(row["County"])
        candidate.append(row["Candidate"])
    
    # Print the total number of registered ballots  
    num_values = len(ballot) 
    print(num_values)

    # find unique values in the 'candidate' variable
    set_candidates = set(candidate)
    
    list_candidates = (list(set_candidates))

    for item in list_candidates:
        print(item)
    
    print(list_candidates)
    

    # create variables that contain the total number and overall percentage of each candidate.
    stockham_count = candidate.count("Charles Casper Stockham")
    stockham_pct = "{:.1%}".format(round(stockham_count / len(candidate), 3))

    doane_count = candidate.count("Raymon Anthony Doane")
    doane_pct = "{:.1%}".format(round(doane_count / len(candidate), 3))

    degette_count = candidate.count("Diana DeGette")
    degette_pct = "{:.1%}".format(round(degette_count / len(candidate), 3))

    # select winner
    if stockham_pct > max(doane_pct, degette_pct):
        winner = "Charles Casper Stockham"
    elif doane_pct > max(stockham_pct, degette_pct):
        winner = "Raymon Anthony Doane"
    else:
        winner = "Diana DeGette"


# Print section
print(" ")
print("Election Results")
print(" ")
print("-------------------------")
print(" ")
print("Total votes: ", len(ballot))
print(" ")   
print("-------------------------") 
print(" ")
print("Charles Casper Stockham:",stockham_pct, "(",stockham_count,")")
print("Diana DeGette:", degette_pct, "(",degette_count,")")
print("Raymon Anthony Doane:", doane_pct, "(",doane_count,")")
print(" ")
print("-------------------------")
print(" ")
print("Winner:", winner)


# export a text file with the results

file = open("evidence.txt", "w")

file.write("Election Results" + "\n")
file.write("-------------------------" + "\n")

file.write("Total votes: " + str(len(ballot)) + "\n")
file.write("-------------------------" + "\n")

file.write("Charles Casper Stockham: " + str(stockham_pct) + " (" + str(stockham_count) + ") " + "\n")
file.write("Diana DeGette: " + str(degette_pct) + " (" + str(degette_count) + ") " + "\n")
file.write("Raymon Anthony Doane: " + str(doane_pct) + " (" + str(doane_count) + ") " + "\n")
file.write("-------------------------" + "\n")

file.write("Winner: " + winner + "\n")

file.close()


    

        