# 2025 Meme Supplier
# memesupplierbusiness@gmail.com
# Maintained by Meme Supplier

import os, sys, subprocess, platform, webbrowser
os.system('clear')

cshellVer = "v0.4"

def command(command):
    subprocess.run([command],
                   shell = True)
def ver():
#         Color        Output
    print(Fore.CYAN  + '\nCSHELL' +
          Fore.BLUE  + ' version: ' +
          Fore.GREEN + cshellVer)
    print(Fore.CYAN  + platform.system() +
                       ' ' +
          Fore.BLUE  + platform.release() +
            '\n')

def commands():
    print('\n' +
#         Color        Output          
          Fore.GREEN + "Available commands:\n")
    print(Fore.CYAN + "echo" +
          Fore.BLUE + " <text>")
    print(Fore.CYAN + "exit")
    print(Fore.CYAN + 'clear')
    print(Fore.CYAN + 'help')
    print(Fore.CYAN + 'commands')
    print(Fore.CYAN + "python")
    print(Fore.CYAN + "shutdown")
    print(Fore.CYAN + "command " +
          Fore.BLUE + "<app/normal terminal command>")
    print(Fore.CYAN + "expr " +
          Fore.BLUE + "<expression>")
    print(Fore.CYAN + 'ver')
    print(Fore.CYAN + "web " +
          
          
          Fore.BLUE + "<desired website>\n")

def credits():
    print(Fore.CYAN + "Meme Supplier" +
          Fore.BLUE + ": owner, programmer, maintainer\n" +
          Fore.GREEN + "2025 Meme Supplier")

def help():
    #         Color        Output
    print(Fore.CYAN   + "Welcome to " +
          Fore.GREEN  + "CShell " +
          Fore.YELLOW + cshellVer)
    print(Fore.CYAN   + "Type " +
          Fore.BLUE   + "\"commands\"" +
          Fore.CYAN   + " for some commands!\n")

if platform.system() == 'Linux':
    isLinux = True
else:
    isLinux = False

if not isLinux:
#         Color       Output
    print(Fore.CYAN + "This script is for " +
          Fore.BLUE + "Linux" +
          Fore.RED  + " only!" +
          Fore.CYAN + " Either install Linux for edit the code " +
          Fore.RED  + "(it may not work as expected or break if you edit the code).\n"  )

# Attempts to confirm Colorama's existence
try:
    coloramaInstalled = True 
    from colorama import Fore, init
    init(autoreset=True)

# If not installed, you will be prompted to install Colorama.
except:
    coloramaInstalled = False
    
    print(Fore.RED + "Colorama doesn't appear to be installed! Would you like to install it?\n(Y or N)\n")
    
    choice = input("\n")
    
    if choice == 'Y' or choice == 'y':
        # Opens the download page for Colorama
        webbrowser.open_new("https://pypi.org/project/colorama/")
    else:
        # Cancels the action, and exits CShell
        print("\nAborted.\nPlease install Colorama to continue.")

if isLinux : help()

while True and coloramaInstalled and isLinux:
                #  Color        Output
    answer = input(Fore.BLUE  + 'cshell' +
                   Fore.GREEN + '$~' +
                   Fore.WHITE + ': ')

#   Goes through and executes commands
    match answer:
#            Input        Response  
        case "clear"    : os.system(answer)
        case "help"     : print() , help()
        case "commands" : commands()
        case "exit"     : sys.exit()
        case "python"   : command('python3')
        case "shutdown" : command('shutdown now')
        case "credits"  : credits()
        case "ver"      : ver()
        case ""         : () # Does nothing
#       Default
        case _ :

#           Multi-syntax
            if    answer.startswith  ("echo ")    : command(answer)
            elif  answer.startswith  ("expr ")    : command(answer)
            elif  answer.startswith  ("command ") : command(answer.replace ("app ","",1))
            elif  answer.startswith  ("web ")     : webbrowser.open_new(answer.replace ("web ","",1))
#           If nothing checks out
            else: print(Fore.RED +
                       answer +
                       ': command or program not found')

# 2025 Meme Supplier
# memesupplierbusiness@gmail.com
# Maintained by Meme Supplier
