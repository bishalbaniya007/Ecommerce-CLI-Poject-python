import sqlite3
from product import Product
from user import User
import json
from order import Order

def create_tables():
  # establishing the connection
  conn = sqlite3.connect("store.db")

  # creating a cursor
  c = conn.cursor()

  # now creating a produdct table
  c.execute(""" CREATE TABLE IF NOT EXISTS products(
            id text,
            name text,
            price real,
            stock integer
            )""")
  
  conn.commit()

  # creating a table called users
  c.execute(""" CREATE TABLE IF NOT EXISTS users(
            id text,
            name text,
            password text,
            role text
            )""")

  conn.commit()

  # creating a table called orders
  c.execute(""" CREATE TABLE IF NOT EXISTS orders(
            id text,
            user_id text,
            ordered_items text,
            status text,
            ordered_at text,
            total real
            )""")

  conn.commit()

  # closing the connection
  conn.close()

def save_products(products):
  conn = sqlite3.connect("store.db")
  
  c = conn.cursor()

  # looping through each product in products(dict) and inserting it into table
  for product in products.values():
    c.execute("INSERT OR REPLACE INTO products VALUES (?, ?, ?, ?)", 
              (product.id, product.name, product.price, product.stock)) 
    
  conn.commit()

  conn.close()

def load_products():
  products_dict = {}

  conn = sqlite3.connect("store.db")

  c = conn.cursor()

  c.execute("SELECT * FROM products")
  for row in c.fetchall():
    products_dict[row[0]] = Product(row[0], row[1], row[2], row[3])

  conn.close()

  return products_dict

def save_users(users):
  conn = sqlite3.connect("store.db")

  c = conn.cursor()

  for user in users.values:
    c.execute("INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?)", 
              (user.id, user.name, user.password, user.role))
    
  conn.commit()

  conn.close()

def load_users():
  users_dict = {}

  conn = sqlite3.connect("store.db")

  c = conn.cursor()

  c.execute("SELECT * FROM users")
  for row in c.fetchall():
    users_dict[row[0]] = User.from_db(row[0], row[1], row[2], row[3])

  conn.close()

  return users_dict


def save_orders(orders):
  conn = sqlite3.connect("store.db")

  c = conn.cursor()

  for order in orders.values():
    items_to_save = {}

    for product_id, item in order.ordered_items.items():
      items_to_save[product_id] = {
          "product": item["product"].to_dict(),  # convert Product to dict
          "quantity": item["quantity"]
      }

    # ← inner loop done, items_to_save is ready
    items_json = json.dumps(items_to_save)  # convert to JSON string
    
    # ← now INSERT into orders table
    c.execute("INSERT OR REPLACE INTO orders VALUES (?, ?, ?, ?, ?, ?)",
              (order.id, order.user_id, items_json, order.total, order.status, str(order.ordered_at)))

  
  conn.commit()

  conn.close()


def load_orders():
  orders_dict = {}

  conn = sqlite3.connect("store.db")

  c = conn.cursor()

  c.execute("SELECT * FROM orders")
  for row in c.fetchall():
    #  Convert ordered_items back from JSON string to dictionary:
    ordered_items = json.loads(row[2])

    # Loop through ordered_items and convert each product dictionary back to a Product object:
    for product_id, item in ordered_items.items():
      item["product"] = Product(item["product"]["id"], item["product"]["name"], 
                                item["product"]["price"], item["product"]["stock"])


    # Create the Order using from_db() and add to orders_dict
    orders_dict[row[0]] = Order.from_db(row[0], row[1], ordered_items, row[3], row[4], row[5])

  conn.close()

  return orders_dict