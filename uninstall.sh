#!/bin/bash

# Define color variables
GREEN="\e[32m"
BLUE="\e[34m"
CYAN="\e[36m"
RESET="\e[0m" # Reset color

sudo echo ""
echo -e "${GREEN}Uninstalling PYShell......\n${RESET}"

if [ -d ~/PYShell ]; then
    echo -e "${CYAN}Removing \"$HOME/PYShell/\"...\n${RESET}"
    sudo rm -rf ~/PYShell/
fi

# Remove the symbolic link
echo -e "${CYAN}Removing the symbolic link for \"$HOME/pyshell/pyshell.py\"...${RESET}"
sudo rm -f /usr/local/bin/pyshell

# Remove the PYShell directory and files
echo -e "${CYAN}Removing \"$HOME/pyshell/\"...${RESET}"
sudo rm -rf ~/pyshell

# Icon
echo -e "${CYAN}Removing \"/usr/share/applications/pyshell.png/\"...${RESET}"
sudo rm -f /usr/share/applications/pyshell.png

# Desktop icons
echo -e "${CYAN}Removing \"/usr/share/applications/pyshell.desktop\"...${RESET}"
sudo rm -f /usr/share/applications/pyshell.desktop

echo -e "${CYAN}\nReloading shell configurations...${RESET}"
source ~/.bashrc

echo -e "${GREEN}\nPYShell has been successfully uninstalled.${RESET}"

read
