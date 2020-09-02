from functools import wraps
from time import time


def timeit(method):
    @wraps(method)
    def timed(*args, **kwargs):
        ts = time()
        return_value = method(*args, **kwargs)
        te = time()

        print(f"{method.__name__}\t{(te - ts) * 1000:.2e}ms")
        return return_value
    return timed


def test_timeit():
    from time import sleep

    @timeit
    def pause_2s():
        print(f"\nstart time: {time()}")
        sleep(2)
        print(f"end time: {time()}")
    
    pause_2s()
