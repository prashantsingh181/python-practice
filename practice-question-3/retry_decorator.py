import functools
import time


def retry(times, delay=0):
    # arguments validation
    if not isinstance(times, int) or times < 0:
        raise TypeError("times should be an int which is greater than 0")

    if not isinstance(delay, int) or delay < 0:
        raise TypeError("delay should be an int which is greater than 0")

    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            # trying function call times + 1 time
            for i in range(times + 1):
                try:
                    print(f"trying {fn.__name__} {i+1} time")
                    value = fn(*args, **kwargs)
                    return value
                except Exception:
                    # if last retry raise the exception
                    if i == times:
                        raise
                    else:
                        # add delay
                        if delay > 0:
                            time.sleep(delay)

                        continue

        return wrapper

    return decorator


@retry(3, 2)
def unstable_api_call():
    raise ValueError("failed")


unstable_api_call()
