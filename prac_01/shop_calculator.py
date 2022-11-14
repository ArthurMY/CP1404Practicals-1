"""
total_item_price = 0
get item_amount
while item_amount <= 0
    display Invalid number of items!
    get item_amount
for i in range(1, item_amount + 1)
    get item_price
    total_item_price += item_price
if total_item_price > 100
    total_item_price -= total_item_price*0.1
display Total price for {item_amount} items is ${total_item_price:.2f}
"""
DISCOUNT = 0.1

total_item_price = 0
item_amount = int(input("Number of items: "))
while item_amount <= 0:
    print("Invalid number of items!")
    item_amount = int(input("Number of items: "))
for i in range(1, item_amount+1):
    item_price = float(input(f"Price of Item {i}: "))
    total_item_price += item_price
if total_item_price > 100:
    total_item_price -= total_item_price*DISCOUNT
print(f"Total price for {item_amount} items is ${total_item_price:.2f}")

