def number_root(num):
    sum_of_nums = 11
    while sum_of_nums > 10:
        sum_of_nums = 0
        for i in str(num):
            sum_of_nums += int(i)
        num = sum_of_nums
    return num
num = input("Enter the number to find the root: ")
print(number_root(num))
