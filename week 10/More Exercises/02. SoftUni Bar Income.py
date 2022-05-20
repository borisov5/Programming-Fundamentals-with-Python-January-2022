import re

income = 0
order = input()

while order != "end of shift":
    matches = re.finditer(r"(%[A-Z][a-z]+%).*(<.+>).*(\|.+?\|)\D*(.+?\$)", order)
    total_price = 0
    for match in matches:
        customer_name = match.group(1).strip("%")
        product = match.group(2).strip("<>")
        quantity = int(match.group(3).strip("|"))
        price = float(match.group(4).strip("$"))
        total_price = quantity * price
        print(f"{customer_name}: {product} - {total_price:.2f}")
    income += total_price
    order = input()

print(f"Total income: {income:.2f}")
