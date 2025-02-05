#!/bin/bash

echo "Uninstalling CShell..."

# Remove the symbolic link
sudo rm -f /usr/local/bin/cshell

# Remove the CShell directory and files
rm -rf ~/cshell

# Confirm uninstallation
if [[ ! -f /usr/local/bin/cshell && ! -d ~/cshell ]]; then
    echo "CShell has been successfully uninstalled."
    echo
else
    echo "Error: CShell could not be completely removed."
fi

exit
