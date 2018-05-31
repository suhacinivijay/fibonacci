def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)

print fibonacci(6)