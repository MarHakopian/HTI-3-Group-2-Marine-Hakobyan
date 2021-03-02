import math

limit = math.ceil(math.log(1000, 2))


def number_guesser(data, start, end, i=0):
    while i <= limit:
        mid = (start + end) // 2
        if i == 0:
            target = int(input('Think of a number between 1 and 999. Input 0 once you’re ready to play: '))
            print('My guess number {}: {}'.format(i + 1, mid))
            return number_guesser(data, start, end, i + 1)
        target = int(input('Pleas enter 1 or -1: '))
        if target == 0:
            return f'So I guessed in {i} steps!'
        elif i == 10 and target != 0:
            return f'I couldn’t guess in 10 steps! This means you cheated!'
        elif target == 1:
            middle1 = (mid + end) // 2
            print('My guess number {}: {}'.format(i + 1, middle1))
            return number_guesser(data, mid, end, i + 1)
        elif target == -1:
            middle2 = (start + mid) // 2
            print('My guess number {}: {}'.format(i + 1, middle2))
            return number_guesser(data, start, mid, i + 1)


seq = list(range(1, 1001))
print(number_guesser(seq, 1, len(seq) - 1))
