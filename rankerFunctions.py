'''
Creator: Victor Sun
Date: July 29, 2018
Program: Functions for DECA Ranker
Imported Files: os
'''
import os
from os.path import join
sortby = {"Overall Score":1,
          "Exam Score":2,
          "Oral 1 Score":3,
          "Oral 2 Score":4}

def getFinalScore(event, chapter, name, name2=""):
    events = {"Apparel and Accessories Marketing Series":"AAM",
              "Accounting Applications Series":"ACT",
              "Automotive Services Marketing Series":"ASM",
              "Business Finance Series":"BFS",
              "Business Growth Plan":"EBG",
              "Business Law and Ethics Team Decision Making":"BLTDM",
              "Business Service Marketing Series":"BSM",
              "Business Services Operations Research":"BOR",
              "Buying and Merchandising Operations Research":"BMOR",
              "Buying and Merchandising Team Decision Making":"BTDM",
              "Creative Marketing Project":"CMP",
              "Community Service Project":"CSP",
              "Entrepreneurship Promotion Project":"EOOPP",
              "Entrepreneurship Series":"ENT",
              "Entrepreneurship Team Decision Making":"ETDM",
              "Fashion Merchandising Promotion Plan":"FMP",
              "Finance Operations Research":"FOR",
              "Financial Consulting":"FCE",
              "Financial Literacy Promotion Project":"FLPP",
              "Financial Services Team Decision Making":"FTDM",
              "Food Marketing Series":"FMS",
              "Franchise Business Plan":"EFB",
              "Hospitality Services Team Decision Making":"HTDM",
              "Hospitality and Tourism Operations Research":"HTOR",
              "Hospitality and Tourism Professional Selling":"HTPS",
              "Hotel and Lodging Management Series":"HLM",
              "Human Resources Management Series":"HRM",
              "Independent Business Plan":"EIB",
              "Innovation Plan":"EIP",
              "International Business Plan":"IBP",
              "Learn and Earn Project":"LEP",
              "Marketing Communications Series":"MCS",
              "Marketing Management Team Decision Making":"MTDM",
              "Personal Financial Literacy":"PFL",
              "Principles of Business Management and Administration":"PBM",
              "Principles of Finance":"PFN",
              "Principles of Marketing":"PMK",
              "Professional Selling":"PSE",
              "Public Relations Project":"PRP",
              "Principles of Hospitality and Tourism":"PHT",
              "Quick Serve Restaurant Management Series":"",
              "Restaurant and Food Service Management Series":"RFSM",
              "Retail Merchandising Series":"RMS",
              "Sports and Entertainment Marketing Operations Research":"SEOR",
              "Sports and Entertainment Marketing Series":"SEM",
              "Sports and Entertainment Marketing Team Decision Making":"STDM",
              "Sports and Entertainment Promotion Plan":"SEPP",
              "Start-up Business Plan":"ESB",
              "Stock Market Game":"",
              "Travel and Tourism Team Decision Making":"TTDM",
              "Virtual Business Challenge Accounting":"",
              "Virtual Business Challenge Fashion":"",
              "Virtual Business Challenge Hotel Management":"",
              "Virtual Business Challenge Personal Finance":"",
              "Virtual Business Challenge Restaurant":"",
              "Virtual Business Challenge Retail":"",
              "Virtual Business Challenge Sports":""}
    for root, folders, files in os.walk(join(os.getcwd(), "data/transcripts")):
        if chapter[:10] in root or chapter[10:] in root:
            n2 = 0
            if name2 != "":
                for f in files:
                    if name2 in f and "txt" in f:
                        fIn = open(join("data/transcripts",root.split("/")[-1], f), encoding="latin-1")
                        for line in fIn:
                            try:
                                n2 = int(line.strip())
                                break
                            except:
                                pass
                        break
            for f in files:
                if name in f and "txt" in f:
                    ar = []
                    fScores = 0
                    arFilled = False
                    eventCorrect = False
                    fIn = open(join("data/transcripts",root.split("/")[-1], f), encoding="latin-1")
                    prevLine = ""
                    for line in fIn:
                        if line[:5] == "Final":
                            fScores += 1
                        try:
                            n = int(line.strip())
                            if not arFilled:
                                if n == sum(ar[:len(ar)-fScores]) and len(ar) != 1:
                                    arFilled = True
                                else:
                                    ar.append(n)
                        except(ValueError):
                            try:
                                if event == "PBM" and line.strip() == "Principles of Business":
                                    eventCorrect = True
                                    break
                                if event == "STDM" and line.strip() == "Sports and Entertainment":
                                    eventCorrect = True
                                    break
                                elif events[prevLine+" "+line.strip()] == event:
                                    eventCorrect = True
                                    break
                                else:
                                    prevLine = line.strip()
                            except(KeyError):
                                try:
                                    if events[line.strip()] == event:
                                        eventCorrect = True
                                        break
                                    else:
                                        prevLine = line.strip()
                                except(KeyError):
                                    prevLine = line.strip()
                                    pass
                    if eventCorrect:
                        for i in range(fScores):
                            ar[len(ar)-i-1] = "F"+str(ar[len(ar)-i-1])
                        if n2:
                            ar[0] = (ar[0] + n2)/2.0
                        return "\t"+"\t".join(map(str,ar))
                    else:
                        return ""
    return ""
        
class Competitor:
    def __init__(self, myID, myEvent, myTeam, myChapter, examScore, oral1Score, oral2Score, myPenalties, overallScore, myChapterID, sortBy):
        self.sort = sortBy
        self.id = myID
        self.event = myEvent
        self.team = myTeam
        self.chapter = myChapter
        self.exam = examScore
        self.oral1 = oral1Score
        self.oral2 = oral2Score
        self.penalties = myPenalties
        self.overall = overallScore
        self.chapterID = myChapterID
    def __str__(self):
        return self.id+"\t"+self.overall
    def __lt__(self, other):
        if self.sort == "Overall Score":
            return self.overall < other.getAttr(1)
        elif self.sort == "Exam Score":
            return self.overall < other.getAttr(2)
        elif self.sort == "Oral 1 Score":
            return self.overall < other.getAttr(3)
        elif self.sort == "Oral 2 Score":
            return self.overall < other.getAttr(4)
    def getAttr(self, attrNum):
        if attrNum == 1:
            return self.overall
        elif attrNum == 2:
            return self.exam
        elif attrNum == 3:
            return self.oral1
        elif attrNum == 4:
            return self.oral2

class Person:
    def __init__(self, myID, firstName, lastName, regional):
        self.id = myID
        self.first = firstName
        self.last = lastName
        self.region = regional
    def __str__(self):
        return self.id+"\t"+self.first+" "+self.last
    def getName(self):
        return self.first+" "+self.last

def getAllPeople():
    fIn = open("data/Timetables.csv", "r", encoding="latin-1")
    fIn.readline()
    allPeople = {}
    try:
        for line in fIn:
            line = line.strip().split(",")
            allPeople[int(line[13])] = Person(line[13], line[17], line[18], line[32])
    except(UnicodeDecodeError):
        print(fIn.readline())
        print(fIn.readline())
    fIn.close()
    return allPeople

def getAllScores(event, sortBy):
    fIn = open("data/scores.txt", "r", encoding="latin-1")
    eventScores = []
    for line in fIn:
        line = line.strip().split(" ")
        if line[0].isdigit():
            if int(line[0]) >= 10000:
                count = 2
                for i in range(3, len(line)):
                    if line[i].isdigit():
                        count = i
                        break
                if len(line[count:]) == 6:
                    if line[2].isdigit():
                        score = Competitor(line[0], line[1], line[2], " ".join(line[3:count]), line[count], line[count+1], line[count+2], line[count+3], line[count+4], line[count+5], sortBy)
                        if score.event == event:
                            eventScores.append(score)
                    else:
                        score = Competitor(line[0], line[1], -1,  " ".join(line[2:count]), line[count], line[count+1], line[count+2], line[count+3], line[count+4], line[count+5], sortBy)
                        if score.event == event:
                            eventScores.append(score)
    fIn.close()
    return eventScores

def getAllFinalists():
    fIn = open("data/transcriptsLabeled.txt")
    finalists = {}
    for line in fIn:
        l = line.strip().split("\t", 1)
        finalists[l[0]] = l[1].split("\t")
    fIn.close()
    return finalists

def getFinalHeadings(event):
    if event[-3:]=="TDM":
        return "\tFExam\tFPCase\tFFCase"
    else:
        if event[0] == "P":
            return "\tFExam\tFPCase\tFFCase"
        else:
            return "\tFExam\tFPCase1\tFPCase2\tFFCase"

def Rank(event, sort, id="", justOne=False, schoolAr=[]):
    fOut = open("output.txt", "w")
    fOut2 = open("output.tsv", "w")
    teams = ["BLTDM", "FTDM", "HTDM", "TTDM", "BTDM", "MTDM", "STDM", "ETDM"]

    allPeople = getAllPeople()
    eventScores = getAllScores(event, sort)
    finalists = getAllFinalists()
    if event in teams:
        teams = []
        for myTeam in eventScores:
            if int(myTeam.id)>= 20000:
                teamNum = myTeam.team
                teamID = myTeam.id
                teamChapter = myTeam.chapter
                team = []
                team.append(myTeam)
                for score in eventScores:
                    if score.team == teamNum and score.id != teamID and score.chapter == teamChapter:
                        team.append(score)
                teams.append(team)
        teams.sort(key=lambda score:int(score[0].getAttr(sortby[sort])), reverse = True) #SORT
        finalsHeading = getFinalHeadings(event)
        fOut.write("Event: "+event+"\nRank\tSchool\t\t\t\t\tID\tName\t\t\tID\tName\t\t\tScore\tRegion\t"+finalsHeading+"\n")
        fOut2.write("Event\tRank\tSchool\tID\tName\tID\tName\tScore\tRegion\t"+finalsHeading+"\n")
        for i in range(len(teams)):
            team = teams[i]
            try:
                title=""
                scorePerson1 = allPeople[int(team[1].id)]
                try:
                    scorePerson2 = allPeople[int(team[2].id)]
                except(IndexError):
                    scorePerson2 = scorePerson1
                if justOne:
                    if scorePerson1.id == id or scorePerson2.id == id or scorePerson1.getName() == id or scorePerson2.getName() == id:
                        team.append(scorePerson1)
                        team.append(scorePerson2)
                        team.append(event)
                        team.append(getFinalScore(event, team[1].chapter, scorePerson1.getName(), scorePerson2.getName()))
                        schoolAr.append((i+1,team))
                        break
                else:
                    finalScores = getFinalScore(event, team[1].chapter, scorePerson1.getName(), scorePerson2.getName())
                    if id != "":
                        if scorePerson1.id == id or scorePerson2.id == id or scorePerson1.getName() == id or scorePerson2.getName() == id:
                            title = "Here"
                    fOut.write(str(i+1)+title+"\t"+team[0].chapter.ljust(35, " ")+"\t"+str(scorePerson1).ljust(25, " ")+"\t"+str(scorePerson2).ljust(25, " ")+"\t"+team[0].overall+"\t"+scorePerson1.region.ljust(12, " ")+finalScores+"\n")
                    fOut2.write(event+"\t"+str(i+1)+"\t"+team[0].chapter+"\t"+str(scorePerson1)+"\t"+str(scorePerson2)+"\t"+team[0].overall+"\t"+scorePerson1.region+finalScores+"\n")
            except (KeyError):
                print("KeyError: "+team[1].id+" "+team[2].id)
    else:
        eventScores = sorted(eventScores, key=lambda score:int(score.getAttr(sortby[sort])), reverse=True) #SORT
        finalsHeading = getFinalHeadings(event)
        fOut.write("Event: "+event+"\nRank\tSchool\t\t\t\t\tID\tName\t\t\tScore\tOral1\tOral2\tExam\tRegion\t"+finalsHeading+"\n")
        fOut2.write("Event\tRank\tSchool\tID\tName\tScore\tOral1\tOral2\tExam\tRegion"+finalsHeading+"\n")
        for i in range(len(eventScores)):
            try:
                score = eventScores[i]
                scorePerson = allPeople[int(score.id)]
                title = ""
                if justOne:
                    if score.id == id or scorePerson.getName() == id:
                        schoolAr.append((i+1,[score, scorePerson, getFinalScore(event, score.chapter, scorePerson.getName())]))
                        break
                else:
                    finalScores = getFinalScore(event, score.chapter, scorePerson.getName())
                    title=""
                    if id != "":
                        if score.id == id or scorePerson.getName() == id:
                            title = "Here"
                    fOut.write(str(i+1)+title+"\t"+score.chapter.ljust(35, " ")+"\t"+str(scorePerson).ljust(25, " ")+"\t"+score.overall+"\t"+score.oral1+"\t"+score.oral2+"\t"+score.exam+"\t"+scorePerson.region.ljust(12, " ")+finalScores+"\n")
                    fOut2.write(event+"\t"+str(i+1)+"\t"+score.chapter+"\t"+str(scorePerson)+"\t"+score.overall+"\t"+score.oral1+"\t"+score.oral2+"\t"+score.exam+"\t"+scorePerson.region+finalScores+"\n")
            except (KeyError):
                print("KeyError: "+score.id)
    fOut.close()
    fOut2.close()

def Find(personID, sortby):
    fIn2 = open("data/Timetables.csv", "r", encoding="latin-1")
    fIn2.readline()
    for line in fIn2:
        line = line.strip().split(",")
        if line[13] == personID or line[17]+" "+line[18] == personID:
            event = line[20]
            break
    try:
        Rank(event, sortby, personID)
    except(UnboundLocalError):
        print("Cannot find "+personID)

def AllFrom(school, sortby):
    fInAll = open("data/Timetables.csv", "r", encoding="latin-1")
    fInAll.readline()
    flag = False
    fOut = open("output.txt", "w")
    fOut2 = open("output.tsv", "w")
    schoolList = []
    for line in fInAll:
        line = line.strip().split(",")
        if line[22] == school:
            event = line[20]
            personID = line[13]
            if event != "LDA" and int(personID) >= 10000:
                try:
                    print("Getting: "+personID)
                    Rank(event, sortby, personID, True, schoolList)
                except(UnboundLocalError):
                    print("Cannot find "+personID)
    schoolList.sort()
    num = len(school)/8+1
    fOut.write("Individual Series Events:\nEvent\tRank\tID\tName\t\t\tScore\tOral1\tOral2\tExam\tRegion\t\tInternationals (Exam, Orals, Finals)\n")
    fOut2.write("Event\tRank\tID\tName\tScore\tOral1\tOral2\tExam\tRegion\tInternational Scores\n")
    for i in schoolList:
        if len(i[1]) == 3:
            rank = i[0]
            score = i[1][0]
            scorePerson = i[1][1]
            fOut.write(score.event+"\t"+str(rank)+"\t"+str(scorePerson).ljust(25, " ")+"\t"+score.overall+"\t"+score.oral1+"\t"+score.oral2+"\t"+score.exam+"\t"+scorePerson.region.ljust(12, " ")+i[1][2]+"\n")
            fOut2.write(score.event+"\t"+str(rank)+"\t"+str(scorePerson).ljust(25, " ")+"\t"+score.overall+"\t"+score.oral1+"\t"+score.oral2+"\t"+score.exam+"\t"+scorePerson.region+i[1][2]+"\n")
    
    num = len(school)/8+1
    fOut.write("\nTeam Series Events:\nEvent\tRank\tID\tName\t\t\tID\tName\t\t\tScore\tRegion\t\tInternationals (Exam, Orals, Finals)\n")
    fOut2.write("Event\tRank\tSchool\tID\tName\tID\tName\tScore\tRegion\tInternational Scores\n")
    for i in range(0,len(schoolList),2):
        if len(schoolList[i][1]) == 7:
            rank = schoolList[i][0]
            team = schoolList[i][1]
            scorePerson1 = team[3]
            scorePerson2 = team[4]
            event = team[5]
            fOut.write(event+"\t"+str(rank)+"\t"+str(scorePerson1).ljust(25, " ")+"\t"+str(scorePerson2).ljust(25, " ")+"\t"+team[0].overall+"\t"+scorePerson1.region.ljust(12, " ")+team[6]+"\n")
            fOut2.write(event+"\t"+str(rank)+"\t"+str(scorePerson1)+"\t"+str(scorePerson2)+"\t"+team[0].overall+"\t"+scorePerson1.region+team[6]+"\n")
    fOut.close()
    fOut2.close()
    fInAll.close()
