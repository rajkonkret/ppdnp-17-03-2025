import time
import numpy as np


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"CZas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_func():
    time.sleep(2)


@measure_time
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Suma is:", suma)


@measure_time
def my_sum_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print("Sum is:", total)


my_func()  # CZas wykonania funkcji my_func: 2.0005042552948
my_for_sum()  # 0.6443283557891846
my_sum_np()
# CZas wykonania funkcji my_func: 2.000105142593384
# Suma is: 112499992500000
# CZas wykonania funkcji my_for_sum: 0.6894419193267822
# Sum is: 112499992500000
# CZas wykonania funkcji my_sum_np: 0.05405402183532715
