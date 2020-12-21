import socket, sys

def server(username):
    s = socket.socket()
    port = 12345
    s.bind(('', port))

    s.listen(5)
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(b'thank you for connectiong')
    
    # while True:
    #     msg = c.recv(1024).decode()
    #     print(msg)
    #     if msg == "stop":
    #         sys.exit()
        
server("test")