class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def display_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Stock Quantity: {self.stock_quantity}")


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)

    def display_cart(self):
        total_price = 0
        print("Shopping Cart:")
        for item in self.items:
            print(f"-----> {item.name}= rs {item.price}")
            total_price += item.price
        print(f"Total Price= rs {total_price}")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.order_history = []

    def add_to_order_history(self, order):
        self.order_history.append(order)


class Order:
    def __init__(self, items, total_price):
        self.items = items
        self.total_price = total_price


# Sample usage:

# Creating products
product1 = Product("Laptop", 40000, 10)
product2 = Product("Headphones", 1000, 20)
product3 = Product("Mouse", 200, 30)
product4= Product("Mobile", 20000, 30)
product5= Product("TV", 20000, 30)

# Creating a shopping cart
cart = ShoppingCart()

# Adding product to  shopping cart
cart.add_item(product1)
cart.add_item(product2)
cart.add_item(product3)
cart.add_item(product4)
cart.add_item(product5)

# shopping cart
cart.display_cart()

# Creating a user
user = User("NANJUNDI", "NK@123")

#remove from shopping cart
cart.remove_item(product1)
cart.remove_item(product5)

# Adding order to user's order history
order = Order(cart.items,21200 )
user.add_to_order_history(order)

# Displaying user's order history
print("User's Order History:")
for order in user.order_history:
    print("Ordered Items:")
    for item in order.items:
        print(f"-----> {item.name}: rs {item.price}")
    print(f"Total Price: rs {order.total_price}")
