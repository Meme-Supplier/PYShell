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
    with open(homePath + "/cshell/logs.txt", "a") as file:
        file.write("\n" + initTime() + ": " + text)

def initTime():
    return datetime.now().strftime("%I:%M:%S")

with open(homePath + "/cshell/logs.txt", "a") as file:
    file.write("\n====== Session start: " + initTime() + " ======")

log("logger: Logger initialized.")
