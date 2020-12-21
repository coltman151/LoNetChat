import socket, errno
from socket import error as socket_error

def connect(ip_address, port, username):
    sock = socket.socket()
    sock.settimeout(5)
    
    try:
        sock.connect((ip_address, port))
    except socket_error as s_err:
        if s_err.errno == errno.ECONNREFUSED:
            print("Connection Refused")
        elif s_err.errno == errno.EHOSTUNREACH:
            print("No Route to Host")
    except socket.timeout:
        print("Connection Timed Out")
    
    print("Connected to {ip_address} on port {port}.")
    
    return sock