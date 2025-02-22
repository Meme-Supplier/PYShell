#!/usr/bin/env python3

"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

from colorama import Fore, init
init(autoreset = True)

"""

Error IDs

1:  Unsupported package manager
2:  File/Directory not found
3:  Git not installed
4:  Password not long enough
5:  Incorrect password
6:  No more attempts
7:  You need to set a password first
8:  Path must be the full path
9:  Unsupported file extension
10: Unsupported package manager (startup)
11: Linux only error

"""

def handle(id):
    
    match id:
        case 1:
            print(Fore.RED + "Unable to execute command: Unsupported package manager!")

        case 2:
            print(Fore.RED + "File/Directory doesn't exist!")

        case 3:
            print(Fore.RED + "Git is not installed. Please install Git.")
        
        case 4:
            print(Fore.RED  + "Password must be at least " +
                  Fore.BLUE + "5 " +
                  Fore.RED  + "characters long!")

        case 5:
            print(Fore.RED + "\nIncorrect password!\n")
        
        case 6:
            print(Fore.RED + "You are out of attempts! Wait 5 seconds to try again!")

        case 7:
            print(Fore.RED  + "You need to set a password first in order to use this command.")
            print(Fore.RED  + "Use the command " +
                  Fore.BLUE + "\"pwd <password>\" " + 
                  Fore.RED  + "to set your password")
        
        case 8:
            print(Fore.RED + "The path to the script must be the full path. " +
                  Fore.CYAN + "\nEx: " +
                  Fore.BLUE + "/home/(your username)/file.cshell")
        
        case 9:
            print(Fore.RED  + "Unsupported file extension! CSHELL only supports files ending with \"" +
                  Fore.BLUE + ".cshell" +
                  Fore.RED  + "\"!")
            
        case 10:
            print(Fore.RED  + "Unsupported package manager! Please use " +
                  Fore.BLUE + "Apt" +
                  Fore.RED  + ", " +
                  Fore.BLUE + "Dnf" +
                  Fore.RED  + ", or " +
                  Fore.BLUE + "Pacman" +
                  Fore.RED  + ".")
        
        case 11:
            print(Fore.CYAN + "This script is for " +
                  Fore.BLUE + "Linux " +
                  Fore.RED  + "only! " +
                  Fore.CYAN + "Either install Linux for edit the code " +
                  Fore.RED  + "(it may not work as expected or break if you edit the code).\n")
            
        # Does nothing
        case _:
            None
