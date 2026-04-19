import database
from store import Store
from cart import Cart
import uuid

def main_menu(store):
  while True:
    print("--- Welcome ---")
    print("\n--- Main menu ---")
    print("\n1. Login")
    print("2. Register")
    print("3. Exit")

    try: 
      choice = int(input("\nEnter your choice: "))
      if choice == 1:
        print("\n--- Logging in ---")
        handle_login(store)
        print("--------------------------------------------\n")

      elif choice == 2:
        print("\n--- Registering a new user ---")
        handle_registration(store)
        print("--------------------------------------------\n")

      elif choice == 3:
        print("--- Exitted successfully ---\n")
        break

      else:
        print("Please choose a valid option.")
        print("--------------------------------------------\n")

    except ValueError:
      print("Invalid input! Please choose a valid option.")
      print("--------------------------------------------\n")

# this funciton is used to login user in main_menu():
def handle_login(store):
  id = input("\nEnter your id: ")
  password = input("Enter your password: ")

  try:
    user = store.login_user(id, password) # this returns an user object 
    print("--- Logged in successfully ---\n")

    if user.is_admin():
      admin_menu(store, user)

    else:
      customer_menu(store, user)

  except ValueError as e:
    print(f"\n{e}")

# this function is to register user in main_menu():
def handle_registration(store):
  id = input("\nEnter your id: ")
  name = input("Enter your name: ")
  password = input("Enter your password: ")

  # this one is for validating the role input
  while True:
    try: 
      role_int = int(input("Choose your role: 1. Admin     2. Customer  : "))
      if role_int == 1:
        role = "admin"
        break
      elif role_int == 2:
        role = "customer"
        break
      else:
        print("Please choose a valid option.")

    except ValueError:
      print("Invalid input! Please choose a valid option")

  try:  
    store.register_users(id, name, password, role)
    print("\n--- Registration successfull ---\n")
  except ValueError as e:
    print(f"\n{e}")
      

def admin_menu(store, user):
  print(f"--- Welcome, {user.name} ---")
  while True:
    print("\n--- Admin Menu ---")
    print("\n1. Add product")
    print("2. Remove product")
    print("3. Update product")
    print("4. View all product")
    print("5. Update order status")
    print("6. View all orders")
    print("7. Logout")

    try:
      choice = int(input("Enter your choice: "))

      if choice == 1:
        print("\n--- Adding a product ---")
        handle_add_product(store)
        print("--------------------------------------------\n")

      elif choice == 2:
        print("\n--- Removing a product ---")
        handle_remove_product(store)
        print("--------------------------------------------\n")
      
      elif choice == 3:
        print("\n--- Updating product ---")
        handle_update_product(store)
        print("--- Product updated successfully ---\n")

      elif choice == 4:
        print("\n--- All Products ---")
        handle_view_all_products(store)
        print("--------------------------------------------\n")

      elif choice == 5:
        print("\n--- Updating order status ---")
        handle_update_order_status(store)
        print("--------------------------------------------\n")

      elif choice == 6:
        print("\n--- All orders ---")
        handle_view_all_orders(store)
        print("--------------------------------------------\n")

      elif choice == 7:
        print("--- Logged out successfully ---\n")
        break

      else:
        print("Please choose a valid option.")
    
    except ValueError:
      print("Invalid choice! Please choose a valid option.")

# this fucntion handles adding a product to a store     
def handle_add_product(store):
  id = input("Enter the product id: ")
  name = input("Enter the product name: ")
  price = float(input("Enter the price of the product: "))
  stock = int(input("Enter the stock of the product: "))

  try:
    store.add_product(id, name, price, stock)
    print("\n--- Product added successfully ---\n")
  except ValueError as e:
    print(f"\n{e}")


# this function handles removing a product from a store
def handle_remove_product(store):
  id = input("Enter the product id: ")

  try:
    store.remove_product(id)
    print("\n--- Product removed successfully ---\n")
  except ValueError as e:
    print(f"\n{e}")


# this function handles updating a product
def handle_update_product(store):
  id = input("Enter the product id: ")

  try:
    print("What do you want to upate?")
    print("1. Name    2. Price    3. Stock    4. All")
    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
      name = input("Enter the new name: ")
      try:
        store.update_product(id, name=name)
        print("--- Product updated successfully ---")

      except ValueError as e:
        print(f"\n{e}")

    elif choice == 2:
      price = float(input("Enter the new price: "))
      try:
        store.update_product(id, price = price)
        print("--- Product updated successfully ---")
      
      except ValueError as e:
        print(f"\n{e}")

    
    elif choice == 3:
      stock = int(input("Enter the new stock: "))
      try:
        store.update_product(id, stock=stock)
        print("--- Product updated successfully ---")
      
      except ValueError as e:
        print(f"\n{e}")

    
    elif choice == 4:
      name = input("Enter the product name: ")
      price = float(input("Enter the price: "))
      stock = int(input("Enter the stock: "))

      try:
        store.update_product(id, name=name, price=price, stock=stock)
        print("--- Product updated successfully ---")
      
      except ValueError as e:
        print(f"\n{e}")

    else:
      print("Please choose a valid optin.")

  except ValueError:
    print("Invalid input! Please choose a valid option")


# this functions shows all the products in the store
def handle_view_all_products(store):
  for product in store.get_all_products().values():
    print(product)

# this function updates the order status
def handle_update_order_status(store):
    try:
      order_id = input("Enter the order id: ")
      print("--- Order status ---")
      print("1. Pending  2. Shipped  3. Delivered  4. Cancelled")
      new_status = int(input("Choose the new status: "))

      if new_status == 1:
        store.update_order_status(order_id, "pending")
        print("\n--- Order status updated successfully ---")

      elif new_status == 2:
        store.update_order_status(order_id, "shipped")
        print("\n--- Order status updated successfully ---")

      elif new_status == 3:
        store.update_order_status(order_id, "delivered")
        print("\n--- Order status updated successfully ---")

      elif new_status == 4:
        store.update_order_status(order_id, "cancelled")
        print("\n--- Order status updated successfully ---")

      else:
        print("Please choose a valid option.")
    except ValueError as e:
      print(f"\n{e}")
    

# this function shows all orders of the user
def handle_view_all_orders(store):
  for order in store.orders.values():
    print(order)


def customer_menu(store, user):
  cart = Cart(user.id)  # creates cart when customer logs in
  print(f"\n--- Welcome, {user.name} ---")    # welcome message
  
  while True:
    print("\n--- Customer menu ---")
    print("\n1. View all products")
    print("2. Add to cart")
    print("3. Remove from cart")
    print("4. View cart")
    print("5. Update quantity")
    print("6. Checkout")
    print("7. View my orders")
    print("8. Logout")

    try:
      choice = int(input("Enter your choice: "))

      if choice == 1:
        print("\n--- All products ---")
        handle_view_all_products(store)
        print("--------------------------------------------\n")

      elif choice == 2:
        print("\n--- Adding product to a cart ---")
        handle_add_to_cart(store, cart)
        print("--------------------------------------------\n")

      elif choice == 3:
        print("\n--- Removing product from a cart ---")
        handle_remove_product_from_cart(store, cart)
        print("--------------------------------------------\n")

      elif choice == 4:
        print("\n--- Viewing my cart ---")
        handle_view_cart(cart)
        print("--------------------------------------------\n")

      elif choice == 5:
        print("\n--- Updating my cart ---")
        handle_update_cart(store, cart)
        print("--------------------------------------------\n")

      elif choice == 6:
        print("\n--- Checking out ---")
        handle_checkout(store, cart, user)
        print("--------------------------------------------\n")

      elif choice == 7:
        print("\n--- Viewing my orders ---")
        handle_view_orders(store, user)
        print("--------------------------------------------\n")

      elif choice == 8:
        print("\n--- Logged out successfully ---")
        print("--------------------------------------------\n")
        break
        
    except ValueError:
      print("Invalid input! Please choose a valid option.")
               

# this function handles adding product to a cart
def handle_add_to_cart(store, cart):
  while True:
    print("\n--- Available products ---")
    for product in store.get_all_products().values():   # printing available products from store
      print(product)
    
    try:
      product_id = input("\nEnter the id of the product you want: ")  # getting product_id and quantity
      quantity = int(input("Enter the quantity: "))

      product = store.get_product(product_id)   # getting product_obj to pass to cart

      cart.add_item(product, quantity)    # passing product_obj and quantity to cart

      print("\n--- Product added to cart ---")

      to_continue = input("\nDo you still wish to continue shopping? (y/n): ")
      if to_continue.lower() == 'y':
        continue
      else:
        break
    
    except ValueError as e:
      print(f"\n{e}")

# this function handles removing product
def handle_remove_product_from_cart(store, cart):
  while True:
    print("\n--- My cart ---")
    handle_view_cart(cart)

    try:
      product_id = input("Enter the product id you want to remove: ")
      product = store.get_product(product_id)
      cart.remove_item(product)

      to_continue = input("Do you still wish to continue? (y/n): ")
      if to_continue.lower() == 'y':
        continue
      else:
        break
    
    except ValueError as e:
      print(f"\n{e}")

# this function prints the products in cart
def handle_view_cart(cart):
  for item in cart.view_cart().values():
    print(f"{item['product'].name} x{item['quantity']}")

# this function hanldes updating qunatity in my cart
def handle_update_cart(store, cart):
  print("\n--- My cart ---")
  handle_view_cart(cart)

  try:
    product_id = input("Enter the id of the product you want to update: ")
    product = store.get_product(product_id)   # getting the product obj
    new_quantity = int(input("Enter the new quantity: "))

    cart.update_quantity(product, new_quantity)

    print("\n--- Product updated successfully ---")
  except ValueError as e:
    print(f"\n{e}")

# this function handles checking out
def handle_checkout(store, cart, user):
  order_id = str(uuid.uuid4())    # generates order id
  try:
    if cart.view_cart():   # view_items returns a cart(dict) and this checks if the cart(dict) is empty or not
      store.place_order(user.id, order_id, cart)

      

      print("\n--- Checked out successfully ---")
      
    else:
      print("\n--- The cart is empty! Can not checkout. ---")

  except ValueError as e:
    print(f"\n{e}")

# this funcion prints all the users orders
def handle_view_orders(store, user):    
  my_orders = store.get_user_orders(user.id)    # returns orders dict

  for order in my_orders.values():
    print(order)

if __name__ == "__main__":
  database.create_tables()    # this creates a table i
  
  my_store  = Store("Walmart")    # creates a new store(object) named "Walmart"

  my_store.products = database.load_products()    # loads the saved products
  my_store.users = database.load_users()
  my_store.orders = database.load_orders()

  main_menu(my_store)