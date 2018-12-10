from Crypto.Cipher import AES
import binascii, sys
from struct import pack, unpack

KEY="9aF738g9AkI112#g"

plaintext = "The message is p".encode("hex") # why my pp hard
cipher2 = "9e128e7bc9ab9cc9d8b13ec77389436a"

def encrypt(message, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, IV)
    return aes.encrypt(message)

def encrypt2(message, passphrase):
    aes = AES.new(passphrase, AES.MODE_ECB)
    return aes.encrypt(message)

def decrypt(message, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, IV)
    return aes.decrypt(message)

def decrypt2(message, passphrase):
    aes = AES.new(passphrase, AES.MODE_ECB)
    return aes.decrypt(message)

encrypted = binascii.unhexlify(cipher2)
decrypted = decrypt2(encrypted, KEY).encode("hex")
int1 = unpack("qq", binascii.unhexlify(decrypted))
int2 = unpack("qq", binascii.unhexlify(plaintext))
iv = pack("qq", int1[0] ^ int2[0], int1[1] ^ int2[1])
print str(iv)

