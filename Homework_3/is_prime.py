def prime_checker(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                result = f"No, {num} is not prime."
                break
            else:
                result = f'Yes, {num} is prime.'
    elif num == 1:
        result = "1 is neither prime nor composite!"
    else:
        result = 'Please enter a natural number!'
    return result


num = int(input('Enter the number to check if it is prime or not: '))
print(prime_checker(num))
