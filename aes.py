from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES key must be 16, 24, or 32 bytes
key = b'0123456789abcdef'

# Create AES cipher
cipher = AES.new(key, AES.MODE_ECB)

# Plain text
text = b'HelloAESWorld!!'

# Encrypt
encrypted = cipher.encrypt(pad(text, 16))

# Decrypt
decrypted = unpad(cipher.decrypt(encrypted), 16)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)







# AES (Advanced Encryption Standard) is a **symmetric-key block cipher** used to encrypt and decrypt data securely. It operates on **fixed-size blocks of 128 bits** and supports key sizes of **128, 192, or 256 bits**.

# Let’s break down how AES works in a clear step-by-step way.

# ---

# # 🔐 1. Basic Idea

# * AES takes **plaintext (input data)** and a **secret key**
# * It transforms the plaintext into **ciphertext (encrypted data)**
# * The same key is used to decrypt it back

# ---

# # 🧱 2. Data Representation

# AES works on a **4 × 4 matrix of bytes**, called the **state**

# Example (128-bit block):

# ```
# [ a0  a4  a8  a12 ]
# [ a1  a5  a9  a13 ]
# [ a2  a6  a10 a14 ]
# [ a3  a7  a11 a15 ]
# ```

# ---

# # 🔁 3. Number of Rounds

# AES performs multiple rounds of processing:

# | Key Size | Number of Rounds |
# | -------- | ---------------- |
# | 128-bit  | 10 rounds        |
# | 192-bit  | 12 rounds        |
# | 256-bit  | 14 rounds        |

# ---

# # ⚙️ 4. Main Steps in Each Round

# Each round (except the last) consists of 4 transformations:

# ### 1. SubBytes (Substitution)

# * Each byte is replaced using a lookup table called the **S-box**
# * Provides **non-linearity** (confusion)

# ---

# ### 2. ShiftRows

# * Rows of the matrix are shifted left:

#   * Row 0 → no shift
#   * Row 1 → shift 1
#   * Row 2 → shift 2
#   * Row 3 → shift 3

# ---

# ### 3. MixColumns

# * Each column is mixed using matrix multiplication
# * Provides **diffusion** (spreads influence of each byte)

# ---

# ### 4. AddRoundKey

# * The current state is XORed with a **round key**
# * Round keys are derived from the original key

# ---

# # 🔑 5. Key Expansion

# * The original key is expanded into multiple **round keys**
# * Each round uses a different key

# ---

# # ▶️ 6. Full AES Encryption Flow

# ### Step 1: Initial Round

# * AddRoundKey only

# ### Step 2: Main Rounds (9/11/13 times)

# * SubBytes
# * ShiftRows
# * MixColumns
# * AddRoundKey

# ### Step 3: Final Round

# * SubBytes
# * ShiftRows
# * AddRoundKey
#   (**No MixColumns in final round**)

# ---

# # 🔓 7. Decryption

# AES decryption performs the **inverse operations**:

# * InvSubBytes
# * InvShiftRows
# * InvMixColumns
# * AddRoundKey

# Applied in reverse order.

# ---

# # 🎯 Key Features of AES

# * Fast and efficient (hardware + software)
# * Strong security (widely used worldwide)
# * Resistant to known attacks (when properly implemented)

# ---

# # 🧠 In Simple Words

# AES works by:
# 👉 Repeatedly **substituting, shifting, mixing, and adding keys**
# 👉 Until the original data becomes unreadable ciphertext

# ---

# If you want, I can:

# * Show a **diagram of AES rounds**
# * Walk through a **numerical example**
# * Compare AES with DES or RSA
