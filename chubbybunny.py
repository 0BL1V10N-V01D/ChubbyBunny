import subprocess
import sys
import os
import readline
import time
import signal
import webbrowser

GREEN = '\33[32m'
YELLOW = '\33[33m'
RED = '\33[31m'
CYAN = '\033[1;36m'
VIOLET = '\33[35m'
END = '\33[0m'
BOLD = '\33[1m'
CURL = '\33[4m'

def signal_handler(sig, frame):
    subprocess.call(['clear'])
    print(RED + BOLD + '[-] (Ctrl + C) detected. Trying to exit...\n')
    time.sleep(1)
    print(GREEN + BOLD + 'Thank you for using Chubby Bunny. Come again.')
    sys.exit(0)

def printBanner():
    print('                    ')
    print('                    ')
    print(GREEN + BOLD + '             /|         ,  ')
    print('           ,///        /|  ')
    print('          // //     ,///   ')
    print('         // //     // //   ')
    print('        || ||    // //     ')
    print('        // //     || ||    ')
    print('        || ||   // //   ' + '  ___ _        _    _           ___                    ')
    print('        || ||  // //    ' + ' / __| |_ _  _| |__| |__ _  _  | _ )_  _ _ _  _ _ _  _ ')
    print('        || || || ||     ' + "| (__| ' \ || | '_ \ '_ \ || | | _ \ || | ' \| ' \ || |")
    print('         \\,\|,|\_//     ' + ' \___|_||_\_,_|_.__/_.__/\_, | |___/\_,_|_||_|_||_\_, |')
    print('          \\)\)\\|/       ' + '                         |__/                     |__/ ')
    print('         )-."" .-(         ')
    print('         //^\` `/^\\        ' + END + BOLD + '[' + GREEN + BOLD + '--' + END + BOLD + ']   Backdoor Creator For Remote Access    [' + GREEN + BOLD + '--' + END + BOLD + ']')
    print(GREEN + BOLD + '        //  |   |  \\       ' + END + BOLD + '[' + GREEN + BOLD + '--' + END + BOLD + ']' + VIOLET + BOLD + '        Created by:' + RED + ' 0BL1V10N V01D        ' + END + BOLD + '[' + GREEN + BOLD + '--' + END + BOLD + ']')
    print(GREEN + BOLD + '      ,/_| ' + END + BOLD + '0' + GREEN + BOLD + '| _ | ' + END + BOLD + '0' + GREEN + BOLD + '|_\,    ' + END + BOLD + '[' + GREEN + BOLD + '--' + END + BOLD + ']' + VIOLET + BOLD + '             Version:' + RED + ' 1.0.0' + END + BOLD + '              [' + GREEN + BOLD + '--' + END + BOLD + ']')
    print(GREEN + BOLD + '    /`    `"=.v.="`    `\\  ' + END + BOLD + '[' + GREEN + BOLD + '--' + END + BOLD + ']' + VIOLET + BOLD + '   Follow me on Github:' + RED + BOLD + ' @0BL1V10N-V01D' + END + BOLD + '   [' + GREEN + BOLD + '--' + END + BOLD + ']')
    print(GREEN + BOLD + '   /`    _."{_,_}"._    `\\ ' + END + BOLD + '[' + GREEN + BOLD + '--' + END + BOLD + ']' + VIOLET + BOLD + '      Follow me on Twitter:' + RED + ' @0V01d' + END + BOLD + '       [' + GREEN + BOLD + '--' + END + BOLD + ']')
    print(GREEN + BOLD + '  `/`  ` \  |||  / `  `\`  ' + END + BOLD + '[' + GREEN + BOLD + '--' + END + BOLD + ']                                         [' + GREEN + BOLD + '--' + END + BOLD + ']')
    print(GREEN + BOLD + '   `",_  \\=^~^=//  _,"`    ' + END + BOLD + '[' + GREEN + BOLD + '--' + END + BOLD + ']       SELECT AN OPTION TO BEGIN:        [' + GREEN + BOLD + '--' + END + BOLD + ']')
    print(GREEN + BOLD + '       "=,\"-=-"/,=         ' + END + BOLD + '[' + GREEN + BOLD + '--' + END + BOLD + '] ._____________________________________. [' + GREEN + BOLD + '--' + END + BOLD + ']')
    print(GREEN + BOLD + "           '---'           " + END + BOLD + '\_.-------------------------------------------._/' + END)
    print('                             ')
    print('                             ')

def startOptionMenu():
    printBanner()
    print(END + BOLD + '     [' + GREEN + BOLD + '1' + END + BOLD + ']' + GREEN + BOLD + '  Create Backdoor With Chubby Bunny')
    print(END + BOLD + '     [' + GREEN + BOLD + '2' + END + BOLD + ']' + GREEN + BOLD + '  Start Chubby Bunny Listener')
    print(END + BOLD + '     [' + GREEN + BOLD + '3' + END + BOLD + ']' + GREEN + BOLD + '  Help')
    print(END + BOLD + '     [' + GREEN + BOLD + '4' + END + BOLD + ']' + GREEN + BOLD + '  Credits')
    print(END + BOLD + '     [' + GREEN + BOLD + '5' + END + BOLD + ']' + GREEN + BOLD + '  Exit')
    print('             ')
    startCMD()

def startCMD():
    while True:
        cmd = input(GREEN + BOLD + ' ┌─[' + RED + 'ChubbyBunny' + GREEN + BOLD + ']--[' + RED + BOLD + '-' + GREEN + BOLD + ']-[' + YELLOW + 'menu' + GREEN + BOLD + ']:\n' + ' └─────► ')
        if cmd == '1':
            subprocess.call(['python3', 'generate.py'])
            enterToContinue = input(GREEN + BOLD + '\n\nPress [ENTER] to return to menu' + END)
            if enterToContinue == '':
                subprocess.call(['clear'])
                startOptionMenu()
            else:
                subprocess.call(['clear'])
                startOptionMenu()
        elif cmd == '2':
            subprocess.call(['python3', 'server.py'])
            enterToContinue = input(GREEN + BOLD + '\n\nPress [ENTER] to return to menu' + END)
            if enterToContinue == '':
                subprocess.call(['clear'])
                startOptionMenu()
            else:
                subprocess.call(['clear'])
                startOptionMenu()
        elif cmd == '3':
            try:
                url = 'https://github.com/0BL1V10N-V01D/ChubbyBunny/blob/master/README.md'
                webbrowser.open_new(url)
            except:
                print(RED + BOLD + "\nCouldn't open help page. Go to https://github.com/0BL1V10N-V01D/ChubbyBunny/blob/master/README.md instead\n")
                time.sleep(5)
            subprocess.call(['clear'])
            startOptionMenu()
            pass
        elif cmd == '4':
            subprocess.call(['clear'])
            print(RED + '==========================================================')
            print(END + BOLD + '                         Credits:                         ')
            print(RED + '==========================================================')
            print(END + BOLD + '\nSpecial Thanks To:')
            print(RED + BOLD + '\nOffensive Security')
            print(VIOLET + BOLD + '\nhttps://www.offensive-security.com/')
            print(YELLOW + BOLD + "\nhttps://www.kali.org/")
            print(RED + BOLD + "\nhttps://github.com")
            back = input(GREEN + BOLD + '\n\nPress [ENTER] to return to menu' + END)
            if enterToContinue == '':
                subprocess.call(['clear'])
                startOptionMenu()
            else:
                subprocess.call(['clear'])
                startOptionMenu()
        elif cmd == '5':
            subprocess.call(['clear'])
            print(RED + BOLD + '[-] Trying to exit...\n')
            time.sleep(1)
            print(GREEN + BOLD + 'Thank you for using Chubby Bunny. Come again.')
            sys.exit(0)
        else:
            subprocess.call(['clear'])
            startOptionMenu()
            pass

def main():
    signal.signal(signal.SIGINT, signal_handler)

    subprocess.call(['clear'])
    startOptionMenu()

if __name__ == '__main__':
    main()
