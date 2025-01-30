from colorama import Fore, Back, Style, init


def help():
    print('\n'+Fore.GREEN+"Available commands:\n")

    print(
          Fore.CYAN+"echo "+
          Fore.BLUE+"<text>"+

          Fore.CYAN+"\nexit\n"+
          "clear\nhelp\npython\nshutdown\napp "
          +Fore.BLUE+"<app/command (such as git/neofetch)>"
          +Fore.CYAN+"\nexpr "+
          Fore.BLUE+"<expression>"+
          Fore.CYAN+
          "\nver\ncredits")
help()
