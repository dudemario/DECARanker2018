'''
Creator: Victor Sun
Date: July 29, 2018
Program: Ranker for 2018 DECA Provincials Competition and International Scores
Imported Files: rankerFunctions

Program Functions:
-Writes to output.txt nicely formatted and in output.tsv for spreadsheet applications
-Use #Hashtag to comment out code, stopping the program from running that function


Rank(<Event Name>, <Sort By>):
Event Name must be a DECA event (non-written) in its abbreviated form, enclosed in quotations.
Ranks all competitors in the event according to the sorting attribute specified.
Sort By is one of: "Overall Score", "Exam Score", "Oral 1 Score", or "Oral 2 Score"
Examples:
Rank("ACT", "Overall Score")

Find(<ID/Name>, <Sort By>):
Use (DECA Provincial ID) or (first and last name seperated by a space), enclosed in quotations.
Locates the competitor and ranks that event. "Here" is displayed beside the competitor's rank in the output files
Sort By is same as above
Examples:
Find("Victor Sun", "Exam Score")
Find("10151", "Oral 1 Score")

AllFrom(<School Name>, <Sort By>):
School Name, usually with abbreviated ending such as HS, SS, CI, etc., enclosed in quotations. 
Ranks every competitor from the school according to their rank in their respective events.
First ranks all the individual events, then all the team events.
Sort By is same as above
*Note: This function takes a while longer than the rest
Examples:
AllFrom("Iroquois Ridge HS", "Oral 2 Score")
'''

from rankerFunctions import Rank, Find, AllFrom

#Rank("BLTDM", "Overall Score")
#Find("Rebecca Lee", "Overall Score")
AllFrom("Iroquois Ridge HS", "Overall Score")
print("Written to output.txt and output.tsv")
