from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
public_key = key.publickey()

cipher = PKCS1_OAEP.new(public_key)
message = b'HelloRSA'
encrypted = cipher.encrypt(message)

cipher = PKCS1_OAEP.new(key)
decrypted = cipher.decrypt(encrypted)

# print(cipher)
print(decrypted)