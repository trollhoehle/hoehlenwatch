#!/usr/bin/python2

### sqlite:
# to initialize the database table:
# sqlite> CREATE TABLE status(mac PRIMARY KEY,ip VARCHAR(128),hostname VARCHAR(128));
# to view the schema:
# sqlite> .schema
# to insert a row into the status table:
# sqlite> INSERT INTO status (mac,ip,hostname) VALUES ('zoranhatnenWIRKLICHkurzenpenis','127.0.0.1','zoranstollewindowskiste');

from execute import execute

print "Fetching results from nmap..."
e = execute('nmap -sP 172.31.97.0/24')
print "nmap run done"

import sqlite3

CREATE_SQL = """CREATE TABLE IF NOT EXISTS status(mac PRIMARY KEY, ip VARCHAR(128), hostname VARCHAR(128), last_seen datetime);"""
INSERT_SQL = """INSERT INTO status (mac, ip, hostname, last_seen) VALUES (?, ?, ?, datetime('now'));"""
UPDATE_SQL = """UPDATE status SET last_seen=datetime('now') WHERE mac = ?;"""

conn = sqlite3.connect('status.db')
conn.execute(CREATE_SQL)

output = e.stdout

lines = output.split('\n')
lines.append('')

linenum = 0
for line in lines:
    print "---"
    linenum +=1
    if 'is up' in line:
        hostline_full = lines[linenum-2].replace('Nmap scan report for ','')
	print hostline_full
        if "(" in hostline_full:
            h = hostline_full.split(' ')
            host_hostname = h[0]
            host_ip = h[1].replace('(','').replace(')','')
        else:
            host_hostname = "unknown_hostname"
            host_ip = hostline_full
        mac = lines[linenum].split(' ')[2:][0]
        if not ":" in mac:
            mac = "unknown_mac"
        if not mac == "unknown_mac":
            print "MAC: %s, HOSTNAME: %s, IP: %s" % (mac, host_hostname,host_ip)
            try:
                conn.execute(INSERT_SQL, (mac, host_ip, host_hostname))
            except sqlite3.IntegrityError:
                # We already know this mac, so we update the last_seen timestamp
                conn.execute(UPDATE_SQL, (mac,))
conn.commit()

