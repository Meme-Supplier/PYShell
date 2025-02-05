#!/bin/bash

echo "Would you like to install or uninstall CShell? (install/uninstall)"
read action

if [[ "$action" == "install" ]]; then
    echo "Installing CShell..."

    # Create cshell directory
    mkdir -p ~/cshell
    
    # Copy CShell script files
    cp cshell.py ~/cshell/cshell.py
    cp reload.sh ~/cshell/reload.sh
    cp uninstall.sh ~/cshell/uninstall.sh
    chmod +x ~/cshell/cshell.py

    # Create a symbolic link in /usr/local/bin
    sudo ln -sf ~/cshell/cshell.py /usr/local/bin/cshell

    # Reload shell configuration
    source ~/.bashrc

    echo "CShell has been installed successfully. You can run it by typing 'cshell'."

elif [[ "$action" == "uninstall" ]]; then
    echo "Uninstalling CShell..."
    
    # Remove the symbolic link
    sudo rm -f /usr/local/bin/cshell

    # Remove CShell files
    rm -f ~/cshell/cshell.py
    rm -f ~/cshell/reload.sh
    rm -f ~/cshell/uninstall.sh

    # Remove cshell directory if empty
    rmdir ~/cshell 2>/dev/null

    # Confirm uninstallation
    if [[ ! -f /usr/local/bin/cshell && ! -d ~/cshell ]]; then
        echo "CShell has been successfully uninstalled."
    else
        echo "Error: CShell could not be completely removed."
    fi

else
    echo "Invalid choice. Please type 'install' or 'uninstall'."
fi

read
