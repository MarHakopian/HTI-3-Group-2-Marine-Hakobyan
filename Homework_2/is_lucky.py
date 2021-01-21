ticket_num = list(input("Enter the number of your ticket: "))
new_list = [int(i) for i in ticket_num]
half = int(len(new_list) / 2)
if len(new_list) % 2 == 0:
    if sum(new_list[:half]) == sum(new_list[half:]):
        print('Yes')
    else:
        print('No')
else:
    print("Error!")

