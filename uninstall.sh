#!/bin/bash
# Define color variables
GREEN="\e[32m"
BLUE="\e[34m"
CYAN="\e[36m"
RESET="\e[0m" # Reset color

sudo echo ""
echo -e "${GREEN}Uninstalling CSHELL......${RESET}"

if [ -d ~/CSHELL ]; then
    echo -e "${CYAN}Removing \"$HOME/CSHELL/\"...${RESET}"
    rm -rf ~/CSHELL/
fi

# Remove the symbolic link
echo -e "${CYAN}Removing the symbolic link for \"$HOME/cshell/cshell.py\"...${RESET}"
sudo rm -f /usr/local/bin/cshell

# Remove the CShell directory and files
echo -e "${CYAN}Removing \"$HOME/cshell/\"...${RESET}"
rm -rf ~/cshell

echo -e "${CYAN}Reloading shell configurations...${RESET}"
source ~/.bashrc

echo -e "${GREEN}CSHELL has been successfully uninstalled.${RESET}"
