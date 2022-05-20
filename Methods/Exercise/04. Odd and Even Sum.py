def get_even_and_odd_numbers(number):
    sum_of_even = 0
    sum_of_odd = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odd += int(digit)
    return sum_of_even, sum_of_odd

number_as_string = input()

even_sum, odd_sum = get_even_and_odd_numbers(number_as_string)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
