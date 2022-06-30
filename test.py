import pyaes
from cryptography.fernet import Fernet
import rsa

def keygen():
    #p - prime number g - privitive modulus of p (less than g)
    p = 13
    g = 6

    user1_privatekey = 5
    user2_privatekey = 4

    user1 = (g**user1_privatekey) % p
    user2 = (g**user2_privatekey) % p
    
    user1_exch = user2
    user2_exch = user1
    

    user1_generated = (user1_exch**user1_privatekey)%p
    user2_generated = (user2_exch**user2_privatekey)%p
    print(user1_generated)
    print(user2_generated)



    #string to byte string cnversion using a generated key
    text = "helloguys"
    key = Fernet.generate_key()
    print(key)
    fernet = Fernet(key)
    byte_string = fernet.encrypt(text.encode())
    print(byte_string)
    print("\n")




    privatekey = user1_generated
    publickey = 8

    #rsa encryption
    bytestring = str(byte_string)
    publickey, privatekey = rsa.newkeys(1000)
    encMessage = rsa.encrypt(bytestring.encode(),publickey)
    print(encMessage) 
    print("\n")

    #________________________________________________________


    #rsa decryption
    decMessage = rsa.decrypt(encMessage, privatekey).decode()
    print(decMessage)

    print("\n")


    #bytestring to string decrypt
    decbyte_string = fernet.decrypt(byte_string).decode()
    print(decbyte_string)

keygen()
