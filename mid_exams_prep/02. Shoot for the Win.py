sequence = input().split()
index = input()
count = 0
while index != "End":
    index = int(index)
    if 0 <= index < len(sequence):
        count += 1
        for i in range(len(sequence)):
            if sequence[i] == "-1":
                continue
            elif sequence[i] > sequence[index]:
                sequence[i] = int(sequence[i]) - int(sequence[index])
            elif sequence[i] <= sequence[index] and index != i:
                sequence[i] = int(sequence[i]) + int(sequence[index])
        sequence[index] = "-1"
    index = input()

print(f"Shot targets: {count} -> ", end="")
for num in sequence:
    print(num, end=" ")
