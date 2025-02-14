#!/bin/bash
# Define color variables
GREEN="\e[32m"
BLUE="\e[34m"
CYAN="\e[36m"
RESET="\e[0m" # Reset color

sudo echo ""
echo -e "${GREEN}Uninstalling CSHELL......${RESET}"
sleep 1

# Remove the symbolic link
echo -e "${CYAN}Removing the symbolic link for \"$HOME/cshell/cshell.py\"...${RESET}"
sudo rm -f /usr/local/bin/cshell
sleep 0.5

# Remove the CShell directory and files
echo -e "${CYAN}Removing \"$HOME/cshell/\"...${RESET}"
rm -rf ~/cshell
sleep 0.5

echo -e "${CYAN}Reloading shell configurations...${RESET}"
source ~/.bashrc
sleep 1

# Confirm uninstallation
echo -e "${CYAN}Confirming uninstallation...${RESET}"
sleep 1

echo -e "${GREEN}CSHELL has been successfully uninstalled.${RESET}"
