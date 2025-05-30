#!/usr/bin/env python3
"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

from colorama import Fore, init
init(autoreset = True)

def list():
    print(f"{Fore.YELLOW}\nAvailable commands:\n")
    print(f"{Fore.CYAN}Command "
          f"{Fore.BLUE}Usage "
          f"{Fore.GREEN}Description ")

#   Exit
    print(Fore.CYAN  + "exit " +
          Fore.GREEN + "Exits PYShell")
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
          Fore.GREEN + " Shows PYShell's version")
#   Lock
    print(Fore.CYAN  + "lock" +
          Fore.GREEN + " Locks the terminal")
#   Xray
    print(Fore.CYAN  + "xray" +
          Fore.GREEN + " Allows you to easily edit PYShell")
#   Reload
    print(Fore.CYAN  + "reload" +
          Fore.GREEN + " Reloads PYShell")
#   Clean
    print(Fore.CYAN  + "clean" +
          Fore.GREEN + " removes unnecessary packages")
#   Reload
    print(Fore.CYAN  + "uptime" +
          Fore.GREEN + " Shows how long your system has been on")
#   Shutdown
    print(Fore.CYAN  + "shutdown" +
          Fore.GREEN + " Shuts down your system")
#   Restart
    print(Fore.CYAN  + "restart" +
          Fore.GREEN + " Reboots your system")
#   Uninstall
    print(Fore.CYAN  + "uninstall" +
          Fore.GREEN + " Uninstalls PYShell.")
#   Create
    print(Fore.CYAN  + "create " +
          Fore.BLUE  + "<path to file>" +
          Fore.GREEN + " Creates a file")
#   Wait
    print(Fore.CYAN  + "wait" +
          Fore.BLUE  + " <time (seconds)>" +
          Fore.GREEN + " Waits your desired time")
#   Pm
    print(Fore.CYAN  + "pm" +
          Fore.BLUE  + " <apt/dnf/pacman> <rest of the command>" +
          Fore.GREEN + " Runs Apt, Dnf, or Pacman.")
#   Copy
    print(Fore.CYAN  + "copy" +
          Fore.BLUE  + " <path to file> <path to destination>" +
          Fore.GREEN + " Copies a file from one place to another.")
#   Newdir
    print(Fore.CYAN  + "newdir" +
          Fore.BLUE  + " <path to directory>" +
          Fore.GREEN + " Creates a directory in the desired path.")
#   Echo
    print(Fore.CYAN  + "echo" +
          Fore.BLUE  + " <text>" +
          Fore.GREEN + " Prints text")
#   Sh
    print(Fore.CYAN  + "sh " +
          Fore.BLUE  + "<commands>" +
          Fore.GREEN + " Runs normal shell commands ")
#   Expr
    print(Fore.CYAN  + "expr " +
          Fore.BLUE  + "<equation>" +
          Fore.GREEN + " Solves a math equation")
#   Web
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
          Fore.GREEN + " Runs a PYShell script")
#   Pscript
    print(Fore.CYAN  + "pscript " +
          Fore.BLUE  + "<path to " +
          Fore.BLUE  + "file>" +
          Fore.GREEN + " Runs a Python script")
#   In
    print(Fore.CYAN  + "in " +
          Fore.BLUE  + "<text>" +
          Fore.GREEN + " Recieves confimation from user")
#   Ls
    print(Fore.CYAN  + "ls " +
          Fore.BLUE  + "<directory>" +
          Fore.GREEN + " Lists the specified directory")
#   Ping
    print(Fore.CYAN  + "ping " +
          Fore.BLUE  + "<web page>" +
          Fore.GREEN + " Pings a web page")
#   Edit
    print(Fore.CYAN  + "edit " +
          Fore.BLUE  + "<text file>" +
          Fore.GREEN + " Edits a text file within the terminal.")
#   Pwd
    print(Fore.CYAN  + "pwd " +
          Fore.BLUE  + "<password>" +
          Fore.GREEN + " Sets a password ")
#   Del
    print(Fore.CYAN  + "del " +
          Fore.BLUE  + "<path to file/directory>" +
          Fore.GREEN + " Deletes a file/directory ")
#   Update
    print(Fore.CYAN  + "update " +
          Fore.GREEN + " Updates your device ")
#   Upgrade
    print(Fore.CYAN  + "upgrade" +
          Fore.GREEN + " Updates PYShell")
#   Logs
    print(Fore.CYAN  + "logs" +
          Fore.GREEN + " Views logs for PYShell.")
#   Dellogs
    print(Fore.CYAN  + "dellogs" +
          Fore.GREEN + " Deletes PYShell's logs.")
#   Time
    print(Fore.CYAN  + "time" +
          Fore.GREEN + " Displays the time.")
#   Title
    print(Fore.CYAN  + "title" +
          Fore.GREEN + " Sets the window title")
#   Rmtitle
    print(Fore.CYAN  + "rmtitle" +
          Fore.GREEN + " Resets window title")

    print()

    __import__("logger").log("cmdList: Commands listed")
