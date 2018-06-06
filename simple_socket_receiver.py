import socket

s = socket.socket()
host = '192.168.4.1' #socket.gethostname()
print host
port = 8080
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

pitch=0
roll=0

while True:
    c, addr = s.accept()
    #print 'conn from',addr
    buf = c.recv(1024)
    #print 'buf', buf
    data = str(buf)
    #print data
    try:
        splt = data.encode("UTF-8").replace(",", ".").split(" ")
        # print splt
        pitch = float(splt[1])
        roll = float(splt[3])
    except Exception as e:
        print "error reading data"
	print e 
    print "pitch", pitch, "... roll", roll
    c.close()
