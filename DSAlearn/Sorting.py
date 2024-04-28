import random
from time import perf_counter
# bubble sort
# insertion sort
# selection sort
# merge sort
# quick sort

def applySorting(func, arr, descending=False) -> None:
    print(f"The sorting algorithm used is '{func.__name__}'")
    start = perf_counter()
    if func.__name__ == 'quick_sort':
        func(arr, 0, len(arr)-1, descending)
    else:
        func(arr, descending)
    end = perf_counter()
    print(f"Time taken : '{end - start}' seconds")

def performance_reader(func):
    def wrapper(*args, **kwargs):
        print(f"Function : {func.__name__}")
        start = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        print(f"Time Taken : {end-start} seconds")
    return wrapper


def bogus_sort(arr, descending=False) -> None:
    _sorted = False
    while not sorted:
        _sorted = True
        for i in range(len(arr)-1):
            if descending:
                if arr[i] < arr[i+1]:
                    _sorted = False
                    random.shuffle(arr)
            else:
                if arr[i] > arr[i+1]:
                    _sorted = False
                    random.shuffle(arr)

@performance_reader
def bubble_sort(arr, descending=False) -> None:
    _sorted = False
    while not _sorted:
        _sorted = True
        for i in range(0, len(arr) - 1):
            if not descending and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                _sorted = False
            elif descending and arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                _sorted = False

@performance_reader
def insertion_sort(arr, descending=False) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        if descending:
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        else:
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

@performance_reader
def selection_sort(arr, descending=False) -> None:
    for i in range(len(arr) - 1):
        min_or_max = i
        for j in range(i, len(arr)):
            if not descending:
                if arr[min_or_max] > arr[j]:
                    min_or_max = j
            else:
                if arr[min_or_max] < arr[j]:
                    min_or_max = j
        arr[min_or_max], arr[i] = arr[i], arr[min_or_max]

def merge_sort(arr, descending=False) -> None:
    if len(arr) > 1:  # base condition
        # split to right and left
        middle = len(arr) // 2
        left_side = arr[:middle]
        right_side = arr[middle:]

        # recursion
        merge_sort(left_side, descending)
        merge_sort(right_side, descending)

        # Merge back
        i = 0
        j = 0
        k = 0
        while i < len(left_side) and j < len(right_side):
            if descending:
                if left_side[i] > right_side[j]:
                    arr[k] = left_side[i]
                    i += 1
                else:
                    arr[k] = right_side[j]
                    j += 1
                k += 1
            else:
                if left_side[i] < right_side[j]:
                    arr[k] = left_side[i]
                    i += 1
                else:
                    arr[k] = right_side[j]
                    j += 1
                k += 1
        while i < len(left_side):
            arr[k] = left_side[i]
            k += 1
            i += 1
        while j < len(right_side):
            arr[k] = right_side[j]
            k += 1
            j += 1

def partition(arr, l, r, descending):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if not descending:
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        else:
            if arr[j] > pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quick_sort(arr, l, r, descending=False):
    if l >= r:  # base condition
        return

    pivot = partition(arr, l, r, descending)
    quick_sort(arr, l, pivot-1, descending)
    quick_sort(arr, pivot+1, r, descending)


# Example usage :
lis = [random.randint(1, 20) for x in range(10)]
print("Unsorted List : ", lis)
bubble_sort(lis)
print("Sorted List : ", lis)
