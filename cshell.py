#!/usr/bin/env python3

"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

try:
    import os
    import sys
    import subprocess
    import platform
    import webbrowser
    import shutil

    os.system("clear")

    pythonMajor = sys.version_info.major # Ex: 3.x.x
    pythonMinor = sys.version_info.minor # Ex: x.12.x
    pythonMicro = sys.version_info.micro # Ex: x.x.3
    pythonVersion = str(pythonMajor) + "." + str(pythonMinor) + "." + str(pythonMicro)

    cshellVer = "v0.9.1"

    locked = False
    passwordSet = False
    password = ''

    #   Attempts to confirm Colorama's existence
    try:
        coloramaInstalled = True 
        from colorama import Fore, init
        init(autoreset=True)

    #   If not installed, you will be prompted to install Colorama.
    except:
        coloramaInstalled = False

        print(Fore.RED + "Colorama doesn't appear to be installed!\n" +
            Fore.RED + "Would you like to install it?\n(Y or N)\n")

        choice = input("\n")

    """
    Define
    functions
    """

    def commands():

        """
        Command list
        """

        print('\n' +
    #         Color        Output          
            Fore.YELLOW + "Available commands:\n")
    #   Exit
        print(Fore.CYAN + "exit " +
            Fore.GREEN + "Exits CShell")
    #   Clear
        print(Fore.CYAN + "clear" +
            Fore.GREEN + " Clears the screen")
    #   Help
        print(Fore.CYAN + "help" +
            Fore.GREEN + " Some info")
    #   Cmds
        print(Fore.CYAN + "cmds" +
            Fore.GREEN + " Lists available commands")
    #   Python
        print(Fore.CYAN + "python" +
            Fore.GREEN + " Opens python")
    #   Ver
        print(Fore.CYAN + "ver" +
            Fore.GREEN + " Shows CShell's version")
    #   Lock
        print(Fore.CYAN + "lock" +
            Fore.GREEN + " Locks the terminal")
    #   Edit
        print(Fore.CYAN + "edit" +
            Fore.GREEN + " Allows you to easily edit CShell")
    #   Reload
        print(Fore.CYAN + "reload" +
            Fore.GREEN + " Reloads CShell")
    #   Reload
        print(Fore.CYAN + "uptime" +
            Fore.GREEN + " Shows how long your system has been on")
    #   Shutdown
        print(Fore.CYAN + "shutdown" +
            Fore.GREEN+ " Shuts down your system")
    #   Uninstall
        print(Fore.CYAN + "uninstall" +
            Fore.GREEN+ " Uninstalls CShell.")
    #   Wait
        print(Fore.CYAN + "wait"     +
            Fore.BLUE + " <time (seconds)>" +
            Fore.GREEN + " Waits your desired time")
    #   Echo
        print(Fore.CYAN + "echo"     +
            Fore.BLUE + " <text>" +
            Fore.GREEN + " Prints text")
    #   Bash
        print(Fore.CYAN + "bash " +
            Fore.BLUE + "<commands>" +
            Fore.GREEN + " Runs normal shell commands " +
            Fore.RED + "Notice: commands like \"cd\" and \"dir\" won't work.")
    #   Expr
        print(Fore.CYAN + "expr "    +
            Fore.BLUE + "<equation>" +
            Fore.GREEN + " Solves a math equation")
    #   Web
        print(Fore.CYAN + "web "     +
            Fore.BLUE + "<website>" +
            Fore.GREEN + " Opens your desired website")
    #   Git
        print(Fore.CYAN + "git <rest of the command>" +
            Fore.GREEN+ " Runs git\n")
    #   Script
        print(Fore.CYAN + "script "     +
            Fore.BLUE + "<path to " +
            Fore.BLUE + "file>" +
            Fore.GREEN + " Runs a CShell script")
    #   In
        print(Fore.CYAN + "in "     +
            Fore.BLUE + "<text>" +
            Fore.GREEN + " Recieves confimation from user")
    #   Ls
        print(Fore.CYAN + "ls "     +
            Fore.BLUE + "<directory>" +
            Fore.GREEN + " Lists the specified directory")
    #   Pwd
        print(Fore.CYAN + "pwd "     +
            Fore.BLUE + "<password>" +
            Fore.GREEN + " Sets a password " +
            Fore.RED + "Notice: Password has to be at least 5 characters long.")
    #   Update
        print(Fore.CYAN + "update "     +
            Fore.GREEN + " Updates your device " +
            Fore.RED + "Notice: Only supports Fedora, Arch, and Debian based distros.")
    #   Upgrade
        print(Fore.CYAN + "upgrade" +
            Fore.GREEN+ " Updates CShell\n")

    def processCommand(answer):
    #   Goes through and executes commands
        match answer:
    #            Input         Response  
            case "clear"     : os.system('clear')
            case "help"      : help()
            case "cmds"      : commands()
            case "exit"      : sys.exit(0)
            case "python"    : command("python3")
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

    #       Commands that require syntax
    #       (Show usage)

            case "echo"   : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "echo <message>")
            case "expr"   : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "expr <equation>")
            case "bash"   : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "bash <command>")
            case "web"    : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "web <website>")
            case "wait"   : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "wait <time (seconds)>")
            case "pwd"    : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "pwd <password>")
            case "script" : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "script <script path>")
            case "ls"     : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "ls <directory>")
            case ''       : ()

            case _ :
    #           Multi-syntax
                if   answer.startswith ("echo ")   : command(answer)
                elif answer.startswith ("expr ")   : command(answer)
                elif answer.startswith ("bash ")   : command(answer.replace("bash " , "" , 1))
                elif answer.startswith ("web ")    : webbrowser.open_new(answer.replace("web " , "" , 1))
                elif answer.startswith ("wait ")   : wait(answer.replace("wait " , "" , 1))
                elif answer.startswith ("pwd ")    : setPwd(answer.replace("pwd " , "" , 1))
                elif answer.startswith ("script ") : script(answer.replace("script " , "" , 1))
                elif answer.startswith ("in ")     : input(answer.replace("in " , "" , 1) + '\n')
                elif answer.startswith ("ls ")     : ls(answer.replace("ls " , "" , 1) + '\n')
                elif answer.startswith ("flatpak") : command(answer)
                elif answer.startswith ("git")     : git()

    #           If nothing checks out
                else: print(Fore.RED +
                        answer +
                        ": invalid command.")
    """
    Info
    """

    def git():
        if gitInstalled():
            command(answer)
        else:
            print(Fore.RED + "Git is not installed. Please install Git.")

    def credits():
        print(Fore.CYAN + "Meme Supplier" +
            Fore.BLUE + ": owner, programmer, maintainer\n" +
            Fore.YELLOW + "Contact: " +
            Fore.BLUE + "memesupplierbusiness@gmail.com\n" +
            Fore.GREEN + "2025 Meme Supplier")

    def help():
    #         Color         Output
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
            Fore.BLUE + sys.version + '\n')

    """
    Scripting
    Commands
    """

    def ls(lsDir):
        command("ls " + lsDir)

    def uninstall():
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

        if len(pwd) < 5: print(Fore.RED  + "Password must be at least " +
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

            while locked:
                print(Fore.CYAN + "Enter password to unlock CShell.")
                pwdAttempt = input()

                if pwdAttempt == password:
                    locked = False
                else:
                    print(Fore.RED + "Incorrect password!\n")
        else:
            print(Fore.RED + "You need to set a password first in order to use this command.")
            print(Fore.RED + "Use the command " +
                Fore.BLUE + "\"pwd <password>\" " + 
                Fore.RED + "to set your password")

    def update():
        if shutil.which("apt"):   
            command("sudo apt update && sudo apt upgrade")
        elif shutil.which("dnf"):   
            command("sudo dnf update")
        elif shutil.which("pacman"):
            command("sudo pacman -Syu")
        else:
            print(Fore.RED + "Unsupported package manager!")

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
        try:    
            command("nano ~/cshell/cshell.py")
        except:
            print(Fore.RED + "Unable to use command: Nano is not installed!")

        print(Fore.BLUE + "\nChanges applied.")
        reload()

    def reload():
        
        print(Fore.CYAN + "\nWould you like to reload CShell?")
        choice = input()

        if choice == 'Y' or choice == 'y': 
            print("Reloading script...")
            os.execv(sys.executable,
                    ['python3'] +
                    sys.argv)
        else:
            print(Fore.RED + "Aborted.")

    def script(scriptPath):
        try:
            with open(scriptPath, "r") as file:
                    for line in file:
                        processCommand(line.strip())
        except:
            print(Fore.RED + "Error: File/directory not found! Try entering the path to the file again!")

    """
    Misc
    """

    def gitInstalled():
        try:
            subprocess.run(["git", "--version"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        check=True)
            return True
        except (subprocess.CalledProcessError,
                FileNotFoundError):
            return False

    """
    Program
    """

    if platform.system() == "Linux":
        isLinux = True
    else:
        isLinux = False

    # Python 3.10 is required
    if pythonMajor == 3 and pythonMinor >= 10:
        sufficentVersion = True
    else:
        sufficentVersion = False
        print("You must have Python 3.10 or newer to run CShell.")
        input()

    if not isLinux:
    #          Color       Output
        print(Fore.CYAN + "This script is for " +
            Fore.BLUE + "Linux " +
            Fore.RED  + "only! " +
            Fore.CYAN + "Either install Linux for edit the code " +
            Fore.RED  + "(it may not work as expected or break if you edit the code).\n"  )

        sys.exit(1)

        if choice == 'Y' or choice == 'y':
    #           Opens the download page for Colorama
            webbrowser.open_new("https://pypi.org/project/colorama/")
        else:
    #           Cancels the action, and exits CShell
            print("\nAborted.\nPlease install Colorama to continue.")

    if isLinux and sufficentVersion:
        help()

    while True and coloramaInstalled and isLinux and sufficentVersion and not locked:
    #                  Color         Output
        answer = input(Fore.BLUE   + 'CShell' +
                    Fore.GREEN  + '$' +
                    Fore.CYAN + '~' +
                    Fore.WHITE  + ': ')

        processCommand(answer)
except:
    print("CShell is corrupted, or missing files. Would you like to reinstall it?\n(Y or N)")
    choice = input()

    if choice == 'Y' or choice == 'y':
        __import__('os').system('bash ~/cshell/upgrade.sh')

"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""
