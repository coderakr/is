# pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'0123456789abcdef'
cipher = AES.new(key, AES.MODE_ECB)

text = b'HelloAESWorld!!'

encrypted = cipher.encrypt(pad(text, 16))
decrypted = unpad(cipher.decrypt(encrypted), 16)

print(encrypted)
print(decrypted)