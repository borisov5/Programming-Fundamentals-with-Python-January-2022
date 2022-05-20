import sys
starting_list = input().split()
number = int(input())
for smalest_ones in range(number):
    min_number = sys.maxsize
    for index in range(len(starting_list)):
        if int(starting_list[index]) < min_number:
            min_number = int(starting_list[index])
    starting_list.remove(str(min_number))
final_list = ", ".join(starting_list)
print(final_list)