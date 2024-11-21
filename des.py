from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Encrypt message using DES
def encrypt_with_des(des_key, message):
    cipher = DES.new(des_key, DES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), DES.block_size))
    return cipher.iv + ct_bytes  # Include IV for decryption

# Decrypt message using DES
def decrypt_with_des(des_key, encrypted_message):
    iv = encrypted_message[:DES.block_size]
    ct = encrypted_message[DES.block_size:]
    cipher = DES.new(des_key, DES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ct), DES.block_size).decode()
    return decrypted_message
