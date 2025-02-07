#!/bin/bash
# Define color variables
RED="\e[31m"
GREEN="\e[32m"
BLUE="\e[34m"
RESET="\e[0m" # Reset color

echo -e "${BLUE}Uninstalling CShell......${RESET}"

# Remove the symbolic link
sudo rm -f /usr/local/bin/cshell
# Remove the CShell directory and files
rm -rf ~/cshell

source ~/.bashrc

# Confirm uninstallation
if [[ ! -f /usr/local/bin/cshell && ! -d ~/cshell ]]; then
    echo -e "${GREEN}CShell has been successfully uninstalled.${RESET}"
else
    echo -e "${RED}Error: CShell could not be completely removed.${RESET}"
fi
exit
