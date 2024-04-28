from time import perf_counter

# def performance_reader(func, arr,  **kwargs):
#     start = perf_counter()
#     result = func(arr, **kwargs)
#     end = perf_counter()
#     print(f"Time taken for {func.__name__} : {end-start} seconds")
#     if not func.__annotations__:
#         return result

def performance_reader(func):
    def wrapper(*args, **kwargs):
        print(f"Function : {func.__name__}()")
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Time taken : {end-start}")
        return result

    return wrapper
def binary_search1(arr, target) -> bool:
    if len(arr) < 1:
        return False
    elif len(arr) == 1:
        return target == arr[0]
        # return True if target == arr[0] else False

    middle = len(arr) // 2
    if arr[middle] == target:
        return True
    elif arr[middle] < target:
        return binary_search1(arr[middle:], target)
    else:
        return binary_search1(arr[:middle], target)

def linear_search1(arr, target) -> bool:
    for i in arr:
        if i == target:
            return True
    return False

def linear_search(arr, target) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search2(arr, target) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search3(arr, target, left=0, right=None) -> int:
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search3(arr, target, mid+1, right)
    else:
        return binary_search3(arr, target, left, mid-1)

def printSomething(lis) -> None:
    print(lis)


lis = [int(x) for x in range(1000)]
print(binary_search3(lis, 825))

# print(performance_reader(linear_search, lis, target=43))
#
# print(performance_reader(linear_search1, lis, target=43))
#
# print(performance_reader(binary_search1, lis, target=43))
#
# print(performance_reader(binary_search2, lis, target=43))
#
# print(performance_reader(binary_search3, lis, target=43))
#
# print(performance_reader(printSomething, lis))
