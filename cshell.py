# 2025 Meme Supplier
# memesupplier@business@gmail.com
# Maintained by Meme Supplier

import os, sys, subprocess, platform
import webbrowser
os.system('clear')

def command(command):
    subprocess.run([command],
                   shell = True)
def ver():
#         Color        Output
    print(Fore.CYAN  + '\nCSHELL'   +
          Fore.BLUE  + ' version: ' +
          Fore.GREEN + 'v0.3')
    print(Fore.CYAN  + platform.system(),
          Fore.BLUE  + platform.release(),
            '\n')

def credits():
#         Color        Output
    print(Fore.CYAN  + "Meme Supplier"+
          Fore.BLUE  + ": owner, programmer, maintainer\n"+
          Fore.GREEN + "2025 Meme Supplier")

if platform.system() == 'Linux':
    isLinux = True
else:
    isLinux = False

if not isLinux:
#         Color       Output
    print(Fore.CYAN + "This script is for "                                             +
          Fore.BLUE + "Linux"                                                           +
          Fore.RED  + " only!"                                                          +
          Fore.CYAN + " Either install Linux for edit the code "                        +
          Fore.RED  + "(it may not work as expected or break if you edit the code).\n" )
    
try: # Attempts to confirm Colorama's existence
    
    coloramaInstalled = True 
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    
except: # If not installed, you will be prompted to install Colorama.
    
    coloramaInstalled = False
    
    print(Fore.RED + "Colorama doesn't appear to be installed! Would you like to install it?\n(Y or N)\n")
    
    choice = input("\n")
    
    if choice == 'Y' or choice == 'y':
        webbrowser.open_new("https://pypi.org/project/colorama/") # Opens the download page for Colorama
    else:
        print("\nAborted.\nPlease install Colorama to continue.") # Cancels the action, and exits CShell
   
while True and coloramaInstalled and isLinux:
                #  Color        Output
    answer = input(Fore.BLUE  + 'cshell' +
                   Fore.GREEN + '$~'     +
                   Fore.WHITE + ': '     )

#   Goes through and executes commands
    match answer:
#              Input          Response  
        case   "clear"    : os.system(answer)
        case   "help"     : import pscripts.help
        case   "exit"     : sys.exit()
        case   "python"   : command('python3') # I added this to make accessing Python easier (you don't need the "3" at the end).
        case   "shutdown" : command('shutdown now')
        case   "credits"  : credits()
        case   "ver"      : ver()
        case     _        : # Default
            
#           Other else - ifs (can't be used with matching/switches)
            if    answer.startswith ("echo ") : command(answer)
            elif  answer.startswith ("expr ") : command(answer)
            elif  answer.startswith ("app ")  :
                app = answer.replace("app ","",1)
                command(app)
            else: print(Fore.RED                       +
                       answer                          +
                       ': command or program not found')
# 2025 Meme Supplier
# memesupplier@business@gmail.com
# Maintained by Meme Supplier
