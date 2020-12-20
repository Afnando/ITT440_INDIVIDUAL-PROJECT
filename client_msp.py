import socket 
import os

class client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
    
    def run(self):
         response = self.socket.recv(1024).decode()
         print(response)
         data = input("Enter a message to server:")
         self.socket.send(data.encode('utf-8'))
         print("Client disconnected")
         self.socket.close()


if __name__ == "__main__":

    try:
        connect = client("192.168.120.11", 2020)
        connect.run()
    except socket.error as e:
        print(str(e))
