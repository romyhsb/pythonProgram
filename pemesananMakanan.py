class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - Price: {self.price}"


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menus = []

    def add_menu(self, menu):
        self.menus.append(menu)

    def remove_menu(self, menu):
        self.menus.remove(menu)


class Order:
    def __init__(self, menu, quantity):
        self.menu = menu
        self.quantity = quantity

    def total_price(self):
        return self.menu.price * self.quantity

    def __str__(self):
        return f"{self.menu.name} - Quantity: {self.quantity}, Total Price: {self.total_price()}"


class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)


def main():
    restaurant = Restaurant("Delicious Restaurant")

    menu1 = Menu("Nasi Goreng", 15000)
    menu2 = Menu("Ayam Bakar", 20000)

    restaurant.add_menu(menu1)
    restaurant.add_menu(menu2)

    customer1 = Customer("John Doe")
    customer2 = Customer("Jane Smith")

    order1 = Order(menu1, 2)
    order2 = Order(menu2, 1)

    customer1.add_order(order1)
    customer2.add_order(order2)

    print(f"{customer1.name}'s Orders:")
    for order in customer1.orders:
        print(order)

    print(f"\n{customer2.name}'s Orders:")
    for order in customer2.orders:
        print(order)


if __name__ == "__main__":
    main()
