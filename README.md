# 🛒 CLI E-Commerce System

A fully functional command-line e-commerce system built in Python. Features role-based access control, secure password hashing, SQLite persistence, and a complete shopping flow from browsing to checkout.

---

## 📁 Project Structure

```
ecommerce/
│
├── models/
│   ├── product.py       # Product class with stock management
│   ├── user.py          # User class with password hashing
│   ├── cart.py          # Cart class with item management
│   └── order.py         # Order class with status tracking
│
├── database.py          # SQLite storage — save/load all data
├── store.py             # Core business logic engine
└── main.py              # CLI interface and menus
```

---

## ✨ Features

### 👤 Authentication
- User registration with hashed passwords (SHA-256)
- Secure login with password verification
- Role-based access: **Admin** and **Customer**

### 🛠️ Admin
- Add, remove, and update products
- View all products and orders
- Update order status (Pending → Shipped → Delivered → Cancelled)

### 🛍️ Customer
- Browse all available products
- Add items to cart with quantity validation
- View, update, and remove cart items
- Checkout and place orders
- View personal order history

### 💾 Data Persistence
- All data saved to a local SQLite database (`store.db`)
- Data survives program restarts
- Complex objects serialized to JSON for storage

---

## 🚀 Getting Started

### Requirements
- Python 3.x
- No external libraries required — uses only Python standard library

### Run the program
```bash
python main.py
```

---

## 🔧 Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3 | Core language |
| SQLite3 | Data persistence |
| hashlib | Password hashing (SHA-256) |
| uuid | Unique order ID generation |
| json | Object serialization |
| datetime | Order timestamps |

---

## 🏗️ Architecture

The project follows a clean **3-layer architecture**:

```
┌─────────────────────────────┐
│         main.py             │  ← CLI layer (menus, input/output)
├─────────────────────────────┤
│         store.py            │  ← Business logic layer
│      models/*.py            │
├─────────────────────────────┤
│        database.py          │  ← Storage layer (SQLite)
└─────────────────────────────┘
```

Each layer has one job. The CLI never talks to the database directly, and the models never handle user input.

---

## 🔐 Security

- Passwords are never stored as plain text
- SHA-256 hashing applied before storage
- Login verifies by hashing input and comparing to stored hash

---

## 📌 Concepts Demonstrated

- Object-Oriented Programming (OOP)
- Class methods (`@classmethod`) for alternative constructors
- Exception handling with custom error messages
- SQLite database with CRUD operations
- JSON serialization/deserialization
- Layered software architecture
- Input validation throughout

---

## 🌱 Future Improvements

- [ ] Convert to web app using Flask
- [ ] Add product search and filtering
- [ ] Add unit tests
- [ ] Add product categories
- [ ] Show cart total before checkout
- [ ] Add password confirmation on register