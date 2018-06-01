def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)

while True:
    something = raw_input('Enter text: ')

    if (is_palindrome(something)):
        print("Yes, it is a palindrome")
        break
    else:
        print("No, it is not a palindrome")
        continue
