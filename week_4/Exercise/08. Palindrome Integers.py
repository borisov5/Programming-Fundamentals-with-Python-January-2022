def is_palindrome(number):
    if number == number[::-1]:
        return True
    else:
        return False

integers = input().split(", ")
for integer in integers:
    print(is_palindrome(integer))
