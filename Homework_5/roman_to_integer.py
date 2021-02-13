dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_nums(roman):
    elements = [dict.get(i) for i in roman]
    new_elements = []
    removed_elements = []
    for i in range(len(elements) - 1):
        if elements[i] < elements[i + 1]:
            m = elements[i + 1] - elements[i]
            new_elements.append(m)
            removed_elements.append(0 - elements[i])
            removed_elements.append(0 - elements[i + 1])
    number = sum(elements) + sum(removed_elements) + sum(new_elements)
    return number


example = input('Please enter the roman numerial: ')
print(roman_nums(example))
