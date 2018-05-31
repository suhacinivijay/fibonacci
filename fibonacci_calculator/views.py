from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import InputForm
import time

UPPER_LIMIT = 900


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


def getfibonacci(number_input):
    if number_input is None:
        return 'Cannot be None'
    try:
        number = int(number_input)
    except ValueError:
        return 'Number has to be an integer'
    if number <= 0:
        return 'Number cannot be zero or negative'
    if number >= UPPER_LIMIT:
        return 'I can only compute until'
    fib = fibonacci(number)
    return fib


@csrf_exempt
def index(request):
    form = InputForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            start = time.clock()
            number_input = form.cleaned_data['number_input']
            fib = getfibonacci(number_input)
            end = time.clock()
            time_taken = end - start
            return render(request, 'index.html', {'form': form, 'time_taken': time_taken, 'result': fib, 'number': number_input})
    if request.method == 'GET':
        return render(request, 'index.html', {'form': form})

