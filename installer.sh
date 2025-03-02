#!/bin/bash

# Define color variables
GREEN="\e[32m"
BLUE="\e[34m"
CYAN="\e[36m"
RESET="\e[0m" # Reset color

sudo echo ""
echo -e "${GREEN}\nInstalling PYShell...${RESET}"

if [ -d ~/pyshell ]; then
    echo -e "${CYAN}\nRemoving \"$HOME/pyshell/\"...${RESET}"
    sudo rm -rf ~/pyshell/
fi

if [ -f /usr/share/applications/pyshell.desktop ]; then
    echo -e "${CYAN}\nRemoving \"/usr/share/applications/pyshell.desktop\"...${RESET}"
    sudo rm -f /usr/share/applications/pyshell.desktop
fi

if [ -f /usr/share/applications/pyshell.png ]; then
    echo -e "${CYAN}Removing \"/usr/share/applications/pyshell.png\"...${RESET}"
    sudo rm -f /usr/share/applications/pyshell.png
fi

echo -e "${CYAN}\nCreating \"$HOME/pyshell/\"...${RESET}"
mkdir -p ~/pyshell

# Copy PYShell script files
echo -e "${CYAN}\nCopying files...${RESET}"

# Python files

# PYShell
echo -e "${BLUE}Copying \"pyshell.py\"...${RESET}"
sudo cp pyshell.py ~/pyshell/pyshell.py

# Cmd list
echo -e "${BLUE}Copying \"cmdList.py\"...${RESET}"
sudo cp cmdList.py ~/pyshell/cmdList.py

# System info
echo -e "${BLUE}Copying \"sysInfo.py\"...${RESET}"
sudo cp sysInfo.py ~/pyshell/sysInfo.py

# Error handling
echo -e "${BLUE}Copying \"error.py\"...${RESET}"
sudo cp error.py ~/pyshell/error.py

# Logger
echo -e "${BLUE}Copying \"logger.py\"...${RESET}"
sudo cp logger.py ~/pyshell/logger.py

# Uninstall
echo -e "${BLUE}Copying \"uninstall.sh\"...${RESET}"
sudo cp uninstall.sh ~/pyshell/uninstall.sh

# Upgrade
echo -e "${BLUE}Copying \"upgrade.sh\"...${RESET}"
sudo cp upgrade.sh ~/pyshell/upgrade.sh

echo -e "${CYAN}Successfully copied files.\n${RESET}"

echo -e "${CYAN}Enabling execution for \"$HOME/pyshell/pyshell.py\"...${RESET}"
sudo chmod +x ~/pyshell/pyshell.py

# Create a symbolic link in /usr/local/bin
echo -e "${CYAN}Creating a symbolic link for \"$HOME/pyshell/pyshell.py\" in \"/usr/local/bin\"...${RESET}"
sudo ln -sf ~/pyshell/pyshell.py /usr/local/bin/pyshell

# Reload shell configuration
echo -e "${CYAN}\nReloading shell configurations...${RESET}"
source ~/.bashrc

# Asks if you want to create a desktop shortcut
echo -e "${BLUE}\nDo you want to create a desktop shortcut? (Recommended)\n(y/n): ${RESET}"
read -p "" answer

case "$answer" in
    [Yy])
        echo -e "${CYAN}\nInstalling icon image...${RESET}"
        sudo cp pyshell.png /usr/share/applications

        echo -e "${CYAN}Installing desktop icon file...${RESET}"
        sudo cp pyshell.desktop /usr/share/applications

        echo -e "${CYAN}Enabling execution...${RESET}"
        sudo chmod +x /usr/share/applications/pyshell.desktop
        ;;
esac

if [ -d ~/PYShell ]; then
    sudo rm -rf ~/PYShell/
fi

echo -e "${GREEN}\nPYShell has been installed successfully.\n${RESET}"
echo -e "${BLUE}Run it by typing \"pyshell\" in your terminal, or the desktop icon if you created one.${RESET}"

read
