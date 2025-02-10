#!/bin/bash

# Define color variables
GREEN="\e[32m"
RESET="\e[0m" # Reset color

echo -e "${BLUE}Installing CShell...${RESET}"

if [ -d ~/cshell ]; then
    rm -rf ~/cshell/
fi

mkdir -p ~/cshell

# Copy CShell script files
cp cshell.py ~/cshell/cshell.py
cp uninstall.sh ~/cshell/uninstall.sh
cp upgrade.sh ~/cshell/upgrade.sh

chmod +x ~/cshell/cshell.py

# Create a symbolic link in /usr/local/bin
sudo ln -sf ~/cshell/cshell.py /usr/local/bin/cshell

# Reload shell configuration
source ~/.bashrc

echo -e "${GREEN}CShell has been installed successfully. You can run it by typing 'cshell'.${RESET}"
