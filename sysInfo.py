#!/usr/bin/env python3

"""
2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

import os
import subprocess

import logger

def getDE(keys):
    """Returns the first found environment variable from the list of keys."""
    for key in keys:
        value = os.getenv(key)
        if value:
            return value
    return "Unknown"

def getWM():
    """Tries to detect the window manager by checking environment variables and processes."""
    wm_env_vars = ["XDG_CURRENT_DESKTOP",
                   "DESKTOP_SESSION"]
    wm = getDE(wm_env_vars)

    # Try getting from wmctrl if available
    try:
        output = subprocess.check_output(["wmctrl",
                                          "-m"],
                                          text=True)
        for line in output.splitlines():
            if line.startswith("Name:"):
                wm = line.split(":", 1)[1].strip()
                break

    except FileNotFoundError:
        pass  # wmctrl not installed

    return wm

def getDistro():
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("PRETTY_NAME="):
                    return line.split("=", 1)[1].strip().strip('"')

    except FileNotFoundError:
        return "Unknown"

def getShell():
    return os.environ.get("SHELL","").split('/')[-1]

logger.log(f"sysInfo: Distro: {getDistro()}")
logger.log(f"sysInfo: Window Manager: {getWM()}")
logger.log(f"sysInfo: Desktop Enviornment: {getDE(["XDG_CURRENT_DESKTOP",
                                                    "DESKTOP_SESSION"])}")
logger.log(f"sysInfo: Terminal: {getShell()}")

logger.log("sysInfo: Retrieved system info")
