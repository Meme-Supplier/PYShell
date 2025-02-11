#!/usr/bin/env python3

"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

import os
import sys
import subprocess
import platform
import webbrowser
import shutil
from pathlib import Path

from colorama import Fore, init
init(autoreset = True)

os.system("clear")

pythonMajor = sys.version_info.major # Ex: 3.x.x
pythonMinor = sys.version_info.minor # Ex: x.12.x
pythonMicro = sys.version_info.micro # Ex: x.x.3
pythonVersion = str(pythonMajor) + "." + str(pythonMinor) + "." + str(pythonMicro)
pythonVersionShort = str(pythonMajor) + "." + str(pythonMinor)

cshellVer = "v1.1"

sufficientPacMan = False

locked = False
passwordSet = False
password = ''

"""
Define
functions
"""

def commands():

    """
    Command
    list
    """

    print('\n' +
#         Color        Output          
          Fore.YELLOW + "Available commands:\n")
#   Exit
    print(Fore.CYAN  + "exit " +
          Fore.GREEN + "Exits CShell")
#   Clear
    print(Fore.CYAN  + "clear" +
          Fore.GREEN + " Clears the screen")
#   Help
    print(Fore.CYAN  + "help" +
          Fore.GREEN + " Some info")
#   Cmds
    print(Fore.CYAN  + "cmds" +
          Fore.GREEN + " Lists available commands")
#   Python
    print(Fore.CYAN  + "python" +
          Fore.GREEN + " Runs the latest Python version")
#   Ver
    print(Fore.CYAN  + "ver" +
          Fore.GREEN + " Shows CShell's version")
#   Lock
    print(Fore.CYAN  + "lock" +
          Fore.GREEN + " Locks the terminal")
#   Edit
    print(Fore.CYAN  + "edit" +
          Fore.GREEN + " Allows you to easily edit CShell")
#   Reload
    print(Fore.CYAN  + "reload" +
          Fore.GREEN + " Reloads CShell")
#   Clean
    print(Fore.CYAN  + "clean" +
          Fore.GREEN + " removes unnecessary packages")
#   Reload
    print(Fore.CYAN  + "uptime" +
          Fore.GREEN + " Shows how long your system has been on")
#   Shutdown
    print(Fore.CYAN  + "shutdown" +
          Fore.GREEN + " Shuts down your system")
#   Uninstall
    print(Fore.CYAN  + "uninstall" +
          Fore.GREEN + " Uninstalls CShell.")
#   Touch
    print(Fore.CYAN  + "touch " +
          Fore.BLUE  + "<text> " +
          Fore.YELLOW  + "> " +
          Fore.BLUE  + "<file>" +
          Fore.GREEN + " Creates a file with text")
#   Wait
    print(Fore.CYAN  + "wait" +
          Fore.BLUE  + " <time (seconds)>" +
          Fore.GREEN + " Waits your desired time")
#   Pm
    print(Fore.CYAN  + "pm" +
          Fore.BLUE  + " <apt/dnf/pacman> <rest of the command>" +
          Fore.GREEN + " Runs Apt, Dnf, or Pacman.")
#   Newdir
    print(Fore.CYAN  + "newdir" +
          Fore.BLUE  + " <path to directory>" +
          Fore.GREEN + " Creates a directory in the desired path." +
          Fore.RED   + "Notice: The path must be the FULL path")
#   Echo
    print(Fore.CYAN  + "echo" +
          Fore.BLUE  + " <text>" +
          Fore.GREEN + " Prints text")
#   Bash
    print(Fore.CYAN  + "bash " +
          Fore.BLUE  + "<commands>" +
          Fore.GREEN + " Runs normal shell commands " +
          Fore.RED   + "Notice: commands like \"cd\" and \"dir\" won't work.")
#   Expr
    print(Fore.CYAN  + "expr " +
          Fore.BLUE  + "<equation>" +
          Fore.GREEN + " Solves a math equation")
#   Web
    print(Fore.CYAN  + "web " +
          Fore.GREEN + " Opens your browser")
#   Web (site)
    print(Fore.CYAN  + "web " +
          Fore.BLUE  + "<website>" +
          Fore.GREEN + " Opens your desired website")
#   Git
    print(Fore.CYAN  + "git " +
          Fore.BLUE  + "<rest of the command>" +
          Fore.GREEN + " Runs git")
#   Script
    print(Fore.CYAN  + "script " +
          Fore.BLUE  + "<path to " +
          Fore.BLUE  + "file>" +
          Fore.GREEN + " Runs a CShell script" +
          Fore.RED   + " Notice: Only supports text files with the file extension \"" +
          Fore.BLUE  + ".cshell" +
          Fore.RED   + "\", and the path must be the FULL path")
#   In
    print(Fore.CYAN  + "in " +
          Fore.BLUE  + "<text>" +
          Fore.GREEN + " Recieves confimation from user")
#   Ls
    print(Fore.CYAN  + "ls " +
          Fore.BLUE  + "<directory>" +
          Fore.GREEN + " Lists the specified directory")
#   Pwd
    print(Fore.CYAN  + "pwd " +
          Fore.BLUE  + "<password>" +
          Fore.GREEN + " Sets a password " +
          Fore.RED   + "Notice: Password has to be at least 5 characters long.")
#   Del
    print(Fore.CYAN  + "del " +
          Fore.BLUE  + "<path to file/directory>" +
          Fore.GREEN + " Deletes a file/directory " +
          Fore.RED   + "Notice: The path must be the FULL path")
#   Update
    print(Fore.CYAN  + "update " +
          Fore.GREEN + " Updates your device " +
          Fore.RED   + "Notice: Only supports Fedora, Arch, and Debian based distros.")
#   Upgrade
    print(Fore.CYAN  + "upgrade" +
          Fore.GREEN + " Updates CShell\n")

def processCommand(answer):
#   Goes through and executes commands
    match answer:
#            Input         Response  
        case "clear"     : os.system('clear')
        case "help"      : help()
        case "python"    : command("python" + pythonVersionShort)
        case "cmds"      : commands()
        case "exit"      : sys.exit(0)
        case "shutdown"  : command("shutdown now")
        case "credits"   : credits()
        case "ver"       : ver()
        case "update"    : update() # updates your system
        case "upgrade"   : upgrade() # updates CShell
        case "lock"      : lock()
        case "edit"      : edit()
        case "reload"    : reload()
        case "in"        : input()
        case "uptime"    : command("uptime")
        case "uninstall" : uninstall()
        case "quit"      : quit()
        case "clean"     : clean()
        case "web"       : webbrowser.open_new('')

#       Commands that require syntax
#       (Show usage)

        case "echo"   : print(Fore.CYAN + "Usage: " +
                              Fore.BLUE + "echo <message>")
        case "expr"   : print(Fore.CYAN + "Usage: " +
                              Fore.BLUE + "expr <equation>")
        case "bash"   : print(Fore.CYAN + "Usage: " +
                              Fore.BLUE + "bash <command>")
        case "wait"   : print(Fore.CYAN + "Usage: " +
                              Fore.BLUE + "wait <time (seconds)>")
        case "pwd"    : print(Fore.CYAN + "Usage: " +
                              Fore.BLUE + "pwd <password>")
        case "script" : print(Fore.CYAN + "Usage: " +
                              Fore.BLUE + "script <script path>")
        case "ls"     : print(Fore.CYAN + "Usage: " +
                              Fore.BLUE + "ls <directory>")
        case "del"    : print(Fore.CYAN + "Usage: " +
                              Fore.BLUE + "del <path to file/directory>")
        case "newdir" : print(Fore.CYAN + "Usage: " +
                              Fore.BLUE + "newdir <path to directory>")
        case "pm"     : print(Fore.CYAN + "Usage: " +
                              Fore.BLUE + "pm <apt/dnf/pacman> <rest of the command>")
        case ''       : ''

        case _ :
#           Multi-syntax
            if   answer.startswith ("echo ")   : print(answer.replace("echo " , "" , 1))
            elif answer.startswith ("expr ")   : print(eval(answer.replace("expr " , "" , 1)))
            elif answer.startswith ("bash ")   : command(answer.replace("bash " , "" , 1))
            elif answer.startswith ("web ")    : webbrowser.open_new(answer.replace("web " , "" , 1))
            elif answer.startswith ("wait ")   : wait(answer.replace("wait " , "" , 1))
            elif answer.startswith ("pwd ")    : setPwd(answer.replace("pwd " , "" , 1))
            elif answer.startswith ("script ") : script(answer.replace("script " , "" , 1))
            elif answer.startswith ("in ")     : input(answer.replace("in " , "" , 1) + '\n')
            elif answer.startswith ("ls ")     : ls(answer.replace("ls " , "" , 1))
            elif answer.startswith ("flatpak") : command(answer)
            elif answer.startswith ("git")     : git()
            elif answer.startswith ("touch ")  : command(answer)
            elif answer.startswith ("del ")    : delete(answer.replace("del " , "" , 1))
            elif answer.startswith ("pm ")     : pm(answer.replace("pm " , "" , 1))

#           If nothing checks out
            else: print(Fore.RED +
                        answer +
                        ": invalid command.")

"""
Scripting
Commands
"""

def pm(cmd):
    if shutil.which("apt") or shutil.which("dnf") or shutil.which("pacman"):
        command(cmd)
    else:
        print(Fore.RED + "Unable to remove packages: Unsupported package manager!")

def newdir(dir):
    Path(dir).mkdir(parents = True,
                    exist_ok = True)
    
    # Verifies of the directory exists
    if os.path.exists(dir):
        print(Fore.GREEN + "Directory successfully created!")
    else:
        print("Error! File/Directory doesn't exist!\nTry again and remember to use the full path!")

def clean():
    if shutil.which("apt"):   
        command("sudo apt autoremove")

    elif shutil.which("dnf"):   
        command("sudo dnf autoremove")

    elif shutil.which("pacman"):
        command("sudo pacman -Rns $(pacman -Qdtq)")
    else:
        print(Fore.RED + "Unable to remove packages: Unsupported package manager!")

def delete(file):
    if os.path.exists(file):
        command("rm -rf " + file)
    else:
        print(Fore.RED + "Error! File/Directory doesn't exist! Remember to use the full path!")

def git():
    if gitInstalled():
        command(answer)
    else:
        print(Fore.RED + "Git is not installed. Please install Git.")

def ls(lsDir):
    command("\nls " + lsDir)

def uninstall():
    global uninstalled
    uninstalled = True

    choice = input(Fore.RED + "Are you sure you want to uninstall CShell?\n" +
                   Fore.WHITE)

    if choice == 'Y' or choice == 'y':
        command("bash ~/cshell/uninstall.sh")
        sys.exit(0)
    else:
        print(Fore.GREEN + "\nAborted.")

def wait(value):
    command("sleep " + value)

def command(command):
    subprocess.run([command],
                   shell = True)
    
def setPwd(pwd):
    global password 
    global passwordSet

    if len(pwd) < 5:
        print(Fore.RED  + "Password must be at least " +
                           Fore.BLUE + "5 " +
                           Fore.RED  + "characters long!")
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
                print(Fore.CYAN + "Enter password to unlock CShell.")
                pwdAttempt = input()

                if pwdAttempt == password:
                    locked = False
                else:
                    print(Fore.RED + "\nIncorrect password!\n")
                    attemptsLeft -= 1
            else:
                os.system("clear")
                print(Fore.RED + "You are out of attempts! Wait 5 seconds to try again!")
                wait(str(5))
                # Resets the attempts
                print()
                attemptsLeft = 5
    else:
        print(Fore.RED  + "You need to set a password first in order to use this command.")
        print(Fore.RED  + "Use the command " +
              Fore.BLUE + "\"pwd <password>\" " + 
              Fore.RED  + "to set your password")

def update():
    if shutil.which("apt"):   
        command("sudo apt update && sudo apt upgrade")

    elif shutil.which("dnf"):   
        command("sudo dnf update")

    elif shutil.which("pacman"):
        command("sudo pacman -Syu")
    else:
        print(Fore.RED + "Unable to update: Unsupported package manager!")

def upgrade():
    print(Fore.CYAN + "Do you want to update CShell?\n" +
          Fore.BLUE + "(Y/N)")
    
    print(Fore.RED + "Note: This will uninstall then reinstall CShell.")
    
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
    
    print(Fore.CYAN + "\nWould you like to reload CShell?")
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
        print(Fore.RED  + "Unsupported file extension! CShell only supports files ending with \"" +
                  Fore.BLUE + ".cshell" +
                  Fore.RED  + "\"!")
    else:
        if answer.endswith(".cshell"):
            try:
                with open(scriptPath, "r") as file:
                        for line in file:
                            processCommand(line.strip())
            except:
                print(Fore.RED + "Error: File/directory not found!")
        
        else:
            print(Fore.RED + "The path to the script must be the full path. " +
                Fore.CYAN + "\nEx: " +
                Fore.BLUE + "/home/(your username)/file.cshell")

"""
Info
"""

def credits():
    print(Fore.CYAN   + "Meme Supplier" +
          Fore.BLUE   + ": owner, programmer, maintainer\n" +
          Fore.YELLOW + "Contact: " +
          Fore.BLUE   + "memesupplierbusiness@gmail.com\n" +
          Fore.GREEN  + "2025 Meme Supplier")

def help():
    if sufficientPacMan and isLinux:
        print(Fore.CYAN   + "Welcome to " +
            Fore.GREEN  + "CShell " +
            Fore.YELLOW + cshellVer)
        print(Fore.CYAN   + "Type " +
            Fore.BLUE   + "\"cmds\"" +
            Fore.CYAN   + " for some commands!\n")

def ver():
#   CShell version
    print(Fore.CYAN  + '\nCSHELL' +
          Fore.BLUE  + ' version: ' +
          Fore.GREEN + cshellVer)
    print(Fore.CYAN  + platform.system() ,
          Fore.BLUE  + platform.release())
    
#   Python version
    print(Fore.CYAN + "Python " +
          Fore.BLUE + sys.version +
          '\n')

"""
Misc
"""

def gitInstalled():
    try:
        subprocess.run(["git", "--version"],
                    stdout = subprocess.PIPE,
                    stderr = subprocess.PIPE,
                    check  = True)
        return True
    except (subprocess.CalledProcessError,
           FileNotFoundError):
        return False

"""
Program
"""

if shutil.which("apt") or shutil.which("dnf") or shutil.which("pacman"):   
    sufficientPacMan = True
else:
    sufficientPacMan = False

    print(Fore.RED  + "Unsupported package manager! Please use " +
          Fore.BLUE + "Apt" +
          Fore.RED  + ", " +
          Fore.BLUE + "Dnf" +
          Fore.RED  + ", or " +
          Fore.BLUE + "Pacman" +
          Fore.RED  + ".")

if platform.system() == "Linux":
    isLinux = True
else:
    isLinux = False

if not isLinux:
    print(Fore.CYAN + "This script is for " +
          Fore.BLUE + "Linux " +
          Fore.RED  + "only! " +
          Fore.CYAN + "Either install Linux for edit the code " +
          Fore.RED  + "(it may not work as expected or break if you edit the code).\n"  )

    sys.exit(1)

help()

while True and isLinux and not locked and sufficientPacMan:

    answer = input(Fore.BLUE   + "CShell" +
                   Fore.GREEN  + '$' +
                   Fore.CYAN   + '~' +
                   Fore.WHITE  + ': ')
    
    processCommand(answer)
