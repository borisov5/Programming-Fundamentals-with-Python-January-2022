number = int(input())
number_is_prime = True
if number > 0:
    for i in range(2, number):
        if number % i == 0:
            number_is_prime = False
print(number_is_prime)