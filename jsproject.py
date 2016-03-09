#!/usr/local/bin/python3
import os
from subprocess import call

wd = os.getcwd() + "/"
call("mkdir -p " + wd + "{js,css,assets/img}", shell=True)

# Create .gitignore from gitignore.io
call("curl -L -s https://www.gitignore.io/api/vim,osx >> " +
     wd + ".gitignore", shell=True)
