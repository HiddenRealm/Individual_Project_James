import sqlite3
import sys

db = sqlite3.connect('/home/james/Documents/Individual_Project_James/application/site.db')
cursor = db.cursor()

def ctb(filename):
    filename = 'Pictures/' + str(filename + 1) + '.jpg'
    with open(filename, 'rb') as p:
        blobData = p.read()
        #blobData = base64.b64encode(p.read())
    return blobData

sql = 'INSERT INTO Players(first_name, last_name, team, worth, posistion, picture) VALUES(?,?,?,?,?,?)'


with open("Players.txt", "r") as r:
    contents = r.read().splitlines()


lines = []
for x in contents:
    lines.append(x.split(", "))

for i in range(100):
    dataTuple = (lines[i][1], lines[i][2], lines[i][3], lines[i][4], lines[i][5], ctb(i))
    cursor.execute(sql, dataTuple)

cursor.close()

db.commit()
db.close()