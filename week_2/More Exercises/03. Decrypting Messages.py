key = int(input())
number_of_lines = int(input())
secret_message = ""
for i in range(number_of_lines):
    message = input()
    message = ord(message)
    current_symbol =  message + key
    secret_message += chr(current_symbol)

print(secret_message)