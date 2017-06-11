def generate_keys():
    prime1 = int(input('Please choose a prime number '))
    prime2 = int(input('Please choose another prime number '))
    prime3 = int(input('Please choose another prime number '))
    primes = sorted([prime1, prime2, prime3])
    public_key = (primes[1] * primes[2], primes[0])

    phi1 = primes[1] - 1
    phi2 = primes[2] - 1
    for d in range(1, phi1 * phi2):
        if d * primes[0] % (phi1 * phi2) == 1:
            private_key = (primes[1] * primes[2], d)

    return(public_key, private_key)

def encrypt(plaintext, public_key):
    encrypted = (plaintext ** public_key[1]) % public_key[0]
    return encrypted

def decrypt(ciphertext, private_key):
    decrypted = ciphertext ** private_key[1] % private_key[0]
    return decrypted

def encrypt_text(plaintext, public_key):
    ciphertext = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890!"£$%^&*()_-+=[]{}:;@~#,<.>/?`¬\|'
    for char in plaintext.lower():
        if char in alphabet:
            val = alphabet.index(char) + 1
            cipher = encrypt(val, public_key)
            ciphertext.append(cipher)
        else:
            pass
    return ciphertext

def decrypt_text(ciphertext, private_key):
    plaintext = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890!"£$%^&*()_-+=[]{}:;@~#,<.>/?`¬\|'
    for val in ciphertext:
        decipher = decrypt(val, private_key) - 1
        char = alphabet[decipher]
        plaintext += char
    return plaintext


