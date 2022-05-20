def len_is_ok(password):
    if 6 <= len(password) <= 10:
        return True
def letters_and_digits(password):
    password = password.split()
    for symbol in password:
        if symbol.isalnum() or symbol.isdigit():
            return True
        else:
            return False
def two_digit(password):
    counter = 0
    for symbol in password:
        if symbol.isdigit():
            counter += 1
    if counter >= 2:
        return True

text = input()
if len_is_ok(text) and letters_and_digits(text) and two_digit(text):
    print("Password is valid")
if not len_is_ok(text):
    print("Password must be between 6 and 10 characters")
if not letters_and_digits(text):
    print("Password must consist only of letters and digits")
if not two_digit(text):
    print("Password must have at least 2 digits")
