import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Czas wykonania funkcji {func.__name__}: {end_time - start_time:.5f} s")
        return result
    return wrapper

@measure_time
def slow_function(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += i * j
    return sum

result = slow_function(1000)
print(result)