# hashlib.sha256() :
# is a constructor method in Python's hashlib module used to create a SHA-256 hash object. 
# SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that produces a unique, fixed-size 64-character hexadecimal string (256 bits) for any given input. 

import hashlib

# Example: SHA-256 hash
text = "Hello World"

# Initialize the hash object
hash_object = hashlib.sha256(text.encode())  # encode string to bytes

# Get the final hexadecimal hash
hex_dig = hash_object.hexdigest()  # get hexadecimal digest

print(hex_dig)