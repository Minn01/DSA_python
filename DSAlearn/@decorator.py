from time import perf_counter
def printSomething(func):
    def wrapper(*args):
        print(f"Function : {func.__name__}()")
        func(*args)
    return wrapper

@printSomething
def printName(name):
    print(f"Name : {name}")


printName("Min Thant")

def performance_reader(func):
    def wrapper(*args, **kwargs):
        print(f"Function : {func.__name__}()")
        start = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        print(f"Time taken : {end-start}")

    return wrapper
