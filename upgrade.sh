#!/bin/bash


GREEN="\e[32m"
RESET="\e[0m" # Reset color

echo -e "${GREEN}Upgrading CShell...${RESET}"

sudo rm -r ~/CSHELL/

git clone https://github.com/Meme-Supplier/CSHELL.git
cd CSHELL
chmod +x installer.sh
./installer.sh

source ~/.bashrc

rm -r ~/CSHELL/

echo -e "${GREEN}CShell successfully updated!${RESET}"

cshell
