# Recursion Problems

# Problem 1
# Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1.
# Compute the result recursively (without loops).
# factorial(1) → 1
# factorial(2) → 2
# factorial(3) → 6

def factorial(n):
    if n == 1:
        return n

    return n * factorial(n - 1)


# print(factorial(1))
# print(factorial(2))
# print(factorial(3))

# The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition.
# The first two values in the sequence are 0 and 1 (essentially 2 base cases).
# Each subsequent value is the sum of the previous two values,
# so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on.
# Define a recursive fibonacci(n) method that returns the nth fibonacci number,
# with n=0 representing the start of the sequence.

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(4))

str_lis = ["h", "e", "l", "l", "o"]


def reverseString(lis, i=0, j=None):
    if not j:
        j = len(lis) - 1

    if i == j or j < i:
        return

    lis[i], lis[j] = lis[j], lis[i]
    return reverseString(lis, i + 1, j - 1)


reverseString(str_lis)
print(str_lis)


def sumDigits(n):
    print(n, end=f": {n%10}\n")
    if len(str(n)) == 1:
        if n == 7:
            return 1
        return 0

    if n % 10 == 7:
        return 1 + sumDigits(int(n/10))

    return sumDigits(int(n/10))


print(sumDigits(717))
print(int(8818/100))
