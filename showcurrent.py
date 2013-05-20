#!/usr/bin/python2

import sqlite3

conn = sqlite3.connect('status.db')
a = conn.execute("select * from status where last_seen > datetime('now', 'localtime', '-20 minute');")

print a.fetchall()

print dir(conn)

