#!/usr/bin/env python3

"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

# System modules
import os
import sys
import subprocess
import platform
import webbrowser
import shutil
from pathlib import Path

from colorama import Fore, init
init(autoreset = True)

sys.dont_write_bytecode = True # Prevents "__pycache__" from being created

# CSHELL modules
import cmdList
import error

pythonMajor = sys.version_info.major # Ex: 3.x.x
pythonMinor = sys.version_info.minor # Ex: x.12.x
pythonMicro = sys.version_info.micro # Ex: x.x.3
pythonVersion = str(pythonMajor) + "." + str(pythonMinor) + "." + str(pythonMicro)
pythonVersionShort = str(pythonMajor) + "." + str(pythonMinor)

cshellVer = "v1.6"

locked = False
passwordSet = False
password = None

"""
Define
functions
"""

def processCommand(answer):
    # Goes through and executes commands
    
    match answer:
        case "clear"     : os.system('clear')
        case "help"      : help()
        case "python"    : command("python" + pythonVersionShort)
        case "cmds"      : cmdList.list()
        case "exit"      : sys.exit(0)
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

        # Commands that require syntax (show usage)
        case "echo"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "echo <message>")
        case "web"     : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "web <site>")
        case "expr"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "expr <equation>")
        case "bash"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "bash <command>")
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
            elif answer.startswith ("expr ")    : print  (eval(answer.replace("expr " , "" , 1)))
            elif answer.startswith ("bash ")    : command(answer.replace("bash " , "" , 1))
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

"""
Scripting
Commands
"""

def web(page):
    webbrowser.open_new_tab(page)

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

def clean():
    if sufficientPacMan():
        if shutil.which("apt"):   
            command("sudo apt autoremove && sudo apt autoclean")

        elif shutil.which("dnf"):   
            command("sudo dnf autoremove")

        elif shutil.which("pacman"):
            command("sudo pacman -Rns $(pacman -Qdtq)")
        else:
            error.handle(1)

        command("rm -rf ~/.cache/*")

def delete(file):
    if os.path.exists(file):
        command("rm -rf " + file)
    else:
        error.handle(2)

def git():
    if gitInstalled():
        command(answer)
    else:
        error.handle(3)

def uninstall():
    global uninstalled
    uninstalled = True

    choice = input(Fore.RED + "Are you sure you want to uninstall CSHELL?\n" +
                   Fore.WHITE)

    if choice == 'Y' or choice == 'y':
        command("bash ~/cshell/uninstall.sh")
        sys.exit(0)
    else:
        print(Fore.GREEN + "\nAborted.")

def wait(value):
    command("sleep " + str(value))

def command(command):
    subprocess.run([command],
                    shell = True)
    
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

def lock():
    if passwordSet:
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

    elif shutil.which("dnf"):   
        command("sudo dnf update")

    elif shutil.which("pacman"):
        command("sudo pacman -Syu")
    else:
        error.handle(1)

def upgrade():
    print(Fore.CYAN + "Do you want to update CSHELL?\n" +
          Fore.BLUE + "(Y/N)\n")

    print(Fore.RED + "Note: This will uninstall then reinstall CSHELL.")

    choice = input()

    if choice == 'Y' or choice == 'y': 
        command("bash ~/cshell/upgrade.sh")
        sys.exit(0)
    else:
        print(Fore.RED + "Aborted.")

def edit():
    command("nano ~/cshell/cshell.py")
    print(Fore.BLUE + "\nChanges applied.")
    reload()

def reload():
    
    print(Fore.CYAN + "\nWould you like to reload CSHELL?")
    choice = input()

    if choice == 'Y' or choice == 'y': 
        print("Reloading script...")
        
        os.execv(sys.executable,
                ["python3"] +
                sys.argv)
    else:
        print(Fore.RED + "Aborted.")    

def script(scriptPath):
    
    if scriptPath.startswith("~/"):
        error.handle(8)
    else:
        if answer.endswith(".cshell"):
            try:
                with open(scriptPath, "r") as file:
                        for line in file:
                            processCommand(line.strip())
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
    if sufficientPacMan() and isLinux:
        print(Fore.CYAN   + "Welcome to " +
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
    print(Fore.CYAN  + platform.system() ,
          Fore.BLUE  + platform.release())

#   Python version
    print(Fore.CYAN + "Python " +
          Fore.BLUE + pythonVersion +
          '\n')

def gitInstalled(): # Is git installed?
    try:
        subprocess.run(["git", "--version"],
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,
                        check  = True)
        return True
    except (subprocess.CalledProcessError,
            FileNotFoundError):
        return False
    
def isLinux():
    if platform.system() == "Linux":
        return True
    else:
        return False

def sufficientPacMan():
    if shutil.which("apt") or shutil.which("dnf") or shutil.which("pacman"):
        return True
    else:
        error.handle(10)
        return False
    
if not isLinux():
    error.handle(11)
    sys.exit(1)

"""
Program
"""

help()

while True and isLinux() and not locked and sufficientPacMan():

    answer = input(Fore.BLUE  + "CSHELL" +
                   Fore.GREEN + '$' +
                   Fore.CYAN  + '~' +
                   Fore.WHITE + ': ')

    processCommand(answer)
