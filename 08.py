import datetime
def log_except(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                time_now = datetime.datetime.today()
                with open(log_file, 'a') as f:
                    f.write(f'{time_now}, {type(e).__name__} \n')
        return wrapper
    return decorator

@log_except('exceptions.log')
def get_sum(a, b):
    return a + b

print(get_sum('k', 1))