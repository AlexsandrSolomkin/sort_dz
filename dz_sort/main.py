import random
import time

def how_long(func, x):
    start = time.time()
    func(x)
    print(f"Скорость работы: {time.time() - start}")

