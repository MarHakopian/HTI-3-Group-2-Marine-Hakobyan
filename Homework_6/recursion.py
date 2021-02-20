
def combination(n, k=None):
    vals = set(range(1, n+1))
    if k is None:
        k = len(vals)
    if k == 1:
        return list(vals)
    res = []
    for i in vals:
        c = combination(n, k-1)
        for e in c:
            l = [i]
            if isinstance(e, list):
                l.extend(e)
            else:
                l.append(e)
            if i <= l[1]:
                res.append(l)
    return res


def count_and_print(a):
    countf = 0
    for i in a:
        countf += 1
        if isinstance(a, int):
            print(i, end=' ')
        else:
            print(*i)
    return f"Total: {countf}"

result = combination(4,3)
print(count_and_print(result))


