
def encrypt(plaintext, shift):
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            ciphertext += alphabet[(alphabet.index(plaintext[i]) + shift) % 26]
        else:
            ciphertext += plaintext[i]
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            plaintext += alphabet[(alphabet.index(ciphertext[i]) - shift) % 26]
        else:
            plaintext += ciphertext[i]
    return plaintext

alphabet = 'abcdefghijklmnopqrstuvwxyz'
choice = ''

while choice not in ['1','2']:
    choice = input('Do you want to encrypt (1) or decrypt (2)? ')
    if choice == '1':
        key = int(input('Please choose a key '))
        plaintext = input('Please type a message to encrypt ').lower()
        print(encrypt(plaintext, key))
    if choice == '2':
        key = int(input('Please choose a key '))
        ciphertext = input('Please type a message to decrypt ').lower()
        print(decrypt(ciphertext, key))
