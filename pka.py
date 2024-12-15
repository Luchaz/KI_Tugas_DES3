from rsa import rsa_keygen, rsa_encrypt, rsa_decrypt

# Generate RSA keys for PKA
PKA_pub, PKA_priv = rsa_keygen()

def distribute_public_key(user_pub_key):
    # Encrypt user public key using PKA private key
    encrypted_key = rsa_encrypt(str(user_pub_key), PKA_priv)
    return encrypted_key

def receive_public_key(encrypted_key):
    # Decrypt encrypted key using PKA public key
    decrypted_key = rsa_decrypt(encrypted_key, PKA_pub)
    return eval(decrypted_key)  # Convert string back to tuple
