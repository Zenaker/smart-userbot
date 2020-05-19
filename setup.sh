#!/bin/bash

# checks for root privileges
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# install python3
sudo apt install python3

# install pip
sudo apt install python3-pip

# install pyrogram
pip3 install pyrogram

# install TgCrypto
pip3 install TgCrypto

# all done!

echo "all requirements installed!"
