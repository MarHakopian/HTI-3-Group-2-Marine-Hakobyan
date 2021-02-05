students = {
    'Henry': 42,
    'Ani': 96,
    'Anna': 84,
    'Narek': 56,
    'Artur': 95,
}
#Version1
# under_60 = [i for i in students if students[i] < 60]
# for i in under_60:
#     students.pop(i)
# print(students)

#Version2
students = dict(filter(lambda x: x if x[1] >= 60 else None, students.items()))
print(students)