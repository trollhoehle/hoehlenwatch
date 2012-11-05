#!/usr/bin/python2

from execute import execute
e = execute('sudo nmap -sP 172.31.97.0/24')

output = e.stdout

lines = output.split('\n')

for line in lines:
    if line.startswith('Nmap scan report for'):
        hostname = line.split('Nmap scan report for ')[1].split(' ')[0]
        print "Hostname: " + hostname


