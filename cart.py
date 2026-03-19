import product

class Cart:
  # if my_cart (items) stays at the class level, every cart object shares the same dictionary. 
  # So user A's items would show up in user B's cart! 

  def __init__(self, user_id):
    self.user_id = user_id
    self.items = {}   #  # each user's cart is separate
   
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
      raise ValueError("Quantity can not be negative")


  def remove_item(self):
    pass

  def update_quantity(self):
    pass

  def calculate_total(self):
    pass

  def checkout(self):
    pass

p1 = product.Product("asdf", "pen", 20, 100)
cart = Cart("101")
print(cart.user_id)

cart.add_item(p1, 20)
print(cart.items)