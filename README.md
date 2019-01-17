# ChubbyBunny Framework

[![Version](https://img.shields.io/badge/ChubbyBunny-1.0.0-brightgreen.svg)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-Linux-orange.svg)]()

<img align="left" width="90" height="90"  src="https://image.flaticon.com/icons/svg/347/347479.svg">

ChubbyBunny is an easy tool used to generate a backdoor for remote access to a Windows machine. This tool a malware with custom coded payloads that can be then easily executed on a Windows machine. The malware that is created with this tool has a high ability to bypass most present-day antivirus detection. This project is still a __work in progress__ so there is a high chance of multiple bugs.

## How to Install :arrow_down::
#### Please use Linux for server and Windows x86 for client
1. ```git clone https://github.com/0BL1V10N-V01D/ChubbyBunny.git```
2. ```cd ChubbyBunny```
3. ```pip install -r requirements.txt```

## How to Use :question::
1. ```cd ChubbyBunny```
3. ```python3 chubbybunny.py```
2. Type ```1``` to generate file. Go through steps
3. Launch listner by running the command ```2```. Follow the steps.
4. Send payload to victim.

## Linux operating systems I recommend :cd::
- Kali Linux 2
- Cyborg
- Parrot
- BackTrack
- Backbox
- Devuan

## Upcoming Features :white_check_mark::
#### Short-term goals:
* Create a way list all connected USB devices
* Create a way to take a picture through the camera and send it
* Stream a live feed of the camera to an http server
* Lock keyboard
* Lock mouse
* Make a keylogger or mouselogger
* Remove directories
* Delete the functionality of <kbd>^C
#### Long-term goals:
* Change desktop background
* A way to find password hash
* Create a way to maintain connection

## Bugs :beetle::
* Inproper socket exit on both machines
* The actual shell part of the code doest't work (it's very glitchy)
* __Submit any issues that you find__
