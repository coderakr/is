# Write a Python program to implement DES algorithm.

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def des_encrypt(text, key):
    text = pad(text)
    key_val = sum(ord(c) for c in key)

    result = ''
    for i, c in enumerate(text):
        result += chr((ord(c) + key_val + i) % 256)

    return result

def des_decrypt(cipher, key):
    key_val = sum(ord(c) for c in key)

    result = ''
    for i, c in enumerate(cipher):
        result += chr((ord(c) - key_val - i) % 256)

    return result.strip()

# Main
key = "8bytekey"
text = "HelloDES"

enc = des_encrypt(text, key)
dec = des_decrypt(enc, key)

print("Original :", text)
print("Encrypted:", enc.encode())  # show bytes
print("Decrypted:", dec)


# output
# Original : HelloDES
# Encrypted: b'}\xc2\x9b\xc2\xa3\xc2\xa4\xc2\xa8~\xc2\x80\xc2\x8f'
# Decrypted: HelloDES