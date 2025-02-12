#!/bin/bash

GREEN="\e[32m"
RESET="\e[0m" # Reset color
CYAN="\e[36m"

echo -e "${GREEN}Upgrading CShell...${RESET}"

cd ~/

echo -e "${CYAN}Removing \"$HOME/CSHELL/\"...${RESET}"
sudo rm -rf ~/CSHELL/

echo -e "${CYAN}Cloning into \"https://github.com/Meme-Supplier/CSHELL.git\"...${RESET}"
git clone https://github.com/Meme-Supplier/CSHELL.git

cd CSHELL

echo -e "${CYAN}Allowing execution for \"installer.sh\"...${RESET}"
chmod +x installer.sh

echo -e "${CYAN}Running the installer...${RESET}"
./installer.sh

echo -e "${CYAN}Reloading shell configurations...${RESET}"
source ~/.bashrc

echo -e "${GREEN}CShell successfully updated!${RESET}"

cshell
