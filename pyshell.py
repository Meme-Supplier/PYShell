#!/usr/bin/env python3

"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

# Prevents "__pycache__" from being created
__import__("sys").dont_write_bytecode = True

# System modules
import os
import sys
import subprocess
import platform
import webbrowser
import shutil

from pathlib import Path
from readline import *
from colorama import Fore, init

# PYShell modules
import cmdList
import error
import sysInfo
import logger

init(autoreset = True)

logger.log("PYShell: Initialized modules.")

def ignoreCtrlC(signum, frame): ()
__import__("signal").signal(__import__("signal").SIGINT, ignoreCtrlC)
logger.log("PYShell: Ctrl + C disabled")

pythonMajor = sys.version_info.major # Ex: 3.x.x
pythonMinor = sys.version_info.minor # Ex: x.12.x
pythonMicro = sys.version_info.micro # Ex: x.x.3
pythonVersion = str(pythonMajor) + "." + str(pythonMinor) + "." + str(pythonMicro)
pythonVersionShort = str(pythonMajor) + "." + str(pythonMinor)
logger.log("PYShell: Python version: " + pythonVersion)

pyshellVer = "v1.8.6"
logger.log("PYShell: PYShell version: " + pyshellVer)

locked = False
passwordSet = False
password = None

logger.log("PYShell: Variables initialized")

# Detecting if the system is linux
if platform.system() == "Linux":
    sufficientPacMan = True
    logger.log("PYShell: System is Linux... Continuing")
else:
    sufficientPacMan = False
    error.handle(11)
    sys.exit(0)

# Detecting a supported pac man
if shutil.which("apt") or shutil.which("dnf") or shutil.which("pacman"):
    isLinux = True
    logger.log("PYShell: Sufficient package manager detected: Continuing...")
else:
    isLinux = False
    error.handle(10)

logger.log("PYShell: PYShell initialized")

"""
Define
functions
"""

def processCommand(answer):
    # Goes through and executes commands

    logger.log("PYShell: Processing command: " + answer)
    
    match answer:
        case "clear"     : os.system('clear'); logger.log("PYShell: Cleared the screen")
        case "help"      : help()
        case "python"    : command("python" + pythonVersionShort)
        case "cmds"      : cmdList.list()
        case "exit"      : logger.log("PYShell: Exiting PYShell..."); sys.exit(0)
        case "shutdown"  : command("shutdown now")
        case "reboot"    : command("reboot")
        case "ping"      : command("ping")
        case "credits"   : credits()
        case "ver"       : ver()
        case "update"    : update()  # updates your system
        case "upgrade"   : upgrade()  # updates PYShell
        case "lock"      : lock()
        case "xray"      : edit()
        case "reload"    : reload()
        case "in"        : input()
        case "uptime"    : command("uptime")
        case "uninstall" : uninstall()
        case "quit"      : quit()
        case "clean"     : clean()
        case "ip"        : command("hostname -I")
        case "logs"      : command("nano ~/pyshell/logs.txt")
        case "dellogs"   : dellogs()
        case "time"      : print(logger.initTime())

        # Commands that require syntax (show usage)
        case "echo"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "echo <message>")
        case "web"     : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "web <site>")
        case "expr"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "expr <equation>")
        case "sh"      : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "sh <command>")
        case "wait"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "wait <time (seconds)>")
        case "pwd"     : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "pwd <password>")
        case "edit"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "edit <path to text file>")
        case "script"  : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "script <script path>")
        case "pscript" : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "pscript <script path>")
        case "ls"      : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "ls <directory>")
        case "del"     : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "del <path to file/directory>")
        case "newdir"  : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "newdir <path to directory>")
        case "pm"      : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "pm <apt/dnf/pacman> <rest of the command>")
        case "copy"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "copy <path to file> <path to destination>")
        case ''        : None

        case _ :

            # Handle multiple commands separated by "&&"
            if " && " in answer:
                for cmd in answer.split(" && "):
                    processCommand(cmd.strip())

                return  # Exit after handling multiple commands

            # Multi-syntax commands
            if   answer.startswith ("echo ")    : print  (answer.replace("echo " , "" , 1))
            elif answer.startswith ("expr ")    : expr()
            elif answer.startswith ("sh ")      : command(answer.replace("sh " , "" , 1))
            elif answer.startswith ("web ")     : web    (answer.replace("web " , "" , 1))
            elif answer.startswith ("wait ")    : wait   (answer.replace("wait " , "" , 1))
            elif answer.startswith ("pwd ")     : setPwd (answer.replace("pwd " , "" , 1))
            elif answer.startswith ("script ")  : script (answer.replace("script " , "" , 1))
            elif answer.startswith ("pscript ") : command("python3 " + answer.replace("pscript " , "" , 1))
            elif answer.startswith ("in ")      : input  (answer.replace("in " , "" , 1) + '\n')
            elif answer.startswith ("ls ")      : command("\nls " + answer.replace("ls " , "" , 1))
            elif answer.startswith ("flatpak")  : command(answer)
            elif answer.startswith ("git")      : git    ()
            elif answer.startswith ("create ")  : command("touch " + answer.replace("create " ,"" , 1))
            elif answer.startswith ("del ")     : delete (answer.replace("del " , "" , 1))
            elif answer.startswith ("pm ")      : pm     (answer.replace("pm " , "" , 1))
            elif answer.startswith ("python")   : command(answer)
            elif answer.startswith ("newdir ")  : command("mkdir " + answer.replace("newdir " , "" , 1))
            elif answer.startswith ("copy ")    : command("cp " + answer.replace("copy " , "" , 1) + " -rf")
            elif answer.startswith ("ping ")    : command(answer)
            elif answer.startswith ("edit ")    : command("nano " + answer.replace("edit " , "" , 1))

            # If nothing checks out
            else: 
                print(Fore.RED + answer + ": invalid command.")
            
            logger.log("PYShell: Executed command: " + answer)

"""
Scripting
Commands
"""

def expr():
    try:
        print(eval(answer.replace("expr " , "" , 1)))
    except:
        error.handle(12)

def dellogs():

    command("rm ~/pyshell/logs.txt -f")
    logger.log("##### Initial log deletion #####")
    os.execv(sys.executable,
                ["python3"] +
                sys.argv)

def web(page):
    webbrowser.open_new_tab(page)
    logger.log("PYShell: Opened webpage " + page)

def pm(cmd):
    if shutil.which("apt") or shutil.which("dnf") or shutil.which("pacman"):
        
        if cmd.startswith("apt") or cmd.startswith("dnf") or cmd.startswith("pacman"):
            command(cmd)
        else:
            error.handle(1)
    else:
        error.handle(1)

def newdir(dir):
    Path(dir).mkdir(parents = True,
                    exist_ok = True)
    logger.log("PYShell: Directory created: " + dir)

def clean():
    if sufficientPacMan == True:
        if shutil.which("apt"):   
            command("sudo apt autoremove && sudo apt autoclean")

        elif shutil.which("dnf"):   
            command("sudo dnf autoremove")

        elif shutil.which("pacman"):
            command("sudo pacman -Rns $(pacman -Qdtq)")
        else:
            error.handle(1)

        command("sudo rm -rf ~/.cache/*")

        logger.log("PYShell: Cleaned up cache")

def delete(file):
    if os.path.exists(file):
        command("rm -rf " + file)
        logger.log("PYShell: Deleted file " + file)
    else:
        error.handle(2)

def git():
    if gitInstalled():
        command(answer)
        logger.log("PYShell: Opened Git")
    else:
        error.handle(3)

def uninstall():
    global uninstalled
    uninstalled = True

    choice = input(Fore.RED + "Are you sure you want to uninstall PYShell?\n" +
                   Fore.WHITE)

    if choice == 'Y' or choice == 'y':
        logger.log("PYShell: Uninstalling: Sorry to see you go :(")
        command("bash ~/pyshell/uninstall.sh")
        sys.exit(0)
    else:
        print(Fore.GREEN + "\nAborted.")
        logger.log("PYShell: Aborted: Uninstall PYShell")

def wait(value):
    command("sleep " + str(value))
    logger.log("PYShell: Waited " + str(value) + "seconds")

def command(command):
    subprocess.run([command],
                    shell = True)
    logger.log("PYShell: Ran shell command: " + command)
    
def setPwd(pwd):
    global password
    global passwordSet

    if len(pwd) < 5:
        error.handle(4)
    else:
        password = pwd
        passwordSet = True

        print(Fore.CYAN + "Password has been set to " +
              Fore.BLUE + password)
        
        logger.log("PYShell: Set password to " + password)

def lock():
    if passwordSet:
        logger.log("PYShell: Locked PYShell")

        os.system("clear")
        
        global locked
        locked = True

        attemptsLeft = 5

        while locked:
            
            if attemptsLeft != 0:
                print(Fore.CYAN + "Enter password to unlock PYShell.")
                pwdAttempt = input()

                if pwdAttempt == password:
                    locked = False
                else:
                    error.handle(5)
                    attemptsLeft -= 1
            else:
                os.system("clear")
                error.handle(6)
                wait(5)
                attemptsLeft = 5
    else:
        error.handle(7)

def update():
    if shutil.which("apt"):   
        command("sudo apt update && sudo apt upgrade")
        logger.log("Successfully updated device.")

    elif shutil.which("dnf"):   
        command("sudo dnf update")
        logger.log("Successfully updated device.")

    elif shutil.which("pacman"):
        command("sudo pacman -Syu")
        logger.log("Successfully updated device.")
    else:
        error.handle(1)

def upgrade():
    print(Fore.CYAN + "Do you want to update PYShell?\n" +
          Fore.BLUE + "(Y/N)\n")

    print(Fore.RED + "Note: This will uninstall then reinstall PYShell.")

    choice = input()

    if choice == 'Y' or choice == 'y': 
        logger.log("PYShell: Upgrading PYShell")
        command("bash ~/pyshell/upgrade.sh")
        sys.exit(0)
    else:
        print(Fore.RED + "Aborted.")
        logger.log("PYShell: Aborted: Upgrade PYShell")

def edit():
    command("nano ~/pyshell/pyshell.py")
    print(Fore.BLUE + "\nChanges applied.")
    logger.log("PYShell: Made changes to PYShell")
    reload()

def reload():
    
    print(Fore.CYAN + "\nWould you like to reload PYShell?")
    choice = input()

    if choice == 'Y' or choice == 'y': 
        print("Reloading script...")

        logger.log("PYShell: Reloaded PYShell")
        
        os.execv(sys.executable,
                ["python3"] +
                sys.argv)
        
    else:
        print(Fore.RED + "Aborted.")
        logger.log("PYShell: Aborted: Reload PYShell")    

def script(scriptPath):
    
    if scriptPath.startswith("~/"):
        error.handle(8)
    else:
        if answer.endswith(".pyshell"):
            try:
                with open(scriptPath, "r") as file:
                        for line in file:
                            processCommand(line.strip())

                logger.log("PYShell: Ran script: " + scriptPath)
            except:
                error.handle(2)
        
        else:
            error.handle(9)

def credits():
    print(Fore.CYAN   + "Meme Supplier" +
          Fore.BLUE   + ": owner, programmer, maintainer\n" +
          Fore.YELLOW + "Contact: " +
          Fore.BLUE   + "memesupplierbusiness@gmail.com\n" +
          Fore.GREEN  + "2025 Meme Supplier")

def help():
    if sufficientPacMan and isLinux:
        print(Fore.CYAN   + "\nWelcome to " +
              Fore.GREEN  + "PYShell " +
              Fore.YELLOW + pyshellVer)
        print(Fore.CYAN   + "Type " +
              Fore.BLUE   + "\"cmds\"" +
              Fore.CYAN   + " for some commands!\n")

def ver():
#   PYShell version
    print(Fore.CYAN  + "\nPYShell" +
          Fore.BLUE  + " version: " +
          Fore.GREEN + pyshellVer)

#   Python version
    print(Fore.CYAN + "Python " +
          Fore.BLUE + pythonVersion +
          '\n')

#   System info

    # Distro
    print(Fore.CYAN + "OS:",
          Fore.BLUE + sysInfo.getDistro())
    
    # Kernel version
    print(Fore.CYAN + "Kernel:",
          Fore.BLUE + platform.release())
    
    # Window Manager
    print(Fore.CYAN + "WM:",
          Fore.BLUE + sysInfo.getWM())
    
    # Desktop Enviornment
    print(Fore.CYAN + "DE:",
          Fore.BLUE + sysInfo.getDE(["XDG_CURRENT_DESKTOP",
                                     "DESKTOP_SESSION"]),
                                     '\n')

def gitInstalled(): # Is git installed?
    logger.log("PYShell: Checking if git is installed...")

    try:
        subprocess.run(["git", "--version"],
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,
                        check  = True)
        
        logger.log("PYShell: Git is installed")

        return True
    except (subprocess.CalledProcessError,
            FileNotFoundError):
        
        logger.log("PYShell: Git is not installed")

        return False

"""
Program
"""

help()

while True and isLinux and not locked and sufficientPacMan:

    answer = input(Fore.BLUE  + "PYShell" +
                   Fore.GREEN + '$' +
                   Fore.CYAN  + '~' +
                   Fore.WHITE + ': ')

    processCommand(answer)
