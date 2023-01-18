import os
import csv

# Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")

with open(csvpath, encoding='utf') as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',') #Specify delimiter and variable that holds contents
    header=next(csvreader) #Read the header row first

    #Prepare variables
    voterids=[] #Generate list named "voterids" for the "Voter ID" column
    counties=[] #Generate list named "counties" for the "County" column
    candidates=[] #Generate list named "candidates" for the "Candidate" column
    candidatenames=[] #Generate list for actual candidate names
    totaleachcan=[] #Generate list for total votes for each found candidate
    resultprintcan=[] #Generate list for result printout of each found candidate
    totaleachcanperc=[] #Generate list for percentage of votes for each found candidate

    #Set start conditions
    line_count=0
    winnervotes=0
    loservotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    
    #Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        voterid=row[0] #Assign column 0 as voterid
        county=row[1] #Assign column 1 as county
        candidate=row[2] #Assign column 2 as candidate
        voterids.append(voterid) #Add next line to list voterids
        counties.append(county) #Add next line to list counties
        candidates.append(candidate) #Add next line to list candidates
    
    line_count= len(voterids) #Count the total number of votes cast in the "Voter ID" column
    
    #print(line_count)

#Begin data analysis

candidatenames.append(candidates[0]) #Pre-loadfirst candidate name for comparison

#First loop is through the list of candidates to determine candidates voted for (variable loop1 as loop index counter)
for loop1 in range (line_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
        candidatenames.append(candidates[loop1+1])

n=len(candidatenames)

#print(n)

#Second loop variable loop2 as loop index counter
for loop2 in range (n): #Range of loop depending on how many candidates were found
    totaleachcan.append(candidates.count(candidatenames[loop2])) #Count total votes of candidates and add to list total

#print(candidatenames)
#print(totaleachcan)

#Third loop variable loop3 as loop index counter

loservotes=line_count #Pre-load loservoters with maximum votes for < comparison

for loop3 in range(n): #Range of loop depending on how many candidates were found
    totaleachcanperc.append(f'{round((totaleachcan[loop3]/line_count*100), 3)}%') #Calculate % per candidate found
    if totaleachcan[loop3]>winnervotes: #Find candidate with highest vote count
        winner=candidatenames[loop3]
        winnervotes=totaleachcan[loop3]
    if totaleachcan[loop3]<loservotes: #Find candidate with lowest vote count
        loser=candidatenames[loop3]
        loservotes=totaleachcan[loop3]

#Fourth loop variable loop4 as loop index counter
for loop4 in range(n):
    resultprintcan.append(f'{candidatenames[loop4]}: {totaleachcanperc[loop4]} ({totaleachcan[loop4]})') #Format list resultprintcan

resultlines='\n'.join(resultprintcan) #Prepare new combined list of results for printout (each candidate with the result gets a new line)

#Generate output lines

analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} \n\
----------------------------\n'

print(analysis) #Output results on screen

#Write into text file named pypoll.txt
output_path = os.path.join(".", "analysis", "PyPoll_analysis.txt")

file1=open(output_path,"w") #Open or if file does not exist then create file named pypoll.txt
file1.writelines(analysis) #Write analysis into pypoll.txt
file1.close() #Close pypoll.txt write mode