#!/bin/bash

GREEN="\e[32m"
RESET="\e[0m" # Reset color
CYAN="\e[36m"

sudo echo ""
echo -e "${GREEN}Upgrading PYShell...${RESET}"

cd ~/

echo -e "${CYAN}Removing \"$HOME/PYShell/\"...${RESET}"
if [ -d ~/PYShell ]; then
    echo -e "${CYAN}Removing \"$HOME/PYShell/\"...${RESET}"
    sudo rm -rf ~/PYShell/
fi

# Icon
if [ -d /usr/share/applications/pyshell.png/ ]; then
    echo -e "${CYAN}Removing \"/usr/share/applications/pyshell.png/\"...${RESET}"
    sudo rm -f /usr/share/applications/pyshell.png
fi

# Desktop icons
echo -e "${CYAN}Removing \"$HOME/Desktop/pyshell.desktop\"...${RESET}"
sudo rm -f ~/Desktop/pyshell.desktop

echo -e "${CYAN}Cloning into \"https://github.com/Meme-Supplier/PYShell.git\"...${RESET}"
git clone https://github.com/Meme-Supplier/PYShell.git

cd PYShell

echo -e "${CYAN}Allowing execution for \"installer.sh\"...${RESET}"
sudo chmod +x installer.sh

echo -e "${CYAN}Running the installer...${RESET}"
./installer.sh

echo -e "${CYAN}Reloading shell configurations...${RESET}"
source ~/.bashrc

echo -e "${GREEN}\nPYShell successfully updated!${RESET}"

read
