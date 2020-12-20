"""
Local Chat app to learn about development of networking by me
"""

from client import client
#from server import server

class chatuser:
    def __init__(self, uname, status):
        self.u = uname
        self.s = status

def main():
    #print("Enter a Username")
    user = chatuser("colton","")
    #user.u = input(">>> ")
    #print("Do you want to open a new room or join existing?")
    #userin = input(">>> ")
    #if userin == "J" or userin == 'j':
    #    client(user.u)
    #elif userin == 'N' or userin == 'n':
    #    server(user.u)
    client(user.u)    

if __name__ == "__main__":
    main()