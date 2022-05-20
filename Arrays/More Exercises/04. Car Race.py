numbers = input().split()
elements = len(numbers) // 2
left_sum = 0
right_sum = 0
winner = ""
total_time = 0
for left_side in range(0, elements):
    number = int(numbers[left_side])
    if number == 0:
        left_sum *= 0.8
    left_sum += number
for right_side in range(-1, -(elements + 1), -1):
    number = int(numbers[right_side])
    if number == 0:
        right_sum *= 0.8
    right_sum += number
if left_sum < right_sum:
    winner = "left"
    total_time = left_sum
else:
    winner = "right"
    total_time = right_sum

print(f"The winner is {winner} with total time: {total_time:.1f}")
