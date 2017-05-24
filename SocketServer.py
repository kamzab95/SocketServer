import socket
import sys
from thread import *

HOST = ''
PORT = 8889

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socked created'

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed ' + str(msg)
    sys.exit()

s.listen(10)
print 'socket is listening'

def send(conn, text):
    text += '[END]'
    conn.send(text)
    print text


def server_thread(conn):
    print 'Connected to server'
    data = 'Connected to server'
    #send(conn, data)
    print 'message sent'

    wait_for_data(conn)


def wait_for_data(conn):
    print 'wait'
    reply = ""
    while True:
        data = conn.recv(1024)
        reply = 'rep: ' + data

        if 'up' in data:
            print 'up'
        if 'down' in data:
            print 'down'
        if 'left' in data:
            print 'left'
        if 'right' in data:
            print 'right'

        if '[END]' in data:
            print reply
            break


    send(conn, reply)
    conn.close()
    print 'close'

while 1:
    print 'wait for connection'
    conn, addr = s.accept()
    print 'Connected ' + addr[0] + ':' + str(addr[1])
    start_new_thread(server_thread, (conn,))
