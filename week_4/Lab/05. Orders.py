def calculate_total_price(product, quantity):
    product_price = 0
    if product == "coffee":
        product_price = 1.5
    elif product == "water":
        product_price = 1
    elif product == "coke":
        product_price = 1.4
    elif product == "snacks":
        product_price = 2

    total_price = product_price * quantity
    return total_price

product_name = input()
product_quantity = int(input())
res = calculate_total_price(product_name, product_quantity)
print(f"{res:.2f}")