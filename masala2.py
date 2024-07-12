import os
os.system("cls")

cheap_products = []

with open("products.txt", "r") as file:
    data = file.read().split("\n")
    
    for line in data:
        if line.strip():
            parts = line.split(", ")
            name = parts[0].strip()
            price = int(parts[1].strip())
            count = int(parts[2].strip())
            product = {
                'name': name,
                'price': price,
                'count': count
            }
            if price < 10:
                cheap_products.append(product)

with open("cheap_products.txt", "w") as cheap_productsFile:
    for product in cheap_products:
        cheap_productsFile.write(f"{product['name']}, {product['price']}, {product['count']}\n")
