dict = {
  "a" : ("apple", 6),
  "b" : 3
}

print(dict["a"])      # returns the value of a i.e (tuple)
print(dict["a"][0])   # returns the value in position 0 of a tuple
print(dict["a"][1])   # returns the value in position 1 of a tuple

dict["a"][1] += 4   # since tuples are immutable this doesnt actually change the value
print(dict["a"][1]) 

# so the solution for updating the quantity is to use nested dictionary
items = {
  "product_id" : {
    "product" : "product-obj",
    "quantity" : "quantity"
  }
}