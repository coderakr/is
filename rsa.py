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



# RSA (named after Ron Rivest, Adi Shamir, and Leonard Adleman) is a widely used public-key cryptographic algorithm. It allows secure communication over an insecure channel by using two keys: a **public key** (shared with everyone) and a **private key** (kept secret).

# ---

# ## 1. Key Idea Behind RSA

# RSA relies on a property of number theory:

# * It is **easy to multiply large prime numbers**
# * But **very hard to factor their product back into primes**

# This is called the **factorization problem**, and RSA’s security depends on it.

# ---

# ## 2. Key Generation (Setup Phase)

# 1. Choose two large prime numbers
#    ( p ) and ( q )

# 2. Compute
#    ( n = p \times q )
#    (This is part of the public key)

# 3. Compute Euler’s totient
#    ( \phi(n) = (p-1)(q-1) )

# 4. Choose a public exponent ( e ) such that
#    ( 1 < e < \phi(n) ) and ( \gcd(e, \phi(n)) = 1 )

# 5. Compute the private key ( d ), where
#    ( d ) is the modular inverse of ( e ) modulo ( \phi(n) )

# ---

# ## 3. Keys

# * **Public Key**: ( (e, n) ) → shared openly
# * **Private Key**: ( (d, n) ) → kept secret

# ---

# ## 4. Encryption

# If someone wants to send a message ( M ):

# [
# C = M^e \mod n
# ]

# * ( C ) = ciphertext
# * Uses the **receiver’s public key**

# ---

# ## 5. Decryption

# The receiver recovers the message using:

# [
# M = C^d \mod n
# ]

# * Uses the **private key**

# ---

# ## 6. Why It Works

# The correctness comes from properties of modular arithmetic and Euler’s theorem:

# [
# (M^e)^d \equiv M \ (\text{mod } n)
# ]

# This works because ( ed \equiv 1 \mod \phi(n) ).

# ---

# ## 7. Simple Example (Small Numbers)

# * Let ( p = 3, q = 11 )
# * ( n = 33 ), ( \phi(n) = 20 )
# * Choose ( e = 3 )
# * Compute ( d = 7 )

# Public key: (3, 33)
# Private key: (7, 33)

# Message ( M = 4 ):

# * Encryption: ( C = 4^3 \mod 33 = 64 \mod 33 = 31 )
# * Decryption: ( M = 31^7 \mod 33 = 4 )

# ---

# ## 8. Applications of RSA

# * Secure web browsing (HTTPS)
# * Digital signatures
# * Email encryption
# * Key exchange in protocols like TLS

# ---

# ## 9. Limitations

# * Slow compared to symmetric encryption
# * Requires large keys (2048+ bits)
# * Vulnerable if primes are small or poorly chosen

# ---

# If you want, I can show a **step-by-step worked example with bigger numbers** or explain how RSA is used in real systems like TLS (Transport Layer Security).
