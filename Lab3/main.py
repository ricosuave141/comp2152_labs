#Aaron-Balayo
#ID: 101575606
#COMP2152-Python
#Lab3

#Question 1: Student Grades
grades = [85, 92, 78, 95, 88]
grades.append()
grades.sort()
print("Sorted grades:", grades)
print("Highest grade:", grades[-1])
print("Lowest grade:", grades[0])
print("Total number of grades:", len(grades))
print("\n" + "-" * 40)

#Question 2: Shopping Cart
cart = ["apples", "banana", "milk", "bread", "eggs"]

print("Number of apples:", cart.count("apples"))
print("Position of milk:", cart.index("milk"))
cart.remove("apples")
removed_item = cart.pop()
print("Removed item using pop:", removed_item)
print("Is banana in cart?", "banana" in cart)
print("Final cart:", cart)
print("\n" + "-" * 40)

#Question 3: Coordinate System
point1 = (3, 5)
point2 = (7, 2)
x1, y1 = point1
x2, y2 = point2
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Point 1:", point1)
print("Point 2:", point2)
print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")
print("Distance between points:", distance)
chars = tuple("PYTHON")
print("Characters tuple:", chars)
for char in chars:
    print(char)
print("\n" + "-" * 40)

#Question 4: Class Attendance
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)
print("Attended both classes:", monday_class & wednesday_class)
print("Attended either class:", monday_class | wednesday_class)
print("Only Monday:", monday_class - wednesday_class)
print("Only one class (not both):", monday_class ^ wednesday_class)
print("Is Monday subset of all students?", monday_class <= (monday_class | wednesday_class))
print("\n" + "-" * 40)

#Question 5: Contact Book
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print("Alice's number:", contacts["Alice"])
contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)
contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)
del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)
print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))
print("\n" + "-" * 40)

#Question 6: Inventory System
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}
print("=== Current Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price}, Quantity: {quantity}")
electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}
all_products = electronics | accessories
print("\nAll product categories:", all_products)
price_list = [price for price, _ in inventory.values()]
price_list.sort()
print("\nPrice list:", price_list)
print("Sorted prices:", price_list)
print("Lowest price: $", price_list[0])
print("Highest price: $", price_list[-1])
inventory["Headphones"] = (49.99, 20)
price, _ = inventory["Mouse"]
inventory["Mouse"] = (price, 12)
del inventory["Monitor"]
print("\n=== Final Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price}, Quantity: {quantity}")