# import cart
from datetime import datetime

class Order:
  def __init__(self, order_id, user_id, ordered_items, total,  status = "pending"):
    self.order_id = order_id
    self.user_id = user_id
    self.ordered_items = ordered_items
    self.total = total
    self.status = status
    self.ordered_at = datetime.now()


  def __str__(self):
    items = ""
    for item in self.ordered_items.values():
      name = item["product"].name
      quantity = item["quantity"]

      items += f"{name} x{quantity}"

    return f"--- Your order summary --- \nOrder id: {self.order_id} \nUser id: {self.user_id} \nItems: {items}\nTotal: Rs.{self.total:,.2f} \nPlaced at: {self.ordered_at} \nStatus: {self.status}"
  

  def update_status(self, new_status):
    status_list = ("pending", "shipped", "delivered", "cancelled")
    if new_status.strip().lower() not in status_list:
      raise ValueError("Invalid status!")
    else:
      self.status = new_status


# cart = cart.Cart("user_id")
# ordered_items = cart.checkout()        # checkout() -> returns ordered items
# total = cart.calculate_total()

# print(ordered_items)
# print(total)

# ordered_time = datetime.now()
# print(ordered_time)

# order = Order("0001", "101", ordered_items, total)

# print(order)