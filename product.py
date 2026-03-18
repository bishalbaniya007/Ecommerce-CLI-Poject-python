# thsi is Product class.
class Product:
  def __init__(self, id, name, price, stock):
    self.id = id
    self.name = name
    self.price = price
    self.stock = stock

  # __str__() --> a special dunder function which provides a readable string 
  #               that describes the object’s state for end-users, rather than developers.

  # Return Type: 
  # The method must return a string. 
  # Returning any other type will result in a TypeError when called via str(). 

  def __str__(self):
    return f"Id: {self.id} | Name: {self.name} | Unit price: Rs. {self.price} | Stock: {self.stock}"

  # re-stocking existing product quantity
  def restock(self, quantity):
    if quantity > 0:
      self.stock += quantity

    else:
      raise ValueError("Restock quantity should be greater than 0")
      # raise keyword:
      # is used to manually trigger an exception, allowing you to signal that an error 
      # or unusual condition has occurred during program


  # reducing quantity of the existing product
  def reduce_stock(self, quantity):
    if quantity > 0 and quantity <= self.stock:
      self.stock -= quantity

    elif quantity <= 0:
      raise ValueError("Quantity should be greater than 0")
    
    else:
      raise ValueError("Not enough stock")

    
# product = Product("asdf", "pen", 10, 100)
# print(product)

# product.reduce_stock(1000)