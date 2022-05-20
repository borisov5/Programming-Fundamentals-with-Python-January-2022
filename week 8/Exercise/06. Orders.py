orders = {}
order = input().split(" ")

while order[0] != "buy":
    name = order[0]
    price = float(order[1])
    quantity = int(order[2])
    if name not in orders:
        orders[name] = [price, quantity]
    else:
        orders[name][0] = price
        orders[name][1] += quantity
    order = input().split(" ")

for k, v in orders.items():
    total_price = v[0] * v[1]
    print(f"{k} -> {total_price:.2f}")
