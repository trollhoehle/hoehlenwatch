#!/usr/bin/python2

import wget

if wget.wget("http://nerdhost.de/testfile.img") == 0:
    print "yo"



