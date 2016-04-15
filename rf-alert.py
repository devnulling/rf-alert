#!/usr/bin/python
# rf-alert
# warn on high RF sensed
# by seek2 https://www.ar15.com/archive/topic.html?b=10&f=22&t=681710
import sys
import os
import time
import subprocess

def main():
    max = -50.0

    for csv in sys.stdin:
        #csv = sys.stdin.readline()
        data = csv[:-1].split(",")

        for i in range(7, len(data)):
            if (float(data[i]) > max):
                max = float(data[i])
                print max

            if (float(data[i]) > 5.0):
                freq = int(data[2]) + int(data[4])*(i-6)
                show = True

                if (freq > 162500000) and ( freq < 162600000):
                    show = False
                
                if (freq > 154200000) and ( freq < 154300000):
                    show = False
                
                if (freq > 152200000) and ( freq < 152300000):
                    show = False

                if (freq > 154450000) and ( freq < 154470000):
                    show = False

                if show:
                    print data[0].strip()+chr(9)+data[1].strip()+chr(9)+str(freq)+chr(9)+data[i].strip()
                    if (float(data[i]) > 10.0):
                        os.popen("echo 'rf rf' | cwpcm -w 20 -F 20 -v 20 -f 400 -lowrez | aplay -q ")
main()
