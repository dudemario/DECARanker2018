# DECARanker2018
Ranks DECA Provincials competitors by overall, exam, or oral scores.

Creator: Victor Sun

Date: July 29, 2018

Program: Ranker for 2018 DECA Provincials Competition

### SQL Version

Main Program File: dbRanker.py

Imported File: dbSetup.py

### Data Structure (Classes, Arrays, and Dictionaries) Version

Main Program File: ProvsRanker.py

Imported Files: rankerFunctions

**Functions:**

Rank(\<Event Name>, \<Sort By>):
Event Name must be a DECA event in its abbreviated form, enclosed in quotations.
Ranks all competitors in the event according to the sorting attribute specified.
Sort By is one of: "overall", "exan", "oral1", or "oral2".
Examples:
Rank("ACT", "overall")

Find(<ID/Name>, \<Sort By>):
Use (DECA Provincial ID) or (first and last name seperated by a space), enclosed in quotations.
Locates the competitor and ranks that event. "Here" is displayed beside the competitor's rank in the output files.
Sort By is same as above.
Examples:
Find("Victor Sun", "exam");
Find("10151", "oral1")

AllFrom(\<School Name>, \<Sort By>):
School Name, usually with abbreviated ending such as HS, SS, CI, etc., enclosed in quotations.
Ranks every competitor from the school according to their rank in their respective events.
First ranks all the individual events, then all the team events.
Sort By is same as above
Examples:
AllFrom("Iroquois Ridge HS", "oral2")

**International Scores: (Only for data structure version)**

First score is for exam,
Next 1/2 scores is for preliminary orals,
Last score is for final case if qualified, denoted with an "F" in front of the score.
