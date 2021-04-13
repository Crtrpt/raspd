#!/usr/bin/env bash
sudo apt install python3
sudo apt install python3-pip
git clone git@github.com:Crtrpt/raspd.git
cd raspd
pip3 install -r requirements.txt
