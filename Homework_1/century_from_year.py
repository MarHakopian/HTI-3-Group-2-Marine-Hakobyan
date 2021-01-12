year = int(input("Enter a year: "))
for i in range(21):
    if 1 + 100*i <= year <= 100 + 100*i:
        print('Century -', i+1)
