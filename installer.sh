#!/bin/bash

# Define color variables
GREEN="\e[32m"
BLUE="\e[34m"
CYAN="\e[36m"
RESET="\e[0m" # Reset color

sudo echo ""
echo -e "${GREEN}Installing PYShell...${RESET}"

if [ -d ~/pyshell ]; then
    echo -e "${CYAN}Removing \"$HOME/pyshell/\"...${RESET}"
    rm -rf ~/pyshell/
fi

if [ -d ~/Desktop/pyshell.desktop ]; then
    echo -e "${CYAN}Removing \"$HOME/Desktop/pyshell.desktop/\"...${RESET}"
    rm -f ~/Desktop/pyshell.desktop/
fi

if [ -d /usr/share/applications/pyshell.png ]; then
    echo -e "${CYAN}Removing \"/usr/share/applications/icon.png/\"...${RESET}"
    sudo rm -f /usr/share/applications/pyshell.png/
fi

echo -e "${CYAN}Creating \"$HOME/pyshell/\"...${RESET}"
mkdir -p ~/pyshell

# Copy PYShell script files
echo -e "${CYAN}Copying files...${RESET}"

# Python files

# PYShell
echo -e "${BLUE}Copying \"pyshell.py\"...${RESET}"
cp pyshell.py ~/pyshell/pyshell.py

# Cmd list
echo -e "${BLUE}Copying \"cmdList.py\"...${RESET}"
cp cmdList.py ~/pyshell/cmdList.py

# System info
echo -e "${BLUE}Copying \"sysInfo.py\"...${RESET}"
cp sysInfo.py ~/pyshell/sysInfo.py

# Error handling
echo -e "${BLUE}Copying \"error.py\"...${RESET}"
cp error.py ~/pyshell/error.py

# Logger
echo -e "${BLUE}Copying \"logger.py\"...${RESET}"
cp logger.py ~/pyshell/logger.py

# Uninstall
echo -e "${BLUE}Copying \"uninstall.sh\"...${RESET}"
cp uninstall.sh ~/pyshell/uninstall.sh

# Upgrade
echo -e "${BLUE}Copying \"upgrade.sh\"...${RESET}"
cp upgrade.sh ~/pyshell/upgrade.sh

echo -e "${CYAN}Successfully copied files.${RESET}"

echo -e "${CYAN}Enabling execution for \"$HOME/pyshell/pyshell.py\"...${RESET}"
chmod +x ~/pyshell/pyshell.py

# Create a symbolic link in /usr/local/bin
echo -e "${CYAN}Creating a symbolic link for \"$HOME/pyshell/pyshell.py\" in \"/usr/local/bin\"...${RESET}"
sudo ln -sf ~/pyshell/pyshell.py /usr/local/bin/pyshell

# Reload shell configuration
echo -e "${CYAN}Reloading shell configurations...${RESET}"
source ~/.bashrc

# Asks if you want to create a desktop shortcut
echo -e "${BLUE}\nDo you want to create a desktop shortcut? (y/n): ${RESET}"
read -p "" answer

case "$answer" in
    [Yy])
        echo -e "${CYAN}Installing icon image...${RESET}"
        sudo cp pyshell.png /usr/share/applications

        echo -e "${CYAN}Installing desktop icon file...${RESET}"
        cp pyshell.desktop ~/Desktop

        echo -e "${CYAN}Enabling execution...${RESET}"
        chmod +x ~/Desktop/pyshell.desktop
        ;;
esac

echo -e "${GREEN}PYShell has been installed successfully. You can run it by typing \"pyshell\".${RESET}"
