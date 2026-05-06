# Assignment 01 – Bitwise AND and XOR on String

s = "Hello World"
print("Original String:", s)

# AND operation with 127
and_result = ''.join(chr(ord(c) & 127) for c in s)

# XOR operation with 127
xor_result = ''.join(chr(ord(c) ^ 127) for c in s)

print("After AND with 127:", and_result)
print("After XOR with 127:", xor_result)

# Verify reversibility of XOR
restored = ''.join(chr(ord(c) ^ 127) for c in xor_result)
print("XOR Restored:", restored)