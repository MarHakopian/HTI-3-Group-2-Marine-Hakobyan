word = input('Enter a string to check if it is palindrome: ')
if word == word[::-1]:
    print('Yes')
else:
    print('No')
