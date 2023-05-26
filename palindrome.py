def is_palindrome(input_str):
    input_str = input_str.replace(" ", "").lower()

    if input_str == input_str[::-1]:
        return True
    else:
        return False

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
