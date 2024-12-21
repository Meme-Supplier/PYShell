import os, sys, subprocess

os.system('clear')
unstable = False

while True:
    answer = input("cshell$~: ")

    if answer.startswith("echo "):  # Check if the input starts with "echo "
        echo = answer.replace("echo ", "", 1)  # Remove the first "echo " only
        print(echo)
    elif answer.startswith("beta "):
        beta = answer.replace("beta ", "", 1)
        if beta == "true":
            unstable = True
            print("Unstable commands enabled")
        else:
            unstable = False
            print("Unstable commands disabled")
    if unstable == True:    
        if answer.startswith("cd "):
            cd = answer.replace("cd ", "", 1)
            print(cd)
            subprocess.run(['cd ',cd], shell = True)
        elif answer == 'dir':
            subprocess.run(['dir'], shell = True)
        elif answer == 'list':
            subprocess.run(['ls'], shell = True)
        elif answer.startswith("run "): 
            run = answer.replace("run ", "", 1)
            subprocess.run(['chmod +x ',
                            run,
                            " ./runtest.run"], shell = True)
    elif answer == "clear":
        os.system(answer)
    elif answer == 'help':
        import pscripts.help
    elif answer == 'exit':
        sys.exit()
    elif answer == 'python':
        try:
            subprocess.run(['python3'], shell = True)
        except:
            print("Python not found. Would you like to install it?\n")
            x = input("")
            if x == 'Y' or x == 'y':
                subprocess.run(['sudo apt install python3'], shell = True)
            else:
                print("Operation canceled.")
    # Neofetch
    elif answer == "neofetch":
        subprocess.run(['neofetch'], shell = True)
    # Shutdown
    elif answer == "shutdown":
        subprocess.run(['shutdown now'], shell = True)
    elif answer.startswith("app "):
        app = answer.replace("app ", "", 1)
        subprocess.run([app], shell = True)