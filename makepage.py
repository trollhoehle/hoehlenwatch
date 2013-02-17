#!/usr/bin/python2

# extremely ugly script to make a webpage with what we got

import sqlite3

CREATE_SQL = """CREATE TABLE IF NOT EXISTS status(mac PRIMARY KEY, ip VARCHAR(128), hostname VARCHAR(128), last_seen datetime);"""
GETSTATUS_SQL = """SELECT mac, ip, last_seen from status order by last_seen desc;"""

conn = sqlite3.connect('status.db')
cursor = conn.cursor()
cursor.execute(GETSTATUS_SQL)

datastructure = cursor.fetchall()

# print html header
print '''<html>
<head></head>
<table border=1>
'''


for row in datastructure:
     print "<tr>"
     one, two, three = row[0], row[1], row[2]
     print "<td>" + one + "</td>"
     print "<td>" + two + "</td>"
     print "<td>" + three + "</td>"
     print "</tr>"

print """</table>
</html>
"""

