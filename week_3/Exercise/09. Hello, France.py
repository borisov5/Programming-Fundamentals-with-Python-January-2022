items = input().split("|")
budget = float(input())
final_profit = budget
profit = 0
for item in items:
    current_item = item.split("->")
    current_price = float(current_item[1])
    current_item = current_item[0]
    if current_item == "Clothes":
        if current_price <= 50:
            if budget >= current_price:
                budget -= current_price
                profit += current_price * 0.4
                price = current_price * 1.4
                print(f"{price:.2f}", end = " ")
    elif current_item == "Shoes":
        if current_price <= 35:
            if budget >= current_price:
                budget -= current_price
                profit += current_price * 0.4
                price = current_price * 1.4
                print(f"{price:.2f}", end=" ")
    elif current_item == "Accessories":
        if current_price <= 20.50:
            if budget >= current_price:
                budget -= current_price
                profit += current_price * 0.4
                price = current_price * 1.4
                print(f"{price:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
final_profit += profit
if final_profit > 150:
    print("Hello, France!")
else:
    print("Not enough money.")