#!/usr/bin/env python3

"""
2025 Meme Supplier
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
pythonVersion = str(f"{pythonMajor}.{pythonMinor}.{pythonMicro}")
pythonVersionShort = str(f"{pythonMajor}.{pythonMinor}")
logger.log(f"PYShell: Python version: {pythonVersion}")

pyshellVer = "v2.1"
logger.log(f"PYShell: PYShell version: {pyshellVer}")

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

def windowTitle(string):
    os.system(f'printf "\033]0;{str(string)}\007"')
    logger.log(f"PYShell: Window title set to: {str(string)}")

def processCommand(answer):
    # Goes through and executes commands

    match answer:
        case "clear"     : os.system('clear')
        case "help"      : help()
        case "python"    : command(f"python{pythonVersionShort}")
        case "cmds"      : cmdList.list()
        case "exit"      : logger.log("PYShell: Exiting PYShell..."); sys.exit(0)
        case "shutdown"  : command("shutdown now")
        case "reboot"    : command("reboot")
        case "ping"      : command("ping")
        case "credits"   : credits()
        case "ver"       : ver()
        case "update"    : update() # updates your system
        case "upgrade"   : upgrade() # updates PYShell
        case "lock"      : lock()
        case "xray"      : edit()
        case "reload"    : reload()
        case "in"        : input()
        case "uptime"    : command("uptime")
        case "uninstall" : uninstall()
        case "quit"      : quit()
        case "clean"     : clean()
        case "logs"      : command("nano ~/pyshell/logs.txt")
        case "dellogs"   : delLogs()
        case "time"      : print(logger.initTime())
        case "rmtitle"   : windowTitle("PYShell")

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
        case "title"   : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "title <window title>")
        case ''        : None

        case _ :

            # Handle multiple commands separated by "&&"
            if " && " in answer:
                for cmd in answer.split(" && "):
                    processCommand(cmd.strip())

                return  # Exit after handling multiple commands

            # Multi-syntax commands
            if   answer.startswith ("echo ")    : command(answer)
            elif answer.startswith ("expr ")    : expr()
            elif answer.startswith ("sh ")      : command("answer.replace("sh " , "" , 1))
            elif answer.startswith ("web ")     : web(answer.replace("web " , "" , 1))
            elif answer.startswith ("wait ")    : wait(answer.replace("wait " , "" , 1))
            elif answer.startswith ("pwd ")     : setPwd(answer.replace("pwd " , "" , 1))
            elif answer.startswith ("script ")  : script(answer.replace("script " , "" , 1))
            elif answer.startswith ("pscript ") : command("python3 " + answer.replace("pscript " , "" , 1))
            elif answer.startswith ("in ")      : input(answer.replace("in " , "" , 1) + '\n')
            elif answer.startswith ("ls ")      : command("\nls " + answer.replace("ls " , "" , 1))
            elif answer.startswith ("flatpak")  : flatpak()
            elif answer.startswith ("git")      : git()
            elif answer.startswith ("create ")  : command("touch " + answer.replace("create " ,"" , 1))
            elif answer.startswith ("del ")     : delete (answer.replace("del " , "" , 1))
            elif answer.startswith ("pm ")      : pm(answer.replace("pm " , "" , 1))
            elif answer.startswith ("python")   : command(answer)
            elif answer.startswith ("newdir ")  : command("mkdir " + answer.replace("newdir " , "" , 1))
            elif answer.startswith ("copy ")    : command("cp " + answer.replace("copy " , "" , 1) + " -rf")
            elif answer.startswith ("ping ")    : command(answer)
            elif answer.startswith ("edit ")    : command("nano " + answer.replace("edit " , "" , 1))
            elif answer.startswith ("title ")   : windowTitle(answer.replace("title " , "" , 1))
            elif answer.startswith ("error ")   : err(answer.replace("error " , "" , 1))

            # If nothing checks out
            else:
                print(f"{Fore.RED}{answer}: invalid command.")

            logger.log(f"PYShell: Executed command: {answer}")

"""
Scripting
Commands
"""

def err(err):
    try:
        error.handle(int(err))
    except:
        error.handle(16)

def flatpak():
    if flatpakInstalled():
        command(answer)
    else:
        error.handle(13)

def expr():
    try:
        print(
            eval(
                 answer.replace("expr " , "" , 1)))
    except:
        error.handle(12)

def delLogs():

    command("rm ~/pyshell/logs.txt -f")
    logger.log("##### Initial log deletion #####")

    os.execv(sys.executable,
             ["python3"] +
             sys.argv)

def web(page):
    if page.startswith("https://www."):
        webbrowser.open_new_tab(page)
    else:
        webbrowser.open_new_tab(f"https://www.{page}")
    logger.log(f"PYShell: Opened webpage {page}")

def pm(cmd):

    if os.geteuid() == 0:
        command("sudo echo \"Sudo is enabled for this command.\"")

    if shutil.which("apt") or shutil.which("dnf") or shutil.which("pacman"):
        command(cmd)
    else:
        error.handle(1)

def newdir(dir):
    Path(dir).mkdir(parents = True,
                    exist_ok = True)

    logger.log(f"PYShell: Directory created: {dir}")

def clean():

    if os.geteuid() == 0:
        command("sudo echo \"Sudo is enabled for this command.\"")

    if sufficientPacMan:
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
        command(f"rm -rf {file}")
        logger.log(f"PYShell: Deleted file {file}")
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

    choice = input(f"{Fore.RED}\nAre you sure you want to uninstall PYShell?\n{Fore.WHITE}")

    if choice == 'Y' or choice == 'y':
        logger.log("PYShell: Uninstalling: Sorry to see you go :(")
        logger.pyShellDeleted = True
        command("bash ~/pyshell/uninstall.sh")
        sys.exit(0)
    else:
        print(f"{Fore.GREEN}\nAborted.")
        logger.log("PYShell: Aborted: Uninstall PYShell")

def wait(time):
    command(f"sleep {str(time)}")
    logger.log(f"PYShell: Waited {str(time)} seconds")

def command(command):
    subprocess.run(command,
                   shell = True)
    logger.log(f"PYShell: Ran shell command: {command}")

def setPwd(pwd):
    global password
    global passwordSet

    if len(pwd) < 5:
        error.handle(4)
    else:
        password = pwd
        passwordSet = True

        print(f"{Fore.CYAN}Password has been set to {Fore.BLUE}{password}")

        logger.log(f"PYShell: Set password to {password}")

def lock():
    if passwordSet:
        logger.log("PYShell: Locked PYShell")

        os.system("clear")

        global locked
        locked = True

        attemptsLeft = 5

        while locked:

            if attemptsLeft != 0:
                print(f"{Fore.CYAN}Enter password to unlock PYShell.")
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
        return

    if sufficientPacMan:
        logger.log("Successfully updated device.")

def upgrade():
    print(f"{Fore.CYAN}Do you want to update PYShell?\n{Fore.BLUE}(Y/N)\n")

    print(f"{Fore.RED}Note: This will uninstall then reinstall PYShell.")

    choice = input()

    if choice == 'Y' or choice == 'y':
        logger.log("PYShell: Upgrading PYShell")
        command("bash ~/pyshell/upgrade.sh")
        sys.exit(0)
    else:
        print(f"{Fore.RED}Aborted.")
        logger.log("PYShell: Aborted: Upgrade PYShell")

def edit():
    if nanoInstalled():
        command("nano ~/pyshell/pyshell.py")

        print(f"{Fore.BLUE}\nChanges applied.")
        logger.log("PYShell: Made changes to PYShell")

        reload()

    else:
        print(f"{Fore.RED}Nano is not installed! Please install it!")
        error.handle(15)

def reload():

    print(f"{Fore.CYAN}\nWould you like to reload PYShell?")
    choice = input()

    if choice == 'Y' or choice == 'y':
        print("Reloading script...")

        logger.log("PYShell: Reloaded PYShell")

        os.execv(sys.executable,
                ["python3"] +
                sys.argv)
    else:
        print(f"{Fore.RED}Aborted.")
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
                logger.log(f"PYShell: Ran script: {scriptPath}")
            except:
                error.handle(2)
        else:
            error.handle(9)

def credits():
    print(f"{Fore.CYAN}Meme Supplier{Fore.BLUE}: owner, programmer, maintainer\n" +
          f"{Fore.YELLOW}Contact: "
          f"{Fore.BLUE}memesupplierbusiness@gmail.com\n" +
          f"{Fore.GREEN}2025 Meme Supplier")

def help():
    if sufficientPacMan and isLinux:
        print(f"{Fore.CYAN}\nWelcome to "
              f"{Fore.GREEN}PYShell "
              f"{Fore.YELLOW}{pyshellVer}")
        print(f"{Fore.CYAN}Type "
              f"{Fore.BLUE}\"cmds\""
              f"{Fore.CYAN} for some commands!\n")

def ver():
#   PYShell version
    print(f"{Fore.CYAN}\nPYShell"
          f"{Fore.BLUE} version: "
          f"{Fore.GREEN}{pyshellVer}")

#   Python version
    print(f"{Fore.CYAN}Python "
          f"{Fore.BLUE}{pythonVersion}\n")

#   System info

    # Distro
    print(f"{Fore.CYAN}OS: "
          f"{Fore.BLUE}{sysInfo.getDistro()}")

    # Kernel version
    print(f"{Fore.CYAN}Kernel: "
          f"{Fore.BLUE}{platform.release()}")

    # Window Manager
    print(f"{Fore.CYAN}WM: "
          f"{Fore.BLUE}{sysInfo.getWM()} ({os.environ.get('XDG_SESSION_TYPE')})")

    # Desktop Enviornment
    print(f"{Fore.CYAN}DE:",
          f"{Fore.BLUE}{sysInfo.getDE(["XDG_CURRENT_DESKTOP","DESKTOP_SESSION"])}")

    print(f"{Fore.CYAN}Terminal: "
          f"{Fore.BLUE}{sysInfo.getShell()}")

    print()

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

        logger.log("PYShell: Git is not installed!")

        return False

def flatpakInstalled(): # Is flatpak installed?
    logger.log("PYShell: Checking if Flatpak is installed...")

    try:
        subprocess.run(["flatpak", "--version"],
                        stdout = subprocess.PIPE,
			stderr = subprocess.PIPE,
                        check  = True)

        logger.log("PYShell: Flatpak is installed")

        return True
    except (subprocess.CalledProcessError,
            FileNotFoundError):

        logger.log("PYShell: Flatpak is not installed")

        return False

def nanoInstalled(): # Is flatpak installed?
    logger.log("PYShell: Checking if Nano is installed...")

    try:
        subprocess.run(["nano", "--version"],
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,
                        check  = True)

        logger.log("PYShell: Nano is installed")

        return True
    except (subprocess.CalledProcessError,
            FileNotFoundError):

        logger.log("PYShell: Nano is not installed")

        return False

"""
Program
"""

help()

windowTitle("PYShell")

while True and isLinux and not locked and sufficientPacMan:

    answer = input(f"{Fore.BLUE}PYShell{Fore.GREEN}${Fore.CYAN}~{Fore.WHITE}: ")

    processCommand(answer)
