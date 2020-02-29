from test2 import *

comando = diferenca[0]
#print(comando)
orientacao = int(input("1 - Horizontal | 2 - Vertical --> "))

if orientacao == 1:
    x,y = comando[0],comando[1]
    print(x)
    print(y)

    if x == -1:
        msg = "forward 20"

    if x == 0:
        pass

    if x == 1:
        msg = "back 20"


import threading 
import socket
import sys
import time
import platform  

host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break



#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

for x in range(1):

    try:

        msg = "command"

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break

    try:

        msg = "takeoff"

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break

    a = input("...")

    try:

        msg = "land"

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break
    
    input("...")
    sock.close()
    break