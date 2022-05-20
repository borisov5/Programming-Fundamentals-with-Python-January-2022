import re

regex = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'
product_group_regex = r'([0-9]+)'
number_of_barcodes = int(input())

for _ in range(number_of_barcodes):
    text_string = input()
    match = re.findall(regex, text_string)
    if match:
        numbers = "".join(match)
        number = re.findall(product_group_regex, numbers)
        product_group = "".join(number)
        if product_group == "":
            print("Product group: 00")
        else:
            print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")

