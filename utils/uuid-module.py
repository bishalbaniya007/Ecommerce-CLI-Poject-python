# The Python uuid module is a built-in tool used to generate Universally Unique Identifiers (UUIDs), which are 128-bit values designed to uniquely identify information in computer systems without a central coordinator. 

# UUID Versions in Python
# uuid1() (Time-based): 
  # Combines the host's MAC address and the current timestamp.
  # Best for: Chronological sorting.

  # Caution: 
  # May leak privacy by revealing your machine's hardware ID.

# uuid3() & uuid5() (Name-based): 
  # Generates a deterministic ID from a namespace (like a URL) and a name.
  # Best for: Reproducible IDs where the same input must always yield the same output.

  # Difference: 
  # uuid3 uses MD5 hashing, while uuid5 uses the more secure SHA-1.

# uuid4() (Random): 
  # Uses cryptographically strong pseudo-random numbers.
  # Best for: General-purpose unique IDs, database keys, and session identifiers.

# uuid7() (New in Python 3.14): 
  # A time-ordered UUID that provides a sortable 48-bit timestamp followed by random bits.

import uuid

# Generate a random UUID
my_id = uuid.uuid4()
print(my_id)        # e.g., 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
print(my_id.hex)    # 'f47ac10b58cc4372a5670e02b2c3d479' (no hyphens)
