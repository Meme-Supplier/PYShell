#!/bin/bash

# Define color variables
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
MAGENTA="\e[35m"
CYAN="\e[36m"
RESET="\e[0m" # Reset color

echo -e "${BLUE}Upgrading CShell...${RESET}"

sudo rm -r ~/CSHELL/
git clone https://github.com/Meme-Supplier/CSHELL.git
cd CSHELL
chmod +x installer.sh
./installer.sh

cshell
