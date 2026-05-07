from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)

# Public key
public_key = key.publickey()

# Create cipher using public key
cipher = PKCS1_OAEP.new(public_key)

# Message
message = b'HelloRSA'

# Encrypt
encrypted = cipher.encrypt(message)

# Create cipher using private key
cipher = PKCS1_OAEP.new(key)

# Decrypt
decrypted = cipher.decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)