import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, *kwargs)
        end  = time.time()
        print(f"{func.__name__} took {round(((end - start) * 1000), 3)} mil seconds")
        return result
    return wrapper