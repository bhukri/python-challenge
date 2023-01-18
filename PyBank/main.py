#import the dependent modules
import os
import csv

# Set path for the csv file 
csvpath = os.path.join(".", "Resources", "budget_data.csv")

#Read using the CSV module
with open(csvpath, encoding='utf') as csvfile:

    #CSV reader specifies the delimiter and variable that holds contents
    csvreader=csv.reader(csvfile, delimiter=',') 
    #Read the header row since there is header 
    header=next(csvreader) 

    #Lists to store data
    months=[]  
    profitloss=[]  

    #initialize
    total=0
    total_months=0
    avg_change=0
    monthly_change=0

    grt_inc=0
    grt_dec=0
    grt_inc_mon=0
    grt_dec_mon=0

    #Read in each row of data after the header and write data into the lists declared
    for row in csvreader:
        #Assign column 0 as month
        month=row[0] 
        #Assign column 1 as profitloss
        proloss=row[1] 
        #Add/append each row to the months List
        months.append(month) 
        #Add/append each row to the profitloss list
        profitloss.append(proloss) 
    
    #find the total months from the length of the list.
    total_months = len(months) 

#Loop through each record to calculate the total amount
for x in range (total_months):
    total=total+int(profitloss[x])  

#Loop through each record to calculate the Profit/Losses details
for y in range (total_months-1): 
    #calculate average change in the Profit/Losses
    avg_change=avg_change+(float(profitloss[y+1])-float(profitloss[y]))  

    #Greatest Increase and Decrease in Profit/Losses 
    #Calculate the monthly change in Profit/Losses
    monthly_change=(float(profitloss[y+1])-float(profitloss[y])) 
    
    #check if monthly change is greater than the current Greatest increase stored
    if monthly_change>grt_inc:
        #set greatest increase with the monthly change
        grt_inc=monthly_change
        #set greatest increase month with the corresponding month
        grt_inc_mon=y
    else:
        #retain the current greatest increase amount
        grt_inc=grt_inc

    #check if monthly change is greater than the current Greatest decrease stored
    if monthly_change<grt_dec:  
        #set greatest decrease with the monthly change
        grt_dec=monthly_change
        #set greatest decrease month with the corresponding month
        grt_dec_mon=y
    else:
        #retain the current greatest decrease amount
        grt_dec=grt_dec

#print analysis output
analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {total_months}\n\
Total : ${total}\n\
Average Change: ${round(avg_change/(total_months-1),2)}\n\
Greatest Increase in Profits: {months[grt_inc_mon+1]} (${int(grt_inc)})\n\
Greatest Decrease in Profits: {months[grt_dec_mon+1]} (${int(grt_dec)})\n'

#print the analysis result to the terminal 
print(analysis)

#Write the analysis result to the txt file
#set the output file path and name
output_path = os.path.join(".", "analysis", "PyBank_analysis.txt")

#open the output file or create if it doesn't exist
output_file=open(output_path,"w") 
#write the analysis result to PyBank_analysis.txt
output_file.writelines(analysis)  
#close the txt file
output_file.close()  