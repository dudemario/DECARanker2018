#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 01:23:07 2019

@author: victor
"""

import sqlite3

def getAllPeople(c):
    fIn = open("data/Timetables.csv", "r", encoding="latin-1")
    fIn.readline()
    for line in fIn:
        line = line.strip().split(",")
        if int(line[13]) >= 10000 and int(line[13]) < 20000:
            c.execute('SELECT id FROM indiv18 WHERE id = ?', (int(line[13]),))
            data = c.fetchall()
            if len(data) == 1:
                c.execute('UPDATE indiv18 SET name = ?, region = ? WHERE id = ?', (line[17] + " " + line[18], line[32], int(line[13])))
            else:
                c.execute('SELECT id FROM team18 WHERE id = ?', (int(line[13]),))
                data = c.fetchall()
                if len(data) == 1:
                    c.execute('UPDATE team18 SET name = ?, region = ? WHERE id = ?', (line[17] + " " + line[18], line[32], int(line[13])))
                else:
                    pass
                    #print("Can't find "+line[13])
    fIn.close()
    c.execute('UPDATE team18 SET name = "Benji Segal", region = "Private" WHERE id = 11984')

def getAllScores(c):
    fIn = open("data/scores.txt", "r", encoding="latin-1")
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
                        if int(line[0]) >= 20000:
                            c.execute("INSERT INTO teamid18 (id, event, team, chapter, exam, oral1, oral2, penalties, overall) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (int(line[0]), line[1], int(line[2]), " ".join(line[3:count]), int(line[count]), int(line[count+1]), int(line[count+2]), int(line[count+3]), int(line[count+4])))
                        else:
                            c.execute("INSERT INTO team18 (id, event, team, chapter, exam, oral1, oral2, penalties, overall) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (int(line[0]), line[1], int(line[2]), " ".join(line[3:count]), int(line[count]), int(line[count+1]), int(line[count+2]), int(line[count+3]), int(line[count+4])))
                    else:
                        c.execute("INSERT INTO indiv18 (id, event, chapter, exam, oral1, oral2, penalties, overall) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (int(line[0]), line[1],  " ".join(line[2:count]), int(line[count]), int(line[count+1]), int(line[count+2]), int(line[count+3]), int(line[count+4])))
    fIn.close()

def createTable(c, conn):
    c.execute('CREATE TABLE IF NOT EXISTS indiv18 (id INT, name TEXT, region TEXT, event TEXT, chapter TEXT, exam INT, oral1 INT, oral2 INT, penalties INT, overall INT)')
    c.execute('CREATE TABLE IF NOT EXISTS team18 (id INT, name TEXT, region TEXT, event TEXT, team INT, chapter TEXT, exam INT, oral1 INT, oral2 INT, penalties INT, overall INT)')
    c.execute('CREATE TABLE IF NOT EXISTS teamid18 (id INT, event TEXT, team INT, chapter TEXT, exam INT, oral1 INT, oral2 INT, penalties INT, overall INT)')
    conn.commit()

def fillInTable(c, conn):
    try:
        getAllScores(c)
        conn.commit()
        getAllPeople(c)
    except():
        pass
    conn.commit()

    
def main():
    conn = sqlite3.connect('DECAScores.db')
    c = conn.cursor()
    createTable(c, conn)
    fillInTable(c, conn)
    c.close()
    conn.close()

if __name__ == "__main__":
    main()