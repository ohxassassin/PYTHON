number = input("Enter a number: ")
reversed_number = number[::-1]
if number == reversed_number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
