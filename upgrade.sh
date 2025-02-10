#!/bin/bash

GREEN="\e[32m"
RESET="\e[0m" # Reset color

echo -e "${GREEN}Upgrading CShell...${RESET}"

cd ~/

sudo rm -rf ~/CSHELL/

git clone https://github.com/Meme-Supplier/CSHELL.git
cd CSHELL
chmod +x installer.sh
./installer.sh

source ~/.bashrc

echo -e "${GREEN}CShell successfully updated!${RESET}"

cshell
