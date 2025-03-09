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
15: Nano not installed
16: Error isn't an integer

"""

def handle(errorID):
    try:
        match errorID:

            case 1:
                print(f"{Fore.RED}Unable to execute command: Unsupported package manager!")
                logger.log("Error 1: Unsupported package manager")

            case 2:
                print(f"{Fore.RED}File/Directory doesn't exist!")
                logger.log("Error 2: Nonexisting file/directory")

            case 3:
                print(f"{Fore.RED}Git is not installed. Please install Git.")
                logger.log("Error 3: Git is not installed")

            case 4:
                print(f"{Fore.RED}Password must be at least "
                      f"{Fore.BLUE}5 "
                      f"{Fore.RED}characters long!")
                logger.log("Error 4: Insufficient password length")

            case 5:
                print(f"{Fore.RED}Incorrect password!")
                logger.log("Error 5: Incorrect password entered")

            case 6:
                print(f"{Fore.RED}You are out of attempts! Wait 5 seconds to try again!")
                logger.log("Error 6: Out of password attempts")

            case 7:
                print(f"{Fore.RED}You need to set a password first in order to use this command.")
                print(f"{Fore.RED}Use the command "
                      f"{Fore.BLUE}\"pwd <password>\" "
                      f"{Fore.RED}to set your password")

                logger.log("Error 7: Password isn't set")

            case 8:
                print(f"{Fore.RED}The path to the script must be the full path. "
                      f"{Fore.CYAN}\nEx: "
                      f"{Fore.BLUE}/home/(your username)/file.pyshell")

                logger.log("Error 8: Full path hasn't been entered")

            case 9:
                print(f"{Fore.RED}Unsupported file extension! PYShell only supports files ending with \""
                      f"{Fore.BLUE}.pyshell"
                      f"{Fore.RED}\"!")

                logger.log("Error 9: File extension not supported.")

            case 10:
                print(f"{Fore.RED}Unsupported package manager! Please use "
                      f"{Fore.BLUE}Apt"
                      f"{Fore.RED}, "
                      f"{Fore.BLUE}Dnf"
                      f"{Fore.RED}, or "
                      f"{Fore.BLUE}Pacman"
                      f"{Fore.RED}.")

                logger.log("Error 10: Unsupported file manager")

            case 11:
                print(f"{Fore.CYAN}This script is for "
                      f"{Fore.BLUE}Linux "
                      f"{Fore.RED}only! "
                      f"{Fore.CYAN}Either install Linux for edit the code "
                      f"{Fore.RED}(it may not work as expected or break if you edit the code).")

                logger.log("Error 11: This script is made for linux ONLY!")

            case 12:
                print(f"{Fore.RED}Incorrect equation!")
                logger.log("Error 12: Incorrect equation entered")

            case 13:
                print(f"{Fore.RED}Flatpak is not installed! Please install it!")
                logger.log("Error 13: Flatpak not installed")
            case 14:
                print(f"{Fore.RED}Logging failed! (You can ignore this message, but if this continues, please reinstall PYShell.)")
                logger.log("Error 14: Logging failed! Skipping...")
            case 15:
                print(f"{Fore.RED}Nano is not installed! Please install it!")
                logger.log("Error 15: Nano not installed")
            case 16:
                print(f"{Fore.RED}Error to handle must be an integer!")
                logger.log("Error 16: Error to handle must be an integer!")

            # Does nothing
            case _:
                None
    except:
        print("Unknown error")
