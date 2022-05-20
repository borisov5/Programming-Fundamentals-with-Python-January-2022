number_of_lines = int(input())
capacity = 255
water_counter = 0
for line in range(number_of_lines):
    current_flow = int(input())
    if capacity - current_flow < 0:
        print("Insufficient capacity!")
        continue
    water_counter += current_flow
    capacity -= current_flow
print(water_counter)