#!/usr/bin/bash
# bash script to install requirments

# Install Node 14
sudo apt update
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
# Install semi-standard (https://github.com/standard/semistandard)
sudo npm install semistandard --global