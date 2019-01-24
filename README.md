# DECARanker2018
Ranks DECA Provincials competitors by overall, exam, or oral scores.

Creator: Victor Sun

Date: July 29, 2018

Program: Ranker for 2018 DECA Provincials Competition and International Scores

### SQL Version

Main Program File: dbRanker.py

Setup File: dbSetup.py

Functions:

Rank(\<Event Name>):
Event Name must be a DECA event in its abbreviated form, enclosed in quotations.
Ranks all competitors in the event according to the sorting attribute specified.
Sort By is one of: "Overall Score", "Exam Score", "Oral 1 Score", or "Oral 2 Score".
Examples:
Rank("ACT", "Overall Score")

### Additional Functions in Data Structure Version

Main Program File: ProvsRanker.py

Imported Files: rankerFunctions

Find(<ID/Name>):
Use (DECA Provincial ID) or (first and last name seperated by a space), enclosed in quotations.
Locates the competitor and ranks that event. "Here" is displayed beside the competitor's rank in the output files.
Sort By is same as above.
Examples:
Find("Victor Sun", "Exam Score");
Find("10151", "Oral 1 Score")

AllFrom(\<School Name>):
School Name, usually with abbreviated ending such as HS, SS, CI, etc., enclosed in quotations.
Ranks every competitor from the school according to their rank in their respective events.
First ranks all the individual events, then all the team events.
Sort By is same as above
*Note: This function takes a while longer than the rest
Examples:
AllFrom("Iroquois Ridge HS", "Oral 2 Score")

Note for International Scores:
First score is for exam,
Next 1/2 scores is for preliminary orals,
Last score is for final case if qualified, denoted with an "F" in front of the score.
