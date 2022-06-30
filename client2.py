import time, socket, sys
from cryptography.fernet import Fernet
import rsa
import pyaes
import math

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 5554
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

while True:
    p = 13
    g = 6
    user2_privatekey = 4
    user2 = (g**user2_privatekey) % p
    bytes_val2 = user2.to_bytes(2, 'big')
    print(bytes_val2)
    s.send(bytes_val2)

    

    message = s.recv(1024)
    #message = message.decode()
    print(s_name, ":", message)
    int_val = int.from_bytes(message, "big")
    print(int_val)

    user2_gene  = (int_val**user2_privatekey)%p
    print("new key"+str(user2_gene))



    encMessage = s.recv(1024)
    print(s_name, ":", encMessage)
    #fernet = s.recv(1024)
    #print("fernet" +str(fernet)


    
    key = Fernet.generate_key()
    fernet = Fernet(key)


    privatekey = user2_gene
    decMessage = rsa.decrypt(encMessage, privatekey).decode('ascii')
    print(decMessage)
    


    

    #bytestring to string decrypt
    #decbyte_string = fernet.decrypt(decMessage).decode()
    #print(decbyte_string)


    '''key = s.recv(1024)
    print(key)
    fernet = s.recv(1024)
    print(fernet)'''

    """message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        s.send(message.encode())rq\
        print("\n")
        break"""
    