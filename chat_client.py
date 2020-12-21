from listener import listener_daemon
from connect import connect
from sender import sender
from datetime import datetime
import socket, errno, threading

class User:
    port = 12345
    
    def __init__(self, username, ip_address, status):
        self.username = username
        self.ip_address = ip_address
        self.status = status
    
def clear():
    pass
    #put stuff to clear terminal here

def main():
    s = socket.socket()
    s.listen(5)
    entered_name = input("Enter your username:")
    entered_ip = input("Enter the IP you wish to connect to:")
    currentuser = User(entered_name, entered_ip, "Online")
    sock_data = connect(currentuser.ip_address, currentuser.port, currentuser.username)
    daemon = threading.Thread(target=listener_daemon, args=(sock_data,), daemon=True)
    daemon.start()
    sender(sock_data)

if __name__ == "__main__":
    main()