def sqaure_decorator(func):
    def wrapped(x):
        print('Вызов функции:', func.__name__)
        result = func(x)
        return result
    return wrapped


@sqaure_decorator
def square(x):
    return x**2


print(square(4))
