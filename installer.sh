#!/bin/bash

# Define color variables
GREEN="\e[32m"
BLUE="\e[34m"
CYAN="\e[36m"
RESET="\e[0m" # Reset color

sudo echo ""
echo -e "${GREEN}Installing CSHELL...${RESET}"

sleep 1

if [ -d ~/cshell ]; then
    echo -e "${CYAN}Removing \"$HOME/cshell/\"...${RESET}"
    rm -rf ~/cshell/
    sleep 0.5
fi

echo -e "${CYAN}Creating \"$HOME/cshell/\"...${RESET}"
mkdir -p ~/cshell
sleep 0.5

# Copy CShell script files
echo -e "${CYAN}Copying files...${RESET}"
sleep 1

echo -e "${BLUE}Copying \"cshell.py\"...${RESET}"
cp cshell.py ~/cshell/cshell.py
sleep 0.5

echo -e "${BLUE}Copying \"uninstall.sh\"...${RESET}"
cp uninstall.sh ~/cshell/uninstall.sh
sleep 0.5

echo -e "${BLUE}Copying \"upgrade.sh\"...${RESET}"
cp upgrade.sh ~/cshell/upgrade.sh
sleep 0.5

echo -e "${CYAN}Successfully copied files.${RESET}"
sleep 1

echo -e "${CYAN}Enabling execution for \"$HOME/cshell/cshell.py\"...${RESET}"
chmod +x ~/cshell/cshell.py
sleep 0.5

# Create a symbolic link in /usr/local/bin
echo -e "${CYAN}Creating a symbolic link for \"$HOME/cshell/cshell.py\" in \"/usr/local/bin\"...${RESET}"
sudo ln -sf ~/cshell/cshell.py /usr/local/bin/cshell
sleep 0.5

# Reload shell configuration
echo -e "${CYAN}Reloading shell configurations...${RESET}"
source ~/.bashrc
sleep 1

echo -e "${GREEN}CSHELL has been installed successfully. You can run it by typing \"cshell\".${RESET}"
