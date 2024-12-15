from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_message = pad(message.encode(), DES.block_size)
    return cipher.encrypt(padded_message)

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_message = cipher.decrypt(ciphertext)
    return unpad(padded_message, DES.block_size).decode()
