# CSHELL - Custom Bash

Features:

- **Scriptable:** CShell allows you to create scripts!
- **Compatability:** CShell is compatible with (almost) ALL commands!
- **Performance:** CShell is fast, and reliable, so you will never encounter any performance issues.
- **And many more!**

## For **Linux** machines only.
### Supported distros:
- **Debian**-based (Ex: Linux Mint, Rasberry Pi OS)
- **Ubuntu**-based (Ex: Linux Mint, Ubunutu)
- **Fedora**-based (Ex: Fedora, Bazzite)
- **Arch**-based (Ex Arch, Manjaro)

**Ubuntu may work as well.**

### Tested on:
- Manjaro
- Linux Mint
- WSL (Ubuntu)
- WSL (Debian)
- Rasberry Pi OS
- Fedora

#
# How to install using commands:

## Here's everything in one line for your convenience:
`rm -rf ~/CSHELL/ && cd ~/ && git clone https://github.com/Meme-Supplier/CSHELL.git && cd CSHELL && chmod +x installer.sh && ./installer.sh && cd ~/`

### 1. Navigate to the home directory
`cd ~/`

### 2. Install Git if not installed

**Debian/Ubuntu distros**
`sudo apt install git`

**Fedora distros**
`sudo dnf install git`

**Arch distros**

### 3. Clone the repo

`rm -rf ~/CSHELL/` **If you get an error, ignore and continue.**

`git clone https://github.com/Meme-Supplier/CSHELL.git`

### 4. Navigate into the cloned repository directory
`cd CSHELL`

### 5. Ensure the installer.sh file has execute permissions
`chmod +x installer.sh`

### 6. Run the installer
`./installer.sh`

### 7. Install Colorama (If not already installed) [REQUIRED]

If you're using **Debian** or **Ubuntu**:

`sudo apt install python3-colorama`

Otherwise:

**Here is everything in one line for your convenience:**
`cd ~/ && python -m venv venv && source venv/bin/activate && pip install colorama`

`cd ~/`

`python3 -m venv venv`

`source venv/bin/activate`

`pip install colorama`

### After installing colorama, restart the instructions from the beginning

**If that doesn't work:**

**https://pypi.org/project/colorama/**

### 8. (OPTIONAL) navigate back to the home directory
`cd ~/`

### 9. Run CShell
`cshell`

**If you have problems with Colorama, try returning to step 7.**

#
# To uninstall:
**Open CShell, then type `uninstall`. That's it.**

#
Maintained by **Meme Supplier**

2025 Meme Supplier
