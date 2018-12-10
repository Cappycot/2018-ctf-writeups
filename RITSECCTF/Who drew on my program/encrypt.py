from Crypto.Cipher import AES
import binascii, sys

KEY="9aF738g9AKI112UU"
IV="0000000000000000"

def encrypt(message, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, IV)
    return aes.encrypt(message)

def decrypt(message, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, IV)
    return aes.decrypt(message)

encrypted = encrypt(sys.argv[1], KEY)
print "encrypted data: {}".format(binascii.hexlify(encrypted))
print "decrypted data: {}".format(decrypt(encrypted, KEY))
