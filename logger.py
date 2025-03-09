#!/usr/bin/env python3

"""
2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

import os
from datetime import datetime

homePath = os.path.expanduser("~")

pyShellDeleted = False

def log(text):
    if not pyShellDeleted:
        try:
            with open(f"{homePath}/pyshell/logs.txt", "a") as file:
                file.write(f"\n[{initTime()}] {text}")
        except:
            __import__("error").handle(14)

def initTime():
    return datetime.now().strftime("%I:%M:%S")

with open(f"{homePath}/pyshell/logs.txt", "a") as file:
    file.write(f"\n====== Session start: [{initTime()}] ======")

log("logger: Logger initialized.")
