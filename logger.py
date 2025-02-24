#!/usr/bin/env python3

"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

import os
from datetime import datetime

homePath = os.path.expanduser("~")
time = datetime.now().strftime("%I:%M:%S")

def log(text):
    with open(homePath + "/cshell/logs.txt", "a") as file:
        time = datetime.now().strftime("%I:%M:%S")
        
        file.write("\n" + time + ": " + text)

with open(homePath + "/cshell/logs.txt", "a") as file:
    file.write("\n====== Session " + time + " ======")

log("Logger: Logger initialized.")
