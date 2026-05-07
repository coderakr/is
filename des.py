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


# It looks like your question got cut off (“Explain the working of des…”). I’ll assume you meant **DES (Data Encryption Standard)**—a classic symmetric-key encryption algorithm. Here’s a clear explanation of how it works:

# ---

# ## 🔐 What is DES?

# **DES (Data Encryption Standard)** is a symmetric-key encryption algorithm, meaning the same key is used for both encryption and decryption. It was widely used for securing data before newer standards replaced it.

# ---

# ## ⚙️ Basic Idea

# DES takes:

# * **64-bit plaintext (input data)**
# * **56-bit key (actual key length; 8 bits are used for parity)**

# …and transforms the plaintext into **64-bit ciphertext** through multiple rounds of processing.

# ---

# ## 🔄 Step-by-Step Working of DES

# ### 1. Initial Permutation (IP)

# * The 64-bit plaintext is rearranged (bits are shuffled) using a fixed permutation table.
# * This doesn’t add security by itself but prepares data for processing.

# ---

# ### 2. Splitting

# * The permuted data is divided into two halves:

#   * Left half (**L₀**) – 32 bits
#   * Right half (**R₀**) – 32 bits

# ---

# ### 3. 16 Rounds of Processing (Feistel Structure)

# DES uses a **Feistel Network** design.

# Each round (i = 1 to 16) does:

# * Lᵢ = Rᵢ₋₁
# * Rᵢ = Lᵢ₋₁ ⊕ f(Rᵢ₋₁, Kᵢ)

# Where:

# * **Kᵢ** = round-specific subkey
# * **f()** = a complex function involving substitution and permutation

# ---

# ### 4. Inside the f-function

# The function **f(R, K)** has several steps:

# #### a) Expansion

# * Expands 32-bit R into 48 bits.

# #### b) Key Mixing

# * XOR with the 48-bit round key.

# #### c) Substitution (S-boxes)

# * Data passes through 8 S-boxes (nonlinear substitution tables).
# * Reduces 48 bits back to 32 bits.

# #### d) Permutation

# * Rearranges bits again for diffusion.

# ---

# ### 5. Final Swap

# * After 16 rounds, the left and right halves are swapped.

# ---

# ### 6. Final Permutation (FP)

# * Reverse of the initial permutation.
# * Produces the final **ciphertext**.

# ---

# ## 🔑 Key Generation (Subkeys)

# * The original 56-bit key is processed to generate **16 different subkeys (K₁ to K₁₆)**.
# * Each round uses a different subkey.

# ---

# ## 🔓 Decryption

# * Same process as encryption, but subkeys are used **in reverse order**.

# ---

# ## ⚠️ Limitations of DES

# * The 56-bit key is too small → vulnerable to brute-force attacks.
# * Replaced by stronger algorithms like:

#   * **Advanced Encryption Standard (AES)**
#   * Triple DES (3DES)

# ---

# ## 🧠 In Short

# DES:

# * Uses **bit permutations + substitutions**
# * Runs **16 rounds of Feistel operations**
# * Produces secure-looking ciphertext—but is now outdated due to weak key size

# ---

# If you meant something else by “des” (like **DES in data structures, dentistry, or economics**), tell me and I’ll explain that instead.
