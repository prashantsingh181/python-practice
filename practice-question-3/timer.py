import time
import functools


def timer(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        value = fn(*args, **kwargs)
        t2 = time.time()
        seconds_taken = t2 - t1
        print(f"{fn.__name__} took {seconds_taken:.2f}s")
        return value

    return wrapper


@timer
def slow_function():
    time.sleep(1)


slow_function()
