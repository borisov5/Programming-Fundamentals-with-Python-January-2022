number = input()
my_list = list(number)
sorted_list = sorted(my_list)
sorted_list.reverse()
largest_number = "".join(sorted_list)
print(largest_number)