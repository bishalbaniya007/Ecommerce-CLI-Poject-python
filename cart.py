import product

class Cart:
  # if my_cart (items) stays at the class level, every cart object shares the same dictionary. 
  # So user A's items would show up in user B's cart! 

  def __init__(self, user_id):
    self.user_id = user_id
    self.items = {}   #  # each user's cart is separate

  # we receive product_obj and quantity as arguments 
  def add_item(self, product, quantity):
    # checking if the quantity is valid and product is in stock
    if quantity > 0 and quantity <= product.stock:

      # checking if the product is already in the cart or not:
      if product.id not in self.items:
        self.items.update({
          product.id : {
            "product" : product,
            "quantity" : quantity
          }})
        
      else:
        new_qty = self.items[product.id]["quantity"] + quantity
         
        # checking for the possibility that the total quantity might exceed total stock
        if new_qty > product.stock:
          raise ValueError("Not enough stock")
         
        self.items[product.id]["quantity"] = new_qty

    # if quantity is valid but not enough in stock
    elif quantity > 0 and quantity > product.stock:
      raise ValueError("Not enough stock")   

    # Invalid quantity  
    else:
      raise ValueError("Quantity must be greater than 0")

  # we receive product_obj and we pop the product to be removed using product.id
  def remove_item(self, product):
    if product.id not in self.items:
      raise ValueError("Product is not in the cart.")
    
    else:
      self.items.pop(product.id)

  # get product_obj and new_qty and replace the existing quantity in cart
  def update_quantity(self, product, new_qty):
    if product.id not in self.items:
      raise ValueError("Product is not in the cart.")

    elif new_qty <= 0:
      raise ValueError("Quantity must be greater than 0.")
    
    elif new_qty > 0 and new_qty <= product.stock:
      self.items[product.id]["quantity"] = new_qty
      
    else:
      raise ValueError("Not enough stock.")
    
  # loop through each items in cart and calculate the total   
  def calculate_total(self):
    total = 0
    for item in self.items.values():
      total += (item["product"].price * item["quantity"])

    return total

  # we return the cart 
  def view_cart(self):
    return self.items

  def checkout(self):
    pass

p1 = product.Product("asdf", "pen", 20, 100)
p2 = product.Product("1111", "book", 100, 100)
cart = Cart("101")

print(cart.items)       # for now cart is empty
cart.add_item(p1, 99)   # add p1 to the cart
print(cart.items)

cart.add_item(p1, 1)    # again adding p1 
print(cart.items)

# cart.remove_item(p1)    # pop p1
# print(cart.items)

print(cart.calculate_total())
print(cart.view_cart())
