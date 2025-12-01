#! /usr/bin/bash

source ./bin/activate
pip install -r requirements.txt
pyinstaller --clean -F -y -n "mark2epub" mark2epub.py