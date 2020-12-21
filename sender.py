import socket

def sender(sock):
    while True:
        message = input(">>> ")
        if message == 'stop':
            sock.send(b'stop')
            break
        else:
            sock.send(message.encode())