import functools

@functools.cache
def fib(n):
    if n == 1 or n == 0: 
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Введите n: "))
print(fib(n))