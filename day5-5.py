def is_palindrome(string):
    reversed_string=string[::-1]
    return string==reversed_string
input_string="madam"
#is_palindrome=is_palindrome(input_string)
if is_palindrome:
    print("this is a palindrome")
else:
    print("this is not a palindrome")
