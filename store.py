import product
import cart
import user
import order

class Store:
  # we create store name and three empty dictionaries for product, user, and order
  def __init__(self, name):
    self.name = name
    self.products = {}
    self.users = {}
    self.orders = {}

  #  the store receives product details and creates a Product object and adds it to self.products.
  # Arguments — the store should receive the raw details and create the Product itself.  
  #           - So arguments should be product_id, name, price, stock and inside the method you create Product(product_id, name, price, stock).
  
  def add_product(self, id, name, price, stock):
    my_product = product.Product(id, name, price, stock)

    # Duplicate check — what if a product with the same id already exists? 
    if id not in self.products:
      self.products.update({id : my_product})
    else:
      raise ValueError("Product already exists!")
    

  # we remove the product from the products dictionary based on product_id
  def remove_product(self, id):
    if id not in self.products:
      raise ValueError("Product does not exist!")
    else:
      self.products.pop(id)

  
  # an admin might want to update the name, price, or stock of an existing product.
  # store.py is the logic layer. It should just receive the data and update it. 
  # the clean approach is default parameters set to None:
  def update_product(self, id, name = None, price = None, stock = None):
    if id not in self.products:
      raise ValueError("Product does not exist!")
    else:
      if name != None:
        self.products[id].name = name

      if price != None:
        self.products[id].price = price

      if stock != None:
        self.products[id].stock = stock


  # creates new users and adds it to self.users
  def register_users(self, id, name, password, role):
    if id not in self.users:
      my_user = user.User(id, name, password, role)
      self.users[id] = my_user
      # self.users.update({id : my_user})

    else:
      raise ValueError("User already exists!")
    
  # finds the user and verifies their password
  def login_user(self, id, password):
    if id not in self.users:
      raise ValueError("User does not exist!")
    
    else:
      if self.users[id].check_password(password):   # checking if the password match 
        return self.users[id]        # returning user object
      
      else:
        raise ValueError("Incorrect password!")
      