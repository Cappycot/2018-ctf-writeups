from Crypto.Cipher import AES
import binascii, sys
from struct import pack, unpack

KEY="9aF738g9AkI112{}{}"
IV="0000000000000000"

#ciphertext = "9e00000000000000000000000000436a808e200a54806b0e94fb9633db9d67f0"
#ciphertext = "e0e56739892838f809739bb5afec7b48625f40e185e7fe0995cc10a5a76994d2"
#ciphertext = "e00000000000000000000005afec7b48625f40e185e7fe0995cc10a5a76994d2"
plaintext = "rotected by AES!".encode("hex")
cipher2 = "808e200a54806b0e94fb9633db9d67f0"

things = []
#hexes = []
#for i in range(48, 58):
    #things.append(chr(i))
#for i in range(65, 91):
    #things.append(chr(i))
#for i in range(97, 123):
for i in range(32, 127):
    things.append(chr(i))

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
int2 = unpack("qq", binascii.unhexlify(plaintext))

for i in range(len(things)):
    for j in range(len(things)):
        newkey = KEY.format(things[i], things[j])
        decrypted = decrypt2(encrypted, newkey).encode("hex")
        int1 = unpack("qq", binascii.unhexlify(decrypted))
        cipher1 = pack("qq", int1[0] ^ int2[0], int1[1] ^ int2[1])
        # print decrypted
        # We originally printed all the possible ciphers but got only one that started with 9e and ended with 436a, but we also have to go back and grab the key too.
        if binascii.hexlify(cipher1) == "9e128e7bc9ab9cc9d8b13ec77389436a":
            print newkey
            print binascii.hexlify(cipher1)
        # print plaintext




