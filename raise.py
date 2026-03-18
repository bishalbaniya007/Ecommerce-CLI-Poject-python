# raise:
# Purpose: to trigger an exception.
# Think of it like “shouting, ‘Something’s wrong!’” in your code.
# On its own, it does not handle the error — it just stops execution unless something catches it.

x = -1
if x < 0:
  raise ValueError("Only positive numbers are allowed")

# Here:
# ValueError is a built-in exception.
# "x cannot be negative" is an optional message describing the error.
# The program stops at the raise line unless you handle it with try…except

