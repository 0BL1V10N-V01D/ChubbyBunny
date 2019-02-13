<p align="center">
  <img src="https://i.imgur.com/uBFu6eS.png">
<p>
  
<h1 align="center">ChubbyBunny Payload Generator</h1>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.7.0-brightgreen.svg">
  </a>
  <a href="https://github.com/0BL1V10N-V01D/ChubbyBunny/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-lightgrey.svg">
  </a>
  <a href="https://github.com/0BL1V10N-V01D/ChubbyBunny">
    <img src="https://img.shields.io/badge/Release-1.1.0-red.svg">
  </a>
    <a href="https://opensource.org">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>

<p align="center">
  Chubby Bunny allow you to generate payloads and control someone's Windows computer remotley. ##BID UPDATE COMING SOON##
</p>

<p align="center">
  :books: This project was created only for learning purposes. We are not responsible for any damage that this causes.
</p>

## Description:

ChubbyBunny is an easy tool used to generate a backdoor for remote access to a Windows machine. This tool creates malware with custom coded payloads that can be then easily executed on a Windows machine. The malware that is created with this tool has a high ability to __bypass__ most present-day antivirus detection. This project is still a __work in progress__ so there is a high chance of multiple bugs.

## Features :key::
- [x] View cleint's system information
- [x] Take screenshots of victim's computer
- [x] Download text files
- [x] Open a URL on victim's PC
- [x] View total amount of memory
- [x] Crash victim's PC
- [x] Lock victim's computer screen
- [x] Shutdowm or restart victim's computer
- [x] Retrieve chrome passwords
- [ ] Upload text files
- [ ] Lock keyboard and mouse

## How to Install :arrow_down::
__Tested On:__ [![Kali)](https://www.google.com/s2/favicons?domain=https://www.kali.org/)](https://www.kali.org) **Kali Linux - Rolling Edition**
1. ```git clone https://github.com/0BL1V10N-V01D/ChubbyBunny.git```
2. ```cd ChubbyBunny```
3. ```pip install -r requirements.txt```
**This generator requires PyInstaller to work!**

## How to Use :question::
1. ```cd ChubbyBunny```
3. ```python chubbybunny.py```
2. Type ```1``` to generate file. Go through steps
3. Launch listener by running the command ```2```. Follow the steps.
4. Send generated payload to victim.
5. Type ```help``` for help

## Screenshots
<img align="left" src="https://i.postimg.cc/bJ3vtSTd/Screenshot-from-2019-01-16-19-36-22.png" width="430" heigt="430">
<img src="https://i.postimg.cc/kGJfTzKf/Screenshot-from-2019-01-16-19-41-31.png" width="397" heigt="397">

## Upcoming Features :white_check_mark::
#### Short-term goals:
* Create a way list all connected USB devices
* Lock keyboard
* Lock mouse
* Make a keylogger or mouselogger
* Upload txt files
* Record microphone
* Remove directories
#### Long-term goals:
* Change desktop background
* A way to find password hash
* Create a way to take a picture through the camera and send it
* Stream a live feed of the camera to an http server
* Create a way to maintain connection

## Contact :email::
**0BL1V10NV01D@protonmail.com**

## Bugs :beetle::
* Inproper socket exit on both machines
* __Submit any issues that you find__
