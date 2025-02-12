#!/bin/bash
# Define color variables
RED="\e[31m"
GREEN="\e[32m"
BLUE="\e[34m"
CYAN="\e[36m"
RESET="\e[0m" # Reset color

echo -e "${GREEN}Uninstalling CShell......${RESET}"

# Remove the symbolic link
echo -e "${CYAN}Removing the symbolic link for \"$HOME/cshell/cshell.py\"...${RESET}"
sudo rm -f /usr/local/bin/cshell

# Remove the CShell directory and files
echo -e "${CYAN}Removing \"$HOME/cshell/\"...${RESET}"
rm -rf ~/cshell

echo -e "${CYAN}Reloading shell configurations...${RESET}"
source ~/.bashrc

# Confirm uninstallation
echo -e "${CYAN}Confirming uninstallation...${RESET}"

if [[ ! -f /usr/local/bin/cshell && ! -d ~/cshell ]]; then
    echo -e "${GREEN}CShell has been successfully uninstalled.${RESET}"
else
    echo -e "${RED}Error: CShell could not be completely removed.${RESET}"
fi
