def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif len(text) > 1 and text[0] == text[-1]:
        text = text[1:-1]
        return is_palindrome(text)
    else:
        return False


input_text = input("Please enter the text: ")
print("Yes" if is_palindrome(input_text) else "No")
