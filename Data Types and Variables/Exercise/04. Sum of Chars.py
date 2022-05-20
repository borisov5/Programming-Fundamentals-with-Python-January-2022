number = int(input())
total_sum = 0
for i in range(1, number + 1):
    symbol = input()
    symbol = ord(symbol)
    total_sum += symbol
print(f"The sum equals: {total_sum}")