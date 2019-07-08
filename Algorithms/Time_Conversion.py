"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

"""

#!/bin/python3

import os
import sys
import re

def timeConversion(s):
    #res = s.split(':')
    res = re.split('(\d+)',s)
    
    if int(res[1]) == 12 and res[6] == 'PM':
        h = str(int(res[1]))
    elif int(res[1]) == 12 and res[6] == 'AM':
        h = '00'
    elif res[6] == 'AM':
        h = '0'+str(int(res[1]))
    elif 0 <= int(res[1]) < 12:
        h = str(int(res[1])+12)
    return h + res[2] + res[3] + res[4] + res[5]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = timeConversion(s)

    f.write(result + '\n')
    f.close()
