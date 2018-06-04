# -*- coding: utf-8 -*-
"""
Spyder Editor

This script will list all the wifi available to your current computer. 
Then, based on the wifi network you specify, it wil try to log on to 
"""

import subprocess
results = subprocess.check_output(["netsh", "wlan", "show", "network"])
# needed in python 3
results = results.decode("ascii") 
print(results)
results = results.replace("\r","")
ls = results.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
print(ssids)