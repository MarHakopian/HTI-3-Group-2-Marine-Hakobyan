def is_heterogram(var_str):
    var = list(var_str.lower())
    while ' ' in var:
        var.remove(' ')
    if len(var) == len(set(var)):
        return True


n = input("Please enter a word or a sentence - ")
print('Yes' if is_heterogram(n) else "No")
