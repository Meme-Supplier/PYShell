#!/usr/bin/env python3

"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

import os
from datetime import datetime

homePath = os.path.expanduser("~")

def log(text):
    try:
        with open(homePath + "/pyshell/logs.txt", "a") as file:
            file.write("\n" + initTime() + ": " + text)
    except: log("logger: Failed to log line! Skipping...")

def initTime():
    return datetime.now().strftime("%I:%M:%S")

with open(homePath + "/pyshell/logs.txt", "a") as file:
    file.write("\n====== Session start: " + initTime() + " ======")

log("logger: Logger initialized.")
