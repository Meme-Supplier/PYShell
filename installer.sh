#!/bin/bash

# Define color variables
GREEN="\e[32m"
BLUE="\e[34m"
CYAN="\e[36m"
RESET="\e[0m" # Reset color

sudo echo ""
echo -e "${GREEN}Installing CSHELL...${RESET}"

if [ -d ~/cshell ]; then
    echo -e "${CYAN}Removing \"$HOME/cshell/\"...${RESET}"
    rm -rf ~/cshell/
fi

echo -e "${CYAN}Creating \"$HOME/cshell/\"...${RESET}"
mkdir -p ~/cshell

# Copy CShell script files
echo -e "${CYAN}Copying files...${RESET}"

# Python files

# Cshell
echo -e "${BLUE}Copying \"cshell.py\"...${RESET}"
cp cshell.py ~/cshell/cshell.py

# Cmd list
echo -e "${BLUE}Copying \"cmdList.py\"...${RESET}"
cp cmdList.py ~/cshell/cmdList.py

# System info
echo -e "${BLUE}Copying \"sysInfo.py\"...${RESET}"
cp sysInfo.py ~/cshell/sysInfo.py

# Error handling
echo -e "${BLUE}Copying \"error.py\"...${RESET}"
cp error.py ~/cshell/error.py

# Logger
echo -e "${BLUE}Copying \"logger.py\"...${RESET}"
cp logger.py ~/cshell/logger.py

# Uninstall
echo -e "${BLUE}Copying \"uninstall.sh\"...${RESET}"
cp uninstall.sh ~/cshell/uninstall.sh

# Upgrade
echo -e "${BLUE}Copying \"upgrade.sh\"...${RESET}"
cp upgrade.sh ~/cshell/upgrade.sh

echo -e "${CYAN}Successfully copied files.${RESET}"

echo -e "${CYAN}Enabling execution for \"$HOME/cshell/cshell.py\"...${RESET}"
chmod +x ~/cshell/cshell.py

# Create a symbolic link in /usr/local/bin
echo -e "${CYAN}Creating a symbolic link for \"$HOME/cshell/cshell.py\" in \"/usr/local/bin\"...${RESET}"
sudo ln -sf ~/cshell/cshell.py /usr/local/bin/cshell

# Reload shell configuration
echo -e "${CYAN}Reloading shell configurations...${RESET}"
source ~/.bashrc

echo -e "${GREEN}CSHELL has been installed successfully. You can run it by typing \"cshell\".${RESET}"
