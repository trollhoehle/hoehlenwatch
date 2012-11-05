#!/usr/bin/python2

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



