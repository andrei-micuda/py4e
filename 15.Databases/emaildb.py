#Counting Email in a Database
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#Delete table if it already exists
cur.execute('DROP TABLE IF EXISTS Counts')

#Create Counts table
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'
fhandle = open(fname)

for line in fhandle:
    
    line = line.strip()

    if not line.startswith('From: '):
        continue

    pieces = line.split()
    email = pieces[1].split('@')
    
    cur.execute('SELECT count FROM Counts WHERE org= ? ', (email[1], ))
    cnt = cur.fetchone()
    #if current organization is not currently in the DB, we insert it
    if cnt is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (email[1], ))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org=?', (email[1], ))


conn.commit()
cur.close()
