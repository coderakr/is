from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES key must be exactly 8 bytes
key = b'8bytekey'

# Create DES cipher
cipher = DES.new(key, DES.MODE_ECB)

# Plain text
text = b'HelloDES'

# Encrypt
encrypted = cipher.encrypt(pad(text, 8))

# Decrypt
decrypted = unpad(cipher.decrypt(encrypted), 8)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)