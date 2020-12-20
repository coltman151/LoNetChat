import socket

s = socket.socket()
host = input("Enter an IP Address:\n>>>")
print(host)
port = 12345

try:
    s.settimeout(5)
    s.connect((host, port))
    print(s.recv(1024))
    s.close()
except socket.timeout:
    print("Connection Timed Out")