price = input()
price_without_taxes = 0

while True:
    if price == "special" or price == "regular":
        break
    else:
        price = float(price)
    if price > 0:
        price_without_taxes += price
    else:
        print("Invalid price!")
    price = input()

taxes = price_without_taxes * 0.2
final_price = price_without_taxes + taxes

if price == "special":
    final_price *= 0.9

if price_without_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")
