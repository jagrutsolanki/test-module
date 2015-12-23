def reverse(text):
    return text[::-1]
def is_palindrome(text):
 return text == reverse(text)

some = raw_input("Enter text:")
if is_palindrome(some):
 print "Yes it is palindrome"
else:
 print "No its not palindrome"
