import socket
import os
from _thread import *

class server(object):
    #declare
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
 
    #listen
    def start(self):
        self.socket.listen(5)
        while True:
            client, addr = self.socket.accept()
            #thread
            start_new_thread(self.run, (client, addr))

    #receive data
    def run(self,client,addr):
             
        print ("\nConnection from : ", addr)
        client.send(str.encode("You are connected to the Server.."))     
        data = client.recv(2048)
        #check data
        if not data:
           print("No message received")
        else:
            msg = data.decode()
            print ("Client message:", msg)
        print ("Client at ", addr , " disconnected...")
      

if __name__ == '__main__':
    
    print(' Server')
    print('*------*')
    print('Waiting...')

    try:
        connect = server('192.168.120.11', 2020)
        connect.start()
    except socket.error as e:
        print(str(e))
   
