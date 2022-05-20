message = list(input())
decrypted_message = []
instruction = input().split("|")
while instruction[0] != "Decode":
    if instruction[0] == "Move":
        number = int(instruction[1])
        for index in range(number):
            x = message.pop(0)
            message.append(x)
    elif instruction[0] == "Insert":
        index = int(instruction[1])
        value = instruction[2]
        reversed_value = value[::-1]
        for symbol in reversed_value:
            message.insert(index, symbol)
    elif instruction[0] == "ChangeAll":
        message[:] = [x if x != instruction[1] else instruction[2] for x in message]
    instruction = input().split("|")

final_message = "".join(message)
print(f"The decrypted message is: {final_message}")
