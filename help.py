from colorama import Fore, Back, Style, init


def help():
    print('\n'+Fore.GREEN+"Available commands:\n")

    print(Fore.CYAN + "echo"+Fore.BLUE+" <text>")
    print(Fore.CYAN + "exit")
    print(Fore.CYAN + 'clear')
    print(Fore.CYAN + 'help')
    print(Fore.CYAN + "python")
    print(Fore.CYAN + "neofetch")
    print(Fore.CYAN + "shutdown")
    print(Fore.CYAN + "app "+Fore.BLUE+"<app>")
    print(Fore.CYAN + "expr "+Fore.BLUE+"<expression>")
    print(Fore.CYAN + 'ver\n')
