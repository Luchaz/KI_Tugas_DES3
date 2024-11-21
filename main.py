from rsa import generate_rsa_keys, encrypt_with_rsa, decrypt_with_rsa
from des import encrypt_with_des, decrypt_with_des
from Crypto.Random import get_random_bytes

def main():
    # Simulate Device 1 (Sender) and Device 2 (Receiver)
    
    # Generate RSA keys for both devices (this would be done once)
    private_key_device_1, public_key_device_1 = generate_rsa_keys()
    private_key_device_2, public_key_device_2 = generate_rsa_keys()
    
    # Device 1 wants to send a message to Device 2
    message = "Hello, Naufal ! Secure message exchange."

    # Generate a random DES key for encryption
    des_key = get_random_bytes(8)  # DES uses 8-byte keys
    
    # Device 1 encrypts the DES key with Device 2's public RSA key
    encrypted_des_key = encrypt_with_rsa(public_key_device_2, des_key)

    # Device 1 encrypts the message using the DES key
    encrypted_message = encrypt_with_des(des_key, message)
    
    # Simulate sending encrypted DES key and message to Device 2
    print(f"Encrypted DES key: {encrypted_des_key}")
    print(f"Encrypted message: {encrypted_message}")

    # Device 2 receives and decrypts the DES key using their private RSA key
    decrypted_des_key = decrypt_with_rsa(private_key_device_2, encrypted_des_key)

    # Device 2 decrypts the message using the DES key
    decrypted_message = decrypt_with_des(decrypted_des_key, encrypted_message)

    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
