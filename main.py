from rsa import rsa_keygen, rsa_encrypt, rsa_decrypt
from pka import distribute_public_key, receive_public_key
from des import des_encrypt, des_decrypt
import os

# Generate RSA keys for two users
user1_pub, user1_priv = rsa_keygen()
user2_pub, user2_priv = rsa_keygen()

# PKA distributes public keys
encrypted_user1_pub = distribute_public_key(user1_pub)
encrypted_user2_pub = distribute_public_key(user2_pub)

# Users receive public keys from PKA
user1_received_pub = receive_public_key(encrypted_user2_pub)
user2_received_pub = receive_public_key(encrypted_user1_pub)

# Generate random DES key
des_key = os.urandom(8)  # DES key must be 8 bytes long

# Encrypt DES key twice (Sender Priv + Receiver Pub)
encrypted_des_key = rsa_encrypt(str(des_key), user1_priv)
final_encrypted_key = rsa_encrypt(str(encrypted_des_key), user2_received_pub)

# Encrypt message with DES
message = "Hello, secure world!"
encrypted_message = des_encrypt(message, des_key)

# Decrypt DES key (Receiver Priv + Sender Pub)
decrypted_des_key = rsa_decrypt(final_encrypted_key, user2_priv)
des_key_received = eval(rsa_decrypt(eval(decrypted_des_key), user1_received_pub))

# Decrypt message with DES
decrypted_message = des_decrypt(encrypted_message, des_key_received)

# Display Results
print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
