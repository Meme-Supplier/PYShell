#!/usr/bin/env python3

"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

from colorama import Fore, init
init(autoreset = True)

import logger

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
12: Incorrect equation entered
13: Flatpak not installed
14: Logging failed

"""

def handle(errorID):
    
    match errorID:

        case 1:
            print(Fore.RED + "Unable to execute command: Unsupported package manager!")
            logger.log("Error 1: Unsupported package manager")

        case 2:
            print(Fore.RED + "File/Directory doesn't exist!")
            logger.log("Error 2: Nonexisting file/directory")

        case 3:
            print(Fore.RED + "Git is not installed. Please install Git.")
            logger.log("Error 3: Git is not installed")
        
        case 4:
            print(Fore.RED  + "Password must be at least " +
                  Fore.BLUE + "5 " +
                  Fore.RED  + "characters long!")
            logger.log("Error 4: Insufficient password length")

        case 5:
            print(Fore.RED + "\nIncorrect password!\n")
            logger.log("Error 5: Incorrect password entered")
        
        case 6:
            print(Fore.RED + "You are out of attempts! Wait 5 seconds to try again!")
            logger.log("Error 6: Out of password attempts")

        case 7:
            print(Fore.RED  + "You need to set a password first in order to use this command.")
            print(Fore.RED  + "Use the command " +
                  Fore.BLUE + "\"pwd <password>\" " + 
                  Fore.RED  + "to set your password")

            logger.log("Error 7: Password isn't set")
        
        case 8:
            print(Fore.RED + "The path to the script must be the full path. " +
                  Fore.CYAN + "\nEx: " +
                  Fore.BLUE + "/home/(your username)/file.pyshell")
            
            logger.log("Error 8: Full path hasn't been entered")
        
        case 9:
            print(Fore.RED  + "Unsupported file extension! PYShell only supports files ending with \"" +
                  Fore.BLUE + ".pyshell" +
                  Fore.RED  + "\"!")
            
            logger.log("Error 9: File extension not supported.")
            
        case 10:
            print(Fore.RED  + "Unsupported package manager! Please use " +
                  Fore.BLUE + "Apt" +
                  Fore.RED  + ", " +
                  Fore.BLUE + "Dnf" +
                  Fore.RED  + ", or " +
                  Fore.BLUE + "Pacman" +
                  Fore.RED  + ".")
            
            logger.log("Error 10: Unsupported file manager")
        
        case 11:
            print(Fore.CYAN + "This script is for " +
                  Fore.BLUE + "Linux " +
                  Fore.RED  + "only! " +
                  Fore.CYAN + "Either install Linux for edit the code " +
                  Fore.RED  + "(it may not work as expected or break if you edit the code).\n")
            
            logger.log("Error 11: This script is made for linux ONLY!")
        
        case 12:
            print(Fore.RED + "Incorrect equation!")
            logger.log("Error 12: Incorrect equation entered")
        
        case 13:
            print(Fore.RED + "Flatpak is not installed! Please install it!")
            logger.log("Error 13: Flatpak not installed")
        case 14:
            print(Fore.RED + "Logging failed! (You can ignore this message, but if this continues, please reinstall PYShell.)")
            logger.log("Error 14: Logging failed! Skipping...")
        
        # Does nothing
        case _:
            None
