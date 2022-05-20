def print_str_list(str_list):
    print("".join(str_list))

text = input()

digits = []
letters = []
symbols = []

for s in text:
    if s.isdigit():
        digits.append(s)
    elif s.isalpha():
        letters.append(s)
    else:
        symbols.append(s)

print_str_list(digits)
print_str_list(letters)
print_str_list(symbols)
