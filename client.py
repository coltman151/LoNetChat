import socket
import errno
from socket import error as socket_error

def client(username):
    s = socket.socket()
    host = input("Enter an IP Address:\n>>>")
    print(host)
    port = 12345
    s.settimeout(5)
    
    try:
        s.connect((host, port))
    except socket_error as serr:
        if serr.errno == errno.ECONNREFUSED:
            print("Connection Refused")
        elif serr.errno == errno.EHOSTUNREACH:
            print("No Route to Host")
    except socket.timeout:
        print("Connection Timed Out")
        
    s.send(b'username')
    print(s.recv(1024))

    while True:
        msg = input(">>> ")
        if msg == "stop":
            break
        else:
            s.send(b'msg')
    
    s.close()