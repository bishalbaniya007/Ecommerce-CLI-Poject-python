import database
from store import Store

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
        handle_update_product()
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
        handle_view_all_orders(store, user)
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
def handle_view_all_orders(store, user):
  for order in store.orders.values():
    print(order)


def customer_menu(store, user):
  pass



if __name__ == "__main__":
  database.create_tables()    # this creates a table i
  
  my_store  = Store("Walmart")    # creates a new store(object) named "Walmart"

  my_store.products = database.load_products()    # loads the saved products
  my_store.users = database.load_users()
  my_store.orders = database.load_orders()

  main_menu(my_store)