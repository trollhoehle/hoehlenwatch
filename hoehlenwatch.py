#!/usr/bin/python2

### sqlite:
# to initialize the database table:
# sqlite> CREATE TABLE status(mac PRIMARY KEY,ip VARCHAR(128),hostname VARCHAR(128));
# to view the schema:
# sqlite> .schema
# to insert a row into the status table:
# sqlite> INSERT INTO status (mac,ip,hostname) VALUES ('zoranhatnenWIRKLICHkurzenpenis','127.0.0.1','zoranstollewindowskiste');

from execute import execute
import sqlite3
import datetime

# datetime string in the format: 2013-05-15 21:21:44
# time = str(datetime.datetime.now()).split('.')[0]

print "Fetching results from nmap..."
e = execute('nmap -sP 172.31.97.0/24')
print "nmap run done"

CREATE_SQL = """CREATE TABLE IF NOT EXISTS status(mac PRIMARY KEY, ip VARCHAR(128), last_seen datetime);"""
INSERT_SQL = """INSERT INTO status (mac, ip, last_seen) VALUES (?, ?, datetime('now', 'localtime'));"""
UPDATE_SQL = """UPDATE status SET last_seen=datetime('now', 'localtime') WHERE mac = ?;"""

conn = sqlite3.connect('status.db')
conn.execute(CREATE_SQL)

output = e.stdout

lines = output.split('\n')
lines.append('')

linenum = 0
for line in lines:
    linenum +=1
    if 'is up' in line:
        hostline_full = lines[linenum-2].replace('Nmap scan report for ','')
        host_ip = hostline_full
        mac = lines[linenum].split(' ')[2:][0]
        if not ":" in mac:
            mac = "unknown_mac"
        if not mac == "unknown_mac":
            print "MAC: %s, IP: %s" % (mac, host_ip)
            try:
                conn.execute(INSERT_SQL, (mac, host_ip))
            except sqlite3.IntegrityError:
                # We already know this mac, so we update the last_seen timestamp
                conn.execute(UPDATE_SQL, (mac,))
conn.commit()

