from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES key must be 16, 24, or 32 bytes
key = b'0123456789abcdef'

# Create AES cipher
cipher = AES.new(key, AES.MODE_ECB)

# Plain text
text = b'HelloAESWorld!!'

# Encrypt
encrypted = cipher.encrypt(pad(text, 16))

# Decrypt
decrypted = unpad(cipher.decrypt(encrypted), 16)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)