import time

def timer(fun):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=fun(*args,**kwargs)
        end=time.time()
        print(f"{fun.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example(n):
    time.sleep(n)

example(2)