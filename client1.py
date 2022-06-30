import time, socket, sys
from cryptography.fernet import Fernet
import rsa
import pyaes
import math

from Components.test import keygen

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = "172.20.13.17"
port = 5554
s.bind((ip, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
           
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())

while True:
    p = 13
    g = 6
    user1_privatekey = 5
    user1 = (g**user1_privatekey) % p
    bytes_val = user1.to_bytes(2, 'big')
    print(bytes_val)
    conn.send(bytes_val)

    message = conn.recv(1024)
    #message = message.decode()
    print(s_name, ":", message)
    int_val2 = int.from_bytes(message, "big")
    print(int_val2)
    

    user1_gene  = (int_val2**user1_privatekey)%p
    print("new key"+str(user1_gene))




    message = input(str("Me : "))
    key = Fernet.generate_key()
    fernet = Fernet(key)
    byte_string = fernet.encrypt(message.encode())
    print(byte_string)



    privatekey = user1_gene
    publickey = 8

    #rsa encryption
    ##global bytestring, encMessage

    bytestring = str(byte_string)
    publickey, privatekey = rsa.newkeys(1024)
    encMessage = rsa.encrypt(bytestring.encode(),publickey)
    print(encMessage) 

    conn.send(encMessage)

    decMessage = rsa.decrypt(encMessage, privatekey).decode()
    print(decMessage)

    

    decbyte_string = fernet.decrypt(byte_string).decode()
    print(decbyte_string)

    #conn.send(decbyte_string)


    


    
'''  message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        conn.send(user1)
        print("\n")
        break'''
    
    