# Assignment 02 – Transposition Cipher

def encrypt(message, key):
    cipher = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key

    return ''.join(cipher)


def decrypt(cipher, key):
    num_cols = key
    num_rows = len(cipher) // key + (1 if len(cipher) % key != 0 else 0)
    num_shaded = (num_cols * num_rows) - len(cipher)

    plain = [''] * num_rows
    col = 0
    row = 0

    for symbol in cipher:
        plain[row] += symbol
        row += 1

        if (row == num_rows) or (row == num_rows - 1 and col >= num_cols - num_shaded):
            row = 0
            col += 1

    return ''.join(plain)


# Input
message = input("Enter message: ")
key = int(input("Enter key (columns): "))

# Process
enc = encrypt(message, key)
dec = decrypt(enc, key)

# Output
print("Encrypted:", enc)
print("Decrypted:", dec)