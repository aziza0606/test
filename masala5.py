import os
os.system("cls")


with open('transactions.txt', 'r') as file:
    transactions = file.readlines()


umumiy = {}

for transaction in transactions:
    customer_id, product_name, price, quantity = transaction.strip().split(',')
    price = float(price)
    quantity = int(quantity)
    total = price * quantity
    
    if customer_id in umumiy:
        umumiy[customer_id] += total
    else:
        umumiy[customer_id] = total


with open('big_spenders.txt', 'w') as file:
    for customer_id, total in umumiy.items():
        if total > 100:
            file.write(f"{customer_id}, {total}\n")
