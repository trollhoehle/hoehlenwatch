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
            host_ip = h[1]
        else:
            host_hostname = "UNKNOWN"
            host_ip = hostline_full
        print "--------------"
        print host_hostname
        print host_ip




