import socket

def listener_daemon(sock):
    while True:
        message = sock.recv(1024).decode()
        if message == 'stop':
            break
        elif message != '':
            print(message)