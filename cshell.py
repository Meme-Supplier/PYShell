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

# CSHELL modules
import cmdList
import error
import sysInfo
import logger

init(autoreset = True)

logger.log("CSHELL: Initialized modules.")

# atexit
def on_exit():
    logger.log("\n====== Session exit: " +
               logger.initTime() +
               " ======")
__import__("atexit").register(on_exit)
logger.log("CSHELL: atexit registered")

def ignoreCtrlC(signum, frame): ()
__import__("signal").signal(__import__("signal").SIGINT, ignoreCtrlC)
logger.log("CSHELL: Ctrl + C disabled")

pythonMajor = sys.version_info.major # Ex: 3.x.x
pythonMinor = sys.version_info.minor # Ex: x.12.x
pythonMicro = sys.version_info.micro # Ex: x.x.3
pythonVersion = str(pythonMajor) + "." + str(pythonMinor) + "." + str(pythonMicro)
pythonVersionShort = str(pythonMajor) + "." + str(pythonMinor)
logger.log("CSHELL: Python version: " + pythonVersion)

cshellVer = "v1.8.5"
logger.log("CSHELL: CSHELL version: " + cshellVer)

locked = False
passwordSet = False
password = None

logger.log("CSHELL: Variables initialized")

# Detecting if the system is linux
if platform.system() == "Linux":
    sufficientPacMan = True
    logger.log("CSHELL: System is Linux... Continuing")
else:
    sufficientPacMan = False
    error.handle(11)
    sys.exit(0)

# Detecting a supported pac man
if shutil.which("apt") or shutil.which("dnf") or shutil.which("pacman"):
    isLinux = True
    logger.log("CSHELL: Sufficient package manager detected: Continuing...")
else:
    isLinux = False
    error.handle(10)

logger.log("CSHELL: CSHELL initialized")

"""
Define
functions
"""

def processCommand(answer):
    # Goes through and executes commands

    logger.log("CSHELL: Processing command: " + answer)
    
    match answer:
        case "clear"     : os.system('clear'); logger.log("CSHELL: Cleared the screen")
        case "help"      : help()
        case "python"    : command("python" + pythonVersionShort)
        case "cmds"      : cmdList.list()
        case "exit"      : logger.log("CSHELL: Exiting CSHELL..."); sys.exit(0)
        case "shutdown"  : command("shutdown now")
        case "reboot"    : command("reboot")
        case "ping"      : command("ping")
        case "credits"   : credits()
        case "ver"       : ver()
        case "update"    : update()  # updates your system
        case "upgrade"   : upgrade()  # updates CSHELL
        case "lock"      : lock()
        case "xray"      : edit()
        case "reload"    : reload()
        case "in"        : input()
        case "uptime"    : command("uptime")
        case "uninstall" : uninstall()
        case "quit"      : quit()
        case "clean"     : clean()
        case "ip"        : command("hostname -I")
        case "logs"      : command("nano ~/cshell/logs.txt")
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
            
            logger.log("CSHELL: Executed command: " + answer)

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

    command("rm ~/cshell/logs.txt -f")
    logger.log("##### Initial log deletion #####")
    os.execv(sys.executable,
                ["python3"] +
                sys.argv)

def web(page):
    webbrowser.open_new_tab(page)
    logger.log("CSHELL: Opened webpage " + page)

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
    logger.log("CSHELL: Directory created: " + dir)

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

        logger.log("CSHELL: Cleaned up cache")

def delete(file):
    if os.path.exists(file):
        command("rm -rf " + file)
        logger.log("CSHELL: Deleted file " + file)
    else:
        error.handle(2)

def git():
    if gitInstalled():
        command(answer)
        logger.log("CSHELL: Opened Git")
    else:
        error.handle(3)

def uninstall():
    global uninstalled
    uninstalled = True

    choice = input(Fore.RED + "Are you sure you want to uninstall CSHELL?\n" +
                   Fore.WHITE)

    if choice == 'Y' or choice == 'y':
        logger.log("CSHELL: Uninstalling: Sorry to see you go :(")
        command("bash ~/cshell/uninstall.sh")
        sys.exit(0)
    else:
        print(Fore.GREEN + "\nAborted.")
        logger.log("CSHELL: Aborted: Uninstall CSHELL")

def wait(value):
    command("sleep " + str(value))
    logger.log("CSHELL: Waited " + str(value) + "seconds")

def command(command):
    subprocess.run([command],
                    shell = True)
    logger.log("CSHELL: Ran shell command: " + command)
    
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
        
        logger.log("CSHELL: Set password to " + password)

def lock():
    if passwordSet:
        logger.log("CSHELL: Locked CSHELL")

        os.system("clear")
        
        global locked
        locked = True

        attemptsLeft = 5

        while locked:
            
            if attemptsLeft != 0:
                print(Fore.CYAN + "Enter password to unlock CSHELL.")
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
    print(Fore.CYAN + "Do you want to update CSHELL?\n" +
          Fore.BLUE + "(Y/N)\n")

    print(Fore.RED + "Note: This will uninstall then reinstall CSHELL.")

    choice = input()

    if choice == 'Y' or choice == 'y': 
        logger.log("CSHELL: Upgrading CSHELL")
        command("bash ~/cshell/upgrade.sh")
        sys.exit(0)
    else:
        print(Fore.RED + "Aborted.")
        logger.log("CSHELL: Aborted: Upgrade CSHELL")

def edit():
    command("nano ~/cshell/cshell.py")
    print(Fore.BLUE + "\nChanges applied.")
    logger.log("CSHELL: Made changes to CSHELL")
    reload()

def reload():
    
    print(Fore.CYAN + "\nWould you like to reload CSHELL?")
    choice = input()

    if choice == 'Y' or choice == 'y': 
        print("Reloading script...")

        logger.log("CSHELL: Reloaded CSHELL")
        
        os.execv(sys.executable,
                ["python3"] +
                sys.argv)
        
    else:
        print(Fore.RED + "Aborted.")
        logger.log("CSHELL: Aborted: Reload CSHELL")    

def script(scriptPath):
    
    if scriptPath.startswith("~/"):
        error.handle(8)
    else:
        if answer.endswith(".cshell"):
            try:
                with open(scriptPath, "r") as file:
                        for line in file:
                            processCommand(line.strip())

                logger.log("CSHELL: Ran script: " + scriptPath)
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
              Fore.GREEN  + "CSHELL " +
              Fore.YELLOW + cshellVer)
        print(Fore.CYAN   + "Type " +
              Fore.BLUE   + "\"cmds\"" +
              Fore.CYAN   + " for some commands!\n")

def ver():
#   CSHELL version
    print(Fore.CYAN  + "\nCSHELL" +
          Fore.BLUE  + " version: " +
          Fore.GREEN + cshellVer)

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
    logger.log("CSHELL: Checking if git is installed...")

    try:
        subprocess.run(["git", "--version"],
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,
                        check  = True)
        
        logger.log("CSHELL: Git is installer")

        return True
    except (subprocess.CalledProcessError,
            FileNotFoundError):
        
        logger.log("CSHELL: Git is not installed")

        return False

"""
Program
"""

help()

while True and isLinux and not locked and sufficientPacMan:

    answer = input(Fore.BLUE  + "CSHELL" +
                   Fore.GREEN + '$' +
                   Fore.CYAN  + '~' +
                   Fore.WHITE + ': ')

    processCommand(answer)
