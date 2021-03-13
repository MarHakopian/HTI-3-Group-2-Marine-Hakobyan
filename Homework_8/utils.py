import sys


def is_odd(value):
    _ = str(value)
    for el in _:
        if int(el) % 2 == 0:
            return False
    else:
        return True


def odd_nums(first, last):
    for i in range(first, last):
        if is_odd(i):
            yield i


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("Please enter 2 arguments")
    start = int(sys.argv[1])
    stop = int(sys.argv[2])

    for o in odd_nums(start, stop):
        print(o, end=' ')
    print()