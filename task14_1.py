def decorator(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        cache[n] = func(n)
        return cache[n]
    return wrapper


@decorator
def fib(n):
    if n == 1 or n == 0: 
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Введите n: "))
print(fib(n))