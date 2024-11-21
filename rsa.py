from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Generate RSA Keys (Public/Private)
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Save keys to files
    with open("private.pem", "wb") as priv_file:
        priv_file.write(private_key)
    with open("public.pem", "wb") as pub_file:
        pub_file.write(public_key)
    
    return private_key, public_key

# Encrypt DES key using RSA public key
def encrypt_with_rsa(public_key, des_key):
    public_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_key = cipher.encrypt(des_key)
    return encrypted_key

# Decrypt DES key using RSA private key
def decrypt_with_rsa(private_key, encrypted_key):
    private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key)
    des_key = cipher.decrypt(encrypted_key)
    return des_key
