import re

def is_match(message):
    regex = r'^([$%])([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'
    matches = re.findall(regex, message)
    if matches:
        tag = matches[0][1]
        res1 = chr(int(matches[0][2]))
        res2 = chr(int(matches[0][3]))
        res3 = chr(int(matches[0][4]))
        decrypted_message = res1 + res2 + res3
        print(f"{tag}: {decrypted_message}")

    else:
        print("Valid message not found!")

number = int(input())

for _ in range(number):
    message = input()
    is_match(message)
