strings = input().split(" ")
total_sum = 0
for string in strings:
    if string == "":
        continue
    front_letter = string[0]
    after_letter = string[-1:]
    number = int(string[1:len(string)-1])
    if ord(front_letter) in range(65, 91):
        total_sum += (number / (ord(front_letter) - 64))
    elif ord(front_letter) in range(97, 123):
        total_sum += (number * (ord(front_letter) - 96))

    if ord(after_letter) in range(65, 91):
        total_sum -= (ord(after_letter) - 64)
    elif ord(after_letter) in range(97, 123):
        total_sum += (ord(after_letter) - 96)


print(f"{total_sum:.2f}")
