#!/bin/bash

GREEN="\e[32m"
RESET="\e[0m" # Reset color
CYAN="\e[36m"

sudo echo ""
echo -e "${GREEN}Upgrading CSHELL...${RESET}"

cd ~/

echo -e "${CYAN}Removing \"$HOME/CSHELL/\"...${RESET}"
if [ -d ~/CSHELL ]; then
    echo -e "${CYAN}Removing \"$HOME/CSHELL/\"...${RESET}"
    rm -rf ~/CSHELL/
fi

echo -e "${CYAN}Cloning into \"https://github.com/Meme-Supplier/CSHELL.git\"...${RESET}"
git clone https://github.com/Meme-Supplier/CSHELL.git

cd CSHELL

echo -e "${CYAN}Allowing execution for \"installer.sh\"...${RESET}"
chmod +x installer.sh

echo -e "${CYAN}Running the installer...${RESET}"
./installer.sh

echo -e "${CYAN}Reloading shell configurations...${RESET}"
source ~/.bashrc

echo -e "${GREEN}CSHELL successfully updated!${RESET}"

cshell
