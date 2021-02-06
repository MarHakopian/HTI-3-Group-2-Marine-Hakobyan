def factorial_f(n):
    factorial_n = 1
    for i in range(1, int(n) + 1):
        factorial_n = factorial_n * i
    return f"The factorial of {n} is {factorial_n}!"


n = input("Enter the number: ") # not n a
print(factorial_f(n))
