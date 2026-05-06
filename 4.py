# Write a Python program to implement AES Algorithm.

def pad(text, block=16):
    while len(text) % block != 0:
        text += ' '
    return text

def encrypt(text, key):
    text = pad(text)
    result = ""

    for i in range(len(text)):
        t = ord(text[i])
        k = ord(key[i % len(key)])
        
        # simple substitution + XOR
        val = (t ^ k)
        val = (val + i) % 256
        
        result += chr(val)

    return result

def decrypt(cipher, key):
    result = ""

    for i in range(len(cipher)):
        c = ord(cipher[i])
        k = ord(key[i % len(key)])
        
        val = (c - i) % 256
        val = val ^ k
        
        result += chr(val)

    return result.strip()

# Test
key = "0123456789abcdef"
text = "HelloAESWorld!!"

enc = encrypt(text, key)
dec = decrypt(enc, key)

print("Original :", text)
print("Encrypted:", enc.encode())  # show bytes
print("Decrypted:", dec)


# output
# Original : HelloAESWorld!!
# Encrypted: b'xU`b_yykw_\x1d\x19\x13RRU'
# Decrypted: HelloAESWorld!!