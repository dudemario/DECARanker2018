#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 01:23:07 2019

@author: victor
"""

import sqlite3
    
def Rank(event, sort, id="", justOne=False, schoolAr=[]):
    conn = sqlite3.connect('DECAScores.db')
    c = conn.cursor()
    fOut = open("output.txt", "w")
    fOut2 = open("output.tsv", "w")
    teams = ["BLTDM", "FTDM", "HTDM", "TTDM", "BTDM", "MTDM", "STDM", "ETDM"]
    if event in teams:
        c.execute('''
                  SELECT 
                      comp1s.*,
                      comp2s.comp2ID,
                      comp2s.comp2Name,
                      comp2s.comp2Exam,
                      comp2s.comp2Oral1,
                      comp2s.comp2Oral2,
                      comp2s.comp2Penalties,
                      comp2s.comp2Overall
                  FROM (
                          SELECT 
                              ids.id AS teamID,
                              t.region,
                              ids.chapter, 
                              ids.exam AS teamexam, 
                              ids.oral1 AS teamoral1, 
                              ids.oral2 AS teamoral2, 
                              ids.penalties AS teampenalties, 
                              ids.overall AS teamoverall, 
                              t.id AS comp1ID, 
                              t.name AS comp1Name, 
                              t.exam AS comp1Exam, 
                              t.oral1 AS comp1Oral1, 
                              t.oral2 AS comp1Oral2, 
                              t.penalties AS comp1Penalties, 
                              t.overall AS comp1Overall
                          FROM 
                              teamid18 AS ids 
                          INNER JOIN 
                              team18 AS t 
                          ON 
                              ids.chapter = t.chapter 
                          WHERE 
                              ids.team = t.team 
                          AND 
                              ids.event = ?
                          AND 
                              t.event = ?
                          ) AS comp1s 
                  LEFT JOIN ( 
                          SELECT 
                              ids.id AS teamID, 
                              t.id AS comp2ID, 
                              t.name AS comp2Name, 
                              t.exam AS comp2Exam, 
                              t.oral1 AS comp2Oral1, 
                              t.oral2 AS comp2Oral2, 
                              t.penalties AS comp2Penalties, 
                              t.overall AS comp2Overall 
                          FROM 
                              teamid18 AS ids 
                          INNER JOIN 
                              team18 AS t 
                          ON 
                              ids.chapter = t.chapter 
                          WHERE 
                              ids.team = t.team 
                          AND 
                              ids.event = ?
                          AND 
                              t.event = ?
                          ) AS comp2s 
                  ON 
                      comp1s.teamID = comp2s.teamID 
                  WHERE 
                      comp1s.comp1Name < comp2s.comp2Name 
                  ORDER BY 
                      ?
                  DESC;''', (event, event, event, event, "comp1s.team"+sort))
        teams = c.fetchall()
        fOut.write("Event: "+event+"\nRank\tSchool\t\t\t\t\tID\tName\t\t\tID\tName\t\t\tScore\tRegion\n")
        fOut2.write("Event\tRank\tSchool\tID\tName\tID\tName\tScore\tRegion\n")
        for i in range(len(teams)):
            team = teams[i]
            try:
                title=""
                '''
                scorePerson1 = allPeople[int(team[1].id)]
                try:
                    scorePerson2 = allPeople[int(team[2].id)]
                except(IndexError):
                    scorePerson2 = scorePerson1
                '''
                if justOne:
                    if team[8] == id or team[9] == id or team[15] == id or team[16] == id:
                        schoolAr.append((i+1,team))
                        break
                else:
                    #finalScores = getFinalScore(event, team[1].chapter, scorePerson1.getName(), scorePerson2.getName())
                    if id != "":
                        if team[8] == id or team[9] == id or team[15] == id or team[16] == id:
                            title = "Here"
                    fOut.write(str(i+1)+title+"\t"+team[2].ljust(35, " ")+"\t"+(str(team[8])+"\t"+team[9]).ljust(25, " ")+"\t"+(str(team[15])+"\t"+team[16]).ljust(25, " ")+"\t"+str(team[7])+"\t"+team[1].ljust(12, " ")+"\n")
                    fOut2.write(event+"\t"+str(i+1)+"\t"+team[2]+"\t"+str(team[8])+"\t"+team[9]+"\t"+str(team[15])+"\t"+team[16]+"\t"+str(team[7])+"\t"+team[1]+"\n")
            except (KeyError):
                print("KeyError: "+team[8]+" "+team[15])
    else:
        c.execute("""
                  SELECT
                      *
                  FROM
                      indiv18 as i
                  WHERE
                      i.event = ?
                  ORDER BY
                      ?
                  DESC
                  """, (event, sort))
        scores = c.fetchall()
        fOut.write("Event: "+event+"\nRank\tSchool\t\t\t\t\tID\tName\t\t\tScore\tOral1\tOral2\tExam\tRegion"+"\n")
        fOut2.write("Event\tRank\tSchool\tID\tName\tScore\tOral1\tOral2\tExam\tRegion"+"\n")
        for i in range(len(scores)):
            try:
                score = scores[i]
                title = ""
                if justOne:
                    if team[0] == id or team[1] == id:
                        schoolAr.append((i+1, score))
                        break
                else:
                    title=""
                    if id != "":
                        if team[0] == id or team[1] == id:
                            title = "Here"
                    fOut.write(str(i+1)+title+"\t"+score[4].ljust(35, " ")+"\t"+(str(score[0])+"\t"+score[1]).ljust(25, " ")+"\t"+str(score[9])+"\t"+str(score[6])+"\t"+str(score[7])+"\t"+str(score[5])+"\t"+score[2].ljust(12, " ")+"\n")
                    fOut2.write(event+"\t"+str(i+1)+"\t"+score[4]+"\t"+str(score[0])+"\t"+score[1]+"\t"+str(score[9])+"\t"+str(score[6])+"\t"+str(score[7])+"\t"+str(score[5])+"\t"+score[2]+"\n")
            except (KeyError):
                print("KeyError: "+score[0])
    fOut.close()
    fOut2.close()
    c.close()
    conn.close()
    
if __name__ == "__main__":
    Rank("BTDM", "overall")
