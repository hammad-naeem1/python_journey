class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to inventory.")

    def show_items(self):
        if not self.items:
            print("Inventory is empty.")
            return

        for item in self.items:
            print(f"Name: {item.name}")
            print(f"Price: {item.price}")
            print(f"Quantity: {item.quantity}")
            print()

    def search_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                print(f"Found: {item.name}")
                print(f"Price: {item.price}")
                print(f"Quantity: {item.quantity}")
                return

        print("Item not found.")

    def remove_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"{item.name} removed.")
                return

        print("Item not found.")

    def increase_quantity(self, name, amount):
        for item in self.items:
            if item.name.lower() == name.lower():
                item.quantity += amount
                print(f"{item.name} quantity is now {item.quantity}.")
                return

        print("Item not found.")

    def decrease_quantity(self, name, amount):
        for item in self.items:
            if item.name.lower() == name.lower():

                if amount > item.quantity:
                    print("Not enough quantity.")
                    return

                item.quantity -= amount
                print(f"{item.name} quantity is now {item.quantity}.")
                return

        print("Item not found.")

    def total_value(self):
        total = 0

        for item in self.items:
            total += item.price * item.quantity

        print(f"Total inventory value: {total}")

    def highest_price(self):
        if not self.items:
            print("Inventory is empty.")
            return

        expensive = max(self.items, key=lambda item: item.price)

        print(f"Most expensive: {expensive.name}")
        print(f"Price: {expensive.price}")

    def largest_quantity(self):
        if not self.items:
            print("Inventory is empty.")
            return

        largest = max(self.items, key=lambda item: item.quantity)

        print(f"Largest quantity: {largest.name}")
        print(f"Quantity: {largest.quantity}")


inventory = Inventory()


while True:
    print("\n--- INVENTORY ---")
    print("1. Add item")
    print("2. Show items")
    print("3. Search item")
    print("4. Remove item")
    print("5. Increase quantity")
    print("6. Decrease quantity")
    print("7. Total inventory value")
    print("8. Most expensive item")
    print("9. Largest quantity")
    print("10. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Item name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        item = Item(name, price, quantity)
        inventory.add_item(item)

    elif choice == "2":
        inventory.show_items()

    elif choice == "3":
        name = input("Enter item name: ")
        inventory.search_item(name)

    elif choice == "4":
        name = input("Enter item name: ")
        inventory.remove_item(name)

    elif choice == "5":
        name = input("Enter item name: ")
        amount = int(input("How much to increase: "))
        inventory.increase_quantity(name, amount)

    elif choice == "6":
        name = input("Enter item name: ")
        amount = int(input("How much to decrease: "))
        inventory.decrease_quantity(name, amount)

    elif choice == "7":
        inventory.total_value()

    elif choice == "8":
        inventory.highest_price()

    elif choice == "9":
        inventory.largest_quantity()

    elif choice == "10":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")