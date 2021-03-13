import time


def warn_slow(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        if duration > 2:
            print(f"execution of {func.__name__} with {(*args, *kwargs.values())} arguments took more than 2 seconds")
        return result

    return inner


@warn_slow
def func_slow(x, y):
    time.sleep(3)


@warn_slow
def func_fast(x, y):
    print(x, y)


func_slow(1, 2)
func_fast(1, 2)