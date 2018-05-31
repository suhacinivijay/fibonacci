from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

UPPER_LIMIT = 10000


def index(request):
    return render(request, 'index.html')


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



@csrf_exempt
def getfibonacci(request):
    input_data = request.form("data", None)
    if input_data is None:
        return JsonResponse({'error': 'Number cannot be Nil'})
    try:
        number = int(input_data)
    except ValueError:
        return JsonResponse({'error': 'Number has to be an integer'})
    if number <= 0:
        return JsonResponse({'error': 'Number cannot be zero or negative'})
    if number >= UPPER_LIMIT:
        return JsonResponse({'error': 'I can only compute until'})
    fib = fibonacci(number)
    return JsonResponse({'data': fib})

