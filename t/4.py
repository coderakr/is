# Write a Python program to implement AES Algorithm.
# pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# 16-byte key
key = b'1234567890abcdef'

# Input
plaintext = input("Enter plaintext: ").encode()

# Create AES cipher (ECB mode)
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt
ciphertext = cipher.encrypt(pad(plaintext, 16))
print("Encrypted (hex):", ciphertext.hex())

# Decrypt
decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), 16)

print("Decrypted:", decrypted.decode())