#!/usr/bin/env python
from datetime import datetime
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.replace('"', "")
    data = line.split(",")
    if data[0][0] == '(':
        if len(data) == 3:
            key, value, tag = data
            key = key.replace("(", "")
            key = key.replace("'", "")
            value = value.replace(")", "")
            value = value.replace("'", "")
            dtDate = datetime.strptime(key, "%d-%m-%Y")
            print tag
            print "{0},{1}\t{2},{3}".format(dtDate.strftime('%b'), dtDate.strftime('%d'), tag, value)
    else:
        key, value = line.split(",")
        dtDate = datetime.strptime(key, "%b-%d-%Y %H:%M")
        print "{0},{1}\t{2},{3}".format(dtDate.strftime('%b'), dtDate.strftime('%d'), "taxi", value)
