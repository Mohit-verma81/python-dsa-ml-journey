def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


text = input("Enter a Word: ")

if is_palindrome(text):
    print("word is Palindrome")
else:
    print("Not a Palindrome")