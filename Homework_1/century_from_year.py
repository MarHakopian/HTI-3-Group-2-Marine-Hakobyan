
year = int(input("Enter a year: "))
century = year // 100
if year % 100 == 0:
    print("Century - ", century)
else:
    print("Century - ", century + 1)