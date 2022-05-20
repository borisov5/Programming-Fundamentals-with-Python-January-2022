divisor = int(input())
boundary = int(input())
largest_integer = 0
for i in range(1, boundary + 1):
    if (i % divisor) == 0:
        largest_integer = i

print(largest_integer)