
# palindrome
def is_palindrome(s):
    return s == s[::-1]

print("Given string is palindrome: Madam ",is_palindrome("madam"))
print("Given string is palindrome: Hello ",is_palindrome("Hello"))