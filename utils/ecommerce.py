# ecommerce.py

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"[{self.product_id}] {self.name} - ${self.price} ({self.stock} in stock)"


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"✅ Product '{product.name}' added successfully.")

    def remove_product(self, product_id):
        for p in self.products:
            if p.product_id == product_id:
                self.products.remove(p)
                print(f"❌ Product '{p.name}' removed successfully.")
                return
        print("⚠️ Product not found.")

    def update_product(self, product_id, name=None, price=None, stock=None):
        for p in self.products:
            if p.product_id == product_id:
                if name:
                    p.name = name
                if price:
                    p.price = price
                if stock:
                    p.stock = stock
                print(f"✏️ Product '{p.name}' updated successfully.")
                return
        print("⚠️ Product not found.")

    def list_products(self):
        if not self.products:
            print("No products available.")
            return
        print("📦 Products:")
        for p in self.products:
            print(p)


def main():
    store = Store()

    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. List Products")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter stock quantity: "))
            product = Product(product_id, name, price, stock)
            store.add_product(product)

        elif choice == "2":
            product_id = input("Enter product ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            price_input = input("Enter new price (leave blank to skip): ")
            stock_input = input("Enter new stock (leave blank to skip): ")

            price = float(price_input) if price_input else None
            stock = int(stock_input) if stock_input else None

            store.update_product(product_id, name, price, stock)

        elif choice == "3":
            product_id = input("Enter product ID to remove: ")
            store.remove_product(product_id)

        elif choice == "4":
            store.list_products()

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("⚠️ Invalid option. Try again.")


if __name__ == "__main__":
    main()