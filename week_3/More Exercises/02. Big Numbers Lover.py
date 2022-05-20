numbers = input().split()
numbers.sort()
numbers.reverse()
number = ""
for i in numbers:
    number += i
print(number)