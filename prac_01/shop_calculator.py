number_of_items = int(input("Number of items: "))
price_of_item = float(input("Price of item: "))
total_price = 0
for i in range(1, number_of_items):
    price_of_item = float(input("price of item: "))
    total_price += price_of_item
if total_price >100:
    total_price *= 0.9

print(f"Total price for {number_of_items} items is ${total_price} ")