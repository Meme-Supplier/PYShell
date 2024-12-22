import os, sys, subprocess, platform
os.system('clear')

def command(command):
    subprocess.run([command], shell = True)

if platform.system() != 'Linux':
    print("This script is for Linux only! Either install Linux for edit the code (it may not work if you edit the code)!")

while True and platform.system() == 'Linux':
    answer = input('cshell$~: ')

    if answer.startswith("echo "):
        echo = answer.replace("echo ", "", 1)
        print(echo)
    elif answer.startswith("expr ") or answer == 'neofetch':
        command(answer)
    elif answer == "clear":
        os.system(answer)
    elif answer.startswith("help"):
        import pscripts.help
    elif answer == 'exit':
        sys.exit()
    elif answer == 'python':
        try:
            command('python3')
        except:
            print("Python not found. Would you like to install it?\n")
            x = input("")
            if x == 'Y' or x == 'y':
                command('sudo apt install python3')
            else:
                print("Operation canceled.")
    elif answer == "shutdown":
        command('shutdown now')
    elif answer.startswith("app "):
        app = answer.replace("app ", "", 1)
        command(app)
    elif answer == 'ver':
        print('\nCSHELL version: v0.2')
        print(platform.system(),platform.release(),'\n')
    else:
        print('Invalid command')
