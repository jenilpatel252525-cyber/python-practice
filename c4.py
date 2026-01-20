import time


def cache(func):
    cache_value={}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper


@cache
def long_run(a,b):
    time.sleep(4)
    return a+b

print(long_run(2,3))
print(long_run(2,3))
print(long_run(2,2))
print(long_run(2,1))
print(long_run(2,2))
