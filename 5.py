# Write a Python program to implement RSA algorithm.
import math

# Function to check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to find gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find modular inverse using Extended Euclidean Algorithm
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Step 1: Choose two prime numbers
p = 61
q = 53

# Step 2: Compute n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = 17
if gcd(e, phi) != 1:
    raise ValueError("e is not coprime with phi")

# Step 4: Compute d (private key)
d = mod_inverse(e, phi)

# Keys
print("Public Key  : (e =", e, ", n =", n, ")")
print("Private Key : (d =", d, ", n =", n, ")")

# Step 5: Encryption
message = 65   # ASCII of 'A'
encrypted = pow(message, e, n)

# Step 6: Decryption
decrypted = pow(encrypted, d, n)

# Output
print("\nOriginal  :", message, "->", chr(message))
print("Encrypted :", encrypted)
print("Decrypted :", decrypted, "->", chr(decrypted))


# output
# Public Key  : (e = 17 , n = 3233 )
# Private Key : (d = 2753 , n = 3233 )

# Original  : 65 -> A
# Encrypted : 2790
# Decrypted : 65 -> A