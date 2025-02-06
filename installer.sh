#!/bin/bash

echo "Installing CShell..."

# Create cshell directory
mkdir -p ~/cshell

# Copy CShell script files
cp cshell.py ~/cshell/cshell.py
cp uninstall.sh ~/cshell/uninstall.sh
chmod +x ~/cshell/cshell.py

# Create a symbolic link in /usr/local/bin
sudo ln -sf ~/cshell/cshell.py /usr/local/bin/cshell

# Reload shell configuration
source ~/.bashrc

echo "CShell has been installed successfully. You can run it by typing 'cshell'."
