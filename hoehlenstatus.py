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
e = execute('sudo nmap -sP 172.31.97.0/24')

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



