import socket
import struct
import binascii


s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

while True:

    pkt = s.recvfrom(2048) # RECV 2048 bytes
    #print repr(pkt)

    ipheader = pkt[0][14:34] # Remember, it's 20 bytes in length. We start at total offset 14 and go to 34.
    ip_hdr = struct.unpack("!8sB3s4s4s", ipheader)
    print ("---------- IP Header -----------")
    print ("TTL:", ip_hdr[1])
    print ("Source IP:", socket.inet_ntoa(ip_hdr[3]))
    print ("Dest IP:", socket.inet_ntoa(ip_hdr[4]))


    tcpheader = pkt[0][34:54] # TCP headers are also 20 bytes in length. We start at offset 34 and go to 54.
    tcp_hdr = struct.unpack("!HH9ss6s", tcpheader)
    print ("---------- TCP Header -----------")
    print ("Source Port:", tcp_hdr[0])
    print ("Destination Port:", tcp_hdr[1])
    print ("Flags:", binascii.hexlify(tcp_hdr[3]))
