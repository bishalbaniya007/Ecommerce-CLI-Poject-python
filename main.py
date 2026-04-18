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
        print("Exit")
        print("--------------------------------------------\n")
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
  pass

def customer_menu(store, user):
  pass



if __name__ == "__main__":
  database.create_tables()    # this creates a table i
  
  my_store  = Store("Walmart")    # creates a new store(object) named "Walmart"

  my_store.products = database.load_products()    # loads the saved products
  my_store.users = database.load_users()
  my_store.orders = database.load_orders()

  main_menu(my_store)