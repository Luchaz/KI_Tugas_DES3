def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_primes():
    # Hardcoded small primes for simplicity
    return [3, 5, 7, 11, 13]

def rsa_keygen():
    primes = generate_primes()
    p = primes[0]
    q = primes[1]
    n = p * q
    totient = (p - 1) * (q - 1)

    e = 3  # Start with a small odd number
    while gcd(e, totient) != 1:
        e += 2  # Increment by 2 to ensure odd numbers only

    d = pow(e, -1, totient)  # Compute modular inverse
    return (e, n), (d, n)  # Return public and private keys

def rsa_encrypt(message, key):
    e, n = key
    return [pow(ord(char), e, n) for char in message]

def rsa_decrypt(ciphertext, key):
    d, n = key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])
