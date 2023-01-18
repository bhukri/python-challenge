#import the dependent modules
import os
import csv

# Set path for the csv file 
csvpath = os.path.join(".", "Resources", "election_data.csv")

#Read using the CSV module
with open(csvpath, encoding='utf') as csvfile:

    #CSV reader specifies the delimiter and variable that holds contents
    csvreader=csv.reader(csvfile, delimiter=',')  
    #Read the header row since there is header 
    header=next(csvreader) 

    #Lists to store data
    voterids=[]  
    counties=[]  
    candidates=[]
    candidate_list=[] 
    total_votes_can=[] 
    can_vote_perc=[] 
    results=[] 
   
    #initialize 
    total_votes=0
    total_candidates=0
    winnervotes=0
    
    #Read in each row of data after the header and write data into the lists
    for row in csvreader:
        #Assign column 0 as voterid
        voterid=row[0] 
        #Assign column 1 as county
        county=row[1] 
        #Assign column 2 as candidate
        candidate=row[2] 
        #Add/append each row to the voterid List
        voterids.append(voterid)
        ##Add/append each row to the county List  
        counties.append(county)  
        #Add/append each row to the candicates List
        candidates.append(candidate) 
    
    #find the total number of votes from the length of the voter id list.
    total_votes= len(voterids) 

#Load the first record from the candidate list to the candidate list 
candidate_list.append(candidates[0]) 

#Loop through to identify the unique candidate names
for a in range (total_votes-1):
    if candidates[a+1] != candidates[a] and candidates[a+1] not in candidate_list:
        candidate_list.append(candidates[a+1])

    #find the total number of candidates from the length of Candidate names list
    total_candidates=len(candidate_list)

#For the total no. of candidates loop through the list to calculate the total votes each candidate got using count fn
for b in range (total_candidates): 
    total_votes_can.append(candidates.count(candidate_list[b])) 

#Loop through to the total number of candidates to calculate the each candidates vote percentage 
for x in range(total_candidates):  
    #vote percentage calculation with rounding to 3 decimal points and append % to it
    can_vote_perc.append(f'{round((total_votes_can[x]/total_votes*100), 3)}%') 

    #find the winner with the total votes count comparison
    if total_votes_can[x]>winnervotes: 
        winner=candidate_list[x]
        winnervotes=total_votes_can[x]

# store the results list for each candidate with name, percentage votes and total votes
for y in range(total_candidates):
    results.append(f'{candidate_list[y]}: {can_vote_perc[y]} ({total_votes_can[y]})')  
    #prepare the result in the block format for output
    resultblock='\n'.join(results)  

#print analysis output
analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {total_votes}\n\
----------------------------\n\
{resultblock}\n\
----------------------------\n\
Winner: {winner} \n\
----------------------------\n'

#print the analysis result to the terminal 
print(analysis) 

#Write the analysis result to the txt file
#set the output file path and name
output_path = os.path.join(".", "analysis", "PyPoll_analysis.txt")

#open the output file or create if it doesn't exist
output_file=open(output_path,"w") 
#write the analysis result to PyBank_analysis.txt
output_file.writelines(analysis)  
#close the txt file
output_file.close() 