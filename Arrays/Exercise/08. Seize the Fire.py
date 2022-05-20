fire_types = input().split("#")
water = int(input())
effort = 0
total_fire = 0
print("Cells:")
for elements in fire_types:
    current_list = elements.split(" = ")
    if current_list[0] == "Low":
        if 1 <= int(current_list[1]) <= 50:
            if water >= int(current_list[1]):
                water -= int(current_list[1])
                effort += float(current_list[1]) * 0.25
                total_fire += int(current_list[1])
                print(f" - {current_list[1]}")
    elif current_list[0] == "Medium":
        if 51 <= int(current_list[1]) <= 80:
            if water >= int(current_list[1]):
                water -= int(current_list[1])
                effort += float(current_list[1]) * 0.25
                total_fire += int(current_list[1])
                print(f" - {current_list[1]}")
    elif current_list[0] == "High":
        if 81 <= int(current_list[1]) <= 125:
            if water >= int(current_list[1]):
                water -= int(current_list[1])
                effort += float(current_list[1]) * 0.25
                total_fire += int(current_list[1])
                print(f" - {current_list[1]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

