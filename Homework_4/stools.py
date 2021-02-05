def func_stool(heights):
    list_int = [int(i) for i in list(heights.split())]
    max_height = max(list_int)
    sum_heights = 0
    for i in list_int:
        sum_heights += max_height - i
    return sum_heights

a = input("Please enter the heights: ")
print(func_stool(a))

