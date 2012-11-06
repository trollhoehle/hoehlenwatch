#!/usr/bin/python2

# sqlite> CREATE TABLE status(mac PRIMARY KEY,ip VARCHAR(128),hostname VARCHAR(128));
# sqlite> .schema
# CREATE TABLE status(mac PRIMARY KEY,ip VARCHAR(128),hostname VARCHAR(128));
# sqlite> INSERT INTO status (mac,ip,hostname) VALUES ('zoranhatnenWIRKLICHkurzenpenis','127.0.0.1','zoranstollewindowskiste');
# sqlite> select * from status;
# zoranhatnenWIRKLICHkurzenpenis|127.0.0.1|zoranstollewindowskiste
# sqlite> delete from status where mac = 'zoranhatnenWIRKLICHkurzenpenis';
# sqlite> 

from execute import execute
e = execute('nmap -sP 172.31.97.0/24')

import sqlite3

CREATE_SQL = """CREATE TABLE IF NOT EXISTS status(mac PRIMARY KEY, ip VARCHAR(128), hostname VARCHAR(128), last_seen datetime);"""
INSERT_SQL = """INSERT INTO status (mac, ip, hostname, last_seen) VALUES (?, ?, ?, datetime('now'));"""
UPDATE_SQL = """UPDATE status SET last_seen=datetime('now') WHERE mac = ?;"""

conn = sqlite3.connect('example.db')
conn.execute(CREATE_SQL)

output = e.stdout

lines = output.split('\n')
lines.append('')

linenum = 0
for line in lines:
    linenum +=1
    if 'is up' in line:
        hostline_full = lines[linenum-2].replace('Nmap scan report for ','')
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
        print "--------------"
        print host_hostname
        print host_ip
        print mac
        print ""
        try:
            conn.execute(INSERT_SQL, (mac, host_ip, host_hostname))
        except sqlite3.IntegrityError:
            # We already know this mac, so we update the last_seen timestamp
            conn.execute(UPDATE_SQL, (mac,))
conn.commit()

